var myChart1 = echarts.init(document.getElementById('graph1'));
var myChart2 = echarts.init(document.getElementById('graph2'));

var option1 = {
    title: {
        text: '时间-总价走势'
    },
    tooltip: {},
    legend: {
        data:['成交总价','挂牌总价','交易差价']
    },
    dataset: {
        source: graph1_data
    },
    xAxis: {type: 'category'},
    yAxis: [
        {
            type: 'value',
            name: '成交/挂牌总价/万元'
        },
        {
            type: 'value',
            name: '交易差价/万元'
        }
    ],
    series: [
        {
            name:'成交总价',
            type: 'bar'
        },
        {
            name:'挂牌总价',
            type: 'bar',
        },
        {
            name:'交易差价',
            type: 'bar',
            yAxisIndex: 1,
        }
    ],
};

var option2 = {
    title: {
        text: '时间-均价走势'
    },
    tooltip: {},
    legend: {
        data:['均价']
    },
    dataset: {
        source: graph2_data
    },
    xAxis: {type: 'category'},
    yAxis: [
        {
            type: 'value',
            name: '均价/元'
        }
    ],
    series: [
        {
            name:'均价',
            type: 'bar'
        }
    ],
};


myChart1.setOption(option1);

myChart2.setOption(option2);