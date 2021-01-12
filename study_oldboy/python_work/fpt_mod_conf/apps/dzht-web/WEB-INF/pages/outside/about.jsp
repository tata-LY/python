<!DOCTYPE html>
<%@ page language="java" import="java.util.*" pageEncoding="UTF-8"%>
<html>
<head>
	<%@ include  file="/WEB-INF/pages/common/head.jsp"%>
	<link rel="stylesheet" href="<%=basePath %>css/pages.css">
	<title>电子合同-签大大</title>
</head>
<body>
	<!-- 头部 -->
	<jsp:include page="/WEB-INF/pages/common/head_top.jsp">
     	<jsp:param value="3" name="top_menu_id"/>
   	</jsp:include>
	<!-- banner -->
	<div id="carousel-example-generic" class="carousel slide" data-ride="carousel">
	  <!-- Wrapper for slides -->
	  <div class="carousel-inner" role="listbox">
	    <div class="item active">
	      <img src="<%=basePath %>images/banner_about.jpg" alt="">
	    </div>
	  </div>
	</div>
	<!-- neirong -->
	<div class="about container">
		<div class="col-xs-12">
			<div class="col-xs-8">
				<img src="<%=basePath %>images/about_01.png" alt="">
				<p>百望电子发票数据服务有限公司，是基于深圳市中润四方信息技术有限公司电子发票平台的技术优势和百望金赋体系服务优势，由中润四方独资设立的高科技企业，专注于企业办公一体化服务。</p>
				<p>百望电票发展至今不仅中标中国联通、中国电信等电信服务商的电子发票系统项目，还为国家电网、顺丰速运等大型企业，京东、唯品会、我买网等知名电商提供企业办公全流程服务，项目实施经验丰富，服务体系有口皆碑。依托现有资源与技术，百望电票推出“签大大”电子合同系统，借此完善百望企业服务生态圈，致力于打造企业无纸化服务生态闭环。</p>
			</div>
			<div class="col-xs-4">
				<img src="<%=basePath %>images/about_02.png" alt="">
			</div>
		</div>
			
		<div class="col-xs-12 fazhan">
			<div class="col-xs-offset-2 col-xs-7"><img src="<%=basePath %>images/about_03.jpg" alt=""></div>
		</div>
		<div class="col-xs-12">
			<div class="col-xs-3 licheng"></div>
			<div class="clearfix"></div>
			<div class="list">
				<div class="col-xs-3 text-right">
					<h5>2017年</h5>
				</div>
				<div class="col-xs-8">
					<div>百望电子发票推出电子合同签约平台“签大大”</div>
				</div>
			</div>
			<div class="list">
				<div class="col-xs-3 text-right">
					<h5>2016年</h5>
				</div>
				<div class="col-xs-8">
					<div>百望电子发票已为广东、天津、上海、福建、厦门、江西、青海、山西、宁波、甘肃、安徽、重庆、贵州等20多个省市的企业提供了电子发票综合服务，电子发票一体化服务覆盖全国。</div>
				</div>
			</div>
			<div class="list">
				<div class="col-xs-3 text-right">
					<h5>2015年</h5>
					<span>11月</span>
					<span>10月</span>
					<span>01月</span>
				</div>
				<div class="col-xs-8">
					<div></div>
					<p>与微信合作，发布商超、加油站等行业一体化服务方案。</p>
					<p>百望电子发票云服务平台——“发票通”云平台（fapiao.com）正式发布。</p>
					<p>中润四方开始为优购、华为、盐田港等企业提供服务。</p>

				</div>
			</div>
			<div class="list">
				<div class="col-xs-3 text-right">
					<h5>2014年</h5>
					<span>09月</span>
				</div>
				<div class="col-xs-8">
					<div></div>
					<p>中润四方开始为唯品会、粤海水务、珠江数码、广州自来水等企业提供服务。</p>

				</div>
			</div>
			<div class="list">
				<div class="col-xs-3 text-right">
					<h5>2012年</h5>
					<span>06月</span>
				</div>
				<div class="col-xs-8">
					<div></div>
					<p>中润四方参与国家八部委在电子商务示范城市启动试点工作，参与标准研究并承建深圳市试点项目。</p>

				</div>
			</div>
			<div class="col-xs-8 col-xs-offset-3 end"></div>
		</div>
	</div>
	<!--footer-->
	<%@ include  file="/WEB-INF/pages/common/footer.jsp"%>
	
	
</body>
</html>