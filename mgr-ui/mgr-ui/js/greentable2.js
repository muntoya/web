/*每行的移入移出效果*/
$(".wContent .w_green_table .table_body tr").live({
	/******hover ****/
	mouseover: function() {
		$(this).addClass("hover");
	},
	mouseout: function() {
		$(this).removeClass("hover");
	},
	click: function() {
		var $chooseAll = $(this).parents(".w_green_table").find(".table_header .cbox");
		if ($(this).hasClass("select")) {
			$(this).removeClass("select");
			$chooseAll.removeClass("select");
		} else {
			$(this).addClass("select");
			$chooseAll.addClass("select");
			var $chooseArr = $(this).parents(".w_green_table").find(".table_body tr");
			$chooseArr.each(function(index) {
				$chooseAll.hasClass("select") && $chooseArr.eq(index).hasClass("select") ? $chooseAll.addClass("select") : $chooseAll.removeClass("select");
			});
		}
		$(this).parents(".w_green_table").find(".table_title .choose_num").text($(this).parents(".w_green_table").find(".table_body tr.select").size());
		return false;
	}
});

$(".wContent .w_green_table .table_header .cbox").live({
	click: function() {
		var $chooseArr = $(this).parents(".w_green_table").find(".table_body tr");
		if ($(this).hasClass("select")) {
			$(this).removeClass("select");
			$chooseArr.each(function() {
				$(this).removeClass("select");
			});
		} else {
			$(this).addClass("select");
			$chooseArr.each(function() {
				$(this).addClass("select");
			});
		}
		$(this).parents(".w_green_table").find(".table_title .choose_num").text($(this).parents(".w_green_table").find(".table_body tr.select").size());
	}
});