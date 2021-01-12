function getMobileCode(){
	var mobile=$("#sjhm").val();
	if(null==mobile || ""==mobile){
		alertMsg("手机号码不能为空");
		return false;
	}
	var mobileYzmKey = $("#mobileYzmKey").val();
	var reg = /^1\d{10}$/;
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

function regGrSubmit(){
	var randomMobile = $("#randomMobile").val();
	var zjmc = $("#zjmc").val();
	var zjlx = $("#zjlx").val();
	var zjhm = $("#zjhm").val();
	var jrfId = $("#jrfId").val();
	var zhmc = $("#zhmc").val();
	var sjhm = $("#sjhm").val();
	var sjyzm = $("#sjyzm").val();
	if(""==zjmc){
		$("[name='errormsg']").text("姓名不能为空");
		$("[name='errormsg']").css("display","block");
		return false;
	}
	if(""==zjhm){
		$("[name='errormsg']").text("证件号码不能为空");
		$("[name='errormsg']").css("display","block");
		return false;
	}
	if("0"==zjlx){//身份证
		 if(!/^[\u4e00-\u9fa5]+$/gi.test(zjmc)){
			 alertMsg("身份证类型时，姓名只能输入汉字");
			 return false;
		 }
	           
		if(zjhm.length==15 || zjhm.length==18){
			var flag = validateIdCard(zjhm);
			if(!flag){
				alertMsg("身份证号输入有误，请重新输入");
				return false;
			}
		}else{
			alertMsg("身份证号输入有误，请重新输入");
			return false;
		}
	}
	if(""==zhmc){
		$("[name='errormsg']").text("邮箱地址不能为空");
		$("[name='errormsg']").css("display","block");
		return false;
	}
	if(zhmc.indexOf("@")>-1 && zhmc.indexOf(".")>-1){
		
	}else{
		$("[name='errormsg']").text("邮箱地址格式不对");
		$("[name='errormsg']").css("display","block");
		return false;
	}
	if(""==sjhm){
		$("[name='errormsg']").text("手机号码不能为空");
		$("[name='errormsg']").css("display","block");
		return false;
	}
	var reg = /^1\d{10}$/;
	if(!reg.test(sjhm)){
		$("[name='errormsg']").text("手机号码格式不对");
		$("[name='errormsg']").css("display","block");
		return false;
	}
	
	$.ajax({
		url : "comIndex.do?method=regGrSub",
		dataType:"json",
		type : "post",
		async : false,
		cache : false,
		data : {"zjmc":zjmc,"zjlx":zjlx,"zjhm":zjhm,"jrfId":jrfId,"zhmc":zhmc,"sjhm":sjhm,"sjyzm":sjyzm,"randomMobile":randomMobile},
		success : function(data) {
			var jsonMap=data.jsonMap;
			var code=jsonMap.code;
			if('0000'==code){
				window.location.href="grrz.do?method=rz";
			}else if("9999"==code){
				alertMsg(jsonMap.codemsg);
			}
		}
	});
}
