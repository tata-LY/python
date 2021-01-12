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
	 <style>
        #box {
            width: 100px;
            height: 100px;
            background-color: aquamarine;
            position: absolute;
        }
    </style>
  </head>
  
  <body>
  <div id="box"></div>
    <script type="text/javascript">
        var oDiv = document.getElementById("box");
        oDiv.onmousedown=function(ev)
        {
            var oEvent = ev; 
            var disX = oEvent.clientX - oDiv.offsetLeft;
            var disY = oEvent.clientY - oDiv.offsetTop;
            document.onmousemove=function (ev)
            {
                oEvent = ev;
                oDiv.style.left = oEvent.clientX -disX+"px";
                oDiv.style.top = oEvent.clientY -disY+"px";
            }
            document.onmouseup=function()
            {
               document.onmousemove=null;
               document.onmouseup=null;
            }
            
        }
        
    </script>
    <H1>Test.jsp</H1>
  </body>
</html>
