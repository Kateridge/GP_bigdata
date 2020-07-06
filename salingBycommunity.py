import pymysql, re, math
from pandas import Series, DataFrame
import pandas as pd
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

    print(sql)
    list_model = ["东", "东南", "南", "西南", "西", "西北", "北", "东北", "其他"]
    value = [0] * 9
    for element in cur:
        re.sub(' ', '', element[0], re.S)
        if element[0] == "东" or element[0] == "南 东":
            value[0] = value[0] + 1
        elif element[0] == "东南":
            value[1] = value[1] + 1
        elif element[0] == "南":
            value[2] = value[2] + 1
        elif element[0] == "西南":
            value[3] = value[3] + 1
        elif element[0] == "西":
            value[4] = value[4] + 1
        elif element[0] == "西北":
            value[5] = value[5] + 1
        elif element[0] == "东北":
            value[7] = value[7] + 1
        elif element[0] == "北" or element[0] == "南 北":
            value[6] = value[6] + 1
        else:
            value[8] = value[8] + 1
    list_return = []
    for i in range(0, 9):
        dic = {}
        if value[i] != '0':
            dic['value'] = value[i]
            dic['name'] = list_model[i]
            list_return.append(dic)
    print(list_return)
    return list_return