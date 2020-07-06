import pymysql,re
import areaInfo as info
import pandas as pd
import connectTodb as db_conn

cur = db_conn.cur


# 按地区：成交日期-总价，均价，多加了成交价hangoutPrice,差价
def saledHouseInfo(countyName, districtName):
    # 挂牌日期列表
    list_month = []
    sql = "SELECT DISTINCT dealTime2 FROM housessaled_table"
    try:
        cur.execute(sql)
    except:
        print("查询失败")
    for element in cur:
        if element[0] != '不存在该项':
            list_month.append(re.findall("(.*?)\.", element[0])[0] + '.' + re.findall("(.*?)\.", element[0])[1])
    list_month = set(list_month)
    list_month = list(list_month)
    list_month.sort()

    district_label = ""
    for info_key in info.area_info.keys():
        if info.area_info[info_key] == districtName:
            district_label = info_key

    sql = "SELECT dealTime2,dealPrice2,dealUnitPrice2,hangoutPrice2 FROM housessaled_table WHERE housingEstate LIKE '%{}'".format(district_label)
    try:
        cur.execute(sql)
    except:
        print("查询失败")
    dealtime = []
    dealprice = []
    dealunitprice = []
    hangoutprice = []
    for element in cur:
        if element[0] != '不存在该项':
            result = re.findall("(.*?)\.(.*?)\.(.*?)", element[0])
        dealtime.append(str(result[0][0] + '.' + result[0][1]))
        dealprice.append(round(float(element[1]), 2))
        dealunitprice.append(round(float(element[2]), 2))
        if element[3] == -1:
            hangoutprice.append(round(float(element[1]), 2))
        else:
            hangoutprice.append(round(float(element[3]), 2))
    dict = {'dealtime': dealtime, 'dealprice': dealprice, 'dealunitprice': dealunitprice,'hangoutprice':hangoutprice}
    dtf = pd.DataFrame(dict)
    dtf1 = dtf.groupby('dealtime').mean().reset_index()
    dtf1 = dtf1.sort_values(axis=0, by=['dealtime'])

    value1 = [0] * len(list_month)
    value2 = [0] * len(list_month)
    value3 = [0] * len(list_month)
    value4 = [0] * len(list_month)

    for row in dtf1.iterrows():
        index = list_month.index(row[1][0])
        value1[index] = round(row[1][1], 2)
        value2[index] = round(row[1][2], 2)
        value3[index] = round(row[1][3], 2)
        value4[index] = round(value3[index] - value1[index], 2)

    list_return = []
    list_return.append(["成交时间", "成交总价", "成交均价", "挂牌总价", "交易差价"])
    for i in range(0, len(list_month)):
        list_return.append([list_month[i], value1[i], value2[i], value3[i], value4[i]])
    print(list_return)
    return list_return


# 按地区：某地区各小区的信息，多加了挂牌价hangoutPrice，差价
def saledHouseChart3(countyName,districtName):
    district_label = ""
    for info_key in info.area_info.keys():
        if  info.area_info[info_key]== districtName:
            district_label = info_key
    sql = "SELECT communityName2,AVG(dealPrice2),AVG(dealUnitPrice2),AVG(hangoutPrice2),AVG(houseArea2), COUNT(communityName2) FROM housessaled_table " \
          "WHERE housingEstate LIKE '%{}' GROUP BY communityName2".format(district_label)
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
        dic['avgdealprice'] = str(round(element[1],2))+ "万元"
        dic['avgdealunitprice'] = str(round(element[2],2)) + "元/平方米"
        if element[3] == -1:
            dic['avghangoutprice'] = str(round(element[1], 2))+ "万元"
            dic['decreaseprice'] = str(round(0 , 2))+ "万元"
        else:
            dic['avghangoutprice'] = str(round(element[3], 2)) + "万元"
            dic['decreaseprice'] = str(round(element[3]-element[1], 2))+ "万元"
        dic['avgarea'] = str(round(element[4],2)) + "平方米"
        dic['num'] = str(element[5]) + "套"
        list_return.append(dic)
    print(list_return)
    return list_return

