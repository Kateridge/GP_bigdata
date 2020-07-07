var myChart1 = echarts.init(document.getElementById("graph1"));
var myChart2 = echarts.init(document.getElementById("graph2"));
var myChart3 = echarts.init(document.getElementById("graph3"));
var myChart4 = echarts.init(document.getElementById("graph4"));
var myChart5 = echarts.init(document.getElementById("graph5"));
var myChart6 = echarts.init(document.getElementById("graph6"));
var myChart7 = echarts.init(document.getElementById("graph7"));
var myChart8 = echarts.init(document.getElementById("graph8"));

var option1 = {
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
            data: graph1_data
        }
    ]
};
var option2 = {
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
            data: graph2_data
        }
    ]
};
var option3 = {
    tooltip: {
        trigger: 'item',
        formatter: "{a} <br/>{b}: {c} ({d}%)"
    },
    series: [
        {
            name:'面积比例',
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
            name:'均价比例',
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
            name:'总价比例',
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
            data: graph6_data
        }
    ]
};
var option7 = {
    tooltip: {},
    legend: {
        data:['均价']
    },
    dataset: {
        source: graph7_data
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
    tooltip: {},
    legend: {
        data:['总价']
    },
    dataset: {
        source: graph8_data
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

myChart1.setOption(option1);
myChart2.setOption(option2);
myChart3.setOption(option3);
myChart4.setOption(option4);
myChart5.setOption(option5);
myChart6.setOption(option6);
myChart7.setOption(option7);
myChart8.setOption(option8);
