/*创建 nfs 服务*/
$("#addNfs").live('click', function(){
	$.ajax({
	    url: '../windows/service/addNfs.html',
	    success: function (data) {
	       createArtDialog("创建 NFS 导出", data);
	    },
	    cache: false
	});
	return false;
})

/*修改 nfs 服务*/
$("#updateNfs").live('click', function(){
	$.ajax({
	    url: '../windows/service/updateNfs.html',
	    success: function (data) {
	        createArtDialog("修改 NFS 导出", data);
	    },
	    cache: false
	});
	return false;
})