<!DOCTYPE html>
<%@ page language="java" import="java.util.*" pageEncoding="UTF-8"%>
<html>
<head>
	<%@ include  file="/WEB-INF/pages/common/head.jsp"%>
	<title>电子合同-签大大</title>
	<link rel="stylesheet" href="<%=basePath %>css/pages.css">
	<script src="<%=basePath %>js/info/info.js"></script>
	<script src="<%=basePath %>js/utils/passwd.js"></script>
	<script src="<%=basePath %>js/utils/md5.js"></script>
</head>
<body onload="showHideSZMM();">
	<!-- 头部 -->
	<jsp:include page="/WEB-INF/pages/common/head_top.jsp">
     <jsp:param value="4" name="top_menu_id"/>
   </jsp:include>
	<!-- banner -->
	<div id="carousel-example-generic" class="carousel slide" data-ride="carousel">
	  <!-- Wrapper for slides -->
	  <div class="carousel-inner" role="listbox">
	    <div class="item active">
	      <img src="<%=basePath %>images/banner_center.jpg" alt="">
	    </div>
	  </div>
	</div>
	<div class="center">
		<div class="container">
			<input type="hidden" name="randomMobile" id="randomMobile" value="${randomMobile}"/>
			<input type="hidden" id="mobileYzmKey" name="mobileYzmKey" value="${mobileYzmKey}"/>
			<input type="hidden" name="randomEmail" id="randomEmail" value="${randomEmail}"/>
			<input type="hidden" id="emailYzmKey" name="emailYzmKey" value="${emailYzmKey}"/>
			<input type="hidden" id="zhmmSjkz" name="zhmmSjkz" value="${commonDataMap.ZHMM}"/>
			
			<input type="hidden" id="sjhmTkHide" name="sjhmTkHide" value="${commonDataMap.SJHM}"/>
			<input type="hidden" id="zhmcTkHide" name="zhmcTkHide" value="${commonDataMap.ZHMC}"/>
			<input  type="hidden" id="randomCodeKey">
		    <input  type="hidden" id="randomCode">
			<!-- 基本信息 -->
			<div class="panel panel-default">
			  <div class="panel-heading">
			    <h3 class="panel-title">基本信息</h3>
			  </div>
			  <div class="panel-body">
			    <div class="form-group">
			    	<div class="col-xs-2">登录密码：</div>
			    	<div class="col-xs-3">*********</div>
			    	<div class="col-xs-1"><a href="javascript:;" class="bianji" data-toggle="modal" data-target="#mima" onclick="alertPassworddlg()">编辑</a></div>
			    	<div class="clearfix"></div>
			    </div>
			    <div class="form-group">
			    	<div class="col-xs-2">名称：</div>
			    	<div class="col-xs-3" title='${INFO_COMMON_MC}'>
	    					<c:choose>
								<c:when test="${INFO_COMMON_MC eq ''}">
									&nbsp;
								</c:when>
								<c:when test="${fn:length(INFO_COMMON_MC)>15}">
								${ fn:substring( INFO_COMMON_MC ,0,15)}...
								</c:when>
								<c:otherwise>
									${INFO_COMMON_MC}
								</c:otherwise>
							</c:choose>
			    	</div>
			    	<div class="clearfix"></div>
			    </div>
			    <div class="form-group">
			    	<div class="col-xs-2">证件号：</div>
			    	<div class="col-xs-3">
			    		<c:choose>
			    			<c:when test="${ZHLX_SESSION ne 'gr' && commonDataMap.SZHY eq '0'}">
			    				${commonDataMap.ZZJGDM}
			    			</c:when>
			    			<c:otherwise>
			    				${commonDataMap.ZJHM}
			    			</c:otherwise>
			    		</c:choose>
			    	</div>
			    	<c:if test="${ZHLX_SESSION ne 'jrf'}">
			    		<c:choose>
			    			<c:when test="${commonDataMap.SHZT eq '0'}">
			    				<div class="col-xs-5 text-danger">
			    					<span data-toggle="tooltip" data-placement="top">待审核</span>
			    				</div>
			    			</c:when>
			    			<c:when test="${commonDataMap.SHZT eq '1'}">
			    				<div class="col-xs-5 text-danger">
			    					<span data-toggle="tooltip" data-placement="top" title="">审核通过</span>
			    				</div>
			    			</c:when>
			    			<c:when test="${commonDataMap.SHZT eq '2'}">
			    				<div class="col-xs-5 text-danger">
			    					<span data-toggle="tooltip" data-placement="top" title="${commonDataMap.SHXX}">审核不通过</span>
			    						<c:choose>
			    							<c:when test="${ZHLX_SESSION eq 'gr'}">
			    								<a href="grrz.do?method=rz"  class="btn btn-link">修改资料</a>
			    							</c:when>
			    							<c:otherwise>
			    								<a href="qyup.do?method=toup"  class="btn btn-link">修改资料</a>
			    							</c:otherwise>
			    						</c:choose>	
			    				</div>
			    			</c:when>
			    		</c:choose>
			    	</c:if>
			    	<div class="clearfix"></div>
			    </div>
			    <div class="form-group">
			    	<div class="col-xs-2">手机号：</div>
			    	<div class="col-xs-3" id="info_sjhm_show_div">${commonDataMap.SJHM}</div>
			    	<div class="col-xs-1"><a href="javascript:;" class="bianji" data-toggle="modal" data-target="#shoujihao">编辑</a></div>
			    	<div class="clearfix"></div>
			    </div>
			    <div class="form-group">
			    	<div class="col-xs-2">邮箱号：</div>
			    	<div class="col-xs-3" id="info_zhmc_show_div">${commonDataMap.ZHMC}</div>
			    	<div class="col-xs-1"><a href="javascript:;" class="bianji" data-toggle="modal" data-target="#email">编辑</a></div>
			    	<div class="clearfix"></div>
			    </div>
			    <p class="text-muted"> * 邮箱变更后，后续请以新邮箱作为登录名登录</p>
			  </div>
			</div>
			<!-- 配置 -->
			<div class="panel panel-default">
			  <div class="panel-heading">
			    <h3 class="panel-title">配置</h3>
			  </div>
			  <div class="panel-body">
			    <p class="text-muted">合同签署完成后发送通知</p>
			    <div class="form-group">
			    	<div class="col-xs-2">短信通知</div>
			    	<div class="col-xs-1"><a href="javascript:void(0)" class="kaitong" id="info_dxtz" onclick="changeTz('info_dxtz');">开通</a></div>
			    	<div class="clearfix"></div>
			    </div>
			    <div class="form-group">
			    	<div class="col-xs-2">邮件通知</div>
			    	<div class="col-xs-1"><a href="javascript:void(0)" class="guanbi" id="info_yjtz" onclick="changeTz('info_yjtz');">关闭</a></div>
			    	<div class="clearfix"></div>
			    </div>
			    
			  </div>
			</div>
		</div>
		
	</div>

	<!--footer-->
	<%@ include  file="/WEB-INF/pages/common/footer.jsp"%>
	
	<!-- 弹框 -->
	<%@ include  file="/WEB-INF/pages/info/info_tk.jsp"%>
	
	
</body>
</html>	
