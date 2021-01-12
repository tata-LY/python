<!DOCTYPE html>
<%@ page language="java" import="java.util.*" pageEncoding="UTF-8"%>
<html>
<head>
	<%@ include  file="/WEB-INF/pages/common/head.jsp"%>
	<title>电子合同-签大大</title>
	<link rel="stylesheet" href="<%=basePath %>css/pages.css">
	<script src="<%=basePath %>js/qy_list/list.js"></script>
	<script src="js/pagination/common.js"></script>
</head>
<body>
	<!-- 头部 -->
	<jsp:include page="/WEB-INF/pages/common/head_top.jsp">
     	<jsp:param value="6" name="top_menu_id"/>
   	</jsp:include>
	<!-- banner -->
	<div id="carousel-example-generic" class="carousel slide" data-ride="carousel">
	  <!-- Wrapper for slides -->
	  <div class="carousel-inner" role="listbox">
	    <div class="item active">
	      <img src="<%=basePath %>images/banner_qiye.jpg" alt="">
	    </div>
	  </div>
	</div>
	<div class="qiye">
		<div class="container">
			<!-- 添加客户流程 -->
			<div class="panel panel-default">
			  <div class="panel-heading">
			    <h3 class="panel-title">添加客户流程</h3>
			  </div>
			  <div class="panel-body">
			    <div class="step">
			    	<div class="tubiao"><img src="<%=basePath %>images/step1.png" alt=""></div>
			    	<h4 class="text-uppercase">STEP <i>1</i></h4>
			    	<p>下载申请表</p>
			    </div>
			    <div class="step">
			    	<div class="tubiao"><img src="<%=basePath %>images/step2.png" alt=""></div>
			    	<h4 class="text-uppercase">STEP <i>2</i></h4>
			    	<p>填写并盖章</p>
			    </div>
			    <div class="step">
			    	<div class="tubiao"><img src="<%=basePath %>images/step3.png" alt=""></div>
			    	<h4 class="text-uppercase">STEP <i>3</i></h4>
			    	<p>提交材料及申请表</p>
			    </div>
			    <div class="step">
			    	<div class="tubiao"><img src="<%=basePath %>images/step4.png" alt=""></div>
			    	<h4 class="text-uppercase">STEP <i>4</i></h4>
			    	<p>我方审核</p>
			    </div>
			    <div class="step">
			    	<div class="tubiao"><img src="<%=basePath %>images/step5.png" alt=""></div>
			    	<h4 class="text-uppercase">STEP <i>5</i></h4>
			    	<p>审核通过</p>
			    </div>
			  </div>
			</div>

			<!-- 企业所需材料 -->
			<div class="panel panel-default">
			  <div class="panel-heading">
			    <h3 class="panel-title">企业所需材料</h3>
			  </div>
			  <div class="panel-body">
			  	<div class="cailiao">
				    <div><i>1</i>营业执照及组织机构代码证盖章复印件（三证合一后仅需营业执照）</div>
					<div><i>2</i>企业信息及CA申请表盖章件</div>
					<div><i>3</i>企业法定代表人/代理人身份证盖章复印件</div>

					<a href="javascript:void(0);" class="btn btn-empty" onclick="downloadXxdj()">下载企业信息及CA申请表</a>
			  	</div>
			  </div>
			</div>

			<!-- 申请证书结果回调URL: -->
			<div class="form-horizontal">
			  <div class="form-group">
			    <label class="col-xs-2 control-label">申请证书结果回调URL</label>
			    <div class="col-xs-9">
			      <input type="text" class="form-control" id="caurl" name="caurl" value="${commonDataMap.CAURL }">
			    </div>
			    <div class="col-xs-1">
			      <button type="button" class="btn btn-orange" onclick="updateJrfInfo();">提交</button>
			    </div>
			  </div>
			  
			</div>

			<!-- 添加新企业客户 -->
			<div class="addnew">
				<a href="qyList.do?method=regQy" class="btn btn-orange"><span class="glyphicon glyphicon-plus" aria-hidden="true"></span> 添加新企业客户</a>
			</div>
			
			<form id="forms" action="qyList.do?method=list"  method="post">	
				<div class="kehuxx">
						<table class="table table-striped table-condensed">
						    <thead>
						        <tr>
						          <th>客户账号</th>
						          <th>客户名称</th>
						          <th>审核状态</th>
						          <th>操作</th>
						        </tr>
						    </thead>
						    <tbody>
						    	<c:forEach var="bean" items="${qyList}">
									<tr>
							          <td>${bean.ZHMC}</td>
							          <td title="${bean.QYMC}">
						          		<c:choose>
											<c:when test="${bean.QYMC eq ''}">
												&nbsp;
											</c:when>
											<c:when test="${fn:length(bean.QYMC)>6}">
											${ fn:substring( bean.QYMC ,0,6)}...
											</c:when>
											<c:otherwise>
												${bean.QYMC}
											</c:otherwise>
										</c:choose>
							          </td>
							          <td>
							          	<span class="btn-tips">
								          	<c:choose>
								          		<c:when test="${bean.SHZT eq '0'}">
								          			未审核
								          		</c:when>
								          		<c:when test="${bean.SHZT eq '1'}">
								          			审核通过
								          		</c:when>
								          		<c:when test="${bean.SHZT eq '2'}">
								          			审核拒绝
								          		</c:when>
								          	</c:choose>
							         	 </span>
							          </td>
							          <td>
							          	<a href="qyList.do?method=qyDetail&qyId=${bean.QYID}" class="chakan" data-toggle="tooltip" data-placement="bottom" title="" data-original-title="查看企业信息">
							          		<span class="glyphicon glyphicon-eye-open" aria-hidden="true"></span>
							          	</a>
							          	<c:if test="${bean.SHZT ne '1'}">
								          	<a href="qyList.do?method=toup&qyId=${bean.QYID}" class="download" data-toggle="tooltip" data-placement="bottom" title="编辑客户信息">
								          		<span class="glyphicon glyphicon-pencil" aria-hidden="true"></span>
								          	</a>
							          	</c:if>
							          </td>
							        </tr>
								</c:forEach>
						    </tbody>
						</table>
						 <c:if test="${total > 0}">
							<%@ include file="/WEB-INF/pages/pagination/common.jsp"%>
						</c:if>
						<c:if test="${total <= 0}">
					  		 <div class="">
								<h3 style="text-align:center;margin:50px auto;color:#999;font-size:24px;">对不起，没找到您想要的数据！</h3>
							 </div>
					    </c:if>
					    
					    
					    
				</div>
			
			</form>
		</div>
	</div>

	<!--footer-->
	<%@ include  file="/WEB-INF/pages/common/footer.jsp"%>
	
</body>
</html>	