/******屏幕高度 ****/
height = document.documentElement.clientHeight - 54;
$('#body_html').height(height);

/*创建公共弹框*/
/**
title 弹框的标题；
data 弹框填充的内容
button 弹框显示的按钮及对应的文本内容
fnConfirm 点击确认按钮后，执行的方法
fnCancel 点击取消按钮后，执行的方法
fnHelp 点击帮助按钮后，执行的方法
*/
function createArtDialog(title, data, button, fnConfirm, fnCancel, fnHelp) {
	var button = createButton(button, fnConfirm, fnCancel, fnHelp);
	var dialog = art.dialog({
		/*id: 'N3690',*/
		title: title,
		lock: true,
		opacity: 0.5,
		top: '42px',
		drag: false,
		content: data,
		button: button
	});
	return dialog;
}

/*创建通用自定义按钮*/
function createButton(button, fnConfirm, fnCancel, fnHelp) {
	var okVal;
	var canceVal;
	var helpVal;
	button && button.okVal ? okVal = button.okVal : okVal = '确定';
	button && button.canceVal ? canceVal = button.canceVal : canceVal = '取消';
	button && button.helpVal ? helpVal = button.helpVal : helpVal = '帮助';
	var button = [
			{
				name: okVal,
				callback: function(){
					fnConfirm ? fnConfirm() : null;
					return false;
				},
				focus: true
			},
			{
				name: canceVal,
				callback: function(){
					fnCancel ? fnCancel() : null;
				}
			},
			{
				name:helpVal,
				callback: function(){
					fnHelp ? fnHelp() : null;
				}
			}
		]
	return button;
}