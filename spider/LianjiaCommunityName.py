import pymysql,csv,re

# user = input("请输入数据库连接用户名：")
# password = input("请输入数据库连接密码：")
try:
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='lianjiaTotal', port=3307)
    cur = conn.cursor()
    print("登录数据库成功！！！")
except Exception:
    print("登录数据库出错，请检查用户名和密码！！！")

sql = "SELECT DISTINCT communityName1 FROM housesonsale_table"

try:
    cur.execute(sql)
except:
    print("查询出错")

with open("communityNameSaling.txt",'w',encoding='utf-8') as fp:
    for e in cur:
        str = '<option value="{}">'.format(e[0])
        fp.write(str + '\n')