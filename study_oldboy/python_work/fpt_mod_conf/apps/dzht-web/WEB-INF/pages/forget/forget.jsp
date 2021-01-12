<!DOCTYPE html>
<%@ page language="java" import="java.util.*" pageEncoding="UTF-8"%>
<html>
<head>
	<%@ include  file="/WEB-INF/pages/common/head.jsp"%>
	<link rel="stylesheet" href="<%=basePath %>css/pages.css">
	<title>电子合同-签大大</title>
	<script src="<%=basePath %>js/forget/forget.js"></script>
	<script src="<%=basePath %>js/utils/passwd.js"></script>
	<script src="<%=basePath %>js/utils/md5.js"></script>
	<!-- 验证码工程引入 -->
	<jsp:include page="/WEB-INF/pages/common/common_yzm.jsp"></jsp:include>
</head>
<body class="forgetbody" onload="showMsg();">
	<!-- 头部 -->
	<%@ include  file="/WEB-INF/pages/common/head_top.jsp"%>
	<div class="container">
		<div class="col-xs-offset-2 col-xs-8 forget">
			<h4 class="text-center">找回密码</h4>
			 <form class="" action="comIndex.do?method=forget" method="post" id="forms">	
				<!-- 用于缓存中保存安全登录产生的随机数的key的一部分 -->
				<input type="hidden" id="loginRandomCode" name="loginRandomCode" value="${loginRandomCode}"/>
				<input type="hidden" id="md5zhmm" name="md5zhmm" />
				<input type="hidden" name="randomMobile" id="randomMobile" value="${randomMobile}"/>
				<input type="hidden" id="mobileYzmKey" name="mobileYzmKey" value="${mobileYzmKey}"/>
				<input type="hidden" id="errormsgHide" name="errormsgHide" value="${errormsg}"/>
				<div class="col-xs-offset-3 col-xs-6">
					<div class="form-horizontal">
					  <div class="form-group">
					    <div class="input-group zhanghu">
					      <input type="text" class="form-control" placeholder="请输入账号"
					      	id="zhmc" name="zhmc" value="${zhmc}" onfocus="clearmsgHide('errormsg');"
		        			onblur="value=value.replace(/[^0-9a-zA-Z@\.\-_]/g,'')"
					      >
					    </div>
					  </div>
					  <div class="form-group">
					    <div class="input-group mima">
					      <input type="password" class="form-control" placeholder="请输入新密码"
					      	id="mm_passwd" name="mm_passwd" onfocus="clearmsgHide('errormsg');">
					    </div>
					  </div>
					  <!-- 引入密码公用样式 -->
					  <div class="form-group">
					 	<div class="col-xs-8">
					 		<%@ include  file="/WEB-INF/pages/common/pwd.jsp"%>
					   </div>
					   <div class="clearfix"></div>
					 </div>
					  <div class="form-group">
					    <div class="input-group mimaqr">
					      <input type="password" class="form-control" placeholder="请确认新密码"
					      	id="mm_passwd2" name="mm_passwd2" onfocus="clearmsgHide('errormsg');">
					    </div>
					  </div>
					  <div class="form-group">
					    <div class="input-group shoujih">
					      <input type="text" class="form-control" placeholder="请输入预留手机号码"
					      	id="sjhm" name="sjhm" value="${sjhm}" onfocus="clearmsgHide('errormsg');"
		        			onblur="value=value.replace(/[^0-9]/g,'')">
					    </div>
					  </div>
					  <div class="form-group">
					  	<div class="col-xs-12">
						   	<div class="yzm" id="yzmDiv">
						          <div style="text-align:left; padding-left: 24px;">
						              <p>请按顺序依次点击下图中的<span id="txtCode"></span>三个字:</p>
						              <div>
						                  <img id="imgCode" src="" />
						                  <a href="javascript:refreshCode()">[刷新]</a>
						                  <p id="verifystatus" style="display:none;" class="">验证结果</p>
						              </div>
						          </div>
						      </div>
						</div>
					  </div>
					  <div class="form-group">
					  	<div class="col-xs-9">
						    <div class="input-group yanzm">
						      <input type="text" class="form-control" placeholder="请输入短信验证码"
						      	id="sjyzm" name="sjyzm" onfocus="clearmsgHide('errormsg');"
		        				onblur="value=value.replace(/[^0-9]/g,'')">
						    </div>
					  	</div>
					  	<div class="col-xs-3">
					  		<button type="button" class="btn btn-empty" onclick="getMobileCode();" name="yzmBut" id="yzmBut">发送验证码</button>
					  	</div>
					  </div>
					  <div class="text-error" id="errormsg"  name="errormsg" style="display:none"></div>
					  <div class="form-group">
					  	<button type="button" class="btn btn-orange" data-toggle="modal" 
					  		onclick="resetPwd();">
					  		提交
					  	</button>
					  </div>
					</div>
				</div>
			</form>
		</div>
	</div>
	<!--footer-->
	<%@ include  file="/WEB-INF/pages/common/footer.jsp"%>
	
	<!-- 弹框 -->
	<%@ include  file="/WEB-INF/pages/forget/forget_tk.jsp"%>
</body>
</html>