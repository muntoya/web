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

		{id:'slot_001_1',pid:'node001',dataObject:{dSlot:'1,2',dType:'SSD',dCop:'30G',dFom:'是', dStatus:''}},
		{id:'slot_001_2',pid:'node001',dataObject:{dSlot:'3,4',dType:'SSD',dCop:'2G',dFom:'否', dStatus:'正在格式化'}},
		{id:'slot_001_3',pid:'node001',dataObject:{dSlot:'5,6',dType:'SSD',dCop:'102G',dFom:'否', dStatus:''}},

		{id:'node002', isLeaf:false, dataObject:{dName:'node002', dIP:'192.168.13.12'},userObject:{isGroup:true}},

		{id:'slot_002_1',pid:'node002',dataObject:{dSlot:'1,2',dType:'SSD',dCop:'30G',dFom:'是', dStatus:''}},
		{id:'slot_002_2',pid:'node002',dataObject:{dSlot:'3,4',dType:'SSD',dCop:'2G',dFom:'否', dStatus:'正在格式化'}},
		{id:'slot_002_3',pid:'node002',dataObject:{dSlot:'5,6',dType:'SSD',dCop:'102G',dFom:'否', dStatus:''}},

		{id:'node003', isLeaf:false, dataObject:{dName:'node003', dIP:'192.168.13.13'},userObject:{isGroup:true}},

		{id:'node004', isLeaf:false, dataObject:{dName:'node004', dIP:'192.168.13.14'},userObject:{isGroup:true}}		 
		  
		];
}

function createCB(infoObj){
	var cb = Core4j.Domhelper.createElement("input",{
	attributeNames:['type'],
	valueObject:{type:'checkbox'}
	});

	return cb;
}

var soCacheGirdTree=new Core4j.toolbox.TableTree4j({
	columns:[
			{width:'28px', renderFunction:createCB},		
			{dataIndex:'dName', width:'98px'},
			{dataIndex:'dIP', isNodeClick:true, width:'126px'},
			{dataIndex:'wwid', width:'86px'},
			{dataIndex:'dSlot', width:'86px'},
			{dataIndex:'dSlot', width:'86px'},
			{dataIndex:'dType', width:'78px'},
			{dataIndex:'dCop', width:'72px'},
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

soCacheGirdTree.build(new chooseDeviceJsonData().jsoninitNodes,true);