$(function() {
	verify_init({
		  chkurl: "com.do?method=authCode",     // 验证码校验的服务url: 为安全起见，校验由系统自身的后台来校验，这里填写本程序的地址。
		  genurl: null,     // 验证码生成的服务url: http://www.fapiao.com/verifycode/， 如果实际环境中存在跨域问题，则可由系统本身的后台作转发，为空则使用chkurl地址。
		  imgid: '#imgCode', 
		  txtid: "#txtCode",
		  onstartverfiy: verifycode_startverfiy,
		  onsuccess: verifycode_success,
		  onerror : verifycode_error
	  });
	  verify_refreshCode(); 
	//$("#password").focus();
    });

    function refreshCode() {
  	  verify_refreshCode();
  	  $("#verifystatus").hide();
    }
    
    function verifycode_startverfiy() {
  	  $("#verifystatus").hide();
    }      

    function verifycode_success() {
  	  $("#verifystatus").attr('class', 'verfiy_success');
  	  $("#verifystatus").html("验证成功！");
  	  $("#verifystatus").show();
    }
    
	  function verifycode_error() {
		  $("#verifystatus").attr('class', 'verfiy_error');
  	  $("#verifystatus").html("验证失败！");
  	  $("#verifystatus").show();
  	  
  	  return true;   // return true表示自动刷新验证码，否则不自动刷新
    }