/** 公共js工具 */
function getContextPath(){   
    var pathName = document.location.pathname;   
    var index = pathName.substr(1).indexOf("/");   
    var result = pathName.substr(0, index+1);   
    return result;   
}  
var baseUrl = getContextPath();//根目录

function postData(url, data, successFun, errorFun, loading) {
	if(loading) loadingShow();
	$.ajax({ 
        type:"POST", 
        url: url,               
        data: data,
		success:function(data){
			if(loading) loadingHide();
			if(typeof(data)==='string'){
				if(data.indexOf('p_timeout')>0 || data.indexOf('p_invalid')>0
						|| data.indexOf('p_relogin')>0) {
					return;
				}
			}
        	if (successFun) successFun(data);
        },
        error: function(XMLHttpRequest, textStatus, errorThrown) {
        	if(loading) loadingHide();
        	if (errorFun) errorFun(XMLHttpRequest, textStatus, errorThrown);
        }
     });
}

function loadingShow(){
	// var loading = document.getElementById("bs-example-modal-sm");
	// loading.style.display = "";
    $(".bs-example-modal-sm .modal-dialog").css("top","40%");
    $("#loadingGif").modal("show");
}

function loadingHide(){
	// var loading = document.getElementById("bs-example-modal-sm");
	// loading.style.display = "none";
    $("#loadingGif").modal("hide");
}

function postForm(url, params) {
	var temp = document.createElement("form");
	temp.action = url;
	temp.method = "post";
	temp.style.display = "none";
	for (var x in params) {
		var opt = document.createElement("input");
		opt.name = x;
		opt.value = params[x];
		temp.appendChild(opt);
	}
	document.body.appendChild(temp);
	temp.submit();
	$(temp).remove();
}

function postJSONData(url, data, successFun, errorFun, loading) {
	if(loading) loadingShow();
	$.ajax({
		type:"POST",
		url: url,
		dataType:"json", 
		data: JSON.stringify(data),
		contentType: "application/json",
		success:function(data){
			if(loading) loadingHide();
			if(typeof(data)==='string'){
				if(data.indexOf('p_timeout')>0 || data.indexOf('p_invalid')>0
						|| data.indexOf('p_relogin')>0) {
					return;
				}
			}
			if (successFun) successFun(data);
		},
		error: function(XMLHttpRequest, textStatus, errorThrown) {
			if(loading) loadingHide();
			if (errorFun) errorFun(XMLHttpRequest, textStatus, errorThrown);
		}
	});
}
//公共提示方法
function tip(msg){
	alertMsg(msg);
}

function toDecimal2(x) { 
    var f = parseFloat(x); 
    if (isNaN(f)) { 
      return false; 
    } 
    var f = Math.round(x*100)/100; 
    var s = f.toString(); 
    var rs = s.indexOf('.'); 
    if (rs < 0) { 
      rs = s.length; 
      s += '.'; 
    } 
    while (s.length <= rs + 2) { 
      s += '0'; 
    } 
    return s; 
}

function toDecimal6(x) { 
    var f = parseFloat(x); 
    if (isNaN(f)) { 
      return false; 
    }
    var s = f.toString(); 
    var rs = s.indexOf('.');
    if(s.length-rs > 6){
    	f = Math.round(x*1000000)/1000000; 
        s = f.toString();
    }
    return s; 
} 

function convInt(v) {
	if (!v)
	   return 0;
	n = parseInt(v);
	if (isNaN(n))
	    return 0;
	else
	    return n;
}

function convFloat(v) {
	if (!v)
	   return 0;
	n = parseFloat(v);
	if (isNaN(n))
	    return 0;
	else
	    return n;
}

function isMobile(s) {
	var patrn = /^1[3,5,7,8]\d{9}$$/;
	if(patrn.test(s))
		return true;
	else
		return false;
}

function isEmail(s){
    var patrn = /^\w+((-\w+)|(\.\w+))*\@[A-Za-z0-9]+((\.|-)[A-Za-z0-9]+)*\.[A-Za-z0-9]+$$/;
    if (patrn.test(s)) return true;
    return false;
}

/** 数字前补零 */
function prefixInteger(num, n) {
	var len = num.toString().length;  
    while(len < n) {  
        num = "0" + num;  
        len++;  
    }  
    return num;
}

function trim(str){ //删除左右两端的空格
    return str.replace(/(^\s*)|(\s*$)/g, "");
}
function ltrim(str){ //删除左边的空格
    return str.replace(/(^\s*)/g,"");
}
function rtrim(str){ //删除右边的空格
    return str.replace(/(\s*$)/g,"");
}

/**
 * 获取ajax请求返回结果,用于回调函数，用法如下：
 * var data = getResult(resp);
 * if(!data) return;
 */
function getResult(resp, showError) {
	if (showError == undefined || showError == null) showError = true;
	if (!resp) {
		if (showError) {
			tip("系统异常");
		}
	} else {            
		var nResult = resp["Result"];
		if (nResult == undefined) {
			if (showError) {
				tip("加载数据失败");
			}
		} else if (nResult == 0) {
			var data = resp["Data"];
			if (data == null)
			    return true;
			else
			    return data;
		} else if (showError) {
			var msg = resp["Error"];
			if (!msg)
			    msg = "未定义错误";
			tip(msg);
		}                  
	}
	return null;
}

/**
 * 设置按钮不可用，当值提交过程中重复点击按钮
 * @param obj
 * @param enabled
 */
function setEnabled(obj, enabled) {
	if (enabled) {
		$(obj).removeAttr('disabled');
	} else {
		$(obj).attr('disabled', 'disabled');
	}
}

function commonSuccessCallBack(resp) {
	var data = getResult(resp);
    if (!data) return;
    tip("操作成功");
}

function commonErrorCallBack(XMLHttpRequest, textStatus, errorThrown) {
	//tip("网络通讯错误，textStatus：" + textStatus + "，status:" + XMLHttpRequest.status + "，readyState:" + XMLHttpRequest.readyState);
	tip("抱歉！网络通信异常~请重试一下");
}

function getFormData(formClass) {
	var target = $('.'+formClass);
	return getTargetData(target);
} 

function getTargetData(target){
	var data = {}, valid_pass = true, valid_msg = "";
	target.find("input,select,textarea").each(function(){
		var $element = $(this), name = $element.attr("name");
		if(name){
			var dataType = $element.attr("data-type");
			var requiredAttr = $element.attr("required"), isRequired = false;
			if(requiredAttr=="required") isRequired = true;
			if($element.is("input")){
				var type = $element.attr("type");
				var value = $element.val() || '';
				if(type=='radio'){
					if($element.is(':checked')) data[name] = value;
				}else if(type=='checkbox'){
					if($element.is(':checked')){
						if(data[name] && value) data[name] = data[name] + ',' + value;
						else if(!data[name]) data[name] = value
					}
				}else{
					data[name] = trim(value);
					if(isRequired && value==""){
						valid_pass = false;
						var msg = $element.attr("required-msg");
						if(msg && valid_msg=="") valid_msg = msg;
					}
					if(dataType=="email" && value!='' && !isEmail(value)){
						valid_pass = false;
						if(valid_msg=="") valid_msg = "请输入有效的邮箱";
					}
					if(dataType=="mobile" && value!='' && !isMobile(value)){
						valid_pass = false;
						if(valid_msg=="") valid_msg = "请输入有效的手机号";
					}
				}
			}else if($element.is("select")){
				var value = $element.find("option:selected").val() || '';
				data[name] = value;
				if(isRequired && value==""){
					valid_pass = false;
					var msg = $element.attr("required-msg");
					if(msg && valid_msg=="") valid_msg = msg;
				}
			}else{
				var value = $element.val() || '';
				data[name] = value;
				if(isRequired && value==""){
					valid_pass = false;
					var msg = $element.attr("required-msg");
					if(msg && valid_msg=="") valid_msg = msg;
				}
			}
		}
	});
	if(!valid_pass){
		data = null;
		if(valid_msg) tip(valid_msg);
	}
    return data;
}

/*
 对Date的扩展，将 Date 转化为指定格式的String
月(M)、日(d)、小时(H)、分(m)、秒(s)、季度(q) 可以用 1-2 个占位符， 
年(y)可以用 1-4 个占位符，毫秒(S)只能用 1 个占位符(是 1-3 位的数字) 
例子： 
(new Date()).Format("yyyy-MM-dd HH:mm:ss.S") ==> 2006-07-02 08:09:04.423 
(new Date()).Format("yyyy-M-d H:m:s.S")      ==> 2006-7-2 8:9:4.18 
*/
Date.prototype.Format = function (fmt) {
	var o = {
	   "M+": this.getMonth() + 1, //月份 
	   "d+": this.getDate(), //日 
	   "H+": this.getHours(), //小时 
	   "m+": this.getMinutes(), //分 
	   "s+": this.getSeconds(), //秒 
	   "q+": Math.floor((this.getMonth() + 3) / 3), //季度 
	   "S": this.getMilliseconds() //毫秒 
	};
	if (/(y+)/.test(fmt)) fmt = fmt.replace(RegExp.$1, (this.getFullYear() + "").substr(4 - RegExp.$1.length));
	for (var k in o)
		if (new RegExp("(" + k + ")").test(fmt)) fmt = fmt.replace(RegExp.$1, (RegExp.$1.length == 1) ? (o[k]) : (("00" + o[k]).substr(("" + o[k]).length)));
	return fmt;
};
/** 判断数组中是否包含指定项 */
Array.prototype.contains = function ( needle ) {
  for (i in this) {
    if (this[i] == needle) return true;
  }
  return false;
}

/** 数字金额大写转换(可以处理整数,小数,负数) */    
var digitUppercase = function(n) {  
    var fraction = ['角', '分'];  
    var digit = [  
        '零', '壹', '贰', '叁', '肆',  
        '伍', '陆', '柒', '捌', '玖'  
    ];  
    var unit = [  
        ['元', '万', '亿'],  
        ['', '拾', '佰', '仟']  
    ];  
    var head = n < 0 ? '负' : '';  
    n = Math.abs(n);  
    var s = '';  
    for (var i = 0; i < fraction.length; i++) {  
        s += (digit[Math.floor(n * 10 * Math.pow(10, i)) % 10] + fraction[i]).replace(/零./, '');  
    }  
    s = s || '整';  
    n = Math.floor(n);  
    for (var i = 0; i < unit[0].length && n > 0; i++) {  
        var p = '';  
        for (var j = 0; j < unit[1].length && n > 0; j++) {  
            p = digit[n % 10] + unit[1][j] + p;  
            n = Math.floor(n / 10);  
        }  
        s = p.replace(/(零.)*零$/, '').replace(/^$/, '零') + unit[0][i] + s;  
    }  
    return head + s.replace(/(零.)*零元/, '元')  
        .replace(/(零.)+/g, '零')  
        .replace(/^整$/, '零元整');  
}

