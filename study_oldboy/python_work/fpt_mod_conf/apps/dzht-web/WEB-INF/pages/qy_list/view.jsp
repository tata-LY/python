<!DOCTYPE html>
<%@ page language="java" import="java.util.*" pageEncoding="UTF-8"%>
<html>
<head>
	<%@ include  file="/WEB-INF/pages/common/head.jsp"%>
	<title>电子合同-签大大</title>
	<link rel="stylesheet" href="<%=basePath %>css/pages.css">
	<link rel="stylesheet" href="<%=basePath %>css/zoomify.min.css">
</head>
<body>
	<!-- 头部 -->
	<jsp:include page="/WEB-INF/pages/common/head_top.jsp">
     	<jsp:param value="6" name="top_menu_id"/>
   	</jsp:include>
	<div class="addnew qiyemessage">
		<div class="container">
			<div class="lujing">
				<ul class="list-inline">
					<li>企业客户管理</li>
					<li>企业客户信息</li>
				</ul>
			</div>
			<div class="panel panel-default">
			  <div class="panel-heading">
			    <h3 class="panel-title">企业客户信息</h3>
			  </div>
			  <div class="panel-body">
			    <div class="form-horizontal">
			    	<div class="col-xs-6">
					  <div class="form-group">
					    <label class="col-xs-3 control-label">邮箱账号</label>
					    <div class="col-xs-9">
					      ${dataMap.ZHMC }
					    </div>
					  </div>
			    	</div>
			    	<div class="col-xs-6">
					  <div class="form-group">
					    <label class="col-xs-3 text-right control-label">企业名称</label>
					    <div class="col-xs-9">
					    	${dataMap.QYMC }
					    </div>
					  </div>
			    	</div>
			    	<div class="col-xs-6">
					  <div class="form-group">
					    <label class="col-xs-3 control-label">企业类型</label>
					    <div class="col-xs-9">
					    	<c:choose>
					    		<c:when test="${dataMap.QYLX eq '01'}">普通企业</c:when>
					    		<c:when test="${dataMap.QYLX eq '02'}">社会团体</c:when>
					    		<c:when test="${dataMap.QYLX eq '03'}">事业单位</c:when>
					    		<c:when test="${dataMap.QYLX eq '04'}">民办非企业</c:when>
					    		<c:when test="${dataMap.QYLX eq '05'}">党政及国家单位</c:when>
					    	</c:choose>
					    </div>
					  </div>
			    	</div>
			    	<div class="col-xs-6">
					  <div class="form-group">
					    <label class="col-xs-3 text-right control-label">办公地址</label>
					    <div class="col-xs-9">
					      ${dataMap.QYDZ }
					    </div>
					  </div>
			    	</div>
			    	<div class="col-xs-6">
					  <div class="form-group">
					    <label class="col-xs-3 control-label">公司电话</label>
					    <div class="col-xs-9">
					      ${dataMap.DHHM }
					    </div>
					  </div>
			    	</div>
			    	<div class="col-xs-6">
					  <div class="form-group">
					    <label class="col-xs-3 text-right control-label">所属地区</label>
					    <div class="col-xs-9">
					        ${dataMap.QYSF }	
					    </div>
					  </div>
			    	</div>
					<div class="clearfix"></div>
				</div>

				<div class="col-xs-12 sanzhyi">
				  <!-- Nav tabs -->
				  <h3>三证</h3>

				  <!-- Tab panes -->
				  <div class="tab-content">
				    <div role="tabpanel" class="tab-pane active">
				    	<div class="form-horizontal row">
				    		<c:choose>
				    			<c:when test="${dataMap.SZHY eq '0' }">
				    				<div class="col-xs-6">
									  <div class="form-group">
									    <label class="col-xs-3 control-label">营业执照号</label>
									    <div class="col-xs-9">
									       ${dataMap.ZJHM }
									    </div>
									  </div>
							    	</div>
							    	<div class="col-xs-6">
									  <div class="form-group">
									    <label class="col-xs-3 control-label">组织机构代码证号</label>
									    <div class="col-xs-9">
									       ${dataMap.ZZJGDM }
									    </div>
									  </div>
							    	</div>
							    	<div class="col-xs-6">
							    		<div class="col-xs-9">
								    		<div class="shilitu"><img src="qyList.do?method=getQyTp&qyId=${dataMap.QYID }&tpzd=YYSWZ" alt=""></div>
								    		<div class="sltwz">营业执照复印件加盖公章</div>
							    		</div>
							    	</div>
							    	<div class="col-xs-6">
							    		<div class="col-xs-9">
								    		<div class="shilitu"><img src="qyList.do?method=getQyTp&qyId=${dataMap.QYID }&tpzd=ZZJGDM" alt=""></div>
								    		<div class="sltwz">组织机构代码证书复印件加盖公章</div>
							    		</div>
							    	</div>
				    			</c:when>
				    			<c:otherwise>
				    				<div class="col-xs-6">
									  <div class="form-group">
									    <label class="col-xs-3 control-label">统一社会信用代码</label>
									    <div class="col-xs-9">
									       ${dataMap.ZJHM }
									    </div>
									  </div>
							    	</div>
							    	<div class="clearfix"></div>
							    	<div class="col-xs-6">
							    		<div class="col-xs-9">
								    		<div class="shilitu"><img src="qyList.do?method=getQyTp&qyId=${dataMap.QYID }&tpzd=YYSWZ" alt=""></div>
								    		<div class="sltwz">营业执照复印件加盖公章</div>
							    		</div>
							    	</div>
				    			</c:otherwise>
				    		</c:choose>
							<div class="clearfix"></div>
						</div>
				    </div>
				  </div>

				</div>
				<div class="clearfix"></div>
				<h4>签章操作人</h4>
				<div class="col-xs-12">
				  <!-- Nav tabs -->
				  <h3>法人</h3>

				  <!-- Tab panes -->
				  <div class="tab-content">
				    <div role="tabpanel" class="tab-pane active">
				    	<div class="form-horizontal row">
					    	<div class="col-xs-6">
							  <div class="form-group">
							    <label class="col-xs-3 control-label">法人姓名</label>
							    <div class="col-xs-9">
							      ${dataMap.FRMC }
							    </div>
							  </div>
					    	</div>
					    	<div class="col-xs-6">
							  <div class="form-group">
							    <label class="col-xs-3 control-label">法人身份证号</label>
							    <div class="col-xs-9">
							      ${dataMap.FRSFZ }
							    </div>
							  </div>
					    	</div>
							<div class="clearfix"></div>
						</div>
						
						<c:if test="${empty dataMap.DLMC}">
							<div class="form-horizontal row">
						    	<div class="col-xs-6">
								  <div class="form-group">
								    <label class="col-xs-3 control-label">代理人姓名</label>
								    <div class="col-xs-9">
								      ${dataMap.DLMC }
								    </div>
								  </div>
						    	</div>
						    	<div class="col-xs-6">
								  <div class="form-group">
								    <label class="col-xs-3 control-label">代理人身份证号</label>
								    <div class="col-xs-9">
								      ${dataMap.DLSFZ }
								    </div>
								  </div>
						    	</div>
								<div class="clearfix"></div>
							</div>
						</c:if>
				    </div>
				  </div>

				  <div class="row">
				  	<div class="col-xs-4">
			    		<div class="shilitu"><img src="qyList.do?method=getQyTp&qyId=${dataMap.QYID }&tpzd=SFZ" alt=""></div>
				    	<div class="sltwz">身份证复印件加盖公章</div>
			    	</div>
			    	<div class="col-xs-4">
			    		<div class="shilitu"><img src="qyList.do?method=getQyTp&qyId=${dataMap.QYID }&tpzd=SQB_1" alt=""></div>
				    	<div class="sltwz">企业信息登记及CA申请表(一)</div>
			    	</div>
			    	<div class="col-xs-4">
			    		<div class="shilitu"><img src="qyList.do?method=getQyTp&qyId=${dataMap.QYID }&tpzd=SQB_2" alt=""></div>
				    	<div class="sltwz">企业信息登记及CA申请表(二)</div>
			    	</div>
			    	<div class="clearfix"></div>
				  </div>
				</div>

			  </div>
			</div>
		</div>
	</div>
	<!--footer-->
	<%@ include  file="/WEB-INF/pages/common/footer.jsp"%>
	

</body>
</html>	