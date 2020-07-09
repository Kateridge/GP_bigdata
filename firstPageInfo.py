import connectTodb as db

curcompute = db.curcompute


# 1.重庆：成交时间——均价
def CQ_DealTime_UnitPrice():
    sql = "SELECT * FROM saled_dealtime"
    try:
        curcompute.execute(sql)
    except:
        print("查询失败")
    list_return = []
    list_return.append(["成交时间", "均价"])
    for element in curcompute:
        list_return.append([element[1], float(element[3])])
    print(list_return)
    return list_return


# 2.重庆：成交时间——挂牌价，成交价
def CQ_DealTime_TotalPrice():
    sql = "SELECT * FROM saled_dealtime"
    try:
        curcompute.execute(sql)
    except:
        print("查询失败")
    list_return = []
    list_return.append(["成交时间", "挂牌价"])
    for element in curcompute:
        list_return.append([element[1], float(element[5])])
    print(list_return)
    return list_return


def CQ_DealTime_TotalPrice2():
    sql = "SELECT * FROM saled_dealtime"
    try:
        curcompute.execute(sql)
    except:
        print("查询失败")
    list_return = []
    list_return.append(["成交时间", "成交价"])
    for element in curcompute:
        list_return.append([element[1], float(element[4])])
    print(list_return)
    return list_return


# 3.成交数最高的5个商圈
def Saled_TopFive_District_By_Number():
    sql = "SELECT * FROM saled_sort_district_by_number"
    try:
        curcompute.execute(sql)
    except:
        print("查询失败")
    count = 0
    list_return = []
    for element in curcompute:
        if count < 5:
            list_return.append([element[1], int(element[2])])
            count = count + 1
        else:
            break;
    print(list_return)
    return list_return


# 4.在售均价最高的5个商圈
def Saling_TopFive_District_By_Unitprice():
    sql = "SELECT * FROM saling_sort_district_by_unitprice"
    try:
        curcompute.execute(sql)
    except:
        print("查询失败")
    count = 0
    list_return = []
    for element in curcompute:
        if count < 5:
            list_return.append([element[1], float(element[3])])
            count = count + 1
        else:
            break;
    print(list_return)
    return list_return


# 5.扇形图——成交房屋户型
def CQ_Saled_HouseModel():
    sql = "SELECT * FROM saled_housemodel"
    try:
        curcompute.execute(sql)
    except:
        print("查询失败")
    list_return = []
    for element in curcompute:
        dic = {}
        dic['value'] = int(element[2])
        dic['name'] = element[1]
        list_return.append(dic)
    return list_return


# 6.扇形图——在售房屋户型
def CQ_Saling_HouseModel():
    sql = "SELECT * FROM saling_housemodel"
    try:
        curcompute.execute(sql)
    except:
        print("查询失败")
    list_return = []
    for element in curcompute:
        dic = {}
        dic['value'] = int(element[2])
        dic['name'] = element[1]
        list_return.append(dic)
    return list_return


# 7.扇形图——在售房屋朝向
def CQ_Saling_HouseFaced():
    sql = "SELECT * FROM saling_housefaced"
    try:
        curcompute.execute(sql)
    except:
        print("查询失败")
    list_return = []
    for element in curcompute:
        dic = {}
        dic['value'] = int(element[2])
        dic['name'] = element[1]
        list_return.append(dic)
    print(list_return)
    return list_return


# 8.扇形图——在售，成交地铁情况
def CQ_IsSubway():
    iscount = 0;
    isnotcount = 0
    sql = "SELECT * FROM saling_hassubway"
    try:
        curcompute.execute(sql)
    except:
        print("查询失败")
    for element in curcompute:
        if element[1] == 0:
            isnotcount = isnotcount + int(element[2])
        else:
            iscount = iscount + int(element[2])

    sql = "SELECT * FROM saled_hassubway"
    try:
        curcompute.execute(sql)
    except:
        print("查询失败")
    for element in curcompute:
        if element[1] == 0:
            isnotcount = isnotcount + int(element[2])
        else:
            iscount = iscount + int(element[2])
    list_return = []
    list_return.append({'value': iscount, 'name': '附近有地铁'})
    list_return.append({'value': isnotcount, 'name': '附近无地铁'})
    print(list_return)
    return list_return


# 9.扇形图——在售房屋装修情况
def CQ_Saling_Decoration():
    sql = "SELECT * FROM saling_decoration"
    try:
        curcompute.execute(sql)
    except:
        print("查询失败")
    list_return = []
    for element in curcompute:
        dic = {}
        dic['value'] = int(element[2])
        dic['name'] = element[1]
        list_return.append(dic)
    return list_return


# 10.扇形图——成交房屋装修情况
def CQ_Saled_Decoration():
    sql = "SELECT * FROM saled_decoration"
    try:
        curcompute.execute(sql)
    except:
        print("查询失败")
    list_return = []
    for element in curcompute:
        dic = {}
        dic['value'] = int(element[2])
        dic['name'] = element[1]
        list_return.append(dic)
    return list_return


# 11.扇形图——在售房屋用途情况
def CQ_Saling_Usage():
    sql = "SELECT * FROM saling_houseusage"
    try:
        curcompute.execute(sql)
    except:
        print("查询失败")
    list_return = []
    for element in curcompute:
        dic = {}
        dic['value'] = int(element[2])
        dic['name'] = element[1]
        list_return.append(dic)
    return list_return


# 12.扇形图——成交房屋用途情况
def CQ_Saled_Usage():
    sql = "SELECT * FROM saled_houseusage"
    try:
        curcompute.execute(sql)
    except:
        print("查询失败")
    list_return = []
    for element in curcompute:
        dic = {}
        dic['value'] = int(element[2])
        dic['name'] = element[1]
        list_return.append(dic)
    return list_return

# 13.扇形图——在售房屋楼层情况
def CQ_Saling_Floor():
    sql = "SELECT * FROM saling_housefloor"
    try:
        curcompute.execute(sql)
    except:
        print("查询失败")
    list_return = []
    for element in curcompute:
        dic = {}
        dic['value'] = int(element[2])
        dic['name'] = element[1]
        list_return.append(dic)
    return list_return


# 14.扇形图——成交房屋楼层情况
def CQ_Saled_Floor():
    sql = "SELECT * FROM saled_housefloor"
    try:
        curcompute.execute(sql)
    except:
        print("查询失败")
    list_return = []
    for element in curcompute:
        dic = {}
        dic['value'] = int(element[2])
        dic['name'] = element[1]
        list_return.append(dic)
    return list_return



# 15.扇形图——合并房屋户型
def Merge_HouseModel():
    saled_model = CQ_Saled_HouseModel()
    saling_model = CQ_Saling_HouseModel()
    list_model1 = []; list_value1 = []
    list_model2 = []; list_value2 = []
    list_model = []
    for element in saled_model:
        list_model1.append(element['name'])
        list_value1.append(element['value'])
        list_model.append(element['name'])
    for element in saling_model:
        list_model2.append(element['name'])
        list_value2.append(element['value'])
        list_model.append(element['name'])
    set_model = set(list_model)
    list_model = list(set_model)
    list_value = [0]*len(list_model)
    for i in range(0,len(list_model)):
        for j in range(0,len(list_model1)):
            if list_model[i] == list_model1[j]:
                list_value[i] = list_value[i] + list_value1[j]
        for j in range(0,len(list_model2)):
            if list_model[i] == list_model2[j]:
                list_value[i] = list_value[i] + list_value2[j]
    list_return = []
    for i in range(0,len(list_model)):
        dic = {}
        dic['value'] = list_value[i]
        dic['name'] = list_model[i]
        list_return.append(dic)
    print(list_return)
    return list_return


# 16.扇形图——合并房屋装修情况
def Merge_HouseDecoration():
    saled_decoration = CQ_Saled_Decoration()
    saling_decoration = CQ_Saling_Decoration()
    list_decoration1 = []; list_value1 = []
    list_decoration2 = []; list_value2 = []
    list_decoration = []
    for element in saled_decoration:
        list_decoration1.append(element['name'])
        list_value1.append(element['value'])
        list_decoration.append(element['name'])
    for element in saling_decoration:
        list_decoration2.append(element['name'])
        list_value2.append(element['value'])
        list_decoration.append(element['name'])
    set_decoration = set(list_decoration)
    list_decoration = list(set_decoration)
    list_value = [0]*len(list_decoration)
    for i in range(0,len(list_decoration)):
        for j in range(0,len(list_decoration1)):
            if list_decoration[i] == list_decoration1[j]:
                list_value[i] = list_value[i] + list_value1[j]
        for j in range(0,len(list_decoration2)):
            if list_decoration[i] == list_decoration2[j]:
                list_value[i] = list_value[i] + list_value2[j]
    list_return = []
    for i in range(0,len(list_decoration)):
        dic = {}
        dic['value'] = list_value[i]
        dic['name'] = list_decoration[i]
        list_return.append(dic)
    print(list_return)
    return list_return


# 17.扇形图——合并房屋用途
def Merge_HouseUsage():
    saled_usage = CQ_Saled_Usage()
    saling_usage = CQ_Saling_Usage()
    list_usage1 = []; list_value1 = []
    list_usage2 = []; list_value2 = []
    list_usage = []
    for element in saled_usage:
        list_usage1.append(element['name'])
        list_value1.append(element['value'])
        list_usage.append(element['name'])
    for element in saling_usage:
        list_usage2.append(element['name'])
        list_value2.append(element['value'])
        list_usage.append(element['name'])
    set_usage = set(list_usage)
    list_usage = list(set_usage)
    list_value = [0]*len(list_usage)
    for i in range(0,len(list_usage)):
        for j in range(0,len(list_usage1)):
            if list_usage[i] == list_usage1[j]:
                list_value[i] = list_value[i] + list_value1[j]
        for j in range(0,len(list_usage2)):
            if list_usage[i] == list_usage2[j]:
                list_value[i] = list_value[i] + list_value2[j]
    list_return = []
    for i in range(0,len(list_usage)):
        dic = {}
        dic['value'] = list_value[i]
        dic['name'] = list_usage[i]
        list_return.append(dic)
    print(list_return)
    return list_return

# 18.扇形图——合并房屋装修情况
def Merge_HouseFloor():
    saled_floor = CQ_Saled_Floor()
    saling_floor = CQ_Saling_Floor()
    list_floor1 = []; list_value1 = []
    list_floor2 = []; list_value2 = []
    list_floor = []
    for element in saled_floor:
        list_floor1.append(element['name'])
        list_value1.append(element['value'])
        list_floor.append(element['name'])
    for element in saling_floor:
        list_floor2.append(element['name'])
        list_value2.append(element['value'])
        list_floor.append(element['name'])
    set_floor = set(list_floor)
    list_floor = list(set_floor)
    list_value = [0]*len(list_floor)
    for i in range(0,len(list_floor)):
        for j in range(0,len(list_floor1)):
            if list_floor[i] == list_floor1[j]:
                list_value[i] = list_value[i] + list_value1[j]
        for j in range(0,len(list_floor2)):
            if list_floor[i] == list_floor2[j]:
                list_value[i] = list_value[i] + list_value2[j]
    list_return = []
    for i in range(0,len(list_floor)):
        dic = {}
        dic['value'] = list_value[i]
        dic['name'] = list_floor[i]
        list_return.append(dic)
    print(list_return)
    return list_return

CQ_DealTime_TotalPrice()