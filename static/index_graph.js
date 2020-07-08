var myChart1 = echarts.init(document.getElementById('graph1'));
var myChart2 = echarts.init(document.getElementById('graph2'));
var myChart3 = echarts.init(document.getElementById('graph3'));
var myChart4 = echarts.init(document.getElementById('graph4'));
var myChart5 = echarts.init(document.getElementById('graph5'));
var myChart6 = echarts.init(document.getElementById('graph6'));
var myChart7 = echarts.init(document.getElementById('graph7'));
var myChart8 = echarts.init(document.getElementById('graph8'));

var option1 = {
    tooltip: {},
    dataset: {
        source: graph1_data
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
            type: 'line'
        }
    ],
    grid: {
        x: 0, //相当于距离左边效果:padding-left
        x2: 10,
        y: 10,  //相当于距离上边效果:padding-top
        bottom: '5%',
        containLabel: true
    }
};

var option2 = {
    tooltip: {},
    dataset: {
        source: graph2_data
    },
    xAxis: {type: 'category'},
    yAxis: [
        {
            type: 'value',
            name: '总价/万元'
        }
    ],
    series: [
        {
            name:'均价',
            type: 'line'
        }
    ],
        grid: {
        x: 10, //相当于距离左边效果:padding-left
        x2: 10,
        y: 10,  //相当于距离上边效果:padding-top
        bottom: '5%',
        containLabel: true
    }
};

var option3 = {
    tooltip: {
        trigger: 'item',
        formatter: "{a} <br/>{b}: {c} ({d}%)"
    },
    series: [
        {
            name:'户型比例',
            type:'pie',
            radius: ['50%', '70%'],
            avoidLabelOverlap: true,
            label: {
                emphasis: {
                    show: true,
                    textStyle: {
                        fontSize: '16',
                        fontWeight: 'bold'
                    }
                }
            },
            labelLine: {
                normal: {
                    show: true
                }
            },
            data: graph3_data
        }
    ]
};


var option4 = {
    tooltip: {
        trigger: 'item',
        formatter: "{a} <br/>{b}: {c} ({d}%)"
    },
    series: [
        {
            name:'户型比例',
            type:'pie',
            radius: ['50%', '70%'],
            avoidLabelOverlap: true,
            label: {
                emphasis: {
                    show: true,
                    textStyle: {
                        fontSize: '16',
                        fontWeight: 'bold'
                    }
                }
            },
            labelLine: {
                normal: {
                    show: true
                }
            },
            data: graph4_data
        }
    ]
};

var option5 = {
    tooltip: {
        trigger: 'item',
        formatter: "{a} <br/>{b}: {c} ({d}%)"
    },
    series: [
        {
            name:'朝向比例',
            type:'pie',
            radius: ['50%', '70%'],
            avoidLabelOverlap: true,
            label: {
                emphasis: {
                    show: true,
                    textStyle: {
                        fontSize: '16',
                        fontWeight: 'bold'
                    }
                }
            },
            labelLine: {
                normal: {
                    show: true
                }
            },
            data: graph5_data
        }
    ]
};

var option6 = {
    tooltip: {
        trigger: 'item',
        formatter: "{a} <br/>{b}: {c} ({d}%)"
    },
    series: [
        {
            name:'是否有地铁比例',
            type:'pie',
            radius: ['50%', '70%'],
            avoidLabelOverlap: true,
            label: {
                emphasis: {
                    show: true,
                    textStyle: {
                        fontSize: '16',
                        fontWeight: 'bold'
                    }
                }
            },
            labelLine: {
                normal: {
                    show: true
                }
            },
            data: graph6_data
        }
    ]
};

var option7 = {
    tooltip: {
        trigger: 'item',
        formatter: "{a} <br/>{b}: {c} ({d}%)"
    },
    series: [
        {
            name:'装修比例',
            type:'pie',
            radius: ['50%', '70%'],
            avoidLabelOverlap: true,
            label: {
                emphasis: {
                    show: true,
                    textStyle: {
                        fontSize: '16',
                        fontWeight: 'bold'
                    }
                }
            },
            labelLine: {
                normal: {
                    show: true
                }
            },
            data: graph7_data
        }
    ]
};

var option8 = {
    tooltip: {
        trigger: 'item',
        formatter: "{a} <br/>{b}: {c} ({d}%)"
    },
    series: [
        {
            name:'装修比例',
            type:'pie',
            radius: ['50%', '70%'],
            avoidLabelOverlap: true,
            label: {
                emphasis: {
                    show: true,
                    textStyle: {
                        fontSize: '16',
                        fontWeight: 'bold'
                    }
                }
            },
            labelLine: {
                normal: {
                    show: true
                }
            },
            data: graph8_data
        }
    ]
};
myChart1.setOption(option1);
myChart2.setOption(option2);
myChart3.setOption(option3);
myChart4.setOption(option4);
myChart5.setOption(option5);
myChart6.setOption(option6);
myChart7.setOption(option7);
myChart8.setOption(option8);