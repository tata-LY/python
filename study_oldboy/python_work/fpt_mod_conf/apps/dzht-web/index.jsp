<!DOCTYPE html>
<%@ page language="java" import="java.util.*" pageEncoding="UTF-8"%>
<html>
<head>
	<%@ include  file="/WEB-INF/pages/common/head.jsp"%>
	<title>电子合同-签大大</title>
	<link rel="stylesheet" href="<%=basePath %>css/pages.css">
	<link rel="stylesheet" href="<%=basePath %>css/jquery.fullPage.css">
	<script src="<%=basePath %>js/css/jquery.fullPage.js"></script>
	<script src="<%=basePath %>js/index.js"></script>
</head>
<body>
	<div id="fullPage">
		<!-- banner -->
		<div class="section banner">
			<!-- 头部 -->
			<jsp:include page="/WEB-INF/pages/common/head_top.jsp">
		     	<jsp:param value="1" name="top_menu_id"/>
		   	</jsp:include>
			<div class="banimg">
				<img src="<%=basePath %>images/banner_00.png" class="banner00" alt="">
				<img src="<%=basePath %>images/banner_01.png" class="banner01" alt="">
				<img src="<%=basePath %>images/banner_02.png" class="banner02" alt="">
				<img src="<%=basePath %>images/banner_03.png" class="banner03" alt="">
				<img src="<%=basePath %>images/banner_04.png" class="banner04" alt="">
				<img src="<%=basePath %>images/banner_05.png" class="banner05" alt="">
				<img src="<%=basePath %>images/banner_06.png" class="banner06" alt="">
				
			</div>
		</div>
		<!-- 特性 -->
		<div class="section texing">
			<div class="container">
				<div class="tx_bt">
					<h2>特性</h2>
					<span>Characteristic</span>
				</div>
				<div class="tx_tb">
					<div class="tx">
						<img src="<%=basePath %>images/tx_0.png" alt="">
						<h4>特性</h4>
						<p>专业的电子合同服务</p>
						<p>让签约更高效与可靠</p>
					</div>
					<div class="tx_list tx_1">
						<img src="<%=basePath %>images/tx_1.png" alt="">
						<h5>随时随地</h5>
					</div>
					<div class="tx_list tx_2">
						<img src="<%=basePath %>images/tx_2.png" alt="">
						<h5>在线编辑</h5>
					</div>
					<div class="tx_list tx_3">
						<img src="<%=basePath %>images/tx_3.png" alt="">
						<h5>合同查验</h5>
					</div>
					<div class="tx_list tx_4">
						<img src="<%=basePath %>images/tx_4.png" alt="">
						<h5>实名认证</h5>
					</div>
					<div class="tx_list tx_5">
						<img src="<%=basePath %>images/tx_5.png" alt="">
						<h5>云存储</h5>
					</div>
				</div>
			</div>
		</div>
		<!-- 电子签名法 -->
		<div class="section dzqmf">
			<div class="container">
				<div class="dzqmf_bt text-center">
					<div class="dztitle">
						<h2>电子签名法</h2>
						<span>Electronic Signature Act</span>
					</div>
					<div class="dzsming">
						<p>电子签名同时符合下列条件的，视为可靠的电子签名</p>
						<p class="text-muted">当事人也可以选择使用符合其约定的可靠条件的电子签名</p>
					</div>
				</div>
				<div class="dzqmf_nr">
					<div class="col-xs-offset-2 col-xs-3 text-center">
						<img src="<%=basePath %>images/qm_01.png" alt="">
						<h5>专有</h5>
						<p>电子签名制作数据用于电子签名时，属于电子签名人专有</p>
					</div>
					<div class="col-xs-offset-2 col-xs-3 text-center">
						<img src="<%=basePath %>images/qm_02.png" alt="">
						<h5>控制</h5>
						<p>签署时电子签名制作数据仅由电子签名人控制</p>
					</div>
					<div class="col-xs-offset-2 col-xs-3 text-center">
						<img src="<%=basePath %>images/qm_03.png" alt="">
						<h5>改动</h5>
						<p>签署后对电子签名的任何改动能够被发现</p>
					</div>
					<div class="col-xs-offset-2 col-xs-3 text-center">
						<img src="<%=basePath %>images/qm_04.png" alt="">
						<h5>发现</h5>
						<p>签署后对数据电文内容和形式的任何改动能够被发现</p>
					</div>
				</div>

			</div>
		</div>
		<!-- 合作伙伴 -->
		<div class="section partner">
			<div class="container">
				<div class="partner_bt">
					<h2>合作伙伴</h2>
					<span>Cooperative Partner</span>
				</div>
				<div class="partnerlogo">
					<div class="col-xs-4"></div>
					<div class="col-xs-4"></div>
					<div class="col-xs-4"></div>
					<div class="col-xs-4"><img src="<%=basePath %>images/partner01.png" alt=""></div>
					<div class="col-xs-4"><img src="<%=basePath %>images/partner02.png" alt=""></div>
					<div class="col-xs-4"><img src="<%=basePath %>images/partner03.png" alt=""></div>
					<div class="col-xs-4"></div>
					<div class="col-xs-4"></div>
					<div class="col-xs-4"></div>
				</div>
			</div>
			<!--footer-->
			<%@ include  file="/WEB-INF/pages/common/footer.jsp"%>
		</div>
	</div>
	
</body>
</html>