import re
from pyspark.sql import SQLContext
from pyspark.sql import SparkSession
import sys,os
import RDD.Config as config

java8_location = config.java8_location
sys.path.append(config.syspath)
os.environ['SPARK_HOME'] = config.spark_home

spark =SparkSession.builder.appName("Saled_DealTime").master("local[*]").getOrCreate()
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
    return (key,(count,averageunit,averagetotal))

# 将dataframe转化为rdd
pairRDD = dataframe_mysql.rdd
# 清洗不存在的数据
pairRDD1 = pairRDD.filter(lambda row:row[5] != '不存在该项')
# 初步提取数据，汇集成元组
pairRDD2 = pairRDD2 = pairRDD1.map(lambda row:(re.findall("(.*?)成交",row[5])[0].replace(" ",""), row[7] , row[6]))
# 正则表达式提取年+月,结果类似于key-value形式，value是一个包含三个元素的元组
pairRDD3 = pairRDD2.map(lambda row:(re.findall("(.*?)\.",row[0])[0] + "." +re.findall("(.*?)\.",row[0])[1] , (row[1], row[2])))
# 对数据进行聚合
pairRDD4 = pairRDD3.groupByKey()
# 对数据进行计算
pairRDD5 = pairRDD4.map(lambda row:compute(row))
# 对数据进行排序
pairRDD6 = pairRDD5.sortByKey()
# 使用collect()函数转化
result = pairRDD6.collect()

# 获得每一个数据项的值
ID = []; Saled_DealTime = []; Saled_HangoutTime_Number = []; Saled_UnitPrice = []; Saled_TotalPrice = [];
idcount = 0
for index,element in result:
    ID.append(idcount)
    Saled_DealTime.append(index)
    Saled_HangoutTime_Number.append(element[0])
    Saled_UnitPrice.append(element[1])
    Saled_TotalPrice.append(element[2])
    idcount = idcount + 1

# 将获得的值存入数据库中
for i in range(0,idcount):
    sql = "INSERT INTO Saled_DealTime VALUES ({},'{}',{},{},{})"\
        .format(ID[i],Saled_DealTime[i],Saled_HangoutTime_Number[i],Saled_UnitPrice[i],Saled_TotalPrice[i])
    try:
        curcompute.execute(sql)
        conncompute.commit()
    except:
        conncompute.rollback()
        print("插入失败")
