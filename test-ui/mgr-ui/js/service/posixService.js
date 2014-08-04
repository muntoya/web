$("#addPosix").live('click', function(){
	$.ajax({
	    url: '../windows/service/addPosix.html',
	    success: function (data) {
	        createArtDialog("创建 POSIX 访问", data);
	    },
	    cache: false
	});
	return false;
})

/*修改 posix 服务*/
$("#updatePosix").live('click', function(){
	$.ajax({
	    url: '../windows/service/updatePosix.html',
	    success: function (data) {
	        createArtDialog("修改 POSIX 访问", data);
	    },
	    cache: false
	});
	return false;
})