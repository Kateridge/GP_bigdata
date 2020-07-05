var myChart = echarts.init(document.getElementById('graph-display'));

var option1 = {
    title: {
        text: '户型比例'
    },
    series:[{
        name: '户型比例',
        type: 'pie',
        radius: '70%',
        data:data
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
        data:data
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
        data:data
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
        data:data
    }]
};

if(flag === 1){
    myChart.setOption(option1);
}
else if(flag === 2){
    myChart.setOption(option2);
}
else if(flag === 3){
    myChart.setOption(option3);
}
else if(flag === 4){
    myChart.setOption(option4);
}

