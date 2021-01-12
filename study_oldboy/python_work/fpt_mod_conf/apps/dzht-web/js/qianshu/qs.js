$(function(){
	$('#sjyzmQs').bind("propertychange input", function() {
		var text = $(this).val();
		var length = text.length;
		if(6==length){
			qsSub();
		}
	
	}); 
});


function qsSub(){
	 var  htId = $("#htId").val();
	 var randomMobile = $("#randomMobile").val();
	 if(""==randomMobile){
		 alertMsg("请先获取验证码");
		 return false;
	 }
	 var sjyzm = $("#sjyzmQs").val();
	 if(""==sjyzm){
		 alertMsg("请填写验证码");
		 return false;
	 }
	 var qzflag = false;
	 var qsStr = "";
	 var i = 0;
	//获取各个签章起始点（左上角那个点）
	$(".htqz").each(function()
		{
			var pDiv = $(this).parent();
			var leftImg = $(pDiv).find("img[name^='leftpage_']");
			var leftName = $(leftImg).attr("name");
			if(typeof(leftName)=="undefined"){
			}else {
				i++;
				qzflag = true;
				var position = $(this).position();
				var left = position.left;
				left = parseInt(left);
				var top = $(this).attr("alt");
//				var top = position.top;
				top = parseInt(top);
				var pageIndex = leftName.substring(9,leftName.length);
				qsStr += pageIndex+","+left+","+top+";";
			}
		});
	if(qzflag== false){
		alertMsg("请至少签一次章");
		return false;
	}
	qsStr = qsStr.substring(0, qsStr.length-1);
	$.ajax({
		url : "qianshu.do?method=qsSub",
		dataType:"json",
		type : "post",
		async : false,
		cache : false,
		data : {"qsStr":qsStr,"htId":htId,"sjyzm":sjyzm,"randomMobile":randomMobile},
		beforeSend: function () {
			$("#loadingGif").modal("show");
	    },
	    complete:function(){
	    	$("#loadingGif").modal("hide");
	    },
		success : function(data) {
			var jsonMap=data.jsonMap;
			var code=jsonMap.code;
			var codemsg = jsonMap.codemsg;
	    	if("0000"==code){
	    		$("#qs_success").modal("show").css({"visibility":"visible","display":"block"});
	    	}else{
	    		alertMsg(codemsg);
	    	}
	    }
	});
}


function getMobileCodeQs(){
	var mobileYzmKey = $("#mobileYzmKey").val();
	var mobile = $("#mobile").val();
	var htId = $("#htId").val();
	$("[name='yzmBut']").attr('disabled',true);
	$.ajax({
		url : "com.do?method=getMobileCodeQs",
		dataType:"json",
		type : "post",
		async : false,
		cache : false,
		data : {"mobile":mobile,"mobileYzmKey":mobileYzmKey,"htId":htId},
		success : function(data) {
	    	  var json = eval(data);
	    	  if(json[0].text==1){
	    			$("[name='qsYzmInputDiv']").addClass("fshinput");
	    			$("[name='qsYzmButDiv']").addClass("fshbtn");
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
}

function buqueDiv(){
	var buqueFlag = $("#buqueFlag").val();
	var buqueys = $("#buqueys").val();
	$("[name=spanDiv_"+buqueys+"]").each(function()
		{
		var srcDiv = $(this).parent().parent().parent();
		if($(srcDiv).hasClass("p")){
			//$(srcDiv).css("display","none");
			}
		});
}

function limitInput(htys,o){
    var value=o.value;
    var min=1;
    var max=htys;
    if(isNumber(value)){
	    if(parseInt(value) < min || parseInt(value) > max){
	        o.value= '';
	    }
    }else{o.value= 1;}
    
}

function changePageIndex(pageIndex){
	$("#pageIndex").val(pageIndex);
}

function qsSuccess(){
	var htId = $("#htId").val();
	window.location.href="htgl.do?method=htView&htId="+htId;
}