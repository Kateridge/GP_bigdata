import pymysql,re
import areaInfo as info
import pandas as pd

try:
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='lianjiaTotal', port=3307)
    cur = conn.cursor()
    # print("登录数据库成功！！！")
except Exception:
    print("登录数据库出错，请检查用户名和密码！！！")

def salingHouseInfo(countyName, districtName):
    # 成交日期列表
    list_month = []
    sql = "SELECT DISTINCT hangoutTime1 FROM housesonsale_table"
    try:
        cur.execute(sql)
    except:
        print("查询失败")
    for element in cur:
        if element[0] != '不存在该项':
            list_month.append(re.findall("(.*?)\-", element[0])[0] + '.' + re.findall("(.*?)\-", element[0])[1])
    list_month = set(list_month)
    list_month = list(list_month)
    list_month.sort()

    print(list_month)

    district_label = ""
    for info_key in info.area_info.keys():
        if  info.area_info[info_key]== districtName:
            district_label = info_key
    print(district_label)

    sql = "SELECT hangoutTime1,price1,unitPrice1 FROM housesonsale_table WHERE housingEstate LIKE '%{}'".format(district_label)
    print(sql)
    try:
        cur.execute(sql)
    except:
        print("查询失败")
    hangouttime = []
    price = []
    unitprice = []
    for element in cur:
        result = re.findall("(.*?)\-(.*?)\-(.*?)", element[0])
        hangouttime.append(str(result[0][0] + '.' + result[0][1]))
        price.append(round(float(element[1]),2))
        unitprice.append(round(float(element[2]),2))
    dict = {'hangouttime': hangouttime, 'price': price, 'unitprice': unitprice}
    dtf = pd.DataFrame(dict)
    dtf1 = dtf.groupby('hangouttime').mean().reset_index()
    dtf1 = dtf1.sort_values(axis=0, by=['hangouttime'])

    value1 = [0] * len(list_month)
    value2 = [0] * len(list_month)

    for row in dtf1.iterrows():
        index = list_month.index(row[1][0])
        value1[index] = round(row[1][1], 2)
        value2[index] = round(row[1][2], 2)

    list_return = []
    list_return.append(["出售时间", "总价", "均价"])
    for i in range(0, len(list_month)):
        list_return.append([list_month[i], value1[i], value2[i]])
    print(list_return)
    return list_return




salingHouseInfo('沙坪坝','大学城')