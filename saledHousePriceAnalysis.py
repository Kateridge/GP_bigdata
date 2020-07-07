import pymysql, re, math
from pandas import Series, DataFrame
import pandas as pd
import connectTodb as db_conn

cur =  db_conn.cur



# 1.成交时间-(均价，成交价，挂牌价，差价，数量，交易周期，降价次数，参观次数，参观人数)
def saledDealTime(communityName):
    # 成交日期列表
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

    # 查询语句
    sql = "SELECT dealTime2, AVG(dealUnitPrice2) , AVG(dealPrice2) , AVG(hangoutPrice2), AVG(dealCycle2), " \
          "AVG(adjustPriceTimes2), AVG(visitTimes2), AVG(followsNum2) " \
          "FROM housessaled_table WHERE communityName2 = '{}' GROUP BY dealTime2".format(communityName)
    try:
        cur.execute(sql)
    except:
        print("查询失败")

    dealtime = []
    dealunitprice = []
    dealprice = []
    hangoutprice = []
    dealcycle = []
    adjustpricetimes = []
    visittimes = []
    followtimes = []
    for element in cur:
        result = re.findall("(.*?)\.(.*?)\.(.*?)", element[0])
        dealtime.append(result[0][0] + '.' + result[0][1])
        dealunitprice.append(round(float(element[1]), 2))
        dealprice.append(round(float(element[2]), 2))
        if element[3] == -1:
            print(element)
            hangoutprice.append(round(float(element[2]), 2))
        else:
            hangoutprice.append(round(float(element[3]), 2))
        dealcycle.append(round(float(element[4]), 2))
        adjustpricetimes.append(round(float(element[5]), 2))
        visittimes.append(round(float(element[6]), 2))
        followtimes.append(round(float(element[7]), 2))

    dict = {'dealtime': dealtime, 'dealunitprice': dealunitprice, 'dealprice': dealprice, 'hangoutprice': hangoutprice,
            'dealcycle': dealcycle, 'adjustpricetimes': adjustpricetimes, 'visittimes': visittimes,
            'followtimes': followtimes}
    dtf = pd.DataFrame(dict)
    dtf1 = dtf.groupby('dealtime').mean().reset_index()
    dtf2 = dtf.groupby('dealtime').count().reset_index()
    dtf1 = dtf1.sort_values(axis=0, by=['dealtime'])
    dtf2 = dtf2.sort_values(axis=0, by=['dealtime'])

    value1 = [0] * len(list_month);
    value2 = [0] * len(list_month);
    value3 = [0] * len(list_month);
    value4 = [0] * len(list_month)
    value5 = [0] * len(list_month);
    value6 = [0] * len(list_month);
    value7 = [0] * len(list_month);
    value8 = [0] * len(list_month);
    value9 = [0] * len(list_month)
    for row in dtf1.iterrows():
        index = list_month.index(row[1][0])
        value1[index] = round(row[1][1], 2)
        value2[index] = round(row[1][2], 2)
        value3[index] = round(row[1][3], 2)
        value4[index] = round(value3[index] - value2[index], 2)
        value6[index] = math.ceil(row[1][4])
        value7[index] = math.ceil(row[1][5])
        value8[index] = math.ceil(row[1][6])
        value9[index] = math.ceil(row[1][7])
    for row in dtf2.iterrows():
        index = list_month.index(row[1][0])
        value5[index] = round(row[1][1], 2)

    list_return = []
    list_return.append(["成交时间", "均价", "成交价", "挂牌价", "差价", "数量", "交易周期", "降价次数", "参观次数", "参观人数"])
    for i in range(0, len(list_month)):
        list_return.append(
            [list_month[i], value1[i], value2[i], value3[i], value4[i], value5[i], value6[i], value7[i], value8[i],
             value9[i]])

    return list_return


# 2.装修情况-(均价，成交价，挂牌价，差价，数量，交易周期，降价次数，参观次数，参观人数)
def saledDecorateStatus(communityName):
    # 装修情况列表
    list_decorate = ['毛坯', '简装', '精装', '其他']

    # 查询语句
    sql = "SELECT decorateStatus2, AVG(dealUnitPrice2) , AVG(dealPrice2) , AVG(hangoutPrice2), COUNT(decorateStatus2) , AVG(dealCycle2), " \
          "AVG(adjustPriceTimes2), AVG(visitTimes2), AVG(followsNum2) FROM housessaled_table WHERE communityName2 = '{}' GROUP BY decorateStatus2".format(
        communityName)
    try:
        cur.execute(sql)
    except:
        print("查询失败")

    decoratestatus = []
    dealunitprice = []
    dealprice = []
    hangoutprice = []
    num = []
    dealcycle = []
    adjustpricetimes = []
    visittimes = []
    followtimes = []
    for element in cur:
        decoratestatus.append(element[0].replace(" ", ""))
        dealunitprice.append(round(float(element[1]), 2))
        dealprice.append(round(float(element[2]), 2))
        if element[3] == -1:
            print(element)
            hangoutprice.append(round(float(element[2]), 2))
        else:
            hangoutprice.append(round(float(element[3]), 2))
        num.append(round(float(element[4]), 2))
        dealcycle.append(round(float(element[5]), 2))
        adjustpricetimes.append(round(float(element[6]), 2))
        visittimes.append(round(float(element[7]), 2))
        followtimes.append(round(float(element[8]), 2))

    dict = {'decoratestatus': decoratestatus, 'dealunitprice': dealunitprice, 'dealprice': dealprice,
            'hangoutprice': hangoutprice, 'num': num, 'dealcycle': dealcycle, 'adjustpricetimes': adjustpricetimes,
            'visittimes': visittimes, 'followtimes': followtimes}
    dtf = pd.DataFrame(dict)
    dtf1 = dtf.groupby('decoratestatus').mean().reset_index()

    value1 = [0] * len(list_decorate);
    value2 = [0] * len(list_decorate);
    value3 = [0] * len(list_decorate);
    value4 = [0] * len(list_decorate)
    value5 = [0] * len(list_decorate);
    value6 = [0] * len(list_decorate);
    value7 = [0] * len(list_decorate);
    value8 = [0] * len(list_decorate);
    value9 = [0] * len(list_decorate)
    for row in dtf1.iterrows():
        index = list_decorate.index(row[1][0])
        value1[index] = round(row[1][1], 2)
        value2[index] = round(row[1][2], 2)
        value3[index] = round(row[1][3], 2)
        value4[index] = round(value3[index] - value2[index], 2)
        value5[index] = math.ceil(row[1][4])
        value6[index] = math.ceil(row[1][5])
        value7[index] = math.ceil(row[1][6])
        value8[index] = math.ceil(row[1][7])
        value9[index] = math.ceil(row[1][8])

    list_return = []
    list_return.append(["装修情况", "均价", "成交价", "挂牌价", "差价", "数量", "交易周期", "降价次数", "参观次数", "参观人数"])
    for i in range(0, len(list_decorate)):
        list_return.append(
            [list_decorate[i], value1[i], value2[i], value3[i], value4[i], value5[i], value6[i], value7[i], value8[i],
             value9[i]])

    return list_return


# 3.户型-(均价，成交价，挂牌价，差价，数量，交易周期，降价次数，参观次数，参观人数)
def saledHousingModel(communityName):
    # 户型列表
    list_model = []
    sql = "SELECT DISTINCT housingModel2 FROM housessaled_table"
    try:
        cur.execute(sql)
    except:
        print("查询失败")
    for element in cur:
        if element[0].replace(" ", "") != '不存在该项' and element[0].replace(" ", "") != '--室--厅' and element[0].replace(
                " ", "") != '车位':
            list_model.append(element[0].replace(" ", ""))
    list_model = set(list_model)
    list_model = list(list_model)
    list_model.sort()

    # 查询语句
    sql = "SELECT housingModel2, AVG(dealUnitPrice2) , AVG(dealPrice2) , AVG(hangoutPrice2), COUNT(housingModel2) , AVG(dealCycle2), " \
          "AVG(adjustPriceTimes2), AVG(visitTimes2), AVG(followsNum2) FROM housessaled_table WHERE communityName2 = '{}' GROUP BY housingModel2".format(
        communityName)
    try:
        cur.execute(sql)
    except:
        print("查询失败")

    housemodel = []
    dealunitprice = []
    dealprice = []
    hangoutprice = []
    num = []
    dealcycle = []
    adjustpricetimes = []
    visittimes = []
    followtimes = []
    for element in cur:
        housemodel.append(element[0].replace(" ", ""))
        dealunitprice.append(round(float(element[1]), 2))
        dealprice.append(round(float(element[2]), 2))
        if element[3] == -1:
            print(element)
            hangoutprice.append(round(float(element[2]), 2))
        else:
            hangoutprice.append(round(float(element[3]), 2))
        num.append(round(float(element[4]), 2))
        dealcycle.append(round(float(element[5]), 2))
        adjustpricetimes.append(round(float(element[6]), 2))
        visittimes.append(round(float(element[7]), 2))
        followtimes.append(round(float(element[8]), 2))

    dict = {'housemodel': housemodel, 'dealunitprice': dealunitprice, 'dealprice': dealprice,
            'hangoutprice': hangoutprice, 'num': num, 'dealcycle': dealcycle, 'adjustpricetimes': adjustpricetimes,
            'visittimes': visittimes, 'followtimes': followtimes}
    dtf = pd.DataFrame(dict)
    dtf1 = dtf.groupby('housemodel').mean().reset_index()

    value1 = [0] * len(list_model);
    value2 = [0] * len(list_model);
    value3 = [0] * len(list_model);
    value4 = [0] * len(list_model)
    value5 = [0] * len(list_model);
    value6 = [0] * len(list_model);
    value7 = [0] * len(list_model);
    value8 = [0] * len(list_model);
    value9 = [0] * len(list_model)
    for row in dtf1.iterrows():
        index = list_model.index(row[1][0])
        value1[index] = round(row[1][1], 2)
        value2[index] = round(row[1][2], 2)
        value3[index] = round(row[1][3], 2)
        value4[index] = round(value3[index] - value2[index], 2)
        value5[index] = math.ceil(row[1][4])
        value6[index] = math.ceil(row[1][5])
        value7[index] = math.ceil(row[1][6])
        value8[index] = math.ceil(row[1][7])
        value9[index] = math.ceil(row[1][8])

    list_return = []
    list_return.append(["户型", "均价", "成交价", "挂牌价", "差价", "数量", "交易周期", "降价次数", "参观次数", "参观人数"])
    for i in range(0, len(list_model)):
        list_return.append(
            [list_model[i], value1[i], value2[i], value3[i], value4[i], value5[i], value6[i], value7[i], value8[i],
             value9[i]])
    return list_return


# 4.是否靠近地铁-(均价，成交价，挂牌价，差价，数量，交易周期，降价次数，参观次数，参观人数)
def saledIsSubway(communityName):
    # 是否存在地铁列表
    list_subway = ['0', '1']

    # 查询语句
    sql = "SELECT subway2, AVG(dealUnitPrice2) , AVG(dealPrice2) , AVG(hangoutPrice2), COUNT(subway2) , AVG(dealCycle2), " \
          "AVG(adjustPriceTimes2), AVG(visitTimes2), AVG(followsNum2) FROM housessaled_table WHERE communityName2 = '{}' GROUP BY subway2".format(
        communityName)
    try:
        cur.execute(sql)
    except:
        print("查询失败")

    subway = []
    dealunitprice = []
    dealprice = []
    hangoutprice = []
    num = []
    dealcycle = []
    adjustpricetimes = []
    visittimes = []
    followtimes = []
    for element in cur:
        subway.append(element[0])
        dealunitprice.append(round(float(element[1]), 2))
        dealprice.append(round(float(element[2]), 2))
        if element[3] == -1:
            print(element)
            hangoutprice.append(round(float(element[2]), 2))
        else:
            hangoutprice.append(round(float(element[3]), 2))
        num.append(round(float(element[4]), 2))
        dealcycle.append(round(float(element[5]), 2))
        adjustpricetimes.append(round(float(element[6]), 2))
        visittimes.append(round(float(element[7]), 2))
        followtimes.append(round(float(element[8]), 2))

    dict = {'subway': subway, 'dealunitprice': dealunitprice, 'dealprice': dealprice,
            'hangoutprice': hangoutprice, 'num': num, 'dealcycle': dealcycle, 'adjustpricetimes': adjustpricetimes,
            'visittimes': visittimes, 'followtimes': followtimes}
    dtf = pd.DataFrame(dict)
    dtf1 = dtf.groupby('subway').mean().reset_index()

    value1 = [0] * len(list_subway);
    value2 = [0] * len(list_subway);
    value3 = [0] * len(list_subway);
    value4 = [0] * len(list_subway)
    value5 = [0] * len(list_subway);
    value6 = [0] * len(list_subway);
    value7 = [0] * len(list_subway);
    value8 = [0] * len(list_subway);
    value9 = [0] * len(list_subway)
    for row in dtf1.iterrows():
        index = list_subway.index(str(row[1][0]))
        value1[index] = round(row[1][1], 2)
        value2[index] = round(row[1][2], 2)
        value3[index] = round(row[1][3], 2)
        value4[index] = round(value3[index] - value2[index], 2)
        value5[index] = math.ceil(row[1][4])
        value6[index] = math.ceil(row[1][5])
        value7[index] = math.ceil(row[1][6])
        value8[index] = math.ceil(row[1][7])
        value9[index] = math.ceil(row[1][8])

    list_return = []
    list_return.append(["是否靠近地铁", "均价", "成交价", "挂牌价", "差价", "数量", "交易周期", "降价次数", "参观次数", "参观人数"])
    for i in range(0, len(list_subway)):
        list_return.append(
            [list_subway[i], value1[i], value2[i], value3[i], value4[i], value5[i], value6[i], value7[i], value8[i],
             value9[i]])
    return list_return


# 子函数编写
# 1.成交时间-均价
def dealTime_dealUnitPrice(communityName):
    L = saledDealTime(communityName)
    list_return = []
    for element in L:
        list_return.append([element[0], element[1]])
    print(list_return)
    return list_return


# 2.成交时间-总价
def dealTime_dealPrice(communityName):
    L = saledDealTime(communityName)
    list_return = []
    for element in L:
        list_return.append([element[0], element[2]])
    print(list_return)
    return list_return


# 3. 成交时间 -- 挂牌总价
def dealTime_hangoutPrice(communityName):
    L = saledDealTime(communityName)
    list_return = []
    for element in L:
        list_return.append([element[0], element[3]])
    print(list_return)
    return list_return


# 4. 成交时间 -- 交易周期
def dealTime_dealCycle(communityName):
    L = saledDealTime(communityName)
    list_return = []
    for element in L:
        list_return.append([element[0], element[6]])
    print(list_return)
    return list_return


# 5. 成交时间 -- 交易差价
def dealTime_DifPrice(communityName):
    L = saledDealTime(communityName)
    list_return = []
    for element in L:
        list_return.append([element[0], element[4]])
    print(list_return)
    return list_return


# 6. 成交时间 -- 成交数量
def dealTime_dealNum(communityName):
    L = saledDealTime(communityName)
    list_return = []
    for element in L:
        list_return.append([element[0], element[5]])
    print(list_return)
    return list_return


#
###########################################################
# 7. 装修程度 -- 均价
def DecorateStatus_dealUnitPrice(communityName):
    L = saledDecorateStatus(communityName)
    list_return = []
    for element in L:
        list_return.append([element[0], element[1]])
    print(list_return)
    return list_return


# 8. 装修程度 -- 成交总价
def DecorateStatus_dealPrice(communityName):
    L = saledDecorateStatus(communityName)
    list_return = []
    for element in L:
        list_return.append([element[0], element[2]])
    print(list_return)
    return list_return


# 9. 装修程度 -- 挂牌总价
def DecorateStatus_hangoutPrice(communityName):
    L = saledDecorateStatus(communityName)
    list_return = []
    for element in L:
        list_return.append([element[0], element[3]])
    print(list_return)
    return list_return


# 10. 装修程度 -- 交易周期
def DecorateStatus_dealCycle(communityName):
    L = saledDecorateStatus(communityName)
    list_return = []
    for element in L:
        list_return.append([element[0], element[6]])
    print(list_return)
    return list_return


# 11. 装修程度 -- 成交差价
def DecorateStatus_DifPrice(communityName):
    L = saledDecorateStatus(communityName)
    list_return = []
    for element in L:
        list_return.append([element[0], element[4]])
    print(list_return)
    return list_return


# 12. 装修程度 -- 成交数量
def DecorateStatus_dealNum(communityName):
    L = saledDecorateStatus(communityName)
    list_return = []
    for element in L:
        list_return.append([element[0], element[5]])
    print(list_return)
    return list_return


#########################################################
# 13. 户型 -- 均价
def HousingModel_dealUnitPrice(communityName):
    L = saledHousingModel(communityName)
    list_return = []
    for element in L:
        list_return.append([element[0], element[1]])
    print(list_return)
    return list_return


# 14. 户型 -- 成交总价
def HousingModel_dealPrice(communityName):
    L = saledHousingModel(communityName)
    list_return = []
    for element in L:
        list_return.append([element[0], element[2]])
    print(list_return)
    return list_return


# 15. 户型 -- 挂牌总价
def HousingModel_hangoutPrice(communityName):
    L = saledHousingModel(communityName)
    list_return = []
    for element in L:
        list_return.append([element[0], element[3]])
    print(list_return)
    return list_return


# 16. 户型 -- 交易周期
def HousingModel_dealCycle(communityName):
    L = saledHousingModel(communityName)
    list_return = []
    for element in L:
        list_return.append([element[0], element[6]])
    print(list_return)
    return list_return


# 17. 户型 -- 交易差价
def HousingModel_DifPrice(communityName):
    L = saledHousingModel(communityName)
    list_return = []
    for element in L:
        list_return.append([element[0], element[4]])
    print(list_return)
    return list_return


# 18. 户型 -- 成交数量
def HousingModel_dealNum(communityName):
    L = saledHousingModel(communityName)
    list_return = []
    for element in L:
        list_return.append([element[0], element[5]])
    print(list_return)
    return list_return


# 19. 是否有地铁 -- 均价
def Issubway_dealUnitPrice(communityName):
    L = saledIsSubway(communityName)
    list_return = []
    for element in L:
        list_return.append([element[0], element[1]])
    print(list_return)
    return list_return


# 20. 是否有地铁 -- 成交总价
def Issubway_dealPrice(communityName):
    L = saledIsSubway(communityName)
    list_return = []
    for element in L:
        list_return.append([element[0], element[2]])
    print(list_return)
    return list_return


# 21. 是否有地铁 -- 挂牌总价
def Issubway_hangoutPrice(communityName):
    L = saledIsSubway(communityName)
    list_return = []
    for element in L:
        list_return.append([element[0], element[3]])
    print(list_return)
    return list_return


# 22. 是否有地铁 -- 交易周期
def Issubway_dealCycle(communityName):
    L = saledIsSubway(communityName)
    list_return = []
    for element in L:
        list_return.append([element[0], element[6]])
    print(list_return)
    return list_return


# 23. 是否有地铁 -- 交易差价
def Issubway_DifPrice(communityName):
    L = saledIsSubway(communityName)
    list_return = []
    for element in L:
        list_return.append([element[0], element[4]])
    print(list_return)
    return list_return


# 24. 是否有地铁 -- 成交数量
def Issubway_dealNum(communityName):
    L = saledIsSubway(communityName)
    list_return = []
    for element in L:
        list_return.append([element[0], element[5]])
    print(list_return)
    return list_return


# 查询表格
def saledHouseChart(communityName):
    sql = "SELECT houseName2, houseArea2, housingModel2, dealUnitPrice2, dealPrice2, hangoutPrice2, " \
          "decorateStatus2, hangoutTime2, dealTime2, houseFloor2, housingHref2 FROM housessaled_table WHERE communityName2 = '{}' ".format(
        communityName)
    try:
        cur.execute(sql)
    except:
        print("查询失败")
    list_return = []
    for element in cur:
        dic = {}
        result = re.findall("(.*?) (.*?)", element[0])
        dic['houseName'] = result[0][0] + " " + result[1][0]
        dic['houseArea'] = str(element[1]) + '平方米'
        dic['houseModel'] = element[2].replace(" ", "")
        dic['dealUnitPrice'] = str(element[3]) + '元/平方米'
        dic['dealPrice'] = str(element[4]) + '万元'
        if element[5] != -1:
            dic['hangoutPrice'] = str(element[5]) + '万元'
        else:
            dic['hangoutPrice'] = str(element[4]) + '万元'
        dic['decorateStatus'] = element[6].replace(" ", "")
        try:
            result = re.findall("(.*?)\-(.*?)\-(.*?) ", element[7])
            dic['hangoutTime'] = result[0][0] + '.' + result[0][1] + '.' + result[0][2]
        except:
            dic['hangoutTime'] = element[7]
        dic['dealTime'] = re.findall("(.*?) 成交", element[8])[0]
        dic['houseFloor'] = element[9].replace(" ", "")
        dic['houseHref'] = element[10]
        list_return.append(dic)
    print(list_return)
    return list_return
