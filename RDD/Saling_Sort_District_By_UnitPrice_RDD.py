import re
from pyspark.sql import SQLContext
from pyspark.sql import SparkSession
import sys,os
import RDD.Config as config
import areaInfo as info

java8_location = config.java8_location
sys.path.append(config.syspath)
os.environ['SPARK_HOME'] = config.spark_home

spark =SparkSession.builder.appName("Sort_District").master("local[*]").getOrCreate()
sc = spark.sparkContext

cur = config.cur
curcompute = config.curcompute
conncompute = config.conncompute

sqlContext = SQLContext(sc)
dataframe_mysql = sqlContext.read.format("jdbc").options(
    url=config.url, driver="com.mysql.jdbc.Driver", dbtable=config.dbtable1, user=config.user, password=config.password).load()
dataframe_mysql.show()

def compute(row):
    key = row[0]
    sumtotal = 0
    sumunit = 0
    count = len(row[1])
    for e in row[1]:
        sumunit = sumunit + e[0]
        sumtotal = sumtotal + e[1]
    averageunit = round((sumunit / count), 2)
    averagetotal = round((sumtotal / count), 2)
    return (averageunit,(key,count,averageunit,averagetotal))

# 将dataframe转化为rdd
pairRDD = dataframe_mysql.rdd
# 清洗不存在的数据
pairRDD1 = pairRDD.filter(lambda row:row[1] != '不存在该项')
# 初步提取数据，汇集成元组
pairRDD2 = pairRDD1.map(lambda row:(row[1].split("_")[1], (row[5] , row[4])))
# 对数据进行聚合
pairRDD3 = pairRDD2.groupByKey()
# 对数据进行计算
pairRDD4 = pairRDD3.map(lambda row:compute(row))
# 对数据进行排序
pairRDD5 = pairRDD4.sortByKey(ascending=False)

# 使用collect()函数转化
result = pairRDD5.collect()

# 获得每一个数据项的值
ID = []; Saling_District = []; Saling_District_Number = []; Saling_UnitPrice = []; Saling_TotalPrice = [];
idcount = 0
for index,element in result:
    ID.append(idcount)
    Saling_District.append(info.area_info[element[0]])
    Saling_District_Number.append(element[1])
    Saling_UnitPrice.append(element[2])
    Saling_TotalPrice.append(element[3])
    idcount = idcount + 1

# 将获得的值存入数据库中
for i in range(0,idcount):
    sql = "INSERT INTO Saling_Sort_District_By_UnitPrice VALUES ({},'{}',{},{},{})"\
        .format(ID[i],Saling_District[i],Saling_District_Number[i],Saling_UnitPrice[i],Saling_TotalPrice[i])
    try:
        curcompute.execute(sql)
        conncompute.commit()
    except:
        conncompute.rollback()
        print("插入失败")
