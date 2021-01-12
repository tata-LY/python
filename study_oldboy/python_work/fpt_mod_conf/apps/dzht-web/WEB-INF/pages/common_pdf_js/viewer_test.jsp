<%@ page language="java" import="java.util.*" pageEncoding="utf-8"%>
<%
String path = request.getContextPath();
String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";
%>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
  <head>
    <base href="<%=basePath%>">
    
    <title>My JSP 'index.jsp' starting page</title>
	<meta http-equiv="pragma" content="no-cache">
	<meta http-equiv="cache-control" content="no-cache">
	<meta http-equiv="expires" content="0">    
	<meta http-equiv="keywords" content="keyword1,keyword2,keyword3">
	<meta http-equiv="description" content="This is my page">
	 <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
    <meta name="google" content="notranslate">
    <title>PDF.js viewer</title>

   <script type="text/javascript">
    var fileId = ${fileId};
    var DEFAULT_URL = '<%=basePath%>/test.do?method=viewPDF&fileId='+fileId;
    </script>
    <jsp:include page="/WEB-INF/pages/common_pdf_js/pdf_js_head.jsp"></jsp:include>
  </head>
<body tabindex="1" class="loadingInProgress">
    <jsp:include page="/WEB-INF/pages/common_pdf_js/pdf_js_body.jsp"></jsp:include>
  </body>
</html>
