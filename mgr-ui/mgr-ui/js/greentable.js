/*每行的移入移出效果*/
$(".table_body tr").live({
	/******hover ****/	
	 mouseover: function() {
		$(this).addClass("hover");
	 },
	 mouseout: function() {
		$(this).removeClass("hover");
	 },
	 /* body 中的复选框*/
	 click:function(){
	 	var $chooseAll = $(this).parents(".tableContainer").find(".table_header .cbox");
	 	var $chooseArr = $(this).parents(".tableContainer").find(".table_body tr");
	 	if ($(this).hasClass("select")) {
			$(this).removeClass("select");
			$chooseAll.removeClass("select");
		}else{
			$(this).addClass("select");									
			$chooseAll.addClass("select");	 
			$chooseArr.each(function(index){
				$chooseAll.hasClass("select")&& $chooseArr.eq(index).hasClass("select")?$chooseAll.addClass("select"):$chooseAll.removeClass("select");
			});		
		}

		var $num = $(this).parents(".tableContainer").find(".choose_num");
		$num.text($(this).parents(".tableContainer").find(".table_body tr.select").size());
		return false;
	 }
});


$(".table_header .cbox").live({
	/* header 中的复选框（全选）*/
	click:function(){
		var $chooseAll = $(this).parents(".tableContainer").find(".table_header .cbox");
	 	var $chooseArr = $(this).parents(".tableContainer").find(".table_body tr");
	 	if ( $(this).hasClass("select") ){
 		$(this).removeClass("select");
 		$chooseArr.each(function(){			
			$(this).removeClass("select");						
		});
	 	}else{
	 		$(this).addClass("select");
	 		$chooseArr.each(function(){			
				$(this).addClass("select");					
			});
	 	}
	 	var $num = $(this).parents(".tableContainer").find(".choose_num");
		$num.text($(this).parents(".tableContainer").find(".table_body tr.select").size());
		return false;
	 }
});