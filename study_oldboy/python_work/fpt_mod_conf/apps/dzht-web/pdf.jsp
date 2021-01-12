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
	<!--
	<link rel="stylesheet" type="text/css" href="styles.css">
	-->
	<script type="text/javascript" src="js/jquery-1.9.1.min.js"></script>
	<script type="text/javascript">
		function abcd(){
			$("#iframe1").attr("src","test.do?method=viewPDF");
		}
	</script>
  </head>
  
  <body onload="abcd();">
    <h1>PDF.JSP</h1>
    <iframe src="about:blank" frameborder="0"style="border: solid 1px black;" marginheight="0"
										marginwidth="0" width="925" height="600" name="iframe1"
										id="iframe1">
										
										</iframe>
  </body>
</html>
