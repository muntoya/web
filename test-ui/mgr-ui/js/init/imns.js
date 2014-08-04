/*修改 iscsi 服务*/
$(".separationModeBtn").live('click', function(){
	$.ajax({
	    url: 'windows/separationMode.html',
	    success: function (data) {
	        createArtDialog("配置分离模式的网络适配器", data);
	    },
	    cache: false
	});
	return false;
})

/*配置 SoCache 模块 按钮*/
$("#configSCBtn").live('click', function(){
	$.ajax({
	    url: 'windows/configSocache.html',
	    success: function (data) {
	        createArtDialog("配置SoCache模块", data);
	        soCacheGirdTree.build(new chooseSoCacheJsonData().jsoninitNodes,true);
	    },
	    cache: false
	});
	return false;
})

chooseSoCacheJsonData= function(){

this.jsonFIFAHeaders=[{
		  	columns:[
		  	{},			
			{dataIndex:'dName'},
			{dataIndex:'dIP'},
			{dataIndex:'wwid'},
			{dataIndex:'dSlot'},
			{dataIndex:'dType'},
			{dataIndex:'dCop'},
			{dataIndex:'dFom'}
			],
			dataObject:{cb:'',dName:'设备名称',dIP:'设备IP', wwid:'wwid', dSlot:'磁盘槽位',dType:'磁盘类型',dCop:'容量大小',dFom:'是否已格式化'},
			trAttributeNames:['classStyle','style'],
			trAttributeValueObject:{classStyle:'init_tt_header',style:'background-color: #CAE783;'}
		  }
		];

this.jsoninitNodes=[
		{id:'node001',dataObject:{dName:'node001', dIP:'192.168.13.11'},userObject:{isGroup:true}},

		{id:'slot_001_1',pid:'node001',dataObject:{wwid:'12345', dSlot:'1,2',dType:'SSD',dCop:'30G',dFom:'是'}},
		{id:'slot_001_2',pid:'node001',dataObject:{wwid:'12345', dSlot:'3,4',dType:'SSD',dCop:'2G',dFom:'否'}},
		{id:'slot_001_3',pid:'node001',dataObject:{wwid:'12345', dSlot:'5,6',dType:'SSD',dCop:'102G',dFom:'否'}},

		{id:'node002', isLeaf:false, dataObject:{dName:'node002', dIP:'192.168.13.12'},userObject:{isGroup:true}},

		{id:'slot_002_1',pid:'node002',dataObject:{wwid:'12345', dSlot:'1,2',dType:'SSD',dCop:'30G',dFom:'是'}},
		{id:'slot_002_2',pid:'node002',dataObject:{wwid:'12345', dSlot:'3,4',dType:'SSD',dCop:'2G',dFom:'否'}},
		{id:'slot_002_3',pid:'node002',dataObject:{wwid:'12345', dSlot:'5,6',dType:'SSD',dCop:'102G',dFom:'否'}},

		{id:'node003', isLeaf:false, dataObject:{dName:'node003', dIP:'192.168.13.13'},userObject:{isGroup:true}},

		{id:'node004', isLeaf:false, dataObject:{dName:'node004', dIP:'192.168.13.14'},userObject:{isGroup:true}}		 
		  
		];
}

function createCB(infoObj){
	if (infoObj.node.isLeaf){
		var cb = Core4j.Domhelper.createElement("input",{
		attributeNames:['type'],
		valueObject:{type:'checkbox'}
		});
	} else{
		var cb = Core4j.Domhelper.createElement("input",{
		attributeNames:['type'],
		valueObject:{type:'radio'}
		});
	}
	return cb;
}

var soCacheGirdTree=new Core4j.toolbox.TableTree4j({
	columns:[
			{width:'28px', renderFunction:createCB},		
			{dataIndex:'dName', width:'76px'},
			{dataIndex:'dIP', isNodeClick:true, width:'126px'},
			{dataIndex:'wwid', width:'86px'},
			{dataIndex:'dSlot', width:'72px'},
			{dataIndex:'dType', width:'72px'},
			{dataIndex:'dCop', width:'80px'},
			{dataIndex:'dFom'},
			],
	treeMode:'gird',
	renderTo:'chooseSoCache',
	useLine:true,
	useIcon:true,
	id:'soCacheTree',
	useCookie:false,	
	headers:new chooseSoCacheJsonData().jsonFIFAHeaders,
	themeName:'init',
	selectMode:'single'
});




