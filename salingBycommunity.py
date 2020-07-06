import pymysql, re, math
from pandas import Series, DataFrame
import pandas as pd
import areaInfo as info
import connectTodb as db_conn

cur = db_conn.cur


# 户型   装修情况   面积  朝向 均价 总价

# 1.户型饼状图：
def salingHouseModel(communityName):
    sql = "SELECT houseingModel1 FROM housesonsale_table WHERE communityName1 = '{}'".format(communityName)
    try:
        cur.execute(sql)
    except:
        print("查询失败")
    list_model = []
    for element in cur:
        list_model.append(element[0].replace(" ", ""))
    list_model.sort()
    set_model = set(list_model)
    set_model = list(set_model)
    value = [0] * len(set_model)
    sum = 0
    for i in range(0, len(set_model)):
        value[i] = list_model.count(set_model[i])
        sum = sum + value[i]
    change_model = []
    change_value = []
    other = ""
    sumother = 0
    for i in range(0, len(set_model)):
        if value[i]/sum < 0.05:
            other = '其他'
            sumother = sumother + value[i]
        else:
            change_model.append(set_model[i])
            change_value.append(value[i])
    if other == '其他':
        change_model.append(other)
        change_value.append(sumother)
    list_return = []
    for i in range(0, len(change_model)):
        dic = {}
        dic['value'] = change_value[i]
        dic['name'] = change_model[i]
        list_return.append(dic)
    print(list_return)
    return list_return


# 2.房屋总价饼状图
def salingDealPrice(communityName):
    sql = "SELECT Price1 FROM housesonsale_table  WHERE communityName1 = '{}'".format(communityName)
    try:
        cur.execute(sql)
    except:
        print("查询失败")
    list_label = ["50万以下", "50-100万", "100-150万", "150-200万", "200万以上"]
    value = [0] * 5
    list_price = []
    for element in cur:
        if element[0] <= 50:
            value[0] = value[0] + 1
        elif element[0] <= 100:
            value[1] = value[1] + 1
        elif element[0] <= 150:
            value[2] = value[2] + 1
        elif element[0] <= 200:
            value[3] = value[3] + 1
        else:
            value[4] = value[4] + 1
    list_return = []
    for i in range(0, 5):
        dic = {}
        if value[i] != 0:
            dic['value'] = value[i]
            dic['name'] = list_label[i]
            list_return.append(dic)
    print(list_return)
    return list_return


# 3.房屋均价饼状图
def salingUnitPrice(communityName):
    sql = "SELECT unitPrice1 FROM housesonsale_table WHERE communityName1 = '{}'".format(communityName)
    try:
        cur.execute(sql)
    except:
        print("查询失败")
    list_label = ["5000元/平方米以下", "5000-10000元/平方米", "10000-15000元/平方米", "15000-20000元/平方米", "20000元/平方米以上"]
    value = [0] * 5
    for element in cur:
        if element[0] <= 5000:
            value[0] = value[0] + 1
        elif element[0] <= 10000:
            value[1] = value[1] + 1
        elif element[0] <= 15000:
            value[2] = value[2] + 1
        elif element[0] <= 20000:
            value[3] = value[3] + 1
        else:
            value[4] = value[4] + 1
    list_return = []
    for i in range(0, 5):
        dic = {}
        if value[i] != 0:
            dic['value'] = value[i]
            dic['name'] = list_label[i]
            list_return.append(dic)
    print(list_return)
    return list_return


# 4.房屋面积饼状图
def salingHouseArea(communintyName):
    sql = "SELECT houseArea1 FROM housesonsale_table WHERE communityName1 = '{}'".format(communintyName)
    try:
        cur.execute(sql)
    except:
        print("查询失败")
    list_label = ["50平方米以下", "50-100平方米", "100-150平方米", "150-200平方米", "200平方米以上"]
    value = [0] * 5
    for element in cur:
        if element[0] <= 50:
            value[0] = value[0] + 1
        elif element[0] <= 100:
            value[1] = value[1] + 1
        elif element[0] <= 150:
            value[2] = value[2] + 1
        elif element[0] <= 200:
            value[3] = value[3] + 1
        else:
            value[4] = value[4] + 1
    list_return = []
    for i in range(0, 5):
        dic = {}
        if value[i] != 0:
            dic['value'] = value[i]
            dic['name'] = list_label[i]
            list_return.append(dic)
    print(list_return)
    return list_return


# 5.装修情况饼状图：
def salingDecorateStatus1(communityName):
    sql = "SELECT decorateStatus1 FROM housesonsale_table WHERE communityName1 = '{}'".format(communityName)
    try:
        cur.execute(sql)
    except:
        print("查询失败")
    list_model = []
    for element in cur:
        list_model.append(element[0].replace(" ", ""))
    list_model.sort()
    set_model = set(list_model)
    set_model = list(set_model)
    value = [0] * len(set_model)
    for i in range(0, len(set_model)):
        value[i] = list_model.count(set_model[i])
    list_return = []
    for i in range(0, len(set_model)):
        dic = {}
        dic['value'] = value[i]
        dic['name'] = set_model[i]
        list_return.append(dic)
    print(list_return)
    return list_return


# 6.房屋朝向饼状图
def salingHouseFaced1(communityName):
    sql = "SELECT houseFaced1 FROM housesonsale_table WHERE communityName1 = '{}'".format(communityName)
    try:
        cur.execute(sql)
    except:
        print("查询失败")

    list_face = []
    for element in cur:
        if(" " in element[0]):
            result = element[0].split(" ")
            list_face.append(result[0])
            list_face.append(result[1])
        else:
            list_face.append(element[0])
    set_face = set(list_face)
    set_face = list(set_face)
    value = [0] * len(set_face)
    for i in range(0, len(set_face)):
        value[i] = list_face.count(set_face[i])
    list_return = []
    for i in range(0, len(set_face)):
        dic = {}
        dic['value'] = value[i]
        dic['name'] = set_face[i]
        list_return.append(dic)
    print(list_return)
    return list_return


#  7.挂牌时间-(总价，均价)（分两个子函数，使用子函数）
def salingHangoutTime(communityName):
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

    # 查询语句
    sql = "SELECT hangoutTime1, AVG(price1) , AVG(unitPrice1)  " \
          "FROM housesonsale_table WHERE communityName1 = '{}' GROUP BY hangoutTime1".format(communityName)
    try:
        cur.execute(sql)
    except:
        print("查询失败")

    hangouttime = []
    price = []
    unitprice = []
    for element in cur:
        result = re.findall("(.*?)\-(.*?)\-(.*?)", element[0])
        hangouttime.append(result[0][0] + '.' + result[0][1])
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
    list_return.append(["挂牌时间", "总价", "均价"])
    for i in range(0, len(list_month)):
        list_return.append(
            [list_month[i], value1[i], value2[i]])
    return list_return

# 7.1挂牌时间-总价柱形图
def hangoutTime_price(communityName):
    L = salingHangoutTime(communityName)
    list_return = []
    for element in L:
        list_return.append([element[0], element[1]])
    print(list_return)
    return list_return

# 7.2挂牌时间-均价柱形图
def hangoutTime_unitPrice(communityName):
    L = salingHangoutTime(communityName)
    list_return = []
    for element in L:
        list_return.append([element[0], element[2]])
    print(list_return)
    return list_return


# 按小区：在售房屋信息表
def salingHouseChart(communityName):
    sql = "SELECT houseName1, housingHref1, houseArea1, houseingModel1, price1,unitPrice1,decorateStatus1,hangoutTime1 " \
          "FROM housesonsale_table WHERE communityName1 = '{}'".format(communityName)
    try:
        cur.execute(sql)
    except:
        print("查询失败")
    list_return = []
    for element in cur:
        dic = {}
        dic['houseName'] = element[0]
        dic['houseHref'] = element[1]
        dic['houseArea'] = str(element[2]) + "平方米"
        dic['houseModel'] = element[3]
        dic['housePrice'] = str(element[4]) + "万元"
        dic['houseUnitPrice'] = str(element[5]) + "元/平方米"
        dic['decorateStatus'] = element[6]
        dic['hangoutTime'] = element[7]
        list_return.append(dic)
    print(list_return)
    return list_return


