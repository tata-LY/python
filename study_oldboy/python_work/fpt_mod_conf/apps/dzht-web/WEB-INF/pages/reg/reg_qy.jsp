<!DOCTYPE html>
<%@ page language="java" import="java.util.*" pageEncoding="UTF-8"%>
<html>
<head>
	<%@ include  file="/WEB-INF/pages/common/head.jsp"%>
	<title>电子合同-签大大</title>
	<link rel="stylesheet" href="<%=basePath %>css/pages.css">
	<link rel="stylesheet" href="<%=basePath %>css/zoomify.min.css">
	<!-- 新的上传插件 -->
	<script src="js/upload_common/upload_reg_qy.js"></script>
	<jsp:include page="/WEB-INF/pages/common/common_upload.jsp"></jsp:include>
	<script src="<%=basePath %>js/reg/reg_qy.js"></script>
	<script src="<%=basePath %>js/utils/validateIdCard.js"></script>
	<script src="<%=basePath %>js/css/zoomify.min.js"></script>
</head>
<body onload="chooseShowRegQy();">
	<!-- 头部 -->
	<jsp:include page="/WEB-INF/pages/common/head_top.jsp">
     <jsp:param value="999" name="top_menu_id"/>
   </jsp:include>
	<div class="addnew">
		<div class="container">
			<div class="lujing">
				<ul class="list-inline">
					<li>企业客户管理</li>
					<li>添加新企业客户</li>
				</ul>
			</div>
			<input type="hidden" name="randomReg"id="randomReg" value="${randomReg }"/>
			<input type="hidden" name="randomMobile" id="randomMobile" value="${randomMobile}"/>
			<input type="hidden" id="mobileYzmKey" name="mobileYzmKey" value="${mobileYzmKey}"/>
			<input type="hidden" name="jrfId"id="jrfId" value="${jrfId}"/>
			<input type="hidden" name="NeedToEditQyId"id="NeedToEditQyId" value="${NeedToEditQyId}"/>
			<input type="hidden" name="NeedToRegEditJrfId"id="NeedToRegEditJrfId" value="${NeedToRegEditJrfId}"/>
			<input type="hidden" name="hideDlrmc"id="hideDlrmc" value="${commonDataMapEdit.DLMC}"/>
			<input type="hidden" name="hideSzhy"id="hideSzhy" value="${commonDataMapEdit.SZHY}"/>
			
			<div class="panel panel-default">
			  <div class="panel-heading">
			    <h3 class="panel-title">添加新企业客户</h3>
			  </div>
			  <div class="panel-body">
			    <div class="form-horizontal">
			    	<div class="col-xs-6">
					  <div class="form-group">
					    <label class="col-xs-3 control-label">邮箱账号</label>
					    <div class="col-xs-9">
					    	<c:choose>
					    		<c:when test="${empty NeedToEditQyId}">
					    			 <input type="text" class="form-control" placeholder=""
								      id="zhmc" name="zhmc" value="${zhmc}"  maxlength=60
					        			onblur="value=value.replace(/[^0-9a-zA-Z@\.\-_]/g,'')"
								      >
					    		</c:when>
					    		<c:otherwise>
					    			${commonDataMapEdit.ZHMC }
					    		</c:otherwise>
					    	</c:choose>
					     
					    </div>
					  </div>
			    	</div>
			    	<div class="col-xs-6">
					  <div class="form-group">
					    <label class="col-xs-3 text-right control-label">企业名称</label>
					    <div class="col-xs-9">
					      <input type="text" class="form-control" placeholder=""
					      	id="qymc" name="qymc"  maxlength=60 value="${commonDataMapEdit.QYMC }"
					      	onKeyDown="maxLengthChg('300','qymc');" onKeyUp="maxLengthChg('300','qymc');"
					      >
					    </div>
					  </div>
			    	</div>
			    	<div class="col-xs-6">
					  <div class="form-group">
					    <label class="col-xs-3 control-label">企业类型</label>
					    <div class="col-xs-9">
					        <select class="form-control" name="qylx" id="qylx">
							  <option value="01" <c:if test="${commonDataMapEdit.QYLX eq '01'}">selected</c:if> >普通企业</option>
							  <option value="02" <c:if test="${commonDataMapEdit.QYLX eq '02'}">selected</c:if> >社会团体</option>
							  <option value="03" <c:if test="${commonDataMapEdit.QYLX eq '03'}">selected</c:if> >事业单位</option>
							  <option value="04" <c:if test="${commonDataMapEdit.QYLX eq '04'}">selected</c:if> >民办非企业</option>
							  <option value="05" <c:if test="${commonDataMapEdit.QYLX eq '05'}">selected</c:if> >党政及国家单位</option>
							</select>
					    </div>
					  </div>
			    	</div>
			    	<div class="col-xs-6">
					  <div class="form-group">
					    <label class="col-xs-3 text-right control-label">办公地址</label>
					    <div class="col-xs-9">
					      <input type="text" class="form-control" placeholder=""
					      	id="qydz" name="qydz"  value="${commonDataMapEdit.QYDZ}"
					      	onKeyDown="maxLengthChg('300','qydz');" onKeyUp="maxLengthChg('300','qydz');"
					      >
					    </div>
					  </div>
			    	</div>
			    	<div class="col-xs-6">
					  <div class="form-group">
					    <label class="col-xs-3 control-label">公司电话</label>
					    <div class="col-xs-9">
					      <input type="text" class="form-control" placeholder=""
					      id="dhhm" name="dhhm" maxlength=30 value="${commonDataMapEdit.DHHM }"
					      >
					    </div>
					  </div>
			    	</div>
			    	<div class="col-xs-6">
					  <div class="form-group">
					    <label class="col-xs-3 text-right control-label">所属地区</label>
					    <div class="col-xs-9">
					        <select class="form-control" name="qysf" id="qysf">
					        	<c:forEach var="bean" items="${areaList}">
					        	 	<option value="${bean.PROVINCE_NAME }" 
					        	 		 <c:if test="${commonDataMapEdit.QYSF eq bean.PROVINCE_NAME }">selected</c:if> 
					        	 		>
					        	 		${bean.PROVINCE_NAME }
					        	 	</option>
					        	</c:forEach>
							</select>
					    </div>
					  </div>
			    	</div>
					<div class="clearfix"></div>
				</div>

				<div class="col-xs-12 sanzhyi">
				  <!-- Nav tabs -->
				  <ul class="nav nav-tabs" role="tablist">
				    <li role="presentation" class="active" id="sanzheng_li">
				    	<a href="#sanzheng" aria-controls="sanzheng" role="tab" data-toggle="tab">三证</a>
				    </li>
				    <li role="presentation" id="sanzhenghy_li">
				    	<a href="#heyi" aria-controls="heyi" role="tab" data-toggle="tab">三证合一</a>
				    </li>
				  </ul>

				  <!-- Tab panes -->
				  <div class="tab-content">
				    <div role="tabpanel" class="tab-pane active" id="sanzheng">
				    	<div class="form-horizontal row">
					    	<div class="col-xs-6">
							  <div class="form-group">
							    <label class="col-xs-3 control-label">营业执照号</label>
							    <div class="col-xs-9">
							      <input type="text" class="form-control" placeholder=""
							      id="yyzz" name="yyzz" maxlength=30
							      	<c:if test="${commonDataMapEdit.SZHY eq '0'}"> value="${commonDataMapEdit.ZJHM}"</c:if>
							      >
							    </div>
							  </div>
					    	</div>
					    	<div class="col-xs-6">
							  <div class="form-group">
							    <label class="col-xs-3 control-label">组织机构代码证号</label>
							    <div class="col-xs-9">
							      <input type="text" class="form-control" placeholder=""
							       id="zzjgdm" name="zzjgdm" maxlength=50 value="${commonDataMapEdit.ZZJGDM }"
							      >
							    </div>
							  </div>
					    	</div>
					    	<div class="col-xs-6">
					    		<div class="col-xs-9 col-xs-offset-3">
						    		<div class="shilitu"><img src="<%=basePath %>images/shili_yyzz.jpg" alt=""></div>
						    		<div class="sltwz">营业执照示例图</div>
					    		</div>
					    	</div>
					    	<div class="col-xs-6">
					    		<div class="col-xs-9 col-xs-offset-3">
						    		<div class="shilitu"><img src="<%=basePath %>images/shili_zjjg.jpg" alt=""></div>
						    		<div class="sltwz">组织机构代码证书示例图</div>
					    		</div>
					    	</div>
					    	<div class="col-xs-6">
					    		<div class="col-xs-9 col-xs-offset-3">
						    		<div class="suoluetu shilitu"><img id="upload_YYZZ_SHOW" alt="" 
						    				<c:if test="${yyzzContentFlag eq '1'}">
												src="data:image/gif;base64,${yyzzContent}"
											</c:if>		
						    			/>
						    		</div>
						    		 <!-- 上传插件 -->
									<span class="smwenzi fileinput-button upload_show_hide" style="margin-top: 5px;">
							            <i class="glyphicon"></i>
							            <span>上传营业执照</span>
							            <input id="upload_YYZZ" type="file" name="upload_YYZZ">
							         </span>
									<!-- 上传插件 -->
					    		</div>
					    	</div>
					    	<div class="col-xs-6">
					    		<div class="col-xs-9 col-xs-offset-3">
						    		<div class="suoluetu shilitu"><img id="upload_ZZJGDM_SHOW" alt=""
						    				<c:if test="${zzjgdmContentFlag eq '1'}">
												src="data:image/gif;base64,${zzjgdmContent}"
											</c:if>	
						    			 />
						    		</div>
						    		 <!-- 上传插件 -->
									<span class="smwenzi fileinput-button upload_show_hide" style="margin-top: 5px;">
							            <i class="glyphicon"></i>
							            <span>上传组织机构代码证书</span>
							            <input id="upload_ZZJGDM" type="file" name="upload_ZZJGDM">
							         </span>
									<!-- 上传插件 -->
					    		</div>
					    	</div>
							<div class="clearfix"></div>
						</div>

				    </div>
				    <div role="tabpanel" class="tab-pane" id="heyi">
				    	<div class="form-horizontal row">
					    	<div class="col-xs-6">
							  <div class="form-group">
							    <label class="col-xs-3 control-label">统一社会信用代码</label>
							    <div class="col-xs-9">
							      <input type="text" class="form-control" placeholder=""
							      	id="tyshxy" name="tyshxy" maxlength=30
							      	<c:if test="${commonDataMapEdit.SZHY eq '1'}"> value="${commonDataMapEdit.ZJHM}"</c:if>
							      >
							    </div>
							  </div>
					    	</div>
							<div class="clearfix"></div>
					    	
					    	<div class="col-xs-12">
					    		<div class="text-center">
					    			<div class="shilitu"><img src="<%=basePath %>images/shili_sanz.jpg" alt=""></div>
						    		<div class="sltwz">营业执照示例图</div>
					    		</div>
					    		<div class="text-center">
						    		<div class="suoluetu shilitu"><img id="upload_TYSHXY_SHOW" alt="" 
						    				<c:if test="${tyshxyContentFlag eq '1'}">
												src="data:image/gif;base64,${tyshxyContent}"
											</c:if>	
						    			/>
						    		</div>
							    	 <!-- 上传插件  统一社会信用-->
									<span class="smwenzi fileinput-button upload_show_hide" style="margin-top: 5px;">
							            <i class="glyphicon"></i>
							            <span>上传营业执照</span>
							            <input id="upload_TYSHXY" type="file" name="upload_TYSHXY">
							         </span>
									<!-- 上传插件 -->
					    		</div>
					    	</div>
					    	
							<div class="clearfix"></div>
						</div>
				    </div>
				  </div>

				</div>
				<div class="clearfix"></div>
				<h4>签章操作人</h4>
				<div class="col-xs-12">
					<p class="text-tips">※ 用于合同签署时实际操作人，可选法人亲自操作或设置代理人代理操作。</p>
				</div>
				<div class="col-xs-12">
				  <!-- Nav tabs -->
				  <ul class="nav nav-tabs" role="tablist">
				    <li role="presentation" class="active" id="faren_a" onclick="showFrDlr('fr');">
				    	<a href="javascript:void(0);" aria-controls="faren" role="tab" data-toggle="tab" >法人</a>
				    </li>
				    <li role="presentation" id="dailiren_a" onclick="showFrDlr('dlr')">
				    	<a href="javascript:void(0);" aria-controls="dailiren" role="tab" data-toggle="tab" >代理人</a>
				    </li>
				  </ul>
				  <!-- Tab panes -->
				  <div class="tab-content">
				    <div role="tabpanel" class="tab-pane active">
				    	<div class="form-horizontal row">
					    	<div class="col-xs-6">
							  <div class="form-group">
							    <label class="col-xs-3 control-label">法人姓名</label>
							    <div class="col-xs-9">
							      <input type="text" class="form-control" placeholder=""
							      	id="frmc" name="frmc" value="${commonDataMapEdit.FRMC }"
					      			onKeyDown="maxLengthChg('60','frmc');" onKeyUp="maxLengthChg('60','frmc');"
							      >
							    </div>
							  </div>
					    	</div>
					    	<div class="col-xs-6">
							  <div class="form-group">
							    <label class="col-xs-3 control-label">法人身份证号</label>
							    <div class="col-xs-9">
							      <input type="text" class="form-control" placeholder=""
							      id="frsfz" name="frsfz" maxlength=30 value="${commonDataMapEdit.FRSFZ }"
							      >
							    </div>
							  </div>
					    	</div>
					    	<div id="show_dailiren_div" style="display:none">
						    	<div class="col-xs-6">
								  <div class="form-group">
								    <label class="col-xs-3 control-label">代理人姓名</label>
								    <div class="col-xs-9">
								      <input type="text" class="form-control" placeholder=""
								      	id="dlmc" name="dlmc" value="${commonDataMapEdit.DLMC }"
					      			onKeyDown="maxLengthChg('60','dlmc');" onKeyUp="maxLengthChg('60','dlmc');"
								      >
								    </div>
								  </div>
						    	</div>
						    	<div class="col-xs-6">
								  <div class="form-group">
								    <label class="col-xs-3 control-label">代理人身份证号</label>
								    <div class="col-xs-9">
								      <input type="text" class="form-control" placeholder=""
								       id="dlsfz" name="dlsfz" maxlength=30 value="${commonDataMapEdit.DLSFZ }"
								      >
								    </div>
								  </div>
						    	</div>
					    	</div>
							<div class="clearfix"></div>
						</div>
				    </div>
				  </div>

				  <div class="row">
				  	<div class="col-xs-4">
			    		<div class="shilitu"><img src="<%=basePath %>images/shili_sfz.jpg" alt=""></div>
				    	<div class="sltwz" id="frdlrslt_div">法人身份证示例图</div>
			    	</div>
			    	<div class="col-xs-4">
			    		<div class="shilitu"><img src="<%=basePath %>images/shili_ca.jpg" alt=""></div>
				    	<div class="sltwz">企业信息登记及CA申请表示例图(一)</div>
			    	</div>
			    	<div class="col-xs-4">
			    		<div class="shilitu"><img src="<%=basePath %>images/shili_dmhm.jpg" alt=""></div>
				    	<div class="sltwz">企业信息登记及CA申请表示例图(二)</div>
			    	</div>
			    	<div class="col-xs-4">
			    		<div class="suoluetu shilitu"><img id="upload_FRDLRSFZ_SHOW" alt="" 
			    				<c:if test="${sfzContentFlag eq '1'}">
												src="data:image/gif;base64,${sfzContent}"
								</c:if>	
			    			/>
			    		</div>
				    	 <!-- 上传插件 -->
						<span class="smwenzi fileinput-button upload_show_hide" style="margin-top: 5px;">
				            <i class="glyphicon"></i>
				            <span id="frdlrslt_span">上传法人身份证</span>
				            <input id="upload_FRDLRSFZ" type="file" name="upload_FRDLRSFZ">
				         </span>
						<!-- 上传插件 -->
			    	</div>
			    	<div class="col-xs-4">
				    	<div class="suoluetu shilitu"><img id="upload_SQB_1_SHOW" alt=""
					    		<c:if test="${sqb1ContentFlag eq '1'}">
												src="data:image/gif;base64,${sqb1Content}"
								</c:if>
				    		/>
				    	</div>
				    	 <!-- 上传插件 -->
						<span class="smwenzi fileinput-button upload_show_hide" style="margin-top: 5px;">
				            <i class="glyphicon"></i>
				            <span>上传企业信息登记及CA申请表(一)</span>
				            <input id="upload_SQB_1" type="file" name="upload_SQB_1">
				         </span>
						<!-- 上传插件 -->
			    	</div>
			    	<div class="col-xs-4">
			    		<div class="suoluetu shilitu"><img id="upload_SQB_2_SHOW" alt=""
			    				<c:if test="${sqb2ContentFlag eq '1'}">
											src="data:image/gif;base64,${sqb2Content}"
								</c:if>
			    			/>
			    		</div>
				    	 <!-- 上传插件 -->
						<span class="smwenzi fileinput-button upload_show_hide" style="margin-top: 5px;">
				            <i class="glyphicon"></i>
				            <span>上传企业信息登记及CA申请表(二)</span>
				            <input id="upload_SQB_2" type="file" name="upload_SQB_2">
				         </span>
						<!-- 上传插件 -->
			    	</div>
			    	<div class="col-xs-12 text-center cadown">
			    		<a href="javascript:void(0);" class="btn-link" onclick="downloadXxdj()">企业信息登记及CA申请表模板下载</a>
			    	</div>
			    	<div class="clearfix"></div>
			    	<div class="form-horizontal haomayz">
				    	<div class="col-xs-6">
						  <div class="form-group">
						    <label class="col-xs-3 control-label">手机号码</label>
						    <div class="col-xs-9">
						      <input type="text" class="form-control" placeholder=""
						       	id="sjhm" name="sjhm"  maxlength=11 value="${commonDataMapEdit.SJHM}"
		        				onblur="value=value.replace(/[^0-9]/g,'')"
						      >
						    </div>
						  </div>
				    	</div>
				    	<div class="col-xs-6">
						  <div class="form-group">
						    <label class="col-xs-3 control-label">手机验证码</label>
						    <div class="col-xs-5">
						      <input type="text" class="form-control" placeholder=""
						      	 	id="sjyzm" name="sjyzm" 
		        					onblur="value=value.replace(/[^0-9]/g,'')"
						      />
						    </div>
						    <div class="col-xs-4">
						    	<button type="button" class="btn btn-empty"  onclick="getMobileCode();"  name="yzmBut" id="yzmBut">发送验证码</button>
						    </div>
						  </div>
				    	</div>
						<div class="clearfix"></div>
					</div>
					<div class="col-xs-offset-4 col-xs-4 tijiao">
						<button type="button" class="btn btn-orange btn-full" onclick="regQySubmit();">提交</button>
					</div>
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