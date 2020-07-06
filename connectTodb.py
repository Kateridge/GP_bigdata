# 连接数据库
import pymysql

try:
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='lianjiaTotal', port=3307)
    cur = conn.cursor()
    # print("登录数据库成功！！！")
except Exception:
    print("登录数据库出错，请检查用户名和密码！！！")