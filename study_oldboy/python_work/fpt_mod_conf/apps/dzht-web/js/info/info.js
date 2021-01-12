//type==1为手机，type==2为邮箱
function getCode(type){
	if(type==1){
		var mobile=$("#sjhm").val();
		if(null==mobile || ""==mobile){
			alertMsg("手机号码不能为空");
			return false;
		}
		if(mobile == $("#sjhmTkHide").val()){
			alertMsg("新旧手机号不能相同");
			return false;
		}
		var mobileYzmKey = $("#mobileYzmKey").val();
		var reg = /^1\d{10}$/;
		if(reg.test(mobile)){
			$("[name='yzmBut']").attr('disabled',true);
			$.ajax({
				url : "com.do?method=getMobileCode",
				dataType:"json",
				type : "post",
				async : false,
				cache : false,
				data : {"mobile":mobile,"mobileYzmKey":mobileYzmKey},
				success : function(data) {
			    	  var json = eval(data);
			    	  if(json[0].text==1){
			    		  	updatebutton();
			    		  	$("#randomMobile").val(json[0].randomMobile);
						}else if(json[0].text==9999){
							$("[name='errormsg_sjh']").html("手机验证码请求过于频繁，请稍后再试");
							$("[name='errormsg_sjh']").css("display","block");
							$("[name='yzmBut']").attr('disabled',false);
							return false;
						}else{
							$("[name='errormsg_sjh']").html("手机验证码发送失败，请稍后再试");
							$("[name='errormsg_sjh']").css("display","block");
							$("[name='yzmBut']").attr('disabled',false);
						    return false;
						}
			    }
			});
		}else{
			$("[name='errormsg_sjh']").text("手机格式错误!");
			$("[name='errormsg_sjh']").css("display","block");
			return false;
		}
	}else if(type==2){
		var zhmc=$("#zhmc").val();
		if(null==zhmc || ""==zhmc){
			alertMsg("邮箱号不能为空");
			return false;
		}
		if(zhmc == $("#zhmcTkHide").val()){
			alertMsg("新旧邮箱号不能相同");
			return false;
		}
		var emailYzmKey = $("#emailYzmKey").val();
		var flag = 0;
		if(zhmc.indexOf("@")>-1 && zhmc.indexOf(".")>-1){
			flag = 1
		}
		if( flag == 1 ){
			$("[name='yzmBut']").attr('disabled',true);
			$.ajax({
				url : "com.do?method=getEmailCode",
				dataType:"json",
				type : "post",
				async : false,
				cache : false,
				data : {"email":zhmc,"emailYzmKey":emailYzmKey},
				success : function(data) {
			    	  var json = eval(data);
			    	  if(json[0].text==1){
			    		  	updatebutton();
			    		  	$("#randomEmail").val(json[0].randomEmail);
						}else if(json[0].text==9999){
							$("[name='errormsg_yxh']").html("邮箱验证码请求过于频繁，请稍后再试");
							$("[name='errormsg_yxh']").css("display","block");
							$("[name='yzmBut']").attr('disabled',false);
							return false;
						}else{
							$("[name='errormsg_yxh']").html("邮箱验证码发送失败，请稍后再试");
							$("[name='errormsg_yxh']").css("display","block");
							$("[name='yzmBut']").attr('disabled',false);
						    return false;
						}
			    }
			});
		}else{
			$("[name='errormsg_yxh']").text("邮箱格式错误!");
			$("[name='errormsg_yxh']").css("display","block");
			return false;
		}
	}
}



//更改手机号
function sjhmChange(){
	var randomMobile = $("#randomMobile").val();
	var sjhm = $("#sjhm").val();
	if(""==sjhm){
		alertMsg("新手机号不能为空");
		return false;
	}
	if(sjhm == $("#sjhmTkHide").val()){
		alertMsg("新旧手机号不能相同");
		return false;
	}
	var sjyzm = $("#sjyzm").val();
	if(""==sjyzm){
		alertMsg("验证码不能为空");
		return false;
	}
	$.ajax({
		url : "info.do?method=updateSJHM",
		dataType:"json",
		type : "post",
		async : false,
		cache : false,
		data : {"sjhm":sjhm,"sjyzm":sjyzm,"randomMobile":randomMobile},
		success : function(data) {
			var jsonMap=data.jsonMap;
			var code=jsonMap.code;
			if('0000'==code){
				$("#info_sjhm_show_div").text(sjhm);
				$("#sjhmTkHide").val(sjhm);
				$("#sjhm_change_success").modal("show").css({"visibility":"visible","display":"block"});
			}else if("9999"==code){
				alertMsg(jsonMap.codemsg);
			}
		}
	});
}

//更改邮箱号/账号
function zhmcChange(){
	var randomEmail = $("#randomEmail").val();
	var zhmc = $("#zhmc").val();
	if(""==zhmc){
		alertMsg("新邮箱号不能为空");
		return false;
	}
	if(zhmc == $("#zhmcTkHide").val()){
		alertMsg("新旧邮箱号不能相同");
		return false;
	}
	var yxyzm = $("#yxyzm").val();
	if(""==yxyzm){
		alertMsg("验证码不能为空");
		return false;
	}
	$.ajax({
		url : "info.do?method=updateZhmc",
		dataType:"json",
		type : "post",
		async : false,
		cache : false,
		data : {"zhmc":zhmc,"yxyzm":yxyzm,"randomEmail":randomEmail},
		success : function(data) {
			var jsonMap=data.jsonMap;
			var code=jsonMap.code;
			var codemsg = jsonMap.codemsg;
			if('0000'==code){
				$("#info_zhmc_show_div").text(zhmc);
				$("#zhmcTkHide").val(zhmc);
				$("#email_change_success").modal("show").css({"visibility":"visible","display":"block"});
			}else if("9999"==code){
				alertMsg(codemsg);
			}
		}
	});
}


function alertPassworddlg(){
	$("#mm_oldpass").val("");
	$("#mm_passwd").val("");
	$("#mm_passwd2").val("");
		$.post("info.do?method=getPwdModifyRandomCodeKey",function(data,struts){
		  	  var jsonMap=data.jsonMap;
		  	  var code=jsonMap.code;
			if('0000'==code){
			  $("#randomCodeKey").val(jsonMap.randomCode);
			  var val= $("#randomCodeKey").val();
			  //alertMsg(val);
				}
		    },"json");
}



//修改密码
function updatePasswd(){
    var oldpass = $("#mm_oldpass").val();
    var passwd = $("#mm_passwd").val();
    var passwd2 = $("#mm_passwd2").val();
    $("[name='errormsg_mm']").html("");
    $("[name='errormsg_mm']").css("display","none");
    if(oldpass==""){
    	$("[name='errormsg_mm']").html("旧密码不能为空");
        $("[name='errormsg_mm']").css("display","block");
	     return;
    }
    if(passwd==""){
    	$("[name='errormsg_mm']").html("新密码不能为空");
        $("[name='errormsg_mm']").css("display","block");
    	return;
    }
    if(passwd.length<8){
    	$("[name='errormsg_mm']").html("密码长度不能低于8位");
    	$("[name='errormsg_mm']").css("display","block");
    	return;
    }
    if(passwd==oldpass){
    	$("[name='errormsg_mm']").html("新旧密码不能相同");
    	$("[name='errormsg_mm']").css("display","block");
        return;
    }
    if(passwd2==""){
    	$("[name='errormsg_mm']").html("请输入确认密码");
    	$("[name='errormsg_mm']").css("display","block");
    	return;
    }
    if(passwd!=passwd2){
    	$("[name='errormsg_mm']").html("两次密码不一致");
    	$("[name='errormsg_mm']").css("display","block");
    	return;
    }
    if(level<3){
    	$("[name='errormsg_mm']").html("请输入8-16位字母、数字、符号两种或两种以上组合！");
    	$("[name='errormsg_mm']").css("display","block");
    	return ;
    }
  //-------md5加密
    //-------------------安全校验----------------------------
	//获取随机验证码
	var randomCode;
	var randomCodeKey= $("#randomCodeKey").val();
	//alertMsg('randomCodeKey=='+randomCodeKey);
	$.ajax({
		url : "info.do?method=getPwdModifyRandomCode",
		dataType:"json",
		type : "post",
		async : false,
		cache : false,
		data : {"randomCodeKey":randomCodeKey},
		success : function(data) {
			var jsonMap=data.jsonMap;
			var code=jsonMap.code;
			if('0000'==code){
				randomCode=jsonMap.randomCode;
			}
		}
	});
	if(null==randomCode||''==randomCode){
		$("#loginPwdmsg").html("获取密码随机校验码失败");
		return;
	}
	//-----------------------------------------------
    //md5加密
    passwd=md5(passwd);
    oldpass=md5(oldpass);
    oldpass=md5(oldpass+randomCode);
	 $.post("info.do?method=updatePasswd",{"oldpass":oldpass,"randomCodeKey":randomCodeKey,"passwd":passwd},function(returnInfo,struts){
			var json = eval(returnInfo);
			if(json[0].text==1){//修改成功
				alertMsg("修改成功");
				$("#mima").modal("hide");
			}else if(json[0].text==0){//旧密码错误
				$("[name='errormsg_mm']").html("旧密码错误");
		    	$("[name='errormsg_mm']").css("display","block");
			}else if(json[0].text==5){
				alertMsg(json[0].msg);
			}else{//修改失败
				alertMsg("修改失败");
			}
		},"json");
    
}

//没有密码的时候，设置密码
function setPasswd(){
    var passwd = $("#passwd").val();
    var passwd2 = $("#passwd2").val();
    $("[name='errormsg_mm']").html("");
    $("[name='errormsg_mm']").css("display","none");
    if(passwd==""){
    	$("[name='errormsg_mm']").html("密码不能为空");
        $("[name='errormsg_mm']").css("display","block");
    	return;
    }
    if(passwd.length<8){
    	$("[name='errormsg_mm']").html("密码长度不能低于8位");
    	$("[name='errormsg_mm']").css("display","block");
    	return;
    }
    if(passwd2==""){
    	$("[name='errormsg_mm']").html("请输入确认密码");
    	$("[name='errormsg_mm']").css("display","block");
    	return;
    }
    if(passwd!=passwd2){
    	$("[name='errormsg_mm']").html("两次密码不一致");
    	$("[name='errormsg_mm']").css("display","block");
    	return;
    }
    if(level<3){
    	$("[name='errormsg_mm']").html("请输入8-16位字母、数字、符号两种或两种以上组合！");
    	$("[name='errormsg_mm']").css("display","block");
    	return ;
    }
    //md5加密
    passwd=md5(passwd);
	 $.post("info.do?method=setPasswd",{"passwd":passwd},function(returnInfo,struts){
			var json = eval(returnInfo);
			if(json[0].text==1){//修改成功
				alertMsg("密码设置成功");
				$("#shezhimima").modal("hide");
				if(json[0].zhlxSession=="gr"){
					window.location.href="info.do?method=info";
				}
			}else if(json[0].text==2){//
				$("[name='errormsg_mm']").html("密码设置失败");
		    	$("[name='errormsg_mm']").css("display","block");
			}else if(json[0].text==3){
				alertMsg("非法请求");
			}else{//修改失败
				alertMsg("密码设置失败");
			}
		},"json");
}

//打开或关闭通知事件
function changeTz(tzId){
	var zt = "";//需要传递过去的状态值
	if($("#"+tzId).hasClass("kaitong")){//表示当前是开通的，需要关闭
		$("#"+tzId).removeClass("kaitong").addClass("guanbi");
	}else if($("#"+tzId).hasClass("guanbi")){//表示当前是关闭的，需要开通
		$("#"+tzId).removeClass("guanbi").addClass("kaitong");
	}
	//留着，写ajax逻辑
	
}

//是否显示设置密码的框
function showHideSZMM(){
	var zhmmSjkz = $("#zhmmSjkz").val();
	if(""==zhmmSjkz){
		$('#shezhimima').modal('show');
	}
}


function emailChangeSuccess(){
	$("#email_change_success").modal("hide");
	window.location.href="index.do?method=login";
}

function sjhmChangeSuccess(){
	$("#sjhm_change_success").modal("hide");
	$("#shoujihao").modal("hide");
}