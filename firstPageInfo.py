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


# 2.重庆：成交时间——总价
def CQ_DealTime_TotalPrice():
    sql = "SELECT * FROM saled_dealtime"
    try:
        curcompute.execute(sql)
    except:
        print("查询失败")
    list_return = []
    list_return.append(["成交时间", "总价"])
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
    print(list_return)
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
    print(list_return)
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
