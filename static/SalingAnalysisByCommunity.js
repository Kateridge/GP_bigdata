var myChart = echarts.init(document.getElementById("hero-donut"));

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
        text: '装修比例'
    },
    series:[{
        name: '装修比例',
        type: 'pie',
        radius: '70%',
        data:data
    }]
};
var option3 = {
    title: {
        text: '面积比例'
    },
    series:[{
        name: '面积比例',
        type: 'pie',
        radius: '70%',
        data:data
    }]
};
var option4 = {
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
var option5 = {
    title: {
        text: '总价比例'
    },
    series:[{
        name: '总价比例',
        type: 'pie',
        radius: '70%',
        data:data
    }]
};
var option6 = {
    title: {
        text: '朝向比例'
    },
    series:[{
        name: '朝向比例',
        type: 'pie',
        radius: '70%',
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
else if(flag === 5){
    myChart.setOption(option5);
}
else if(flag === 6){
    myChart.setOption(option6);
}