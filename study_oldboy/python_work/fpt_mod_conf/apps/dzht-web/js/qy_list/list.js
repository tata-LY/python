//下载 企业信息登记表模板
function downloadXxdj(){
	location.href="template/qyxxdjjcasqb.docx";
}


function updateJrfInfo(){
	var caurl = $("#caurl").val();
	if(caurl==""){
		alertMg("回调URL不能为空");
		return false;
	}
	$.ajax({
		url : "qyList.do?method=updateJrfInfo",
		dataType:"json",
		type : "post",
		async : false,
		cache : false,
		data : {"caurl":caurl},
		success : function(data) {
			var jsonMap=data.jsonMap;
			var code=jsonMap.code;
			var codemsg = jsonMap.codemsg;
			if('0000'==code){
				alertMsg("回调地址修改成功");
			}else if("9999"==code){
				alertMsg(codemsg);
			}
		}
	});
	
	
	
}