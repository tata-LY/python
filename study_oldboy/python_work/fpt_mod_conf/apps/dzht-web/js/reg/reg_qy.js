$(function(){
	$('.shilitu img').zoomify();
})

function chooseShowRegQy(){
	var hideDlrmc = $("#hideDlrmc").val();
	var hideSzhy = $("#hideSzhy").val();
	if(hideDlrmc){
		showFrDlr("dlr");
	}else{
		showFrDlr("fr");
	}
	if("1"==hideSzhy){//0要三证，1三证合一
		$("#sanzhenghy_li").addClass("active").siblings().removeClass("active");
		$("#heyi").addClass("active").siblings().removeClass("active");
		
	}
}
//下载 企业信息登记表模板
function downloadXxdj(){
	location.href="template/qyxxdjjcasqb.docx";
}

function showFrDlr(frdlr){
	if("fr"==frdlr){
		$("#faren_a").addClass("active").siblings().removeClass("active");
		$("#show_dailiren_div").css("display","none");
		$("#frdlrslt_div").text("法人身份证示例图");		
		$("#frdlrslt_span").text("上传法人身份证");
	}else if("dlr"==frdlr){
		$("#show_dailiren_div").css("display","block");
		$("#dailiren_a").addClass("active").siblings().removeClass("active");
		$("#frdlrslt_div").text("代理人身份证示例图");		
		$("#frdlrslt_span").text("上传代理人身份证");
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
						$("[name='yzmBut']").attr('disabled',false);
						alertMsg("手机验证码请求过于频繁，请稍后再试");
						return false;
					}else{
						$("[name='yzmBut']").attr('disabled',false);
						alertMsg("手机验证码发送失败，请稍后再试");
					    return false;
					}
		    }
		});
	}else{
		alertMsg("手机格式错误!");
		return false;
	}
}

function regQySubmit(){
	var randomMobile = $("#randomMobile").val();
	var randomReg = $("#randomReg").val();
	var NeedToEditQyId = $("#NeedToEditQyId").val();
	var NeedToRegEditJrfId = $("#NeedToRegEditJrfId").val();
	var jrfId = $("#jrfId").val();
	var zhmc = "";
	if(""==NeedToEditQyId){
		zhmc = $("#zhmc").val();//账号名称
		if(""==zhmc){
			alertMsg("邮箱账号不能为空");
			return false;
		}
		if(zhmc.indexOf("@")>-1 && zhmc.indexOf(".")>-1){
			
		}else{
			alertMsg("邮箱账号格式不对");
			return false;
		}
	}
	var qymc = $("#qymc").val();//企业名称
	if(""==qymc){
		alertMsg("企业名称不能为空");
		return false;
	}
	var qylx = $("#qylx").val();//企业类型
	var qydz = $("#qydz").val();//企业地址
	if(""==qydz){
		alertMsg("企业地址不能为空");
		return false;
	}
	var dhhm = $("#dhhm").val();//电话号码
	if(""==dhhm){
		alertMsg("企业电话不能为空");
		return false;
	}
	var qysf = $("#qysf").val();//企业省份
	
	var yyzz = $("#yyzz").val();//营业执照号
	var zzjgdm = $("#zzjgdm").val();//组织机构代码
	var tyshxy = $("#tyshxy").val();//统一社会信用代码
	var szhy = "0";//三证合一，0否，1是
	if($("#sanzheng_li").hasClass("active")){//当前选中三证
		if(""==yyzz){
			alertMsg("营业执照号不能为空");
			return false;
		}
		if(""==zzjgdm){
			alertMsg("组织机构代码证号不能为空");
			return false;
		}
		if(! $('#upload_YYZZ_SHOW').attr('src') ){//营业执照
			alertMsg("请先上传营业执照");
			return false;
	  }
	    if(! $('#upload_ZZJGDM_SHOW').attr('src') ){//组织结构代码证书
			alertMsg("请先上传组织结构代码证书");
			return false;
	  }
	}else{//三证合一
		szhy = "1";
		if(""==tyshxy){
			alertMsg("统一社会信用代码不能为空");
			return false;
		}
		 if(! $('#upload_TYSHXY_SHOW').attr('src') ){//营业执照
				alertMsg("请先上传营业执照");
				return false;
		  }
	}
	var frmc = $("#frmc").val();//法人名称
	if(""==frmc){
		alertMsg("法人姓名不能为空");
		return false;
	}
	//=====留空起
	var frsfz = $("#frsfz").val();//法人身份证
	if(""==frsfz){
		alertMsg("法人身份证号不能为空");
		return false;
	}
	if(frsfz.length==15 || frsfz.length==18){
		var flag = validateIdCard(frsfz);
		if(!flag){
			alertMsg("法人身份证号输入有误，请重新输入");
			return false;
		}
	}else{
		alertMsg("法人身份证号输入有误，请重新输入");
		return false;
	}
	
	var dlmc = $("#dlmc").val();//代理人名称
	var dlsfz = $("#dlsfz").val();//代理人身份证
	if($("#dailiren_a").hasClass("active")){//当前选中的是代理人
		if(""==dlmc){
			alertMsg("代理人姓名不能为空");
			return false;
		}
		if(""==dlsfz){
			alertMsg("代理人身份证号不能为空");
			return false;
		}
		if(dlsfz.length==15 || dlsfz.length==18){
			var flag = validateIdCard(dlsfz);
			if(!flag){
				alertMsg("代理身份证号输入有误，请重新输入");
				return false;
			}
		}else{
			alertMsg("代理身份证号输入有误，请重新输入");
			return false;
		}
	}
	//=====留空止
	var sjhm = $("#sjhm").val();//手机号码
	if(""==sjhm){
		alertMsg("手机号码不能为空");
		return false;
	}
	var reg = /^1\d{10}$/;
	if(!reg.test(sjhm)){
		alertMsg("手机号码格式不对");
		return false;
	}
	var sjyzm = $("#sjyzm").val();//手机验证码
	if(""==sjyzm){
		alertMsg("手机验证码不能为空");
		return false;
	}

  if(! $('#upload_FRDLRSFZ_SHOW').attr('src') ){//法人代理人身份证
	alertMsg("请先上传身份证");
		return false;
  }
  if(! $('#upload_SQB_1_SHOW').attr('src') ){//企业申请表图1
	alertMsg("请先上传企业申请表图1");
		return false;
  }
  if(! $('#upload_SQB_2_SHOW').attr('src') ){//企业申请表图2
	alertMsg("请先上传企业申请表图2");
		return false;
  }
	
	
	$.ajax({
		url : "comIndex.do?method=regQySub",
		dataType:"json",
		type : "post",
		async : false,
		cache : false,
		data : 	{"zhmc":zhmc,"qymc":qymc,"qylx":qylx,"qydz":qydz,"dhhm":dhhm,"qysf":qysf,
				"yyzz":yyzz,"zzjgdm":zzjgdm,"tyshxy":tyshxy,"frmc":frmc,"frsfz":frsfz,
				"dlmc":dlmc,"dlsfz":dlsfz,"sjhm":sjhm,"sjyzm":sjyzm,"randomMobile":randomMobile,
				"jrfId":jrfId,"szhy":szhy,"randomReg":randomReg},
		success : function(data) {
			var jsonMap=data.jsonMap;
			var code=jsonMap.code;
			if('0000'==code){
				if(NeedToRegEditJrfId){
					window.location.href="qyList.do?method=list";
				}else{
					window.location.href="info.do?method=info";
				}
			}else if("9999"==code){
				alertMsg(jsonMap.codemsg);
			}
		}
	});

}

