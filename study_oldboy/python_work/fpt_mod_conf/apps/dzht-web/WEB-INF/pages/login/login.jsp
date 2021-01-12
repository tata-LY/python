<!DOCTYPE html>
<%@ page language="java" import="java.util.*" pageEncoding="UTF-8"%>
<html>
<head>
	<%@ include  file="/WEB-INF/pages/common/head.jsp"%>
	<!-- 验证码工程引入 -->
	<jsp:include page="/WEB-INF/pages/common/common_yzm.jsp"></jsp:include>
	<link rel="stylesheet" href="<%=basePath %>css/login.css">
	<script src="<%=basePath %>js/login/login.js?version=0121"></script>
	<script src="<%=basePath %>js/utils/md5.js"></script>
	<title>电子合同-签大大</title>
</head>
<body onload="choiceShow();">
	<div class="login">
		<div class="logo text-center"><img src="<%=basePath %>images/logo_black.jpg" alt=""></div>
		<div class="col-xs-offset-2 col-xs-8">
			 <form class="" action="index.do?method=loginSubmit" method="post" id="forms">	
				<!-- 用于缓存中保存安全登录产生的随机数的key的一部分 -->
				<input type="hidden" id="loginRandomCode" name="loginRandomCode" value="${loginRandomCode}"/>
				<input type="hidden" id="md5zhmm" name="md5zhmm" />
				<input type="hidden" name="randomMobile" id="randomMobile" value="${randomMobile}"/>
				<input type="hidden" id="mobileYzmKey" name="mobileYzmKey" value="${mobileYzmKey}"/>
				<input type="hidden" id="needsjyzm" name="needsjyzm" value="${needsjyzm}"/>
				<input type="hidden" id="dllx_back" name="dllx_back" value="${dllx}"/>
				<input type="hidden" id="errormsgHide" name="errormsgHide" value="${errormsg}"/>
		
				<div class="form-horizontal">
				  <div class="form-group">
				    <div class="input-group zhanghu">
				      <input type="text" class="form-control" placeholder="请输入邮箱号"
				      	id="zhmc" name="zhmc" value="${zhmc}" onfocus="clearmsgHide('errormsg');"
		        		onblur="value=value.replace(/[^0-9a-zA-Z@\.\-_]/g,'')"
				      >
				    </div>
				  </div>
				  <div class="form-group" id="sjhmDiv" style="display:none">
				    <div class="input-group shoujih">
				      <input type="text" class="form-control" placeholder="请输入预留手机号"
				      id="sjhm" name="sjhm" value="${sjhm}" onfocus="clearmsgHide('errormsg');"
		        		onblur="value=value.replace(/[^0-9]/g,'')"
				      >
				    </div>
				  </div>
				  <div class="form-group" id="sjhmyzmDiv" style="display:none">
				  	<div class="col-xs-7">
					    <div class="input-group yanzm">
					      <input type="text" class="form-control" placeholder="请输入短信验证码"
					      id="sjyzm" name="sjyzm" onfocus="clearmsgHide('errormsg');"
		        		onblur="value=value.replace(/[^0-9]/g,'')"
					      >
					    </div>
				  	</div>
				  	<div class="col-xs-5">
				  		<button type="button" class="btn btn-empty" onclick="getMobileCode();">发送验证码</button>
				  	</div>
				  </div>
				  <div class="form-group" id="zhmmDiv">
				    <div class="input-group mima">
				      <input type="password" class="form-control" placeholder="请输入密码" 
				      id="zhmm" name="zhmm" onfocus="clearmsgHide('errormsg');"
				     >
				    </div>
				  </div>
				  <div class="form-group">
				    <label class="radio-inline">
					  <input type="radio" name="dllx" id="dllx_2" value="2" checked>普通用户
					</label>
					<label class="radio-inline">
					  <input type="radio" name="dllx" id="dllx_1" value="1">接入方平台
					</label>
				  </div>
				  <div class="text-error" id="errormsg" style="display:none">${errormsg}</div>
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
				  <div class="form-group text-right"><a class="btn-link" href="forget.html">忘记密码</a></div>
				  <div class="form-group">
				  	<button type="button" class="btn btn-orange  btn-full" onclick="loginSubmit();">登录</button>
				  </div>
				  <div class="form-group">还没有账号？<a class="btn-link" href="<c:url value='/comIndex.do?method=reg'/>">立即注册</a></div>
				</div>
			</form>
		</div>
		<div class="clearfix"></div>
	</div>
	<div class="text-center">
		<a class="btn-link" href="<c:url value='/index.do?method=index'/>">返回官网</a>
	</div>
</body>
</html>