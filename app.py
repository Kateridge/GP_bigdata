import pymysql
from flask import Flask, render_template, send_file, request
import saledHousePriceAnalysis as saled
import saledHouseSourceAnalysis as saled_src
import saledBydistrict as saled_district
import salingBycommunity as saling
import salingBydistrict as saling2
import firstPageInfo as index

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False


@app.route('/')
def jump_home1():
    graph1_data = index.CQ_DealTime_UnitPrice()
    graph2_data = index.CQ_DealTime_TotalPrice()
    top5_num = index.Saled_TopFive_District_By_Number()
    top5_unitprice = index.Saling_TopFive_District_By_Unitprice()
    graph3_data = index.Merge_HouseModel()
    graph4_data = index.Merge_HouseDecoration()
    graph5_data = index.CQ_Saling_HouseFaced()
    graph6_data = index.CQ_IsSubway()
    graph7_data = index.CQ_Saling_Floor()
    graph8_data = index.Merge_HouseUsage()
    graph9_data = index.CQ_DealTime_TotalPrice2()
    return render_template('index.html', graph1_data=graph1_data, graph2_data=graph2_data,
                           top5_num=top5_num, top5_unitprice=top5_unitprice,
                           graph5_data=graph5_data, graph6_data=graph6_data,
                           graph3_data=graph3_data, graph4_data=graph4_data,
                           graph7_data=graph7_data, graph8_data=graph8_data,
                           graph9_data=graph9_data)


@app.route('/index.html')
def jump_home2():
    graph1_data = index.CQ_DealTime_UnitPrice()
    graph2_data = index.CQ_DealTime_TotalPrice()
    top5_num = index.Saled_TopFive_District_By_Number()
    top5_unitprice = index.Saling_TopFive_District_By_Unitprice()
    graph3_data = index.Merge_HouseModel()
    graph4_data = index.Merge_HouseDecoration()
    graph5_data = index.CQ_Saling_HouseFaced()
    graph6_data = index.CQ_IsSubway()
    graph7_data = index.CQ_Saling_Floor()
    graph8_data = index.Merge_HouseUsage()
    graph9_data = index.CQ_DealTime_TotalPrice2()
    return render_template('index.html', graph1_data=graph1_data, graph2_data=graph2_data,
                           top5_num=top5_num, top5_unitprice=top5_unitprice,
                           graph5_data=graph5_data, graph6_data=graph6_data,
                           graph3_data=graph3_data, graph4_data=graph4_data,
                           graph7_data=graph7_data, graph8_data=graph8_data,
                           graph9_data=graph9_data)


@app.route('/history_district.html')
def jump_history_district():
    return render_template('history_district.html')


@app.route('/history_district_analyze.html')
def jump_history_district2():
    para = request.args
    graph1_data = saled_district.dealtime_and_price(para['district_name'], para['area_name'])
    graph2_data = saled_district.dealtime_and_price2(para['district_name'], para['area_name'])
    data_table = saled_district.saledHouseChart3(para['district_name'], para['area_name'])
    communityName = para['area_name']
    return render_template('history_district_analyze.html', graph1_data=graph1_data, graph2_data=graph2_data,
                           data_table=data_table, communityName=communityName)


@app.route('/history_price.html')
def jump_history_price1():
    return render_template('history_price.html')


@app.route('/history_source.html')
def jump_history_source1():
    return render_template('history_source.html')


@app.route('/history_price_analyze.html', methods=['POST'])
def jump_history_price2():
    para = request.form
    communityName = para['community_name']
    # x轴成交时间
    if para['x_value'] == 'Dealdate' and para['y_value'] == 'AveragePrice':
        data = saled.dealTime_dealUnitPrice(para['community_name'])
        data_table = saled.saledHouseChart(para['community_name'])
        flag = 1
    elif para['x_value'] == 'Dealdate' and para['y_value'] == 'TotalPrice':
        data = saled.dealTime_dealPrice(para['community_name'])
        data_table = saled.saledHouseChart(para['community_name'])
        flag = 2
    elif para['x_value'] == 'Dealdate' and para['y_value'] == 'TotalPrice2':
        data = saled.dealTime_hangoutPrice(para['community_name'])
        data_table = saled.saledHouseChart(para['community_name'])
        flag = 3
    elif para['x_value'] == 'Dealdate' and para['y_value'] == 'SaleTime':
        data = saled.dealTime_dealCycle(para['community_name'])
        data_table = saled.saledHouseChart(para['community_name'])
        flag = 4
    elif para['x_value'] == 'Dealdate' and para['y_value'] == 'DifferentPrice':
        data = saled.dealTime_DifPrice(para['community_name'])
        data_table = saled.saledHouseChart(para['community_name'])
        flag = 5
    elif para['x_value'] == 'Dealdate' and para['y_value'] == 'SaleNumber':
        data = saled.dealTime_dealNum(para['community_name'])
        data_table = saled.saledHouseChart(para['community_name'])
        flag = 6
    # x轴装修
    elif para['x_value'] == 'Status' and para['y_value'] == 'AveragePrice':
        data = saled.DecorateStatus_dealUnitPrice(para['community_name'])
        data_table = saled.saledHouseChart(para['community_name'])
        flag = 7
    elif para['x_value'] == 'Status' and para['y_value'] == 'TotalPrice':
        data = saled.DecorateStatus_dealPrice(para['community_name'])
        data_table = saled.saledHouseChart(para['community_name'])
        flag = 8
    elif para['x_value'] == 'Status' and para['y_value'] == 'TotalPrice2':
        data = saled.DecorateStatus_hangoutPrice(para['community_name'])
        data_table = saled.saledHouseChart(para['community_name'])
        flag = 9
    elif para['x_value'] == 'Status' and para['y_value'] == 'SaleTime':
        data = saled.DecorateStatus_dealCycle(para['community_name'])
        data_table = saled.saledHouseChart(para['community_name'])
        flag = 10
    elif para['x_value'] == 'Status' and para['y_value'] == 'DifferentPrice':
        data = saled.DecorateStatus_DifPrice(para['community_name'])
        data_table = saled.saledHouseChart(para['community_name'])
        flag = 11
    elif para['x_value'] == 'Status' and para['y_value'] == 'SaleNumber':
        data = saled.DecorateStatus_dealNum(para['community_name'])
        data_table = saled.saledHouseChart(para['community_name'])
        flag = 12
    # x轴户型
    elif para['x_value'] == 'Housetype' and para['y_value'] == 'AveragePrice':
        data = saled.HousingModel_dealUnitPrice(para['community_name'])
        data_table = saled.saledHouseChart(para['community_name'])
        flag = 13
    elif para['x_value'] == 'Housetype' and para['y_value'] == 'TotalPrice':
        data = saled.HousingModel_dealPrice(para['community_name'])
        data_table = saled.saledHouseChart(para['community_name'])
        flag = 14
    elif para['x_value'] == 'Housetype' and para['y_value'] == 'TotalPrice2':
        data = saled.HousingModel_hangoutPrice(para['community_name'])
        data_table = saled.saledHouseChart(para['community_name'])
        flag = 15
    elif para['x_value'] == 'Housetype' and para['y_value'] == 'SaleTime':
        data = saled.HousingModel_dealCycle(para['community_name'])
        data_table = saled.saledHouseChart(para['community_name'])
        flag = 16
    elif para['x_value'] == 'Housetype' and para['y_value'] == 'DifferentPrice':
        data = saled.HousingModel_DifPrice(para['community_name'])
        data_table = saled.saledHouseChart(para['community_name'])
        flag = 17
    elif para['x_value'] == 'Housetype' and para['y_value'] == 'SaleNumber':
        data = saled.HousingModel_dealNum(para['community_name'])
        data_table = saled.saledHouseChart(para['community_name'])
        flag = 18
    # x轴地铁
    elif para['x_value'] == 'Underground' and para['y_value'] == 'AveragePrice':
        data = saled.Issubway_dealUnitPrice(para['community_name'])
        data_table = saled.saledHouseChart(para['community_name'])
        flag = 19
    elif para['x_value'] == 'Underground' and para['y_value'] == 'TotalPrice':
        data = saled.Issubway_dealPrice(para['community_name'])
        data_table = saled.saledHouseChart(para['community_name'])
        flag = 20
    elif para['x_value'] == 'Underground' and para['y_value'] == 'TotalPrice2':
        data = saled.Issubway_hangoutPrice(para['community_name'])
        data_table = saled.saledHouseChart(para['community_name'])
        flag = 21
    elif para['x_value'] == 'Underground' and para['y_value'] == 'SaleTime':
        data = saled.Issubway_dealCycle(para['community_name'])
        data_table = saled.saledHouseChart(para['community_name'])
        flag = 22
    elif para['x_value'] == 'Underground' and para['y_value'] == 'DifferentPrice':
        data = saled.Issubway_DifPrice(para['community_name'])
        data_table = saled.saledHouseChart(para['community_name'])
        flag = 23
    elif para['x_value'] == 'Underground' and para['y_value'] == 'SaleNumber':
        data = saled.Issubway_dealNum(para['community_name'])
        data_table = saled.saledHouseChart(para['community_name'])
        flag = 24
    return render_template('history_price_analyze.html', data=data, flag=flag, data_table=data_table,
                           communityName=communityName)


@app.route('/history_source_analyze.html', methods=['GET'])
def jump_history_source2():
    para = request.args
    graph1_data = saled_src.saledHouseModel(para['community_name'])
    graph2_data = saled_src.saledDealPrice(para['community_name'])
    graph3_data = saled_src.saledDealUnitPrice(para['community_name'])
    graph4_data = saled_src.saledHouseArea(para['community_name'])
    data_table = saled_src.saleHouseChart2(para['community_name'])
    communityName = para['community_name']
    return render_template('history_source_analyze.html', graph1_data=graph1_data, graph2_data=graph2_data,
                           graph3_data=graph3_data, graph4_data=graph4_data, data_table=data_table, communityName=communityName)


@app.route('/onsale_bycommunity.html')
def jump_onsale_community1():
    return render_template('onsale_bycommunity.html')


@app.route('/onsale_bydistrict.html')
def jump_onsale_district1():
    return render_template('onsale_bydistrict.html')


@app.route('/onsale_bycommunity_analyze.html', methods=['GET'])
def jump_onsale_community2():
    para = request.args
    graph1_data = saling.salingHouseModel(para['community_name'])
    graph2_data = saling.salingDecorateStatus1(para['community_name'])
    graph3_data = saling.salingHouseArea(para['community_name'])
    graph4_data = saling.salingUnitPrice(para['community_name'])
    graph5_data = saling.salingDealPrice(para['community_name'])
    graph6_data = saling.salingHouseFaced1(para['community_name'])
    graph7_data = saling.hangoutTime_unitPrice(para['community_name'])
    graph8_data = saling.hangoutTime_price(para['community_name'])
    data_table = saling.salingHouseChart(para['community_name'])
    communityName = para['community_name']
    return render_template('onsale_bycommunity_analyze.html', graph1_data=graph1_data, graph2_data=graph2_data,
                           graph3_data=graph3_data, graph4_data=graph4_data, graph5_data=graph5_data,
                           graph6_data=graph6_data, graph7_data=graph7_data, graph8_data=graph8_data,
                           data_table=data_table, communityName=communityName)


@app.route('/onsale_bydistrict_analyze.html', methods=['POST'])
def jump_onsale_district2():
    para = request.form
    data = saling2.salingHouseInfo(para['district_name'], para['area_name'])
    data_table = saling2.salingHouseChart2(para['district_name'], para['area_name'])
    communityName = para['area_name']
    return render_template('onsale_bydistrict_analyze.html', data=data, data_table=data_table, communityName=communityName)



if __name__ == '__main__':
    app.run()
