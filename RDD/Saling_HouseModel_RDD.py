import re
from pyspark.sql import SQLContext
from pyspark.sql import SparkSession
import sys,os
import RDD.Config as config
import areaInfo as info

java8_location = config.java8_location
sys.path.append(config.syspath)
os.environ['SPARK_HOME'] = config.spark_home

spark =SparkSession.builder.appName("Saling_HouseModel").master("local[*]").getOrCreate()
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
    return (count,(key,count,averageunit,averagetotal))

# 将dataframe转化为rdd
pairRDD = dataframe_mysql.rdd
# 清洗不存在的数据
pairRDD1 = pairRDD.filter(lambda row:row[9] != '不存在该项' and row[9].replace(" ","") != '车位' and row[9].replace(" ","") != '--室--厅')
# 初步提取数据，汇集成元组
pairRDD2 = pairRDD1.map(lambda row:(row[9].replace(" ",""), (row[5] , row[4])))
# 对数据进行聚合
pairRDD3 = pairRDD2.groupByKey()
# 对数据进行计算
pairRDD4 = pairRDD3.map(lambda row:compute(row))
# 对数据进行排序
pairRDD5 = pairRDD4.sortByKey(ascending=False)

# 使用collect()函数转化
result = pairRDD5.collect()

# 获得每一个数据项的值
ID = []; Saling_HouseModel = []; Saling_HouseModel_Number = []
idcount = 0
count_other = 0
for index,element in result:
    if element[1] < 600:
        count_other = count_other + element[1]
    else:
        ID.append(idcount)
        Saling_HouseModel.append(element[0])
        Saling_HouseModel_Number.append(element[1])
        idcount = idcount + 1
ID.append(idcount)
Saling_HouseModel.append("其他")
Saling_HouseModel_Number.append(count_other)
idcount = idcount + 1
# 将获得的值存入数据库中
for i in range(0,idcount):
    sql = "INSERT INTO Saling_HouseModel VALUES ({},'{}',{})"\
        .format(ID[i],Saling_HouseModel[i],Saling_HouseModel_Number[i])
    try:
        curcompute.execute(sql)
        conncompute.commit()
    except:
        conncompute.rollback()
        print("插入失败")




