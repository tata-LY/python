<%@ page language="java" import="java.util.*" pageEncoding="UTF-8"%>
<%
	String path = request.getContextPath();
	String basePath = request.getScheme() + "://"+ request.getServerName() + ":" + request.getServerPort()+ path + "/";
%>
<%@ include  file="/WEB-INF/pages/common/common.jsp"%>
<%@ include  file="/WEB-INF/pages/common/common_waiting.jsp"%>
<!-- head.html -->
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta http-equiv="X-UA-Compatible" content="ie=edge">
<%@ taglib uri="http://java.sun.com/jstl/core_rt" prefix="c"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/functions" prefix="fn" %>
<!-- 新 Bootstrap 核心 CSS 文件 -->
<link href="<%=basePath %>css/bootstrap.min.css" rel="stylesheet">
<link href="<%=basePath %>css/common.css" rel="stylesheet">
<script src="<%=basePath %>js/jquery-1.9.1.min.js"></script>
<script src="<%=basePath %>js/utils/common.js"></script>
<script src="<%=basePath %>js/utils/alertMsg.js"></script>
<script src="<%=basePath %>js/css/bootstrap.min.js"></script>

<!-- end head.html -->
