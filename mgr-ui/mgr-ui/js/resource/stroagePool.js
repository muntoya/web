$(function() {     
    $('#itemInfo').bind('itemClick', getInfo);
    //setInterval(refreshTableData, 5000);  // 定时刷新页面
})

$('#itemInfo h2 a').live({
	click:function(){
		$(this).siblings().removeClass('choose');
		$(this).addClass('choose');
		$('#itemInfo').trigger('itemClick');
		return false;
	}
})

function getInfo(){
	var selectedNum = $('#mainTable .table_body tr.select').size();
	if ( selectedNum != 1){
		var str = '<div id="tabInfo" class="panel_content p_12_24 h150"></div>';
		$('#tabInfo').replaceWith(str);
	}else{
		var id = $('#mainTable .table_body tr.select').attr('attr');
		var url='';
		if ($('#pool_detail').hasClass('choose')) {
			url = '/api/resource/pages/pool/' + id + '/detail';
		}else if ($('#pool_lun').hasClass('choose')){
			url = '/api/resource/pages/pool/' + id + '/lun';
		}else if ($('#pool_disk').hasClass('choose')){
			url = '/api/resource/pages/pool/' + id + '/disk';
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

function refreshTableData(){	
	var tempSelect = getSelected();
	$.ajax({
        type: 'GET',
        url: '/api/resource/pages/pool/list',        
        success: function(respond) {
            $('#mainTable .table_body').replaceWith(respond);
            setSelected(tempSelect);
            $('#itemInfo').trigger('itemClick');
        }
    })
}

function getSelected(){
	var selectedTR = $('#mainTable .table_body tr.select');
	var temp = [];
	selectedTR.each(function(){
		temp.push($(this).attr('attr'));
	});
	return temp;	
}

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