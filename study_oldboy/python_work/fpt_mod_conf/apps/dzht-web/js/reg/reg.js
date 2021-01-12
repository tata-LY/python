function choiceShow(){
	var zhlx = $("#zhlx").val();
	var errormsg = $("#errormsgHide").val();
	if(""!=errormsg){
		$("#errormsg").css("display","block");
	}else{
		$("#errormsg").css("display","none");
	}
	if(""!=zhlx){
		if("1"==zhlx){
			$("#regTypeGr").addClass("active").siblings().removeClass("active");
		}else if("2"==zhlx){
			$("#regTypeQy").addClass("active").siblings().removeClass("active");
		}
	}
}

function changeRegType(typeId){
	$("#"+typeId).addClass("active").siblings().removeClass("active");
}

//注册第一步，填入邀请码，然后校验
function checkRegInviteCode(){
	var yqm = $("#yqm").val();
	if(null==yqm || ""==yqm){
		$("#errormsg").html("邀请码不能为空");
		$("#errormsg").css("display","block");
		return false;
	}
	if($("#regTypeGr").hasClass("active")){
		$("#zhlx").val("1");
	}else if($("#regTypeQy").hasClass("active")){
		$("#zhlx").val("2");
	}
	var zhlx = $("#zhlx").val();
	if (!m_verifykey) {
		  alertMsg("请先完成验证码确认.");
		  return;
	  }
	$.ajax({
		url : "comIndex.do?method=checkRegInviteCode",
		dataType:"json",
		type : "post",
		async : false,
		cache : false,
		data : {"yqm":yqm,"zhlx":zhlx},
		success : function(data) {
			var jsonMap=data.jsonMap;
			var code=jsonMap.code;
			var jrfId = jsonMap.jrfId;
			if('0000'==code){
				if("1"==zhlx){
					window.location.href="comIndex.do?method=regGr&jrfId="+jrfId;
				}else if("2"==zhlx){
					window.location.href="comIndex.do?method=regQy&jrfId="+jrfId;
				}
			}else{
				alertMsg(jsonMap.codemsg);
			}
	    }
	});
}