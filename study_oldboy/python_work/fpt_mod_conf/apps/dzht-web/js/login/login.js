function choiceShow(){
	var needsjyzm = $("#needsjyzm").val();
	var dllx = $("#dllx_back").val();
	$("#dllx_"+dllx).prop("checked", true);
	if("1"==needsjyzm){
		$("#sjhmDiv").css("display","block");
		$("#sjhmyzmDiv").css("display","block");
		$("#zhmmDiv").css("display","none");
	}else{
		$("#sjhmDiv").css("display","none");
		$("#sjhmyzmDiv").css("display","none");
		$("#zhmmDiv").css("display","block");
	}
	var errormsg = $("#errormsgHide").val();
	if(""!=errormsg){
		$("#errormsg").css("display","block");
	}
}

function getMobileCode(){
	var mobile=$("#sjhm").val();
	var reg = /^1\d{10}$/;
	var dllx = $("#dllx").val();
	var mobileYzmKey = $("#mobileYzmKey").val();
	if(reg.test(mobile)){
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
		    		  	$("#randomMobile").val(json[0].randomMobile);
					}else if(json[0].text==9999){
						$("#errormsg").html("手机验证码请求过于频繁，请稍后再试");
						$("#errormsg").css("display","block");
						return false;
					}else{
					    $("#errormsg").html("手机验证码发送失败，请稍后再试");
					    $("#errormsg").css("display","block");
					    return false;
					}
		    }
		});
	}else{
		$("#errormsg").text("手机格式错误!");
		$("#errormsg").css("display","block");
		return false;
	}

}



function loginSubmit(){
	var needsjyzm = $("#needsjyzm").val();
	var zhmc = $("#zhmc").val();
	var zhmm = $("#zhmm").val();
		if(zhmc==""){
			$("#errormsg").text("登录账号不能为空");
			$("#errormsg").css("display","block");
			return;
		}
		if("1"==needsjyzm){//手机验证码的登录
			
		}else{//常规账号登录
			if(zhmm==""){
				$("#errormsg").text("密码不能为空");
				$("#errormsg").css("display","block");
				return;
			}
		}
		
		 // m_verifykey为系统字符串变量，为null时表示未验证，否则为已验证的key.
		  if (!m_verifykey) {
			  alertMsg("请先完成验证码确认.");
			  return;
		  }
		//====判断是否需要强制修改密码======
		
		//====判断是否需要强制修改密码======  
		//-------------------安全登录起----------------------------
		//获取随机验证码
		var randomNum;
		var loginRandomCode=$("#loginRandomCode").val();
		$.ajax({
			url : "index.do?method=getLoginRandomCode",
			dataType:"json",
			type : "post",
			async : false,
			cache : false,
			data : {"loginRandomCode":loginRandomCode},
			success : function(data) {
				var jsonMap=data.jsonMap;
				var code=jsonMap.code;
				if('0000'==code){
					randomNum=jsonMap.randomCode;
				}
			}
		});
		if(null==randomNum||''==randomNum){
			return;
		}
		var md5zhmm=md5(zhmm);
		md5zhmm=md5(md5zhmm+randomNum);
		$("#md5zhmm").val(md5zhmm);
		//----------------安全登录止-------------------------------
		
		$("#forms").submit();
}