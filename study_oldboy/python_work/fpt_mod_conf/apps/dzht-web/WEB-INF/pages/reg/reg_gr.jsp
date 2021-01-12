<!DOCTYPE html>
<%@ page language="java" import="java.util.*" pageEncoding="UTF-8"%>
<html>
<head>
	<%@ include  file="/WEB-INF/pages/common/head.jsp"%>
	<title>个人材料自助提交系统</title>
	<script src="<%=basePath %>js/css/zoomify.min.js"></script>
	<link rel="stylesheet" href="<%=basePath %>css/qianshu.css">
	<script src="<%=basePath %>js/reg/reg_gr.js"></script>
	<script src="<%=basePath %>js/utils/validateIdCard.js"></script>
	<!-- 验证码工程引入 -->
	<jsp:include page="/WEB-INF/pages/common/common_yzm.jsp"></jsp:include>
</head>
<body>
	<!-- 头部 -->
	<jsp:include page="/WEB-INF/pages/common/head_top.jsp">
     	<jsp:param value="999" name="top_menu_id"/>
   </jsp:include>
	<div class="gr_zltj container">
		<div class="col-xs-offset-3 col-xs-6">
		 	<form class="" action="comIndex.do?method=regGrSub" method="post" id="forms">	
				<input type="hidden" name="randomMobile" id="randomMobile" value="${randomMobile}"/>
				<input type="hidden" id="mobileYzmKey" name="mobileYzmKey" value="${mobileYzmKey}"/>
				<input type="hidden" id="jrfId" name="jrfId" value="${jrfId}"/>
				<div class="form-horizontal">
				  <div class="form-group">
				    <label class="col-xs-3 control-label">姓名</label>
				    <div class="col-xs-9">
				      <input type="text" class="form-control" placeholder=""
				      id="zjmc" name="zjmc" value="${zjmc}" onfocus="clearmsgHide('errormsg');"
				      onKeyDown="maxLengthChg('300','zjmc');" onKeyUp="maxLengthChg('300','zjmc');"
				      >
				    </div>
				  </div>
				  <div class="form-group">
				    <label class="col-xs-3 control-label">证件类型</label>
				    <div class="col-xs-9">
				       <select class="form-control" name="zjlx" id="zjlx">
						  <option value="0">身份证</option>
						  <option value="1">港澳台通行证</option>
						  <option value="2">护照</option>
						  <option value="3">其它</option>
						</select>
				    </div>
				  </div>
				  <div class="form-group">
				    <label class="col-xs-3 control-label">证件号码</label>
				    <div class="col-xs-9">
				      <input type="text" class="form-control" placeholder=""
				      id="zjhm" name="zjhm" value="${zjhm}" onfocus="clearmsgHide('errormsg');" maxlength=60
				      >
				    </div>
				  </div>
				  <div class="form-group">
				    <label class="col-xs-3 control-label">邮箱地址</label>
				    <div class="col-xs-9">
				      <input type="text" class="form-control" placeholder=""
				      id="zhmc" name="zhmc" value="${zhmc}" onfocus="clearmsgHide('errormsg');" maxlength=60
				      >
				    </div>
				  </div>
				  <div class="form-group">
				    <label class="col-xs-3 control-label">手机号码</label>
				    <div class="col-xs-9">
				      <input type="text" class="form-control" placeholder=""
				      id="sjhm" name="sjhm" value="${sjhm}" onfocus="clearmsgHide('errormsg');" maxlength=11
			        		onblur="value=value.replace(/[^0-9]/g,'')"
				      >
				    </div>
				  </div>
				  <div class="form-group">
				  	<div class="col-xs-12">
					   	<div class="yzm" id="yzmDiv" style="display:block;margin-left:159px;">
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
				  <div class="form-group shoujiyz">
				    <label class="col-xs-3 control-label">手机验证码</label>
				    <div class="col-xs-6">
				      <input type="text" class="form-control" placeholder=""
				      id="sjyzm" name="sjyzm" onfocus="clearmsgHide('errormsg');"
			        		onblur="value=value.replace(/[^0-9]/g,'')"
				      >
				    </div>
				    <div class="col-xs-3 fasong">
				  		<button type="button" class="btn btn-empty" onclick="getMobileCode();" name="yzmBut" id="yzmBut">发送验证码</button>
				  	</div>
				  </div>
				  <div class="text-error" name="errormsg" id="errormsg" style="display:none">${errormsg}</div>
				  <div class="form-group">
				  	<div class="col-xs-offset-3 col-xs-9">
				  		<a href="javascript:void(0);" class="btn btn-orange btn-full" onclick="regGrSubmit();">提交</a>
				  	</div>
				  </div>
				</div>
			</form>
		</div>
	</div>
	<!--footer-->
	<%@ include  file="/WEB-INF/pages/common/footer.jsp"%>
	
	
</body>
</html>