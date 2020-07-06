var myChart1 = echarts.init(document.getElementById('graph1'));
var myChart2 = echarts.init(document.getElementById('graph2'));
var myChart3 = echarts.init(document.getElementById('graph3'));
var myChart4 = echarts.init(document.getElementById('graph4'));

var option1 = {
    title: {
        text: '户型比例'
    },
    series:[{
        name: '户型比例',
        type: 'pie',
        radius: '70%',
        data: graph1_data
    }]
};

var option2 = {
    title: {
        text: '总价比例'
    },
    series:[{
        name: '总价比例',
        type: 'pie',
        radius: '70%',
        roseType: 'angle',
        data: graph2_data
    }]
};

var option3 = {
    title: {
        text: '均价比例'
    },
    series:[{
        name: '均价比例',
        type: 'pie',
        radius: '70%',
        data: graph3_data
    }]
};

var option4 = {
    title: {
        text: '面积比例'
    },
    series:[{
        name: '面积比例',
        type: 'pie',
        radius: '70%',
        roseType: 'angle',
        data: graph4_data
    }]
};

myChart1.setOption(option1);
myChart2.setOption(option2);
myChart3.setOption(option3);
myChart4.setOption(option4);

