function clearmsg(msgId){
	var msgObj = document.getElementById(msgId);
	msgObj.innerHTML="";
}


function clearmsgHide(msgId){
	var msgObj = document.getElementById(msgId);
	msgObj.innerHTML="";
	$("#"+msgId).css("display","none");
}
function clearmsgName(msgName){
	var msgObj = document.getElementsByName(msgName);
	msgObj.innerHTML="";
}


function clearmsgHideName(msgName){
	var msgObj = document.getElementsByName(msgName);
	msgObj.innerHTML="";
	$("[name='"+msgName+"']").css("display","none");
}



function maxLengthChg(maxLength,id){
	var content = $("#"+id).val();
	var length = getLengthUTF(content,3);
	if(length>maxLength){
		$("#"+id).val(subUTF(content,maxLength,3));
	}
}

/**
 * 获取包含utf-8编码的汉字的字符长度
 * @param str
 * @returns {Number}
 */
function getLengthUTF(str,num) {
	  ///<summary>获得字符串实际长度，中文3，英文1</summary>
	  ///<param name="str">要获得长度的字符串</param>
	  var realLength = 0, len = str.length, charCode = -1;
	  for (var i = 0; i < len; i++) {
	    charCode = str.charCodeAt(i);
	    if (charCode >= 0 && charCode <= 128) realLength += 1;
	    else realLength += num;
	  }
	  return realLength;
	};

function subUTF(str,length,num) {
	//一个汉字算3个长度,英文1个
    var len = 0;
    var ch;
    var temp="";
    for (var i = 0; i < str.length; i++) {
        ch = str.charCodeAt(i);
        if (ch >= 0 && ch <= 255) {
            len++;
        }
        else {
            len += num;
        }
        if(len > length) {
        	break; 
        }else{
        	 temp += str.charAt(i);     //将当前内容加到临时字符串        
        }      
        //如果全部是单字节字符，就直接返回源字符串     
        } 
    return temp;
    }




//提示
$(function () {
  $('[data-toggle="tooltip"]').tooltip();
});
// 设置密码
//$(function () {
//  $('#shezhimima').modal('show');
//});
// toggle
$(function () {
	$(".biaoge a.gaikuang").click(function(){
        var $this = $(this);
        var gaikuang = $this.parent().parent().next(".qs_gaikuang");
        if(gaikuang.css("display")=="none"){
            $this.removeClass("glyphicon-chevron-down").addClass("glyphicon-chevron-up");
        }else{
            $this.removeClass("glyphicon-chevron-up").addClass("glyphicon-chevron-down");
        }
        $(gaikuang).slideToggle("normal");
    });
})


var resetTimes = 60;
var times = 60;
function updatebutton(){
	if(--times>0){
		$("[name='yzmBut']").text(times+"秒后可重新获取");
	    setTimeout('updatebutton()',1000);
	}else{
		times=resetTimes;
		$("[name='yzmBut']").attr('disabled',false);
		$("[name='yzmBut']").text("获取验证码");
		$("[name='qsYzmInputDiv']").removeClass("fshinput");
		$("[name='qsYzmButDiv']").removeClass("fshbtn");
		$("[name='mobile']").attr("readonly",false);
	}
}


function isNumber(obj) {
    return obj == +obj;
}
