function showMsg(){
	var errormsg = $("#errormsgHide").val();
	if(""!=errormsg){
		$("#errormsg").css("display","block");
	}
}


function getMobileCode(){
	var mobile=$("#sjhm").val();
	if(null==mobile || ""==mobile){
		alertMsg("手机号码不能为空");
		return false;
	}
	var reg = /^1\d{10}$/;
	var mobileYzmKey = $("#mobileYzmKey").val();
	if(reg.test(mobile)){
		 if (!m_verifykey) {
			  alertMsg("请先完成验证码确认.");
			  return;
		  }
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
						refreshCode();
						$("[name='yzmBut']").attr('disabled',false);
						$("[name='errormsg']").html("手机验证码请求过于频繁，请稍后再试");
						$("[name='errormsg']").css("display","block");
						return false;
					}else{
						refreshCode();
						$("[name='yzmBut']").attr('disabled',false);
						$("[name='errormsg']").html("手机验证码发送失败，请稍后再试");
						$("[name='errormsg']").css("display","block");
					    return false;
					}
		    }
		});
	}else{
		$("[name='errormsg']").text("手机格式错误!");
		$("[name='errormsg']").css("display","block");
		return false;
	}
}

function resetPwd(){
    var passwd = $("#mm_passwd").val();
    var passwd2 = $("#mm_passwd2").val();
    var zhmc = $("#zhmc").val();
    if(zhmc==""){
    	$("[name='errormsg']").html("账号不能为空");
        $("[name='errormsg']").css("display","block");
    	return;
    }
    if(zhmc.indexOf("@")>-1 && zhmc.indexOf(".")>-1){
    	
	}else{
		$("[name='errormsg']").html("账号格式不对");
        $("[name='errormsg']").css("display","block");
    	return;
	}
    $("[name='errormsg']").html("");
    $("[name='errormsg']").css("display","none");
    if(passwd==""){
    	$("[name='errormsg']").html("新密码不能为空");
        $("[name='errormsg']").css("display","block");
    	return;
    }
    if(passwd.length<8){
    	$("[name='errormsg']").html("密码长度不能低于8位");
    	$("[name='errormsg']").css("display","block");
    	return;
    }
    if(passwd2==""){
    	$("[name='errormsg']").html("请输入确认密码");
    	$("[name='errormsg']").css("display","block");
    	return;
    }
    if(passwd!=passwd2){
    	$("[name='errormsg']").html("两次密码不一致");
    	$("[name='errormsg']").css("display","block");
    	return;
    }
    if(level<3){
    	$("[name='errormsg']").html("请输入8-16位字母、数字、符号两种或两种以上组合！");
    	$("[name='errormsg']").css("display","block");
    	return ;
    }
    
    var sjhm = $("#sjhm").val();
    if(sjhm==""){
    	$("[name='errormsg']").text("手机号码不能为空!");
		$("[name='errormsg']").css("display","block");
		return false;
    }
    var reg = /^1\d{10}$/;
	if(reg.test(sjhm)){
		
	}else{
		$("[name='errormsg']").text("手机格式错误!");
		$("[name='errormsg']").css("display","block");
		return false;
	}
    var sjyzm = $("#sjyzm").val();
    if(sjyzm==""){
    	$("[name='errormsg']").text("手机验证码不能为空!");
		$("[name='errormsg']").css("display","block");
		return false;
    }
	//-----------------------------------------------
    //md5加密
    passwd=md5(passwd);
    var randomMobile = $("#randomMobile").val();
   
	 $.post("comIndex.do?method=reset",{"sjyzm":sjyzm,"sjhm":sjhm,"randomMobile":randomMobile,"passwd":passwd,"zhmc":zhmc},function(data,struts){
		 	var jsonMap=data.jsonMap;
			var code=jsonMap.code;
			if('0000'==code){
				$("#forget_success").modal("show").css({"visibility":"visible","display":"block"});
			}else if("9999"==code){
				alertMsg(jsonMap.codemsg);
			}
		},"json");
}

function resetSuccess(){
	$("#forget_success").modal("hide");
	window.location.href="index.do?method=login";
}