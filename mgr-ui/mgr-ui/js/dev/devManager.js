//cpu 
var cpu = echarts.init(document.getElementById('cpuInfo'));
var cpuOpt = { 
		tooltip : {trigger: 'axis'},animation:false,
        legend: {orient : 'horizontal',x :'center', y : 'bottom', textStyle: {fontSize: 11,fontWeight: 'normal',color: '#333',fontFamily:'微软雅黑'}},                  
        grid:{ y: '20', height:'165', backgroundColor:'#fff', x:'10%', x2: '10%'},
        xAxis : [{type : 'category',boundaryGap : false, axisLabel:{interval:9}, axisLine:{lineStyle:{color:'#cccccc', type:'solid',width:'1'}}}],
        yAxis : [{type : 'value',axisLine:{lineStyle:{color:'#cccccc', type:'solid',width:'2'}},}]};

 var cpuSer = [{name:'Idle',type:'line',symbol: 'none',itemStyle : {normal:{color:'#e21ed2', lineStyle:{width: '1'}}}},
                {name:'User',type:'line',symbol: 'none',itemStyle : {normal:{color:'#4f7fc9', lineStyle:{width: '1'}}}},
                {name:'System',type:'line',symbol: 'none',itemStyle : {normal:{color:'#eeda87', lineStyle:{width: '1'}}}}];


 var cpuData = [{"ir": 59,"iw": 367,"or": 577,"ow": 448,"time": "16:00"}, {"ir": 87,"iw": 53,"or": 485,"ow": 222,"time": "16:10"},{"ir": 255,"iw": 158,"or": 684,"ow": 244,"time": "16:20"},{"ir": 89,"iw": 568,"or": 224,"ow": 847,"time": "16:30"},{"ir": 59,"iw": 367,"or": 577,"ow": 448,"time": "16:40"}]

$(function(){
	getCPU();
});

function getCPU(){
	var cpuData = getCpuData();
	cpu.setOption(getIOValue(cpuData, cpuOpt, cpuSer));
}

function getCpuData(){
	var arr = [];
	var time = 0;
	for(var i=0; i < 60; i++){
		var obj = {};
		obj.now = Math.round(Math.random() * 100);
		obj.avg = Math.round(Math.random() * 100);
		obj.max = Math.round(Math.random() * 100);		
		obj.time = time + ":00";
		time += 1;
		arr.push(obj);
	}
	return arr;
}

function getIOValue(value, opt, ser){
    timeArr = [], irArr = [], iwArr = [], orArr = [];
    for (var i =0; i < value.length; i++){
        timeArr.push(value[i].time);
        orArr.push(value[i].now);        
        irArr.push(value[i].avg);
        iwArr.push(value[i].max);
    }

    opt.xAxis[0].data = timeArr;//X 轴
    ser[0].data = orArr;    
    ser[1].data = irArr;
    ser[2].data = iwArr;

    opt.series = ser;
    return opt;
}