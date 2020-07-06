import pymysql, re
import areaInfo as info

# 连接数据库
try:
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='lianjiaTotal', port=3307)
    cur = conn.cursor()
    # print("登录数据库成功！！！")
except Exception:
    print("登录数据库出错，请检查用户名和密码！！！")


# 1.房屋户型扇形图
def saledHouseModel(communintyName):
    sql = "SELECT housingModel2 FROM housessaled_table WHERE communityName2 = '{}'".format(communintyName)
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


# 2.房屋总价扇形图
def saledDealPrice(communintyName):
    sql = "SELECT dealPrice2 FROM housessaled_table WHERE communityName2 = '{}'".format(communintyName)
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


# 3.房屋均价扇形图
def saledDealUnitPrice(communintyName):
    sql = "SELECT dealUnitPrice2 FROM housessaled_table WHERE communityName2 = '{}'".format(communintyName)
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


# 4.房屋面积扇形图
def saledHouseArea(communintyName):
    sql = "SELECT houseArea2 FROM housessaled_table WHERE communityName2 = '{}'".format(communintyName)
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


# 房源分析表
def saleHouseChart2(communityName):
    sql = "SELECT dealUnitPrice2, dealPrice2, hangoutPrice2, " \
          "dealCycle2, housingEstate FROM housessaled_table WHERE communityName2 = '{}'".format(
        communityName)
    try:
        cur.execute(sql)
    except:
        print("查询失败")
    sum_count = 0;
    sum_dealUnitPrice = 0;
    sum_dealPrice = 0;
    sum_hangoutPrice = 0;
    sum_dealCycle = 0;
    for element in cur:
        sum_count = sum_count + 1
        sum_dealUnitPrice = sum_dealUnitPrice + element[0]
        sum_dealPrice = sum_dealPrice + element[1]
        sum_hangoutPrice = sum_hangoutPrice + element[2]
        sum_dealCycle = sum_dealCycle + element[3]
        housingEstate = element[4]
    avg_dealUnitPrice = round(int(sum_dealUnitPrice) / sum_count, 2)
    avg_dealPrice = round(int(sum_dealPrice) / sum_count, 2)
    avg_hangoutPrice = round(int(sum_hangoutPrice) / sum_count, 2)
    avg_dealCycle = round(int(sum_dealCycle) / sum_count, 2)
    label_district = housingEstate.split("_")[1]
    label_county = ""
    for county_elem in info.county:
        for district_elem in info.district[county_elem]:
            if label_district == district_elem:
                label_county = county_elem
    list_return = {'communityName': communityName, 'label_county': info.area_info[label_county],
                   'label_district': info.area_info[label_district], 'avg_dealUnitPrice': avg_dealUnitPrice,
                   'avg_dealPrice': avg_dealPrice, 'avg_hangoutPrice': avg_hangoutPrice,
                   'avg_dealCycle': avg_dealCycle, 'sum_count': sum_count}
    print(list_return)
    return list_return
