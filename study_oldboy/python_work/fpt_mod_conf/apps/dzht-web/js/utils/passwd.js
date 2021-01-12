var level =0;

$(function(){
	$('#mm_passwd,#passwd').bind("propertychange input", function() {
		
		var __th = $(this);
		var valueTh = __th.val();
		if (!valueTh) {
			primary();
			level = 0;
			return;
		}
		if(valueTh.indexOf(" ")>-1){
			valueTh = valueTh.replace(" ","");//去掉空格
			__th.val(valueTh);
		}
		if (valueTh.length < 8) {
			weak();
			level = 1;
			return;
		}
		var _r = checkPassword(__th);
		if (_r < 1) {
			primary();
			level = 1;
			return;
		}
		if (_r > 0 && _r < 2) {
			level = 1; 
			weak();
		}else if(_r==2){
			medium();
			level = 2; 
		} else if (_r > 2 && _r < 4) {
			medium();
			level = 3; 
		} else if (_r >= 4) {
			level = 3; 
			tough();
		}
	}); 
})

function checkPassword(pwdinput) {
	var maths, smalls, bigs, corps, cat, num;
	var str = $(pwdinput).val();
	var len = str.length;

	var cat = /.{16}/g
	if (len == 0) return 1;
	if (len > 16) { $(pwdinput).val(str.match(cat)[0]); }
	cat = /.*[\u4e00-\u9fa5]+.*$/
	if (cat.test(str)) {
		return -1;
	}
	cat = /\d/;
	var maths = cat.test(str);
	cat = /[a-z]/;
	var smalls = cat.test(str);
	cat = /[A-Z]/;
	var bigs = cat.test(str);
	var corps = corpses(pwdinput);
	var num = maths + smalls + bigs + corps;
	//console.log("maths=="+maths+"  smalls=="+smalls+"  bigs=="+bigs+"  corps=="+corps+"  num=="+num);
	if (len < 8) { return 1; }
	if (len >= 8 && len <= 16) {
		if (num == 1) return 2;
		if (num == 2) return 3;
		if (num == 3) return 4;
		if (num == 4) return 5;
	}
}

function corpses(pwdinput) {
	var cat = /./g
	var str = $(pwdinput).val();
	var sz = str.match(cat)
	for (var i = 0; i < sz.length; i++) {
		cat = /\d/;
		maths_01 = cat.test(sz[i]);
		cat = /[a-z]/;
		smalls_01 = cat.test(sz[i]);
		cat = /[A-Z]/;
		bigs_01 = cat.test(sz[i]);
		if (!maths_01 && !smalls_01 && !bigs_01) { return true; }
	}
	return false;
}


function primary(){
	$("[name='weakSpan']").attr('class', '').siblings().attr("class","");
	$("[name='showSpanTips").attr("class","text-danger").text("");
}

function weak(){
	$("[name='weakSpan']").attr('class', 'progress-bar-danger').siblings().attr("class","");
	$("[name='showSpanTips']").attr("class","text-danger").text("弱");
}

function medium(){
	$("[name='weakSpan']").attr('class', 'progress-bar-danger');
	$("[name='mediumSpan']").attr('class', 'progress-bar-warning');
	$("[name='toughSpan']").attr("class","");
	$("[name='showSpanTips']").attr("class","text-warning").text("中");
}
function tough(){
	$("[name='weakSpan']").attr('class', 'progress-bar-danger');
	$("[name='mediumSpan']").attr('class', 'progress-bar-warning');
	$("[name='toughSpan']").attr('class', 'progress-bar-success');
	$("[name='showSpanTips']").attr("class","text-success").text("强");
}