$(function () { 
	var randomReg = $("#randomReg").val();
	//个人手持身份证
	$("#upload_GRSCSFZ").fileupload({
		url: 'upload.do?method=upload_GRSCSFZ',
		dataType: 'json',
		autoUpload: true,
		formData : {'randomReg':randomReg},
		acceptFileTypes: /(\.|\/)(gif|jpg|bmp|png|jpeg?)$/i,
		maxFileSize: 2*1024*1024
	}).on('fileuploadadd', function (e, data) {
		$(this).attr("disabled",true);
	}).on('fileuploadprocessalways', function (e, data) {
		if(data.files.error){
			$(this).removeAttr("disabled");
			if(data.files[0].error=='File type not allowed'){
				alertMsg("请上传图片类型文件");
			}
			if(data.files[0].error=='File is too large'){
				alertMsg("上传文件过大，请上传小于2MB的文件");
			}  
		} 
	}).on('fileuploadprogressall', function (e, data) {
		$(".upload_show_hide,#upload_GRSCSFZ").attr("disabled","disabled");//禁用上传按钮
		var progress = parseInt(data.loaded / data.total * 100, 10);
		$(".abcdefg").css("display","block");//显示进度条
		$('.progress-bar-warning').css('width',progress + '%');
	}).on('fileuploaddone', function (e, data) {
		$(".abcdefg").css("display","none");//隐藏进度条
		$('.progress-bar-warning').css("width","0");
		$(".upload_show_hide,#upload_GRSCSFZ").removeAttr("disabled");//放开上传按钮
		var dataResult = data.result;
		var jsonMap = dataResult.jsonMap;
		var code=jsonMap.code;
		var msg = jsonMap.codemsg;
		if(code=='0000'){
			alertMsg("上传成功");
			var hbaseContent = jsonMap.hbaseContent;
			insertSrc("upload_GRSCSFZ",hbaseContent);
		}else{
			alertMsg(msg);
			return;
		}
	});
	

	//这个是对应最上面的括号的
   }) 
   
   
   
   
  

function insertSrc(id,hbaseContent){
	 var agent = window.navigator.userAgent;
    var isIE7 = agent.indexOf('MSIE 7.0') != -1;
    var isIE8 = agent.indexOf('MSIE 8.0') != -1;
    if (isIE7 || isIE8){
   	 document.getElementById(id+"_SHOW").src="data:image/gif;base64," + hbaseContent+new Date();
    }else{
   	 $("#"+id+"_SHOW").attr("src", "data:image/gif;base64," + hbaseContent);
    }
}
