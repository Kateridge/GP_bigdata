import pymysql,csv,re

# user = input("请输入数据库连接用户名：")
# password = input("请输入数据库连接密码：")
try:
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='lianjiaTotal', port=3307)
    cur = conn.cursor()
    print("登录数据库成功！！！")
except Exception:
    print("登录数据库出错，请检查用户名和密码！！！")


county = ['jiangbei', 'yubei', 'nanan', 'banan', 'shapingba', 'jiulongpo', 'yuzhong', 'dadukou', 'jiangjing', 'beibei', 'kaizhouqu', 'wushanxian1', 'wuxixian', 'xiushantujiazumiaozuzizhixian', 'youyangtujiazumiaozuzizhixian', 'rongchangqu', 'pengshuimiaozutujiazuzizhixian', 'zhongxian', 'fengjiexian', 'dianjiangxian', 'chengkouxian', 'tongliang', 'bishan', 'hechuang', 'changshou1', 'wanzhou', 'fuling']
district = {
    'jiangbei':['beibinlu', 'dashiba', 'dazhulin', 'guanyinqiao', 'haierlu', 'hongensi', 'huahuiyuan', 'huangnibang', 'jiangbeizui', 'jiazhou', 'longtousi', 'longxing', 'nanqiaosi', 'ranjiaba', 'shimahe', 'shizishan', 'songshuqiao', 'wulidian1', 'yuzui'],
    'yubei':['beihuan', 'caifuzhongxin1', 'cuiyun', 'huayuanxincun', 'huixing', 'konggangxincheng', 'lianglu', 'lijia', 'longxi', 'qibozhongxin', 'renhe', 'shuangbei', 'xinpaifang', 'yuanboyuan', 'yuanyang', 'yuelai', 'zhaomushan', 'zhongyanggongyuan'],
    'nanan':['bagongli', 'chayuanxinqu', 'danlonglu', 'danzishi', 'liugongli', 'nanbinlu', 'nanping', 'nanshan3', 'qigongli', 'rongqiaobandao', 'sigongli'],
    'banan':['jieshi', 'lijiatuo1', 'longzhouwan', 'nanquan', 'ronghuibandao', 'yudong2'],
    'shapingba':['chenjiaqiao', 'ciqikou', 'daping', 'daxuecheng2', 'fengtianlu', 'gongrencun', 'hualongqiao', 'laodonglu', 'lieshimu', 'lishuwan', 'sanxiaguangchang', 'shabinlu', 'shazhengjie', 'shiqiaopu', 'tianxingqiao', 'xiaolongkan', 'xiyong', 'yanggongqiao', 'yubeilu', 'zhanxilu'],
    'jiulongpo':['baguocheng', 'baishiyi', 'binjiangxincheng2', 'caiyunhu', 'chenjiaping', 'dongbuxincheng', 'dongwuyuan1', 'erlang', 'funiuxi', 'huangjueping', 'huayan', 'jiangjinjiaoxian', 'maoxiangou', 'mawangxiang', 'panlong1', 'shipingqiao', 'shuangshan', 'tiaodeng', 'xiejiawan', 'xipeng', 'yangjiaping', 'yuanjiagang'],
    'yuzhong':['chaotianmen', 'jiefangbei1', 'lianglukou', 'shangqingsi'],
    'dadukou':['buxingjie', 'dadukouqufu', 'jianshecun', 'jiugongmiao'],
    'jiangjing':['binjiangzhonglu', 'deganpianqu', 'dongmen1', 'langshanpianqu', 'laochengqu', 'xiangruipianqu', 'xiduan'],
    'beibei':['beibeilaochengqu', 'caijia', 'chaoyangqu4', 'chengbeixinqu', 'chengnanxinqu', 'xiema'],
    'kaizhouqu':['kaizhouqu1'],
    'wushanxian1':['wushanxian3'],
    'wuxixian':['yunyang1'],
    'xiushantujiazumiaozuzizhixian':['xiushan'],
    'youyangtujiazumiaozuzizhixian':['qianjiang1'],
    'rongchangqu':['dazu1', 'rongchang'],
    'pengshuimiaozutujiazuzizhixian':['pengshui', 'shizhu1', 'wulongxian1'],
    'zhongxian':['liangping1', 'zhongxian1'],
    'fengjiexian':['fengjie'],
    'dianjiangxian':['dianjiangxian1'],
    'chengkouxian':[],
    'tongliang':['tongliang 1'],
    'bishan':['bishan1'],
    'hechuang':['hechuan'],
    'changshou1':['changshou'],
    'wanzhou':['wanzhouqu'],
    'fuling':['fuling1']
}

# countytest = ['jiangbei','banan']
# districttest = {
#     'jiangbei': ['beibinlu', 'dashiba', 'dazhulin', 'guanyinqiao', 'haierlu', 'hongensi', 'huahuiyuan', 'huangnibang',
#                  'jiangbeizui', 'jiazhou', 'longtousi', 'longxing', 'nanqiaosi', 'ranjiaba', 'shimahe', 'shizishan',
#                  'songshuqiao', 'wulidian1', 'yuzui'],
#
#     'banan':['jieshi', 'lijiatuo1', 'longzhouwan', 'nanquan', 'ronghuibandao', 'yudong2'] #, 'lijiatuo1'
# }

countytest = ['jiangbei', 'yubei', 'nanan', 'banan', 'shapingba', 'jiulongpo', 'yuzhong', 'dadukou', 'jiangjing', 'beibei', 'kaizhouqu', 'wushanxian1', 'wuxixian', 'xiushantujiazumiaozuzizhixian', 'youyangtujiazumiaozuzizhixian', 'rongchangqu', 'pengshuimiaozutujiazuzizhixian', 'zhongxian', 'fengjiexian', 'dianjiangxian', 'chengkouxian', 'tongliang', 'bishan', 'hechuang', 'changshou1', 'wanzhou', 'fuling']
districttest = {
    'jiangbei':['beibinlu', 'dashiba', 'dazhulin', 'guanyinqiao', 'haierlu', 'hongensi', 'huahuiyuan', 'huangnibang', 'jiangbeizui', 'jiazhou', 'longtousi', 'longxing', 'nanqiaosi', 'ranjiaba', 'shimahe', 'shizishan', 'songshuqiao', 'wulidian1', 'yuzui'],
    'yubei':['beihuan', 'caifuzhongxin1', 'cuiyun', 'huayuanxincun', 'huixing', 'konggangxincheng', 'lianglu', 'lijia', 'longxi', 'qibozhongxin', 'renhe', 'shuangbei', 'xinpaifang', 'yuanboyuan', 'yuanyang', 'yuelai', 'zhaomushan', 'zhongyanggongyuan'],
    'nanan':['bagongli', 'chayuanxinqu', 'danlonglu', 'danzishi', 'liugongli', 'nanbinlu', 'nanping', 'nanshan3', 'qigongli', 'rongqiaobandao', 'sigongli'],
    'banan':['jieshi', 'lijiatuo1', 'longzhouwan', 'nanquan', 'ronghuibandao', 'yudong2'],
    'shapingba':['chenjiaqiao', 'ciqikou', 'daping', 'daxuecheng2', 'fengtianlu', 'gongrencun', 'hualongqiao', 'laodonglu', 'lieshimu', 'lishuwan', 'sanxiaguangchang', 'shabinlu', 'shazhengjie', 'shiqiaopu', 'tianxingqiao', 'xiaolongkan', 'xiyong', 'yanggongqiao', 'yubeilu', 'zhanxilu'],
    'jiulongpo':['baguocheng', 'baishiyi', 'binjiangxincheng2', 'caiyunhu', 'chenjiaping', 'dongbuxincheng', 'dongwuyuan1', 'erlang', 'funiuxi', 'huangjueping', 'huayan', 'jiangjinjiaoxian', 'maoxiangou', 'mawangxiang', 'panlong1', 'shipingqiao', 'shuangshan', 'tiaodeng', 'xiejiawan', 'xipeng', 'yangjiaping', 'yuanjiagang'],
    'yuzhong':['chaotianmen', 'jiefangbei1', 'lianglukou', 'shangqingsi'],
    'dadukou':['buxingjie', 'dadukouqufu', 'jianshecun', 'jiugongmiao'],
    'jiangjing':['binjiangzhonglu', 'deganpianqu', 'dongmen1', 'langshanpianqu', 'laochengqu', 'xiangruipianqu', 'xiduan'],
    'beibei':['beibeilaochengqu', 'caijia', 'chaoyangqu4', 'chengbeixinqu', 'chengnanxinqu', 'xiema'],
    'kaizhouqu':['kaizhouqu1'],
    'wushanxian1':['wushanxian3'],
    'wuxixian':['yunyang1'],
    'xiushantujiazumiaozuzizhixian':['xiushan'],
    'youyangtujiazumiaozuzizhixian':['qianjiang1'],
    'rongchangqu':['dazu1', 'rongchang'],
    'pengshuimiaozutujiazuzizhixian':['pengshui', 'shizhu1', 'wulongxian1'],
    'zhongxian':['liangping1', 'zhongxian1'],
    'fengjiexian':['fengjie'],
    'dianjiangxian':['dianjiangxian1'],
    'chengkouxian':[],
    'tongliang':['tongliang 1'],
    'bishan':['bishan1'],
    'hechuang':['hechuan'],
    'changshou1':['changshou'],
    'wanzhou':['wanzhouqu'],
    'fuling':['fuling1']
}

sql1 = "DELETE FROM county_table"
sql2 = "DELETE FROM district_table"
sql3 = "DELETE FROM housingestate_table"
sql4 = "DELETE FROM housesonsale_table"
sql5 = "DELETE FROM housessaled_table"
try:
    cur.execute(sql5)
    cur.execute(sql4)
    cur.execute(sql3)
    cur.execute(sql2)
    cur.execute(sql1)
    conn.commit()
except:
    conn.rollback()
    print("删除初始表格失败！！！")



# 插入county_table
for county_elem in county:
    sql = "INSERT INTO county_table VALUES ('{}')".format(county_elem)
    try:
        cur.execute(sql)
        conn.commit()
    except:
        conn.rollback()
        print("插入county({})失败".format(county_elem))

# 插入distinct_table
for county_elem in county:
    for district_elem in district[county_elem]:
        sql = "INSERT INTO district_table VALUES ('{}','{}')".format(district_elem, county_elem)
        try:
            cur.execute(sql)
            conn.commit()
        except:
            conn.rollback()
            print("插入district({})失败".format(district_elem))

# 插入housingestate_table
for county_elem in countytest:
    for district_elem in districttest[county_elem]:
        estate_list = []
        estate_saling = []
        estate_saled = []
        path = ".\data\salingt\{}\lianjia_saling_{}_{}.csv".format(county_elem,county_elem,district_elem)
        print(path)
        with open(path,'r',encoding='utf-8') as fp:
            reader = csv.reader(fp)
            for i,row in enumerate(reader):
                if i > 0:
                    estate_list.append(row[4])
                    estate_saling.append(row[4])
        path = ".\data\saledt\{}\lianjia_saled_{}_{}.csv".format(county_elem,county_elem,district_elem)
        print(path)
        with open(path,'r',encoding='utf-8') as fp:
            reader = csv.reader(fp)
            for i,row in enumerate(reader):
                if i > 0:
                    estate_list.append(row[2])
                    estate_saled.append(row[2])
        estate_set = set(estate_list)
        estate_list_set = list(estate_set)

        estate_num_saling = [0] * len(estate_list_set)
        estate_num_saled = [0] * len(estate_list_set)
        for i in range(0,len(estate_list_set)):
            for e in estate_saling:
                if estate_list_set[i] == e:
                    estate_num_saling[i] = estate_num_saling[i] + 1
        for i in range(0,len(estate_list_set)):
            for e in estate_saled:
                if estate_list_set[i] == e:
                    estate_num_saled[i] = estate_num_saled[i] + 1

        for i in range(0,len(estate_list_set)):
            sql = "INSERT INTO housingestate_table VALUES ('{}','{}',{},{})".format(estate_list_set[i]+'_'+district_elem,district_elem,estate_num_saling[i],estate_num_saled[i])
            try:
                cur.execute(sql)
                conn.commit()
            except:
                conn.rollback()
                print("插入estate({}   {})失败".format(estate_list_set[i],district_elem))

# 插入housesOnSale_table
for county_elem in countytest:
    for district_elem in districttest[county_elem]:
        path = ".\data\salingt\{}\lianjia_saling_{}_{}.csv".format(county_elem,county_elem,district_elem)
        with open(path,'r',encoding='utf-8') as fp:
            reader = csv.reader(fp)
            for i, row in enumerate(reader):
                if i > 0:
                    houseID = county_elem + "_" + district_elem + "_" + str(i)
                    housingEstate = row[4] + "_" + district_elem
                    houseName = row[0]
                    houseHref = row[1]

                    try:
                        price = float(re.findall("(.*?)万", row[2])[0])
                    except:
                        price = -1

                    try:
                        unitPrice = float(re.findall("(.*?)元/平方米", row[3])[0])
                    except:
                        unitPrice = -1

                    communityName = row[4]
                    areaName = row[5]
                    visitTime = row[6]
                    houseModel = row[7]
                    houseFloor = row[8]

                    try:
                        houseArea = float(re.findall("(.*?)㎡",row[9])[0])
                    except:
                        houseArea = -1

                    houseStructure = row[10]

                    try:
                        innerArea = float(re.findall("(.*?)㎡",row[11])[0])
                    except:
                        innerArea = -1

                    houseType = row[12]
                    houseFaced = row[13]
                    architectureStructure = row[14]
                    decorateStatus = row[15]
                    householder = row[16]
                    hasElevator = row[17]
                    hangoutTime = row[18]
                    dealOwner = row[19]
                    lastDeal = row[20]
                    houseUsage = row[21]
                    houseAgeLimit = row[22]
                    houseBelong = row[23]
                    mortgageInfo = row[24]
                    houseCopy = row[25]

                    if row[26].find("地铁") != -1:
                        subway = 1
                    else:
                        subway = 0

                    houseLabel = row[26]
                    houseTransport = row[27].replace("'","")
                    housePackage = row[28].replace("'","")
                    neighborInfo = row[29].replace("'","")
                    coreDeal = row[30].replace("'","")

                    print("saling:" + houseID+"     "+houseHref)

                    sql = "INSERT INTO housesonsale_table VALUES ('{}','{}','{}','{}',{},{},'{}','{}','{}','{}','{}',{},'{}',{},'{}','{}'," \
                          "'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}',{},'{}','{}','{}','{}','{}')".format(
                        houseID,housingEstate,houseName,houseHref,price,unitPrice,communityName,areaName,
                        visitTime,houseModel,houseFloor,houseArea,houseStructure,innerArea,houseType,houseFaced,
                        architectureStructure,decorateStatus,householder,hasElevator,hangoutTime,dealOwner,lastDeal,houseUsage,
                        houseAgeLimit,houseBelong,mortgageInfo,houseCopy,subway,houseLabel,houseTransport,housePackage,
                        neighborInfo,coreDeal
                    )
                    try:
                        cur.execute(sql)
                        conn.commit()
                    except:
                        conn.rollback()
                        print("housingestate({})失败".format(houseID))

# 插入housesSaled_table
for county_elem in countytest:
    for district_elem in districttest[county_elem]:
        path = ".\data\saledt\{}\lianjia_saled_{}_{}.csv".format(county_elem,county_elem,district_elem)
        with open(path,'r',encoding='utf-8') as fp:
            reader = csv.reader(fp)
            for i, row in enumerate(reader):
                if i > 0:
                    houseID = county_elem + "_" + district_elem + "_" + str(i)
                    housingEstate = row[2] + "_" + district_elem

                    houseName = row[0]
                    houseHref = row[1]
                    communityName = row[2]
                    dealTime = row[3]

                    try:
                        dealPrice = float(re.findall("(.*?)万",row[4])[0])
                    except:
                        dealPrice = -1
                    try:
                        dealUnitPrice = float(re.findall("(.*?)元/平方米",row[5])[0])
                    except:
                        dealUnitPrice = -1
                    try:
                        hangoutPrice = float(re.findall("(.*?)万",row[6])[0])
                    except:
                        hangoutPrice = -1
                    try:
                        dealCycle = int(re.findall("(.*?)天",row[7])[0])
                    except:
                        dealCycle = -1
                    try:
                        adjustPriceTimes = int(re.findall("(.*?)次",row[8])[0])
                    except:
                        adjustPriceTimes = -1
                    try:
                        visitTimes = int(re.findall("(.*?)次",row[9])[0])
                    except:
                        visitTimes = -1
                    try:
                        followsNum = int(re.findall("(.*?)人",row[10])[0])
                    except:
                        followsNum = -1
                    try:
                        viewNum = int(re.findall("(.*?)人",row[11])[0])
                    except:
                        viewNum = -1

                    houseModel = row[12]
                    houseFloor = row[13]

                    try:
                        houseArea = float(re.findall("(.*?)㎡",row[14])[0])
                    except:
                        houseArea = -1

                    houseStructure = row[15]

                    try:
                        innerArea = float(re.findall("(.*?)㎡",row[16])[0])
                    except:
                        innerArea = -1

                    houseType = row[17]
                    houseFaced = row[18]

                    try:
                        buildYear = int(row[19])
                    except:
                        buildYear = -1

                    decorateStatus = row[20]
                    architectureStructure = row[21]
                    householdPer = row[23]
                    hasElevator = row[24]
                    lianjiaID = row[25]
                    dealOwner = row[26]
                    hangoutTime = row[27]
                    houseUsage = row[28]
                    houseAgeLimit = row[29]
                    houseBelong = row[30]
                    recordDetail = row[31]

                    if row[32].find("地铁") != -1:
                        subway = 1
                    else:
                        subway = 0

                    houseLabel = row[32]
                    CoreDeal = row[33].replace("'","")
                    neighborInfo = row[34].replace("'","")
                    housePackage = row[35].replace("'","")
                    houseTransport = row[36].replace("'","")

                    # print(houseID, housingEstate, houseName, houseHref, communityName, dealTime, dealPrice, dealUnitPrice,
                    #     hangoutPrice, dealCycle, adjustPriceTimes, visitTimes, followsNum, viewNum, houseModel,houseFloor,
                    #     houseArea, houseStructure, innerArea, houseType, houseFaced, buildYear, decorateStatus,architectureStructure,
                    #     householdPer, hasElevator, lianjiaID, dealOwner, hangoutTime, houseUsage, houseAgeLimit,houseBelong,
                    #     recordDetail, subway, houseLabel, CoreDeal, neighborInfo, housePackage, houseTransport)

                    print("saled:" + houseID + "     " + houseHref)

                    sql = "INSERT INTO housessaled_table VALUES ('{}','{}','{}','{}','{}','{}',{},{},{},{},{},{},{},{},'{}','{}'," \
                          "{},'{}',{},'{}','{}',{},'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}'," \
                          "'{}',{},'{}','{}','{}','{}','{}')".format(
                        houseID, housingEstate, houseName, houseHref, communityName, dealTime, dealPrice, dealUnitPrice,
                        hangoutPrice, dealCycle, adjustPriceTimes, visitTimes, followsNum, viewNum, houseModel, houseFloor,
                        houseArea, houseStructure, innerArea, houseType, houseFaced, buildYear, decorateStatus, architectureStructure,
                        householdPer, hasElevator, lianjiaID, dealOwner, hangoutTime, houseUsage, houseAgeLimit, houseBelong,
                        recordDetail, subway, houseLabel, CoreDeal, neighborInfo, housePackage, houseTransport
                    )
                    try:
                        cur.execute(sql)
                        conn.commit()
                    except:
                        conn.rollback()
                        print("housingestate({})失败".format(houseID))


cur.close()
conn.close()

