$(function () { 
	var randomReg = $("#randomReg").val();
	
	//营业执照
	$("#upload_YYZZ").fileupload({
        url: 'upload.do?method=upload_YYZZ',
        dataType: 'json',
        autoUpload: true,
        formData : {'randomReg':randomReg},
        acceptFileTypes: /(\.|\/)(gif|jpg|bmp|png|jpeg?)$/i,
        maxFileSize: 3*1024*1024
	}).on('fileuploadadd', function (e, data) {
		  $(this).attr("disabled",true);
	}).on('fileuploadprocessalways', function (e, data) {
		if(data.files.error){
		   $(this).removeAttr("disabled");
		   if(data.files[0].error=='File type not allowed'){
		       alertMsg("请上传图片类型文件");
		   }
		   if(data.files[0].error=='File is too large'){
		     alertMsg("上传文件过大，请上传小于3MB的文件");
		   }  
		} 
	}).on('fileuploadprogressall', function (e, data) {
	   $(".upload_show_hide,#upload_YYZZ").attr("disabled","disabled");//禁用上传按钮
	   var progress = parseInt(data.loaded / data.total * 100, 10);
	   $(".abcdefg").css("display","block");//显示进度条
	   $('.progress-bar-warning').css('width',progress + '%');
	}).on('fileuploaddone', function (e, data) {
		$(".abcdefg").css("display","none");//隐藏进度条
        $('.progress-bar-warning').css("width","0");
		$(".upload_show_hide,#upload_YYZZ").removeAttr("disabled");//放开上传按钮
		var dataResult = data.result;
		var jsonMap = dataResult.jsonMap;
		var code=jsonMap.code;
		var msg = jsonMap.codemsg;
		if(code=='0000'){
			alertMsg("上传成功");
        	var hbaseContent = jsonMap.hbaseContent;
        	insertSrc("upload_YYZZ",hbaseContent);
        }else{
        	alertMsg(msg);
			return;
        }
	});
	
	//组织机构代码
	$("#upload_ZZJGDM").fileupload({
		url: 'upload.do?method=upload_ZZJGDM',
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
		$(".upload_show_hide,#upload_ZZJGDM").attr("disabled","disabled");//禁用上传按钮
		var progress = parseInt(data.loaded / data.total * 100, 10);
		$(".abcdefg").css("display","block");//显示进度条
		$('.progress-bar-warning').css('width',progress + '%');
	}).on('fileuploaddone', function (e, data) {
		$(".abcdefg").css("display","none");//隐藏进度条
		$('.progress-bar-warning').css("width","0");
		$(".upload_show_hide,#upload_ZZJGDM").removeAttr("disabled");//放开上传按钮
		var dataResult = data.result;
		var jsonMap = dataResult.jsonMap;
		var code=jsonMap.code;
		var msg = jsonMap.codemsg;
		if(code=='0000'){
			alertMsg("上传成功");
			var hbaseContent = jsonMap.hbaseContent;
			insertSrc("upload_ZZJGDM",hbaseContent);
		}else{
			alertMsg(msg);
			return;
		}
	});
	
	
	//营业执照-统一社会信用
	$("#upload_TYSHXY").fileupload({
		url: 'upload.do?method=upload_TYSHXY',
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
		$(".upload_show_hide,#upload_TYSHXY").attr("disabled","disabled");//禁用上传按钮
		var progress = parseInt(data.loaded / data.total * 100, 10);
		$(".abcdefg").css("display","block");//显示进度条
		$('.progress-bar-warning').css('width',progress + '%');
	}).on('fileuploaddone', function (e, data) {
		$(".abcdefg").css("display","none");//隐藏进度条
		$('.progress-bar-warning').css("width","0");
		$(".upload_show_hide,#upload_TYSHXY").removeAttr("disabled");//放开上传按钮
		var dataResult = data.result;
		var jsonMap = dataResult.jsonMap;
		var code=jsonMap.code;
		var msg = jsonMap.codemsg;
		if(code=='0000'){
			alertMsg("上传成功");
			var hbaseContent = jsonMap.hbaseContent;
			insertSrc("upload_TYSHXY",hbaseContent);
		}else{
			alertMsg(msg);
			return;
		}
	});
	
	
	
	//法人代理人身份证
	$("#upload_FRDLRSFZ").fileupload({
		url: 'upload.do?method=upload_FRDLRSFZ',
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
		$(".upload_show_hide,#upload_FRDLRSFZ").attr("disabled","disabled");//禁用上传按钮
		var progress = parseInt(data.loaded / data.total * 100, 10);
		$(".abcdefg").css("display","block");//显示进度条
		$('.progress-bar-warning').css('width',progress + '%');
	}).on('fileuploaddone', function (e, data) {
		$(".abcdefg").css("display","none");//隐藏进度条
		$('.progress-bar-warning').css("width","0");
		$(".upload_show_hide,#upload_FRDLRSFZ").removeAttr("disabled");//放开上传按钮
		var dataResult = data.result;
		var jsonMap = dataResult.jsonMap;
		var code=jsonMap.code;
		var msg = jsonMap.codemsg;
		if(code=='0000'){
			alertMsg("上传成功");
			var hbaseContent = jsonMap.hbaseContent;
			insertSrc("upload_FRDLRSFZ",hbaseContent);
		}else{
			alertMsg(msg);
			return;
		}
	});
	
	
	
	//企业申请表图片1
	$("#upload_SQB_1").fileupload({
		url: 'upload.do?method=upload_SQB_1',
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
		$(".upload_show_hide,#upload_SQB_1").attr("disabled","disabled");//禁用上传按钮
		var progress = parseInt(data.loaded / data.total * 100, 10);
		$(".abcdefg").css("display","block");//显示进度条
		$('.progress-bar-warning').css('width',progress + '%');
	}).on('fileuploaddone', function (e, data) {
		$(".abcdefg").css("display","none");//隐藏进度条
		$('.progress-bar-warning').css("width","0");
		$(".upload_show_hide,#upload_SQB_1").removeAttr("disabled");//放开上传按钮
		var dataResult = data.result;
		var jsonMap = dataResult.jsonMap;
		var code=jsonMap.code;
		var msg = jsonMap.codemsg;
		if(code=='0000'){
			alertMsg("上传成功");
			var hbaseContent = jsonMap.hbaseContent;
			insertSrc("upload_SQB_1",hbaseContent);
		}else{
			alertMsg(msg);
			return;
		}
	});
	
	
	
	//企业申请表图片2
	$("#upload_SQB_2").fileupload({
		url: 'upload.do?method=upload_SQB_2',
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
		$(".upload_show_hide,#upload_SQB_2").attr("disabled","disabled");//禁用上传按钮
		var progress = parseInt(data.loaded / data.total * 100, 10);
		$(".abcdefg").css("display","block");//显示进度条
		$('.progress-bar-warning').css('width',progress + '%');
	}).on('fileuploaddone', function (e, data) {
		$(".abcdefg").css("display","none");//隐藏进度条
		$('.progress-bar-warning').css("width","0");
		$(".upload_show_hide,#upload_SQB_2").removeAttr("disabled");//放开上传按钮
		var dataResult = data.result;
		var jsonMap = dataResult.jsonMap;
		var code=jsonMap.code;
		var msg = jsonMap.codemsg;
		if(code=='0000'){
			alertMsg("上传成功");
			var hbaseContent = jsonMap.hbaseContent;
			insertSrc("upload_SQB_2",hbaseContent);
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