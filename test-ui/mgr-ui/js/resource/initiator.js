$(function() {     
    $('#itemInfo').bind('itemClick', getInfo);
    // setInterval(refreshTableData, 5000);  // 定时刷新页面
})

// tab 点击事件
$('#itemInfo h2 a').live({
	click:function(){
		$(this).siblings().removeClass('choose');
		$(this).addClass('choose');
		$('#itemInfo').trigger('itemClick');
		return false;
	}
})

// 获取 tab 标签信息
function getInfo(){
	var selectedNum = $('#mainTable .table_body tr.select').size();
	if ( selectedNum != 1){
		var str = '<div id="tabInfo" class="panel_content p_12_24 h150"></div>';
		$('#tabInfo').replaceWith(str);
	}else{
		var id = $('#mainTable .table_body tr.select').attr('attr');
		var url='';
		if ($('#init_detail').hasClass('choose')) {
			url = '/api/resource/pages/initiator/' + id + '/detail';
		}
		$.ajax({
	        type: 'GET',
	        url: url,        
	        success: function(respond) {
	            $('#tabInfo').replaceWith(respond);
	        }
	    })
	}	
}

// 刷新主表格数据
function refreshTableData(){	
	var tempSelect = getSelected();
	$.ajax({
        type: 'GET',
        url: '/api/resource/pages/initiator/list',        
        success: function(respond) {
            $('#mainTable .table_body').replaceWith(respond);
            setSelected(tempSelect);
            $('#itemInfo').trigger('itemClick');
        }
    })
}

// 获取当前选中数据，放入 id， 返回数组
function getSelected(){
	var selectedTR = $('#mainTable .table_body tr.select');
	var temp = [];
	selectedTR.each(function(){
		temp.push($(this).attr('attr'));
	});
	return temp;	
}

//  根据传入数组数据，将对应id 的tr 设置为选中状态
function setSelected(selt){
	var tr = $('#mainTable .table_body tr');
	tr.each(function(){
		for (var i=tr.length-1; i>=0; i--){
			if ($(this).attr('attr') == selt[i]){
				$(this).addClass('select');				
				break;
			}
		}
	});
}