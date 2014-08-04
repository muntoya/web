$(".table_body tr").live({	
	/*每行的移入移出效果*/
	mouseover: function() {
		$(this).addClass("hover");
	},
	mouseout: function() {
		$(this).removeClass("hover");
	},
	//行上点击
	click: function(){
		$(this).siblings().removeClass('select');
		$(this).addClass("select");
		setHeader($(this).parents(".tableContainer"));
	}
})

/*行内 checkbox 点击*/
$('.table_body tr .cbox').live({
	click:function(){		
	 	if ($(this).parent().hasClass("select")) {
			$(this).parent().removeClass("select");			
		}else{
			$(this).parent().addClass("select");
		}
		setHeader($(this).parents(".tableContainer"));
		return false;
	}
});
/* header 中的复选框（全选）*/
$(".table_header .cbox").live({	
	click:function(){		
	 	var $trCB = $(this).parents(".tableContainer").find(".table_body tr");
	 	if ( $(this).hasClass("select") ){
	 		$(this).removeClass("select");
	 		$trCB.each(function(){			
				$(this).removeClass("select");						
			});			
	 	}else{
	 		$(this).addClass("select");
	 		$trCB.each(function(){			
				$(this).addClass("select");
			});
	 	}
	 	var $num = $(this).parents(".tableContainer").find(".choose_num");
		$num.text($(this).parents(".tableContainer").find(".table_body tr.select").size());

		if (container.attr("id") == "mainTable"){
			$('#itemInfo').trigger('itemClick');//自定义事件，表示表格选中内容有变化
		}
		return false;
	 }
});

function setHeader(container){
	var totalSize = container.find(".table_body tr").size();
	var selectedSize = container.find(".table_body tr.select").size();

	var $headerCB = container.find(".table_header .cbox");

	if ($headerCB){
		if (totalSize > 0 && totalSize == selectedSize){
			$headerCB.addClass('select');
		} else {
			$headerCB.removeClass('select');
		}
		container.find(".choose_num").text(selectedSize);
	}

	if (container.attr("id") == "mainTable"){
		$('#itemInfo').trigger('itemClick');//自定义事件，表示表格选中内容有变化
	}
}