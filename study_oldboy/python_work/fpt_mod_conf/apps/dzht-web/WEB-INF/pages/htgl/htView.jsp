<%--
  Created by IntelliJ IDEA.
  User: d
  Date: 2017/11/15
  Time: 10:40
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%
    String path = request.getContextPath();
    String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";
%>
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
    <base href="<%=basePath%>">
    <title>Title</title>
    <meta http-equiv="pragma" content="no-cache">
    <meta http-equiv="cache-control" content="no-cache">
    <meta http-equiv="expires" content="0">
    <meta http-equiv="keywords" content="keyword1,keyword2,keyword3">
    <meta http-equiv="description" content="This is my page">
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
    <meta name="google" content="notranslate">
    <script type="text/javascript">
        var htId = '${htId}';
        var DEFAULT_URL = '<%=basePath%>/htgl.do?method=downloadPdf&htId='+htId;
    </script>
    <jsp:include page="/WEB-INF/pages/common_pdf_js/pdf_js_head.jsp"></jsp:include>
</head>
<body tabindex="1" class="loadingInProgress">
<jsp:include page="/WEB-INF/pages/common_pdf_js/pdf_js_body.jsp"></jsp:include>
</body>
</html>
