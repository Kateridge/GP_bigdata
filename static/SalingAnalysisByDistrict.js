var myChart = echarts.init(document.getElementById('graph_display'));

var option1 = {
    title: {
        text: '时间-总/均价'
    },
    tooltip: {},
    legend: {
        data:['总价','均价']
    },
    dataset: {
        source:data
    },
    xAxis: {type: 'category'},
    yAxis: [
        {
            type: 'value',
            name: '总价/万元'
        },
        {
            type: 'value',
            name: '均价/元',
        }
    ],
    series: [
        {
            name:'总价',
            type: 'bar'
        },
        {
            name:'均价',
            type: 'bar',
            yAxisIndex: 1,
        }
    ],
};

myChart.setOption(option1);