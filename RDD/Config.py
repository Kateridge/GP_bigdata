import pymysql

try:
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='lianjiaTotal', port=3307)
    cur = conn.cursor()
    # print("登录数据库成功！！！")
except Exception:
    print("登录数据库出错，请检查用户名和密码！！！")

try:
    conncompute = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='lianjiaCompute', port=3307)
    curcompute = conncompute.cursor()
    # print("登录数据库成功！！！")
except Exception:
    print("登录数据库出错，请检查用户名和密码！！！")

url = "jdbc:mysql://127.0.0.1:3307/lianjiaTotal"
urlcompute = "jdbc:mysql://127.0.0.1:3307/lianjiaCompute"
dbtable1="housesonsale_table"
dbtable2="housessaled_table"
user="root"
password="123456"

java8_location = "G:\setup\java8\jdk1.8.0_191"
syspath = 'D:\WorkSpace\pycharm\LianjiaRdd'
spark_home = 'D:\hadoop-3.1.1\spark-2.4.4-bin-hadoop2\spark-2.4.4-bin-hadoop2.7'


