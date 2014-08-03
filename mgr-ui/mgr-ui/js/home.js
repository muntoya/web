/************************图表需要的相关数据*******************************/
//存储池
var pool = echarts.init(document.getElementById('pool'));
//lun
var lun = echarts.init(document.getElementById('lun'));
//吞吐率
var tp = echarts.init(document.getElementById('tp'));
//IOPS
var sr = echarts.init(document.getElementById('sr'));

var poolOpt = {animation:false,
    title:{text:"存储池",x:'center',y:20,textStyle: {fontSize: 12,fontWeight: 'normal',color: '#333',fontFamily:'微软雅黑'}},
   tooltip:{trigger: 'item', formatter: "{b}<br/>{c}GB"},   
    legend: {orient : 'vertical', y : 154, data:['可用容量','已用容量']},
    color: ['#8bc8e6', '#efefef'] 
};
 /*tooltip:{trigger: 'item', formatter: "{b}<br/>{c}GB({d}%)"},*/
var lunOpt = {animation:false,
    title:{text:"LUN",x:'center',y:20,textStyle: {fontSize: 12,fontWeight: 'normal',color: '#333',fontFamily:'微软雅黑'}},   
    tooltip:{trigger: 'item', formatter: "{b}<br/>{c}GB"},
    legend: {orient : 'vertical', y : 154, data:['可用容量','已用容量']},
    color: ['#efe696', '#efefef'] 
};

var tpOpt = { tooltip : {trigger: 'axis'},animation:false,
                legend: {orient : 'horizontal',x :'center', y : 'top', selected: {'内部读流量' : false,  '内部写流量' : false},data:['对外读流量','对外写流量', '内部读流量', '内部写流量'],textStyle: {fontSize: 11,fontWeight: 'normal',color: '#333',fontFamily:'微软雅黑'}},                  
                grid:{ y: '30', height:'108', backgroundColor:'#fff'},
                xAxis : [{type : 'category',boundaryGap : false,axisLine:{lineStyle:{color:'#cccccc', type:'solid',width:'1'}}}],
                yAxis : [{type : 'value',axisLine:{lineStyle:{color:'#cccccc', type:'solid',width:'2'}},}]};

 var tpSer = [{name:'对外读流量',type:'line',symbol: 'none',itemStyle : {normal:{color:'#e21ed2', lineStyle:{width: '1'}}}},
                {name:'对外写流量',type:'line',symbol: 'none',itemStyle : {normal:{color:'#4f7fc9', lineStyle:{width: '1'}}}},
                {name:'内部读流量',type:'line',symbol: 'none',itemStyle : {normal:{color:'#eeda87', lineStyle:{width: '1'}}}},
                {name:'内部写流量',type:'line',symbol: 'none',itemStyle : {normal:{color:'#c1e07e', lineStyle:{width: '1'}}}}];
 var srOpt = {tooltip : {trigger: 'axis'},animation:false,
            legend: {orient : 'horizontal',x :'center',y : 'top',selected: {'内部读IOPS' : false,  '内部写IOPS' : false},
                    data:['对外读IOPS','对外写IOPS', '内部读IOPS', '内部写IOPS'],textStyle: {fontSize: 11,fontWeight: 'normal',color: '#333',fontFamily:'微软雅黑'}},                  
            grid:{ y: '30',height:'108',backgroundColor:'#fff'},
            xAxis : [{type : 'category',boundaryGap : false,axisLine:{lineStyle:{color:'#cccccc', type:'solid',width:'1'}}}],
            yAxis : [{type : 'value',axisLine:{lineStyle:{color:'#cccccc', type:'solid',width:'2'}}} ]};
 var srSer = [{name:'对外读IOPS',type:'line',symbol: 'none',itemStyle : {normal:{color:'#e21ed2', lineStyle:{width: '1'}}} },
            {name:'对外写IOPS',type:'line',symbol: 'none',itemStyle : {normal:{color:'#4f7fc9', lineStyle:{width: '1'}}}},
            {name:'内部读IOPS',symbol: 'none',type:'line',itemStyle : {normal:{color:'#eeda87', lineStyle:{width: '1'}}}},
            {name:'内部写IOPS',type:'line',symbol: 'none',itemStyle : {normal:{color:'#c1e07e', lineStyle:{width: '1'}}}}];

/***************************************** function ***************************************************/
$(function() {     
    getChart();// 获取图表数据
    setInterval(refreshData, 5000);  // 定时刷新页面
})

// 刷新页面
function refreshData(){
    getChart();
    getContent();
}

//刷新图表，获取数据后解析为需要的格式，然后drawchart
function getChart(){ 
    getPie();
    getIO();
}

//刷新模块， 获取数据后直接填充到节点内
function getContent(){
    getSystemInfo();
    getWranning();
}

//获取 “存储资源容量统计” 数据并drawPie
function getPie(){
    $.ajax({
        type: 'GET',
        url: '/api/home/storage',        
        success: function(respondJson) {
            var respond = eval('(' + respondJson + ')');
            getLUN(respond.lun);
            getPool(respond.pool);
        }
    })
}
//获取 “ 统计数据” 数据并drawLine
function getIO(){
    $.ajax({
        type: 'GET',
        url: '/api/home/io',        
        success: function(respondJson) {
            var respond = eval('(' + respondJson + ')');
            if ($.cookie('tpSelected')){
                var selectedTP =  $.cookie('tpSelected');
                selectedTP = eval('(' + selectedTP + ')');                
                tpOpt.legend.selected = selectedTP;
            }  
            if ($.cookie('srSelected')){
                var selectedSR =  $.cookie('srSelected');
                selectedSR = eval('(' + selectedSR + ')');                
                srOpt.legend.selected = selectedSR;
            }                   
            tp.setOption(getIOValue(respond.throughput, tpOpt, tpSer));
            sr.setOption(getIOValue(respond.iops, srOpt, srSer));
            tp.on('legendSelected', setTPLegend);
            sr.on('legendSelected', setSRLegend);      
        }
    })
}

function setTPLegend(param) {
     var selected = param.selected;     
     var tpSelected = JSON.stringify(selected);
     $.cookie('tpSelected', tpSelected);    
}
function setSRLegend(param) {
     var selected = param.selected;     
     var srSelected = JSON.stringify(selected);
     $.cookie('srSelected', srSelected); 
}

//刷新'系统概况'
function getSystemInfo(){
    $.ajax({
        type: 'GET',
        url: '/api/home/pages/baseinfo',        
        success: function(respond) {
            $('#sysInfo').html(respond);
        }
    })
}

//刷新'报警信息'
function getWranning(){
    $.ajax({
        type: 'GET',
        url: '/api/home/pages/warning',        
        success: function(respond) {
            $('#warning').html(respond);
        }
    })
}

function getSerObj(poolValue){
    var ser = {};
    ser.type = 'pie';
    ser.radius = '55%';
    ser.center = ['50%', '50%'];
    ser.itemStyle = {normal:{label:{show:false},labelLine:{show:false}}};
    var ava = {};
    ava.value = poolValue.available;
    ava.name ='可用容量';

    var used = {};
    used.value = poolValue.used;
    used.name ='已用容量';
    ser.data=[ava, used];
    return ser;
}

function getPool(poolValue){
    var ser = getSerObj(poolValue);
    poolOpt.series = [ser];
    pool.setOption(poolOpt);
}

function getLUN(lunValue){
    var ser = getSerObj(lunValue);
    lunOpt.series = [ser];
    lun.setOption(lunOpt);
}

function getIOValue(value, opt, ser){
    timeArr = [], irArr = [], iwArr = [], orArr = [], owArr = [];
    for (var i =0; i < value.length; i++){
        timeArr.push(value[i].time);
        orArr.push(value[i].or);
        owArr.push(value[i].ow);
        irArr.push(value[i].ir);
        iwArr.push(value[i].iw);
    }

    opt.xAxis[0].data = timeArr;//X 轴
    ser[0].data = orArr;
    ser[1].data = owArr;
    ser[2].data = irArr;
    ser[3].data = iwArr;

    opt.series = ser;
    return opt;
}