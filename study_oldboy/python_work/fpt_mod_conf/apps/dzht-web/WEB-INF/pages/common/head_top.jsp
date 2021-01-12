<%@ page language="java" import="java.util.*" pageEncoding="UTF-8"%>
<%@ taglib uri="http://java.sun.com/jstl/core_rt" prefix="ctop"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/functions" prefix="fntop" %>
<%
	String path_top = request.getContextPath();
	String basePath_top = request.getScheme() + "://"
			+ request.getServerName() + ":" + request.getServerPort()
			+ path_top + "/";
%>
<script>
	function logout(){
		window.location.href="info.do?method=logout";
	}
	$(function(){
		var style = document.createElement("style");
		document.head.appendChild(style);
		sheet = style.sheet
		var head_top_shzt = $("#head_top_shzt").val();
		var head_top_zhlx = $("#head_top_zhlx").val();
		if("gr"==head_top_zhlx || "qy"==head_top_zhlx){
			if("1"==head_top_shzt){
				sheet.insertRule('.top_nav .col-xs-3 .loginxx:after {background-image: url(<%=basePath_top %>images/renzheng.png);}', 0);
			}else{
				sheet.insertRule('.top_nav .col-xs-3 .loginxx:after {background-image: url(<%=basePath_top %>images/weirenzheng.png);}', 0);
			}
		}else{
				sheet.insertRule('.top_nav .col-xs-3 .loginxx:after {background-image: url(<%=basePath_top %>images/renzheng.png);}', 0);
		}
	});
</script>
	<div class="top_nav">
	  <div class="container">
	    <div class="row">
	      <div class="col-xs-2"><a href="<ctop:url value='/index.do?method=index'/>"><img src="<%=basePath_top %>images/dzht_logo.png" alt=""></a></div>
	      <input type="hidden" name="head_top_shzt" id="head_top_shzt" value="${sessionScope.commonDataMap.SHZT}"/> 
	      <input type="hidden" name="head_top_zhlx" id="head_top_zhlx" value="${sessionScope.ZHLX_SESSION}"/> 
	      <div class="col-xs-7">
	        <ul class="nav nav-justified">
	          <li><a href="<ctop:url value='/index.do?method=index'/>"
	          	<ctop:if test="${param.top_menu_id==1}">class="active" </ctop:if>
	          >首页</a></li>
	          <li><a href="<ctop:url value='/about.do?method=product'/>"
	          		<ctop:if test="${param.top_menu_id==2}">class="active" </ctop:if>
	          		>产品</a>
	          </li>
	          <li>
	          	<a href="<ctop:url value='/about.do?method=about'/>"
	          		<ctop:if test="${param.top_menu_id==3}">class="active" </ctop:if>
	          		>关于我们</a>
	          </li>
	          <ctop:if test="${not empty sessionScope.ZHID}">
		          <li><a href="<ctop:url value='/info.do?method=info'/>"   
		          		<ctop:if test="${param.top_menu_id==4}">class="active" </ctop:if>
		          	>客户中心</a></li>
		          <li><a href="<ctop:url value='/htgl.do?method=index'/>"
		          	<ctop:if test="${param.top_menu_id==5}">class="active" </ctop:if>
		          >合同管理</a></li>
		          <ctop:if test="${sessionScope.ZHLX_SESSION eq 'jrf' }">
		          <li><a href="<ctop:url value='/qyList.do?method=list'/>"
		          		<ctop:if test="${param.top_menu_id==6}">class="active" </ctop:if>
		          >企业客户管理</a></li>
		          </ctop:if>
	          </ctop:if>
	        </ul>
	      </div>
	      <div class="col-xs-3 text-right">
		      <ctop:choose>
		      	<ctop:when test="${not empty sessionScope.ZHID}">
		      	 	<div class="loginxx">
			          <p>
			          	<ctop:choose>
							<ctop:when test="${INFO_COMMON_MC eq ''}">
								&nbsp;
							</ctop:when>
							<ctop:when test="${fntop:length(INFO_COMMON_MC)>13}">
							${ fntop:substring( INFO_COMMON_MC ,0,13)}...
							</ctop:when>
							<ctop:otherwise>
								${INFO_COMMON_MC}
							</ctop:otherwise>
						</ctop:choose>
			          	</p>
			          <p>
			          
			          <ctop:choose>
							<ctop:when test="${sessionScope.ZHMC eq ''}">
								&nbsp;
							</ctop:when>
							<ctop:when test="${fntop:length(sessionScope.ZHMC)>25}">
							${ fntop:substring( sessionScope.ZHMC ,0,25)}...
							</ctop:when>
							<ctop:otherwise>
								${sessionScope.ZHMC}
							</ctop:otherwise>
						</ctop:choose>
			          </p>
			        </div>
	        <button type="button" class="btn-link" onclick="logout();">退出</button>
		      	</ctop:when>
		      	<ctop:otherwise>
			        <a class="btn btn-orange" href="<ctop:url value='/index.do?method=login'/>" role="button">登录</a>
			        <a class="btn btn-empty" href="<ctop:url value='/comIndex.do?method=reg'/>" role="button">注册</a>
		      	</ctop:otherwise>
		      </ctop:choose>
		  </div>
	    </div>
	  </div>
	</div>