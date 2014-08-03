/*网卡设置*/
$("#networkCard").live('click', function(){
	$.ajax({
	    url: '../windows/device/networkCard.html',
	    success: function (data) {
	       createArtDialog("网卡管理", data);
	    },
	    cache: false
	});
	/*var oHead = document.getElementsByTagName('HEAD').item(0);
    var oScript= document.createElement("script");
    oScript.type = "text/javascript";
    oScript.src="../../js/greentable2.js";
    oHead.appendChild( oScript);*/
	//$("head").append("<script src='../../js/greentable2.js'><\/script>");
	return false;
})

/*关闭窗口时移除 greentable2.js*/


/*增加网卡*/
$("#addNetworkCard").live('click', function(){
	$.ajax({
	    url: '../windows/device/addNetworkCard.html',
	    success: function (data) {
	        createArtDialog("添加网卡", data);
	    },
	    cache: false
	});
	return false;
})

/*修改网卡*/
$("#updateNetworkCard").live('click', function(){
	$.ajax({
	    url: '../windows/device/updateNetworkCard.html',
	    success: function (data) {
	       createArtDialog("修改网卡", data);
	    },
	    cache: false
	});
	return false;
})


/*分组*/
$("#grouping").live('click', function(){
	$.ajax({
	    url: '../windows/device/grouping.html',
	    success: function (data) {
	       createArtDialog("分组", data);
	    },
	    cache: false
	});
	return false;
})