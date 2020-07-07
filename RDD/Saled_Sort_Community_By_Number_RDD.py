import re
from pyspark.sql import SQLContext
from pyspark.sql import SparkSession
import sys,os
import RDD.Config as config
import areaInfo as info

java8_location = config.java8_location
sys.path.append(config.syspath)
os.environ['SPARK_HOME'] = config.spark_home

spark =SparkSession.builder.appName("Sort_Community").master("local[*]").getOrCreate()
sc = spark.sparkContext

cur = config.cur
curcompute = config.curcompute
conncompute = config.conncompute

sqlContext = SQLContext(sc)
dataframe_mysql = sqlContext.read.format("jdbc").options(
    url=config.url, driver="com.mysql.jdbc.Driver", dbtable=config.dbtable2, user=config.user, password=config.password).load()
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
    return (count,(key,count,averageunit,averagetotal))

# 将dataframe转化为rdd
pairRDD = dataframe_mysql.rdd
# 清洗不存在的数据
pairRDD1 = pairRDD.filter(lambda row:row[4] != '不存在该项')
# 初步提取数据，汇集成元组
pairRDD2 = pairRDD1.map(lambda row:(row[4], (row[7] , row[6])))
# 对数据进行聚合
pairRDD3 = pairRDD2.groupByKey()
# 对数据进行计算
pairRDD4 = pairRDD3.map(lambda row:compute(row))
# 对数据进行排序
pairRDD5 = pairRDD4.sortByKey(ascending=False)

# 使用collect()函数转化
result = pairRDD5.collect()

# 获得每一个数据项的值
ID = []; Saled_District = []; Saled_District_Number = []; Saled_UnitPrice = []; Saled_TotalPrice = [];
idcount = 0
for index,element in result:
    ID.append(idcount)
    Saled_District.append(element[0])
    Saled_District_Number.append(element[1])
    Saled_UnitPrice.append(element[2])
    Saled_TotalPrice.append(element[3])
    idcount = idcount + 1

# 将获得的值存入数据库中
for i in range(0,idcount):
    sql = "INSERT INTO Saled_Sort_Community_By_Number VALUES ({},'{}',{},{},{})"\
        .format(ID[i],Saled_District[i],Saled_District_Number[i],Saled_UnitPrice[i],Saled_TotalPrice[i])
    try:
        curcompute.execute(sql)
        conncompute.commit()
    except:
        conncompute.rollback()
        print("插入失败")
