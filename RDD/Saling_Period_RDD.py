import re
from pyspark.sql import SQLContext
from pyspark.sql import SparkSession
import sys,os
import RDD.Config as config

java8_location = config.java8_location
sys.path.append(config.syspath)
os.environ['SPARK_HOME'] = config.spark_home

spark =SparkSession.builder.appName("Saled_Period").master("local[*]").getOrCreate()
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
    return (key,(count,averageunit,averagetotal))

def countPeriod(inum,result):
    number = 0
    sumunitprice = 0
    count = 0
    for index, element in result:
        if count < inum:
            number = number + element[0]
            sumunitprice = sumunitprice + element[0] * element[1]
            count = count + 1
        else:
            break;
    unitprice = round(float(sumunitprice/number), 2)
    return [number, unitprice]

# 将dataframe转化为rdd
pairRDD = dataframe_mysql.rdd
# 清洗不存在的数据
pairRDD1 = pairRDD.filter(lambda row:row[20] != '不存在该项')
# 正则表达式提取年+月,结果类似于key-value形式，value是一个包含三个元素的元组
pairRDD2 = pairRDD1.map(lambda row:(re.findall("(.*?)\-",row[20])[0] + "." +re.findall("(.*?)\-",row[20])[1] , (row[5], row[4])))
# 对数据进行聚合
pairRDD3 = pairRDD2.groupByKey()
# 对数据进行计算
pairRDD4 = pairRDD3.map(lambda row:compute(row))
# 对数据进行排序
pairRDD5 = pairRDD4.sortByKey(ascending=False)
# 使用collect()函数转化
result = pairRDD5.collect()

# 获得每一个数据项的值
ID = []; Saled_DealTime = []; Saled_HangoutTime_Number = []; Saled_UnitPrice = []; Saled_TotalPrice = [];
idcount = 0
for index,element in result:
    print(index)
    print(element)
    ID.append(idcount)
    Saled_DealTime.append(index)
    Saled_HangoutTime_Number.append(element[0])
    Saled_UnitPrice.append(element[1])
    Saled_TotalPrice.append(element[2])
    idcount = idcount + 1

# 将获得的值存入数据库中
list_period = ["近一月","近半年","近一年","全部"]
list_result = []
list_month = countPeriod(1,result)
list_halfyear = countPeriod(6,result)
list_fullyear = countPeriod(12,result)
list_all = countPeriod(len(result),result)
list_result.append(list_month);list_result.append(list_halfyear)
list_result.append(list_fullyear);list_result.append(list_all)
for i in range(0,len(list_period)):
    sql = "INSERT INTO Saling_Period VALUES ({},'{}',{},{})" \
        .format(i, list_period[i], list_result[i][0], list_result[i][1])
    try:
        curcompute.execute(sql)
        conncompute.commit()
    except:
        conncompute.rollback()
        print("插入失败")

