<!DOCTYPE html>
<%@ page language="java" import="java.util.*" pageEncoding="UTF-8"%>
<html>
<head>
	<%@ include  file="/WEB-INF/pages/common/head.jsp"%>
	<title>电子合同-签大大</title>
	<link rel="stylesheet" href="<%=basePath %>css/pages.css">
	<link rel="stylesheet" href="<%=basePath %>css/jquery.fullPage.css">
	<script src="<%=basePath %>js/css/jquery.fullPage.js"></script>
	<script src="<%=basePath %>js/outside/product.js"></script>
</head>
<body>
	<div id="fullPage">
		<!-- banner -->
		<div class="section probanner">
			<!-- 头部 -->
			<jsp:include page="/WEB-INF/pages/common/head_top.jsp">
		     	<jsp:param value="2" name="top_menu_id"/>
		   	</jsp:include>
			<div class="container">
				<div class="banimg">
					<img src="<%=basePath %>images/pro_ban01.png" class="pro_ban01" alt="">
					<img src="<%=basePath %>images/pro_ban02.png" class="pro_ban02" alt="">
					<img src="<%=basePath %>images/pro_ban03.png" class="pro_ban03" alt="">
				</div>
				<div class="pro_jiami">
					<div class="col-xs-4">
						<img src="<%=basePath %>images/pro_ban04.png" alt="">
					</div>
					<div class="col-xs-4">
						<img src="<%=basePath %>images/pro_ban05.png" alt="">
					</div>
					<div class="col-xs-4">
						<img src="<%=basePath %>images/pro_ban06.png" alt="">
					</div>
				</div>
			</div>
		</div>
		<div class="section wuzhihua">
			<div class="wzimg">
				<img src="<%=basePath %>images/wzh01.png" alt="">
				<img src="<%=basePath %>images/wzh02.png" alt="">
				<img src="<%=basePath %>images/wzh03.png" alt="">
				<img src="<%=basePath %>images/wzh04.png" alt="">
				<img src="<%=basePath %>images/wzh05.png" alt="">
			</div>
			<div class="wzneirong">
				<p><span class="text-orange">无纸化办公</span>解决方案</p>
				<p>优化你的整个业务</p>
			</div>

		</div>
		<div class="section baozhang">
			<div class="bzimg"><img src="<%=basePath %>images/baozhang01.png" alt=""></div>
			<div class="bzneirong">
				<p>相关法律法规支持</p>
				<p>合同效益<span class="text-orange">有保障</span></p>
			</div>
		</div>
		<div class="section jiami">
			<div class="jmimg">
				<img src="<%=basePath %>images/jiami01.png" alt="">
				<img src="<%=basePath %>images/jiami02.png" alt="">
				<img src="<%=basePath %>images/jiami03.png" alt="">
				<img src="<%=basePath %>images/jiami04.png" alt="">
				<img src="<%=basePath %>images/jiami05.png" alt="">
			</div>
			<div class="jmneirong">
				<p>信息安全，<span class="text-orange">全程加密</span></p>
				<p>篡改可被发现，合同可第三方校验</p>
			</div>
			<!--footer-->
			<%@ include  file="/WEB-INF/pages/common/footer.jsp"%>
		</div>
	</div>

</body>
</html>