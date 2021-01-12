function showHide(){
	var reg_gr_rz_zjlx = $("#reg_gr_rz_zjlx").val();
	if("0"==reg_gr_rz_zjlx){
		
	}else {
		$("#paizhao_li").addClass("active").siblings().removeClass("active");
		$("#yinhangka_li").css("display","none");
		$("#paizhao").addClass("active").siblings().removeClass("active");
		$("#yinhangka").css("display","none");
	}
}

function changeRzType(id){
	$("#"+id+"_li").addClass("active").siblings().removeClass("active");
	$("#"+id).addClass("active").siblings().removeClass("active");
}

function grrzSub(rzfs){
	if("yinhangka"==rzfs){//银行卡认证
		var yhkh = $("#yhkh").val();
		var ylhm = $("#ylhm").val();
		if(""==yhkh){
			alertMsg("银行卡号不能为空");
			return false;
		}
		if(""==ylhm){
			alertMsg("银行卡预留手机号不能为空");
			return false;
		}
		var reg = /^1\d{10}$/;
		if(!reg.test(ylhm)){
			alertMsg("手机号格式不对");
			return false;
		}
		$.ajax({
			url : "grrz.do?method=yinhk",
			dataType:"json",
			type : "post",
			async : false,
			cache : false,
			data : {"yhkh":yhkh,"ylhm":ylhm},
			success : function(data) {
				var jsonMap=data.jsonMap;
				var code=jsonMap.code;
				if("0000"==code){
					alertMsg("认证成功");
					window.location.href="info.do?method=info"
				}else{
					alertMsg(jsonMap.codemsg);
				}
		    }
		});
	}else if("paizhao"==rzfs){//拍照认证
		if( $('#upload_GRSCSFZ_SHOW').attr('src') ){
			var randomReg = $("#randomReg").val();
			
			$.ajax({
				url : "grrz.do?method=paiz",
				dataType:"json",
				type : "post",
				async : false,
				cache : false,
				data : {"randomReg":randomReg},
				success : function(data) {
					var jsonMap=data.jsonMap;
					var code=jsonMap.code;
					if("0000"==code){
						alertMsg("认证提交成功，待工作人员审核");
						window.location.href="info.do?method=info"
					}else{
						alertMsg(jsonMap.codemsg);
					}
			    }
			});
			}else{
				alertMsg("请先上传手持身份证照");
				return false;
			    // 为空
			}
	}
}