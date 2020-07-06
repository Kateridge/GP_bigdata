import pymysql,re
import areaInfo as info
import pandas as pd
import connectTodb as db_conn

cur = db_conn.cur


# 按地区：挂牌日期-总价，均价
def salingHouseInfo(countyName, districtName):
    # 挂牌日期列表
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

    district_label = ""
    for info_key in info.area_info.keys():
        if info.area_info[info_key] == districtName:
            district_label = info_key
    print(districtName)
    print(district_label)
    sql = "SELECT hangoutTime1,price1,unitPrice1 FROM housesonsale_table WHERE housingEstate LIKE '%{}'".format(district_label)
    try:
        cur.execute(sql)
    except:
        print("查询失败")
    hangouttime = []
    price = []
    unitprice = []
    for element in cur:
        if element[0] != '不存在该项':
            result = re.findall("(.*?)\-(.*?)\-(.*?)", element[0])
        hangouttime.append(str(result[0][0] + '.' + result[0][1]))
        price.append(round(float(element[1]), 2))
        unitprice.append(round(float(element[2]), 2))
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


# 按地区：某地区各小区的信息
def salingHouseChart2(countyName,districtName):
    district_label = ""
    for info_key in info.area_info.keys():
        if  info.area_info[info_key]== districtName:
            district_label = info_key
    sql = "SELECT communityName1,AVG(price1),AVG(unitPrice1),AVG(houseArea1), COUNT(communityName1) FROM housesonsale_table " \
          "WHERE housingEstate LIKE '%{}' GROUP BY communityName1".format(district_label)
    try:
        cur.execute(sql)
    except:
        print("查询失败")
    list_return = []
    for element in cur:
        dic = {}
        dic['communityName'] = element[0]
        dic['countyName'] = countyName
        dic['districtName'] = districtName
        dic['avgprice'] = str(round(element[1],2))+ "万元"
        dic['avgunitprice'] = str(round(element[2],2)) + "元/平方米"
        dic['avgarea'] = str(round(element[3],2)) + "平方米"
        dic['num'] = str(element[4]) + "套"
        list_return.append(dic)
    print(list_return)
    return list_return
