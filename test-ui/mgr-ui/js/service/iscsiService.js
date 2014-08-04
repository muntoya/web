/*创建 iscsi 服务*/
$("#addIscsi").live('click', function(){
	$.ajax({
	    url: '../windows/service/addIscsi.html',
	    success: function (data) {
	        createArtDialog("创建 ISCSI 服务", data);
	    },
	    cache: false
	});
	return false;
})

/*修改 iscsi 服务*/
$("#updateIscsi").live('click', function(){
	$.ajax({
	    url: '../windows/service/updateIscsi.html',
	    success: function (data) {
	        createArtDialog("创建 ISCSI 服务", data);
	    },
	    cache: false
	});
	return false;
})

/*配置启动器*/
$("#configInitiator").live('click', function(){
	$.ajax({
	    url: '../windows/service/configInitiator.html',
	    success: function (data) {
	        createArtDialog("配置启动器", data);
	    },
	    cache: false
	});
	return false;
})

/* 添加启动器 */
$("#addInitiator").live('click', function(){
	$.ajax({
	    url: '../windows/resouce/addInitiator.html',
	    success: function (data) {
	        createArtDialog("添加启动器", data);
	    },
	    cache: false
	});
	return false;
})

/*修改启动器*/
$("#updateInitiator").live('click', function(){
	$.ajax({
	    url: '../windows/resource/updateInitiator.html',
	    success: function (data) {
	        createArtDialog("修改启动器", data);
	    },
	    cache: false
	});
	return false;
})