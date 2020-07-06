import pymysql
from flask import Flask, render_template, send_file, request
import saledHousePriceAnalysis as saled
import saledHouseSourceAnalysis as saled_src
import salingBycommunity as saling
import salingBydistrict as saling2

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False


@app.route('/')
def jump_home1():
    return render_template('index.html')


@app.route('/index.html')
def jump_home2():
    return render_template('index.html')


@app.route('/history_price.html')
def jump_history_price1():
    return render_template('history_price.html')


@app.route('/history_source.html')
def jump_history_source1():
    return render_template('history_source.html')


@app.route('/history_price_analyze.html', methods=['POST'])
def jump_history_price2():
    para = request.form
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
    return render_template('history_price_analyze.html', data=data, flag=flag, data_table=data_table)


@app.route('/history_source_analyze.html', methods=['POST'])
def jump_history_source2():
    para = request.form
    if para['select_value'] == 'Housetype':
        data = saled_src.saledHouseModel(para['community_name'])
        data_table = saled_src.saleHouseChart2(para['community_name'])
        flag = 1
    elif para['select_value'] == 'TotalPrice':
        data = saled_src.saledDealPrice(para['community_name'])
        data_table = saled_src.saleHouseChart2(para['community_name'])
        flag = 2
    elif para['select_value'] == 'AveragePrice':
        data = saled_src.saledDealUnitPrice(para['community_name'])
        data_table = saled_src.saleHouseChart2(para['community_name'])
        flag = 3
    elif para['select_value'] == 'HouseSquare':
        data = saled_src.saledHouseArea(para['community_name'])
        data_table = saled_src.saleHouseChart2(para['community_name'])
        flag = 4
    return render_template('history_source_analyze.html', data=data, flag=flag, data_table=data_table)


@app.route('/onsale_bycommunity.html')
def jump_blank():
    return render_template('onsale_bycommunity.html')


@app.route('/onsale_bydistrict.html')
def jump_profile():
    return render_template('onsale_bydistrict.html')


@app.route('/onsale_bycommunity_analyze.html', methods=['POST'])
def jump_community():
    para = request.form
    if para['select_value'] == 'Housetype':
        data = saling.salingHouseModel(para['community_name'])
        data_table = saling.salingHouseChart(para['community_name'])
        flag = 1
    elif para['select_value'] == 'Status':
        data = saling.salingDecorateStatus1(para['community_name'])
        data_table = saling.salingHouseChart(para['community_name'])
        flag = 2
    elif para['select_value'] == 'Housesquare':
        data = saling.salingHouseArea(para['community_name'])
        data_table = saling.salingHouseChart(para['community_name'])
        flag = 3
    elif para['select_value'] == 'Averageprice':
        data = saling.salingUnitPrice(para['community_name'])
        data_table = saling.salingHouseChart(para['community_name'])
        flag = 4
    elif para['select_value'] == 'Totalprice':
        data = saling.salingDealPrice(para['community_name'])
        data_table = saling.salingHouseChart(para['community_name'])
        flag = 5
    elif para['select_value'] == 'Orientation':
        data = saling.salingHouseFaced1(para['community_name'])
        data_table = saling.salingHouseChart(para['community_name'])
        flag = 6
    return render_template('onsale_bycommunity_analyze.html', data=data, flag=flag, data_table=data_table)


@app.route('/onsale_bydistrict_analyze.html', methods=['POST'])
def jump_area():
    para = request.form
    data = saling2.salingHouseInfo(para['district_name'], para['area_name'])
    data_table = saling2.salingHouseChart2(para['district_name'], para['area_name'])
    return render_template('onsale_bydistrict_analyze.html', data=data, data_table=data_table)


@app.route('/bdmap')
def bdmap():
    return render_template('baidumap.html')


@app.route('/graph2')
def graph2():
    return render_template('graph.html')


@app.route('/graph3')
def graph3():
    return render_template('graph.html')


if __name__ == '__main__':
    app.run()
