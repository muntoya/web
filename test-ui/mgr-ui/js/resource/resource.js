/************************图表需要的相关数据*******************************/
var lun = echarts.init(document.getElementById('lun'));
var pool = echarts.init(document.getElementById('pool'));
var lunOpt = {
    title:{text: '可映射 LUN 容量统计',x:'center',textStyle: {fontSize: 14,fontWeight: 'bold',color: '#333',fontFamily:'微软雅黑'}},   
    tooltip:{trigger: 'item', formatter: "{b}<br/>{c} ({d}%)"},
    legend: {orient : 'vertical', x: 'right', y : 'center', data:['LUN：未映射','LUN：已映射']}
};

var poolOpt = {
    title:{text: '存储池容量统计', x:'center',textStyle: {fontSize: 14,fontWeight: 'bold',color: '#333',fontFamily:'微软雅黑'}},
    tooltip:{trigger: 'item', formatter: "{b}<br/>{c}GB ({d}%)"},   
    legend: {orient : 'vertical', x: 'right', y : 'center', data:['可用容量','已用容量']}
};

var lunSer = [{name:'', type:'pie', radius : '55%', center: ['50%', '50%']}];
var poolSer = [{name:'', type:'pie', radius : '55%', center: ['50%', '50%']}];


/************************************** function ******************************************************/
$(function() {     
    getPie();// 获取图表数据
})

//获取 “存储资源容量统计” 数据并drawPie
function getPie(){
    $.ajax({
        type: 'GET',
        url: '/api/resource/overview',        
        success: function(respondJson) {
            var respond = eval('(' + respondJson + ')');
            getLUN(respond.lun);
            getPool(respond.pool);
        }
    })
}

function getPool(poolValue){
    getPoolSerObj(poolValue);
    pool.setOption(poolOpt);
}

function getLUN(lunValue){
    getLunSerObj(lunValue);    
    lun.setOption(lunOpt);
}

function getLunSerObj(lunValue){    
    var ava = {};
    ava.value = lunValue.unmapped;
    ava.name ='LUN：未映射';

    var used = {};
    used.value = lunValue.mapped;
    used.name ='LUN：已映射';
    lunSer[0].data=[ava, used];
    lunOpt.series = lunSer;
}

function getPoolSerObj(poolValue){    
    var ava = {};
    ava.value = poolValue.available;
    ava.name ='可用容量';

    var used = {};
    used.value = poolValue.used;
    used.name ='已用容量';
    poolSer[0].data=[ava, used];
    poolOpt.series = poolSer;
}