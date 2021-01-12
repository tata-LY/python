<!DOCTYPE html>
<%@ page language="java" import="java.util.*" pageEncoding="UTF-8"%>
<html>
<head>
	<%@ include  file="/WEB-INF/pages/common/head.jsp"%>
	<title>个人材料自助提交系统</title>
	<link rel="stylesheet" href="<%=basePath %>css/qianshu.css">
	<script src="<%=basePath %>js/reg/reg_gr_rz.js"></script>
	<link rel="stylesheet" href="<%=basePath %>css/zoomify.min.css">
	<script src="<%=basePath %>js/css/zoomify.min.js"></script>
	<!-- 新的上传插件 -->
	<script src="<%=basePath %>js/upload_common/upload_reg_gr_rz.js"></script>
	<jsp:include page="/WEB-INF/pages/common/common_upload.jsp"></jsp:include>
</head>
<body onload="showHide();">
	<!-- 头部 -->
	<jsp:include page="/WEB-INF/pages/common/head_top.jsp">
     	<jsp:param value="999" name="top_menu_id"/>
   </jsp:include>
	<div class="gr_zltj container">
		<form class="" action="grrz.do?method=rzsub" method="post" id="forms">	
			<input type="hidden" name="reg_gr_rz_zjlx" id="reg_gr_rz_zjlx" value="${sessionScope.commonDataMap.ZJLX}"/>
			<input type="hidden" name="reg_gr_rz_shzt" id="reg_gr_rz_shzt" value="${sessionScope.commonDataMap.SHZT}"/>
			<input type="hidden" name="randomReg"id="randomReg" value="${randomReg }"/>
			<div class="col-xs-offset-3 col-xs-6">
				<!-- Nav tabs -->
				<ul class="nav nav-tabs" role="tablist">
				    <li role="presentation" class="active" id="yinhangka_li" onclick="changeRzType('yinhangka');">
				    	<a href="javascript:void(0);" aria-controls="yinhangka" role="tab" data-toggle="tab">银行卡认证</a>
				    </li>
				    <li role="presentation" id="paizhao_li"  onclick="changeRzType('paizhao');">
				    	<a href="javascript:void(0);" aria-controls="paizhao" role="tab" data-toggle="tab">拍照认证</a>
				    </li>
				</ul>
				<!-- Tab panes -->
				<div class="tab-content">
				    <div role="tabpanel" class="tab-pane active" id="yinhangka">
						<div class="form-horizontal">
						  <div class="form-group">
						    <label class="col-xs-3 control-label">银行卡号</label>
						    <div class="col-xs-9">
						      <input type="text" class="form-control" placeholder=""
						      	 id="yhkh" name="yhkh" maxlength=60
						      >
						    </div>
						  </div>
						  <div class="form-group">
						    <label class="col-xs-3 control-label">预留手机号</label>
						    <div class="col-xs-9">
						      <input type="text" class="form-control" placeholder=""
						      	 id="ylhm" name="ylhm" maxlength=11
						      >
						    </div>
						  </div>
						  <div class="form-group">
						  	<div class="col-xs-offset-3 col-xs-9">
						  		<a href="javascript:void(0);" class="btn btn-orange btn-full" onclick="grrzSub('yinhangka');">提交</a>
						  	</div>
						  </div>
						</div>
				    </div>
				    <div role="tabpanel" class="tab-pane" id="paizhao">
				    	<div class="col-xs-12">
				    		<div class="text-center">
				    			<div class="shilitu"><img src="<%=basePath %>images/shili_scsfz.jpg" alt=""></div>
					    		<div class="sltwz">手持身份证照片示例图</div>
				    		</div>
				    		<div class="text-center">
					    		<div class="suoluetu shilitu">
					    			<img id="upload_GRSCSFZ_SHOW" alt="" 
										<c:if test="${scsfzContentFlag eq '1'}">
											src="data:image/gif;base64,${scsfzContent}"
										</c:if>
									/>
					    		</div>
					    		 <!-- 上传插件 -->
								<span class="smwenzi fileinput-button upload_show_hide" style="margin-top: 5px;">
						            <i class="glyphicon"></i>
						            <span>上传手持身份证照片</span>
						            <input id="upload_GRSCSFZ" type="file" name="upload_GRSCSFZ">
						         </span>
								<!-- 上传插件 -->
				    		</div>
				    		<div class="tijiaopz">
			    			<a href="javascript:void(0);" class="btn btn-orange btn-full" onclick="grrzSub('paizhao');">提交</a>
			    			</div>
				    	</div>
				    </div>
				</div>
			</div>
		
		</form>
	</div>
	<!--footer-->
	<%@ include  file="/WEB-INF/pages/common/footer.jsp"%>
	
	
</body>
</html>