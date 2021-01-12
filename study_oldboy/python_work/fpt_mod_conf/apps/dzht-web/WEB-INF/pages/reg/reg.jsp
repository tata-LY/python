<!DOCTYPE html>
<%@ page language="java" import="java.util.*" pageEncoding="UTF-8"%>
<html>
<head>
	<%@ include  file="/WEB-INF/pages/common/head.jsp"%>
	<!-- 验证码工程引入 -->
	<jsp:include page="/WEB-INF/pages/common/common_yzm.jsp"></jsp:include>
	<link rel="stylesheet" href="<%=basePath %>css/login.css">
	<script src="<%=basePath %>js/reg/reg.js"></script>
	<title>电子合同-签大大</title>
</head>
<body onload="choiceShow();">
	<div class="login">
		<div class="logo text-center"><img src="<%=basePath %>images/logo_black.jpg" alt=""></div>
		<div class="col-xs-offset-2 col-xs-8">
			 <form class="" action="comIndex.do?method=checkRegInviteCode" method="post" id="forms">	
			 	<input type="hidden" id="zhlx" name="zhlx" value="${zhlx}"/>
			 	<input type="hidden" id="errormsgHide" name="errormsgHide" value="${errormsg}"/>
				<div class="form-horizontal">
				  <div class="form-group">
				  	<div class="xuanze">
					  	<a href="javascript:;" class="active" onclick="changeRegType('regTypeQy');" id="regTypeQy">企业</a>
					  	<a href="javascript:;" onclick="changeRegType('regTypeGr');" id="regTypeGr">个人</a>
				  	</div>
				  </div>
				  <div class="form-group">
				    <div class="input-group yaoqingm">
				      <input type="text" class="form-control" placeholder="请输入邀请码"
				      	id="yqm" name="yqm" onfocus="clearmsgHide('errormsg');"
			        		onblur="value=value.replace(/[^0-9a-zA-Z@\.\-_]/g,'')"
				      >
				    </div>
				  </div>
				  <div class="form-group">
				  	<div class="text-error" id="errormsg" style="display:none">${errormsg}</div>
				  </div>
				  <div class="form-group">
				  	<div class="col-xs-12">
					   	<div class="yzm" id="yzmDiv" style="display:block;margin-left:-28px;">
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
				  	<button type="button" class="btn btn-orange  btn-full" onclick="checkRegInviteCode();">注册</button>
				  </div>
				  <div class="form-group">*邀请码请向平台方获取</div>
				</div>
			</form>
		</div>
		<div class="clearfix"></div>
	</div>
	<div class="text-center">
		<a href="<c:url value='/index.do?method=index'/>">返回官网</a>
		<span>我有账号，<a href="<c:url value='/index.do?method=login'/>">马上登陆</a></span>
	</div>
</body>
</html>