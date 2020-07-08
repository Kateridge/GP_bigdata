//初始化echarts,并和框体map绑定。
var myChart = echarts.init(document.getElementById('main-map'));

/**
此版本通过设置geoindex && seriesIndex: [1] 属性来实现geo和map共存，来达到hover散点和区域显示tooltip的效果

默认情况下，map series 会自己生成内部专用的 geo 组件。但是也可以用这个 geoIndex 指定一个 geo 组件。这样的话，map 和 其他 series（例如散点图）就可以共享一个 geo 组件了。并且，geo 组件的颜色也可以被这个 map series 控制，从而用 visualMap 来更改。
当设定了 geoIndex 后，series-map.map 属性，以及 series-map.itemStyle 等样式配置不再起作用，而是采用 geo 中的相应属性。

http://echarts.baidu.com/option.html#series-map.geoIndex

并且加了pin气泡图标以示数值大小
*/

var uploadedDataURL = "https://geo.datav.aliyun.com/areas_v2/bound/500000_full.json";
myChart.showLoading();
$.getJSON(uploadedDataURL, function(geoJson) {
    echarts.registerMap('chongqing', geoJson);
    myChart.hideLoading();
    var geoCoordMap = {
        '万州区': [108.380246, 30.807807],
        '涪陵区': [107.394905, 29.703652],
        '渝中区': [106.56288, 29.556742],
        '大渡口区': [106.48613, 29.481002],
        '江北区': [106.532844, 29.575352],
        '沙坪坝区': [106.4542, 29.541224],
        '九龙坡区': [106.480989, 29.523492],
        '南岸区': [106.560813, 29.523992],
        '北碚区': [106.437868, 29.82543],
        '綦江区': [106.651417, 29.028091],
        '大足区': [105.715319, 29.700498],
        '渝北区': [106.512851, 29.601451],
        '巴南区': [106.519423, 29.381919],
        '黔江区': [108.782577, 29.527548],
        '长寿区': [107.074854, 29.833671],
        '江津区': [106.253156, 29.283387],
        '合川区': [106.265554, 29.990993],
        '永川区': [105.894714, 29.348748],
        '南川区': [107.098153, 29.156646],
        '璧山区': [106.231126, 29.593581],
        '铜梁区': [106.054948, 29.839944],
        '潼南区': [105.841818, 30.189554],
        '荣昌区': [105.594061, 29.403627],
        '梁平区': [107.800034, 30.672168],
        '城口县': [108.6649, 31.946293],
        '丰都县': [107.73248, 29.866424],
        '垫江县': [107.348692, 30.330012],
        '武隆区': [107.75655, 29.32376],
        '忠县': [108.037518, 30.291537],
        '云阳县': [108.697698, 30.930529],
        '奉节县': [109.465774, 31.019967],
        '巫山县': [109.878928, 31.074843],
        '巫溪县': [109.628912, 31.3966],
        '石柱土家族自治县': [108.112448, 29.99853],
        '秀山土家族苗族自治县': [108.996043, 28.444772],
        '酉阳土家族苗族自治县': [108.767201, 28.839828],
        '彭水苗族土家族自治县': [108.166551, 29.293856],
        '开州区': [108.388696, 31.162529]
    }
    var datavalue = [
        {name: '万州区', value: 122},
        {name: '涪陵区', value: 39},
        {name: '渝中区', value: 118},
        {name: '大渡口区', value: 87},
        {name: '江北区', value: 289},
        {name: '沙坪坝区', value: 422},
        {name: '九龙坡区', value: 283},
        {name: '南岸区', value: 367},
        {name: '北碚区', value: 128},
        {name: '綦江区', value: 39},
        {name: '大足区', value: 45},
        {name: '渝北区', value: 491},
        {name: '巴南区', value: 189},
        {name: '黔江区', value: 24},
        {name: '长寿区', value: 187},
        {name: '江津区', value: 167},
        {name: '合川区', value: 47},
        {name: '永川区', value: 214},
        {name: '南川区', value: 53},
        {name: '璧山区', value: 89},
        {name: '铜梁区', value: 39},
        {name: '潼南区', value: 33},
        {name: '荣昌区', value: 40},
        {name: '梁平区', value: 18},
        {name: '城口县', value: 3},
        {name: '丰都县', value: 12},
        {name: '垫江县', value: 39},
        {name: '武隆区', value: 10},
        {name: '忠县', value: 5},
        {name: '云阳县', value: 8},
        {name: '奉节县', value: 4},
        {name: '巫山县', value: 3},
        {name: '巫溪县', value: 2},
        {name: '石柱土家族自治县', value: 1},
        {name: '秀山土家族苗族自治县', value: 11},
        {name: '酉阳土家族苗族自治县', value: 13},
        {name: '彭水苗族土家族自治县', value: 5},
        {name: '开州区', value:123},
    ];
    var max = 480, min = 9; // todo
    var maxSize4Pin = 100, minSize4Pin = 20;

  var convertData = function (data) {
    var res = [];
    for (var i = 0; i < data.length; i++) {
        var geoCoord = geoCoordMap[data[i].name];
        if (geoCoord) {
            res.push({
                name: data[i].name,
                value: geoCoord.concat(data[i].value)
                //value: data[i].value
            });
        }
    }
    return res;
};


    option = {
        title: {
            text: '重庆市近一周房屋交易数据图',
            subtext: '',
            x: 'center',
            textStyle: {
                color: '#000'
            }
        },
        tooltip: {
            trigger: 'item',
            formatter: function (params) {
              if(typeof(params.value)[2] == "undefined"){
                  	return params.name + ' : ' + params.value;
              }else{
              	return params.name + ' : ' + params.value[2];
              }
            }
        },
        legend: {
            orient: 'vertical',
            y: 'bottom',
            x: 'right',
            data: ['credit_pm2.5'],
            textStyle: {
                color: '#fff'
            }
        },
        visualMap: {
            show: false,
            min: 0,
            max: 500,
            left: 'left',
            top: 'bottom',
            text: ['高', '低'], // 文本，默认为数值文本
            calculable: true,
            seriesIndex: [1],
            inRange: {
                // color: ['#3B5077', '#031525'] // 蓝黑
                // color: ['#ffc0cb', '#800080'] // 红紫
                // color: ['#3C3B3F', '#605C3C'] // 黑绿
                //color: ['#0f0c29', '#302b63', '#24243e'] // 黑紫黑
                // color: ['#23074d', '#cc5333'] // 紫红
                 color: ['#00467F', '#A5CC82'] // 蓝绿
                // color: ['#1488CC', '#2B32B2'] // 浅蓝
                // color: ['#00467F', '#A5CC82'] // 蓝绿
                // color: ['#00467F', '#A5CC82'] // 蓝绿
                // color: ['#00467F', '#A5CC82'] // 蓝绿
                // color: ['#00467F', '#A5CC82'] // 蓝绿

            }
        },
        // toolbox: {
        //     show: true,
        //     orient: 'vertical',
        //     left: 'right',
        //     top: 'center',
        //     feature: {
        //             dataView: {readOnly: false},
        //             restore: {},
        //             saveAsImage: {}
        //             }
        // },
        geo: {
            show: true,
            map: 'chongqing',
            label: {
                normal: {
                    show: false
                },
                emphasis: {
                    show: false,
                }
            },
            roam: true,
            itemStyle: {
                normal: {
                    areaColor: '#031525',
                    borderColor: '#3B5077',
                },
                emphasis: {
                    areaColor: '#2B91B7',
                }
            }
        },
        series : [
      {
            name: 'credit_pm2.5',
            type: 'scatter',
            coordinateSystem: 'geo',
            data: convertData(datavalue),
            symbolSize: function (val) {
                return val[2] / 10;
            },
            label: {
                normal: {
                    formatter: '{b}',
                    position: 'right',
                    show: true
                },
                emphasis: {
                    show: true
                }
            },
            itemStyle: {
                normal: {
                    color: '#05C3F9'
                }
            }
        },
         {
            type: 'map',
            map: 'chongqing',
            geoIndex: 0,
            aspectScale: 0.75, //长宽比
            showLegendSymbol: false, // 存在legend时显示
            label: {
                normal: {
                    show: false
                },
                emphasis: {
                    show: false,
                    textStyle: {
                        color: '#fff'
                    }
                }
            },
            roam: true,
            itemStyle: {
                normal: {
                    areaColor: '#031525',
                    borderColor: '#3B5077',
                },
                emphasis: {
                    areaColor: '#2B91B7'
                }
            },
            animation: false,
            data: datavalue
        },
        {
            name: '点',
            type: 'scatter',
            coordinateSystem: 'geo',
            symbol: 'pin',
            //symbolSize:50,
            symbolSize: function (val) {
                var a = (maxSize4Pin - minSize4Pin) / (max - min);
                var b = minSize4Pin - a*min;
                b = maxSize4Pin - a*max;
                return a*val[2]+b;
            },
            label: {
                normal: {
                    formatter: function(obj) {
                        console.log(obj.data.value[2]);
                        return obj.data.value[2]
                    },
                    show: true,
                    textStyle: {
                        color: '#fff',
                        fontSize: 9,
                    }
                }
            },
            itemStyle: {
                normal: {
                    color: '#F62157', //标志颜色
                }
            },
            zlevel: 6,
            data: convertData(datavalue),
        },
        {
            name: 'Top 5',
            type: 'effectScatter',
            coordinateSystem: 'geo',
            data: convertData(datavalue.sort(function (a, b) {
                return b.value - a.value;
            }).slice(0, 40)),
            symbolSize: function (val) {
                return val[2] / 10;
            },
            showEffectOn: 'render',
            rippleEffect: {
                brushType: 'stroke'
            },
            hoverAnimation: true,
            label: {
                normal: {
                    formatter: '{b}',
                    position: 'right',
                    show: true
                }
            },
            itemStyle: {
                normal: {
                    color: '#05C3F9',
                    shadowBlur: 50,
                    shadowColor: '#05C3F9'
                }
            },
            zlevel: 3
        },

    ]
    };
    myChart.setOption(option);
});