var myChart = echarts.init(document.getElementById('graph_display'));

var option1 = {
    title: {
        text: '成交时间-均价'
    },
    tooltip: {},
    legend: {
        data:['均价']
    },
    dataset: {
        source:data
    },
    xAxis: {type: 'category'},
    yAxis: {
        type: 'value',
            name: '均价/元',
    },
    series: [{
        type: 'bar'
    }],
};

var option2 = {
    title: {
        text: '成交时间-总价'
    },
    tooltip: {},
    legend: {
        data:['总价']
    },
    dataset: {
        source:data
    },
    xAxis: {type: 'category'},
    yAxis: {
        type: 'value',
            name: '总价/万元',
    },
    series: [{
        type: 'bar'
    }],
};

var option3 = {
    title: {
        text: '成交时间 - 挂牌总价'
    },
    tooltip: {},
    legend: {
        data:['挂牌总价']
    },
    dataset: {
        source:data
    },
    xAxis: {type: 'category'},
    yAxis: [
        {
        type: 'value',
            name: '挂牌总价/万元',
        }
    ],
    series: [
        {
            name: '挂牌总价',
            type: 'bar'
        }
    ],
};

var option4 = {
    title: {
        text: '成交时间 - 交易周期'
    },
    tooltip: {},
    legend: {
        data:['交易周期']
    },
    dataset: {
        source:data
    },
    xAxis: {type: 'category'},
    yAxis: [
        {
        type: 'value',
            name: '交易周期/天',
        }
    ],
    series: [
        {
            name: '交易周期',
            type: 'bar'
        }
    ],
};

var option5 = {
    title: {
        text: '成交时间 - 交易差价'
    },
    tooltip: {},
    legend: {
        data:['交易差价']
    },
    dataset: {
        source:data
    },
    xAxis: {type: 'category'},
    yAxis: [
        {
        type: 'value',
            name: '交易差价/万元',
        }
    ],
    series: [
        {
            name: '交易差价',
            type: 'bar'
        }
    ],
};

var option6 = {
    title: {
        text: '成交时间 - 成交数量'
    },
    tooltip: {},
    legend: {
        data:['成交数量']
    },
    dataset: {
        source:data
    },
    xAxis: {type: 'category'},
    yAxis: [
        {
        type: 'value',
            name: '成交数量/套',
        }
    ],
    series: [
        {
            name: '成交数量',
            type: 'bar'
        }
    ],
};

var option7 = {
    title: {
        text: '装修程度 - 均价'
    },
    tooltip: {},
    legend: {
        data:['均价']
    },
    dataset: {
        source:data
    },
    xAxis: {type: 'category'},
    yAxis: [
        {
        type: 'value',
            name: '均价/元',
        }
    ],
    series: [
        {
            name: '均价',
            type: 'bar'
        }
    ],
};

var option8 = {
    title: {
        text: '装修程度 - 总价'
    },
    tooltip: {},
    legend: {
        data:['总价']
    },
    dataset: {
        source:data
    },
    xAxis: {type: 'category'},
    yAxis: [
        {
        type: 'value',
            name: '总价/万元',
        }
    ],
    series: [
        {
            name: '总价',
            type: 'bar'
        }
    ],
};

var option9 = {
    title: {
        text: '装修程度 - 挂牌总价'
    },
    tooltip: {},
    legend: {
        data:['挂牌总价']
    },
    dataset: {
        source:data
    },
    xAxis: {type: 'category'},
    yAxis: [
        {
        type: 'value',
            name: '挂牌总价/万元',
        }
    ],
    series: [
        {
            name: '挂牌总价',
            type: 'bar'
        }
    ],
};

var option10 = {
    title: {
        text: '装修程度 - 交易周期'
    },
    tooltip: {},
    legend: {
        data:['交易周期']
    },
    dataset: {
        source:data
    },
    xAxis: {type: 'category'},
    yAxis: [
        {
        type: 'value',
            name: '交易周期/天',
        }
    ],
    series: [
        {
            name: '交易周期',
            type: 'bar'
        }
    ],
};

var option11 = {
    title: {
        text: '装修程度 -- 成交差价'
    },
    tooltip: {},
    legend: {
        data:['成交差价']
    },
    dataset: {
        source:data
    },
    xAxis: {type: 'category'},
    yAxis: [
        {
        type: 'value',
            name: '成交差价/万元',
        }
    ],
    series: [
        {
            name: '成交差价',
            type: 'bar'
        }
    ],
};

var option12 = {
    title: {
        text: '装修程度 - 成交数量'
    },
    tooltip: {},
    legend: {
        data:['成交数量']
    },
    dataset: {
        source:data
    },
    xAxis: {type: 'category'},
    yAxis: [
        {
        type: 'value',
            name: '成交数量/套',
        }
    ],
    series: [
        {
            name: '成交数量',
            type: 'bar'
        }
    ],
};

var option13 = {
    title: {
        text: '户型 - 均价'
    },
    tooltip: {},
    legend: {
        data:['均价']
    },
    dataset: {
        source:data
    },
    xAxis: {type: 'category'},
    yAxis: [
        {
        type: 'value',
            name: '均价/元',
        }
    ],
    series: [
        {
            name: '均价',
            type: 'bar'
        }
    ],
};

var option14 = {
    title: {
        text: '户型 - 总价'
    },
    tooltip: {},
    legend: {
        data:['总价']
    },
    dataset: {
        source:data
    },
    xAxis: {type: 'category'},
    yAxis: [
        {
        type: 'value',
            name: '总价/万元',
        }
    ],
    series: [
        {
            name: '总价',
            type: 'bar'
        }
    ],
};

var option15 = {
    title: {
        text: '户型 -- 挂牌总价'
    },
    tooltip: {},
    legend: {
        data:['挂牌总价']
    },
    dataset: {
        source:data
    },
    xAxis: {type: 'category'},
    yAxis: [
        {
        type: 'value',
            name: '挂牌总价/万元',
        }
    ],
    series: [
        {
            name: '挂牌总价',
            type: 'bar'
        }
    ],
};

var option16 = {
    title: {
        text: '户型 - 交易周期'
    },
    tooltip: {},
    legend: {
        data:['交易周期']
    },
    dataset: {
        source:data
    },
    xAxis: {type: 'category'},
    yAxis: [
        {
        type: 'value',
            name: '交易周期/天',
        }
    ],
    series: [
        {
            name: '交易周期',
            type: 'bar'
        }
    ],
};

var option17 = {
    title: {
        text: '户型 - 交易差价'
    },
    tooltip: {},
    legend: {
        data:['交易差价']
    },
    dataset: {
        source:data
    },
    xAxis: {type: 'category'},
    yAxis: [
        {
        type: 'value',
            name: '交易差价/万元',
        }
    ],
    series: [
        {
            name: '交易差价',
            type: 'bar'
        }
    ],
};

var option18 = {
    title: {
        text: '户型 - 成交数量'
    },
    tooltip: {},
    legend: {
        data:['成交数量']
    },
    dataset: {
        source:data
    },
    xAxis: {type: 'category'},
    yAxis: [
        {
        type: 'value',
            name: '成交数量/套',
        }
    ],
    series: [
        {
            name: '成交数量',
            type: 'bar'
        }
    ],
};

var option19 = {
    title: {
        text: '是否有地铁 - 均价'
    },
    tooltip: {},
    legend: {
        data:['均价']
    },
    dataset: {
        source:data
    },
    xAxis: {type: 'category'},
    yAxis: [
        {
        type: 'value',
            name: '均价/元',
        }
    ],
    series: [
        {
            name: '均价',
            type: 'bar'
        }
    ],
};

var option20 = {
    title: {
        text: '是否有地铁 - 总价'
    },
    tooltip: {},
    legend: {
        data:['总价']
    },
    dataset: {
        source:data
    },
    xAxis: {type: 'category'},
    yAxis: [
        {
        type: 'value',
            name: '总价/万元',
        }
    ],
    series: [
        {
            name: '总价',
            type: 'bar'
        }
    ],
};

var option21 = {
    title: {
        text: '是否有地铁 -- 挂牌总价'
    },
    tooltip: {},
    legend: {
        data:['挂牌总价']
    },
    dataset: {
        source:data
    },
    xAxis: {type: 'category'},
    yAxis: [
        {
        type: 'value',
            name: '挂牌总价/万元',
        }
    ],
    series: [
        {
            name: '挂牌总价',
            type: 'bar'
        }
    ],
};

var option22 = {
    title: {
        text: '是否有地铁 - 交易周期'
    },
    tooltip: {},
    legend: {
        data:['交易周期']
    },
    dataset: {
        source:data
    },
    xAxis: {type: 'category'},
    yAxis: [
        {
        type: 'value',
            name: '交易周期/天',
        }
    ],
    series: [
        {
            name: '交易周期',
            type: 'bar'
        }
    ],
};

var option23 = {
    title: {
        text: '是否有地铁 - 交易差价'
    },
    tooltip: {},
    legend: {
        data:['交易差价']
    },
    dataset: {
        source:data
    },
    xAxis: {type: 'category'},
    yAxis: [
        {
        type: 'value',
            name: '交易差价/万元',
        }
    ],
    series: [
        {
            name: '交易差价',
            type: 'bar'
        }
    ],
};

var option24 = {
    title: {
        text: '是否有地铁 - 成交数量'
    },
    tooltip: {},
    legend: {
        data:['成交数量']
    },
    dataset: {
        source:data
    },
    xAxis: {type: 'category'},
    yAxis: [
        {
        type: 'value',
            name: '成交数量/套',
        }
    ],
    series: [
        {
            name: '成交数量',
            type: 'bar'
        }
    ],
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
else if(flag === 7){
    myChart.setOption(option7);
}
else if(flag === 8){
    myChart.setOption(option8);
}
else if(flag === 9){
    myChart.setOption(option9);
}
else if(flag === 10){
    myChart.setOption(option10);
}
else if(flag === 11){
    myChart.setOption(option11);
}
else if(flag === 12){
    myChart.setOption(option12);
}
else if(flag === 13){
    myChart.setOption(option12);
}
else if(flag === 14){
    myChart.setOption(option14);
}
else if(flag === 15){
    myChart.setOption(option15);
}
else if(flag === 16){
    myChart.setOption(option16);
}
else if(flag === 17){
    myChart.setOption(option17);
}
else if(flag === 18){
    myChart.setOption(option18);
}
else if(flag === 19){
    myChart.setOption(option19);
}
else if(flag === 20){
    myChart.setOption(option20);
}
else if(flag === 21){
    myChart.setOption(option21);
}
else if(flag === 22){
    myChart.setOption(option22);
}
else if(flag === 23){
    myChart.setOption(option23);
}
else if(flag === 24){
    myChart.setOption(option24);
}
