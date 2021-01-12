<!DOCTYPE html>
<%@ page language="java" import="java.util.*" pageEncoding="UTF-8"%>
<html>
<head>
<script>
		//这一截js必须放在jquery引用之前
		document.ready = function (callback) {
            ///兼容FF,Google
            if (document.addEventListener) {
                document.addEventListener('DOMContentLoaded', function () {
                    document.removeEventListener('DOMContentLoaded', arguments.callee, false);
                    callback();
                }, false)
            }
             //兼容IE
            else if (document.attachEvent) {
                document.attachEvent('onreadytstatechange', function () {
                      if (document.readyState == "complete") {
                                document.detachEvent("onreadystatechange", arguments.callee);
                                callback();
                       }
                })
            }
            else if (document.lastChild == document.body) {
                callback();
            }
        }

		window.onload = function () {
            // alert('onload');
        };
        document.ready(function () {
        	
			var jssor_1 = document.getElementById( "jssor_1" );
			var pdfimg = document.getElementById( "pdfimg" );
			var height = document.body.offsetHeight - 115;
			pdfimg.style.height = jssor_1.style.height = height + "px";
            // alert('ready');
        });

	</script>
	<%@ include  file="/WEB-INF/pages/common/head.jsp"%>
	<title>电子合同-签大大</title>
	<script src="<%=basePath %>js/css/vue.min.js"></script>
	
	<script src="<%=basePath %>js/css/jssor.slider-21.1.6.min.js"></script>
	<script src="<%=basePath %>js/css/jquery-ui.js"></script>
	<!-- jquery-ui在签署qianshu.js前面引用 -->
	<script src="<%=basePath %>js/css/qianshu.js"></script>
	<link rel="stylesheet" href="<%=basePath %>css/qianshu.css">
	<script src="<%=basePath %>js/qianshu/qs.js"></script>

	
	
	
	
</head>
<body onload="buqueDiv()">
	<input type="hidden" name="htys" id="htys" value="${htys}"/>
	<input type="hidden" name="htId" id="htId" value="${htId}"/>
	<input type="hidden" name="buqueys" id="buqueys" value="${buqueys}"/>
	<input type="hidden" name="buqueFlag" id="buqueFlag" value="${buqueFlag}"/>
	<input type="hidden" name="randomMobile" id="randomMobile" value="${randomMobile}"/>
	<input type="hidden" id="mobileYzmKey" name="mobileYzmKey" value="${mobileYzmKey}"/>
	<input type="hidden" id="mobile" name="mobile" value="${commonDataMap.SJHM}"/>
	<!-- 头部 -->
	<div class="top_nav">
		<div class="container">
			<div class="row">
				<div class="col-xs-2">
				<!-- 
					<img src="<%=basePath %>images/dsf_logo.png" alt="">
				 -->
				</div>
				<div class="col-xs-8"><h3>个人材料自助提交系统</h3></div>
				<div class="col-xs-2 text-right">
					<a  href="<c:url value='/index.do?method=index'/>"><img src="<%=basePath %>images/dzht_logo.png" alt=""></a>
				 -->d
				</div>
			</div>
		</div>
	</div>
	<!-- 合同信息 -->
	<div class="container">
		<div class="row">
			<div class="col-xs-9 ht_name">
				<div class="col-xs-8 text-left"><span class="text-muted">合同名称：</span>${htDataMap.HTMC}</div>
				<div class="col-xs-4 text-right"><span class="text-muted">发件人：</span>${htDataMap.JRFMC}</div>
			</div>
			<div class="clearfix"></div>
		</div>
	</div>
	<div class="ht_main container"  style="padding-left: 0px; padding-right: 0px;">
		<div class="row jssor_1" id="jssor_1" style="position: relative; margin: 0 auto; top: 0px; left: 0px; width: 1170px; height: 588px; overflow: hidden; visibility: hidden; background-color: #ececec;">
			<!-- Loading Screen -->
			<div data-u="loading" style="position: absolute; top: 0px; left: 0px;">
				<div style="filter: alpha(opacity=70); opacity: 0.7; position: absolute; display: block; top: 0px; left: 0px; width: 100%; height: 100%;"></div>
				<div style="position:absolute;display:block;background:url('<%=basePath %>images/qianshu/loading.gif') no-repeat center center;top:0px;left:0px;width:100%;height:100%;"></div>
			</div>

			<!-- left -->
			<div class="col-xs-9 ht_neirong">
				<div data-u="slides" id="pdfimg" class="pdfimg" style="cursor: default; position: relative; top: 0px; left: 0px; width: 877px; height: 588px; overflow: hidden;">
					<c:forEach  var="bean" begin="1" end="${buqueys}" step="1">
						<div data-p="150.00" style="display: none;" >
							<div class="current">
								<c:choose>
									<c:when test="${buqueFlag eq '1' && bean eq buqueys}">
										<img src="<%=basePath %>images/qianshu/blank.png" data-u="image" data-nodrag="true" name="leftpage_${bean}"/>
									</c:when>
									<c:otherwise>
										<img src="com.do?method=getHtTp&htId=${htId}&tps=${bean}" data-u="image" data-nodrag="true" name="leftpage_${bean}"/>
									</c:otherwise>
								</c:choose>
							
							</div>
							<div data-u="thumb" onclick="changePageIndex('${bean}')" >
								<c:choose>
									<c:when test="${buqueFlag eq '1' && bean eq buqueys}">
										<img src="<%=basePath %>images/qianshu/blank.png"  />
									</c:when>
									<c:otherwise>
										<img src="com.do?method=getHtTp&htId=${htId}&tps=${bean}"  />
									</c:otherwise>
								</c:choose>							
								<span name="spanDiv_${bean}">${bean}</span>
							</div>
						</div>
					</c:forEach>
				</div>
			</div>
			<!-- right -->
			<div class="col-xs-3 ht_right">
				<div class="ht_sfqz">
					<div class="ht_qz">
						<h5>签章样式</h5>
						<div class="htqz">
							<img src="qianshu.do?method=getQzTp" alt="">
						</div>
					</div>
					<div class="ht_sf disnone">
						<h5>身份验证</h5>
						<p class="text-muted">
							验证码将会发送至预留手机：
							${ fn:substring( commonDataMap.SJHM ,0,3)}****${ fn:substring( commonDataMap.SJHM ,7,11)}
						</p>
						<div class="col-xs-12">
						  <div class="col-xs-6" name="qsYzmInputDiv">
						    <input type="text" class="form-control input-sm" placeholder="" id="sjyzmQs" name="sjyzmQs" maxlength=6>
						  </div>
						  <div class="col-xs-6" name="qsYzmButDiv""><button type="button" class="btn btn-empty btn-sm" name="yzmBut" onclick="getMobileCodeQs();">发验证码</button></div>
						</div>
						<a href="javascript:;" class="btn btn-orange">继续签名</a>
					</div>
				</div>
				<div class="ht_yeqian">
					<div class="yeshu" id="pagesum">
						<span class="page-sum">
							<input type="text" onkeyup="limitInput('${buqueys}',this);" value="1" id="pageIndex"/>
						 	/ 
							 <strong class="allPage">${buqueys}</strong>页
						</span>
				        <a href="javascript:;" class="page-btn btn btn-empty btn-xs">GO</a>
					</div>
					<!-- Thumbnail Navigator -->
					<div data-u="thumbnavigator" class="jssort01-99-66" data-autocenter="2" style="position:absolute;right:0px;top:340px;width:277px;height:380px;" >
						<!-- Thumbnail Item Skin Begin -->
						<div data-u="slides" style="cursor: default;">
							<div data-u="prototype" class="p">
								<div class="w">
									<div data-u="thumbnailtemplate" class="t"></div>
								</div>
								<div class="c"></div>
							</div>
						</div>
						<!-- Thumbnail Item Skin End -->
					</div>
				</div>
			</div>
			
			<!-- Arrow Navigator -->
			<span data-u="arrowleft" class="jssora05l" data-autocenter="2" style="top:0px;left:0px;width:37px;height:68px;"></span>
			<span data-u="arrowright" class="jssora05r" data-autocenter="2" style="top:0px;right: 25%;width:37px;height:68px;"></span>
		</div>
		<!-- #endregion Jssor Slider End -->
	</div>
<!--footer-->
	<%@ include  file="/WEB-INF/pages/common/footer.jsp"%>
	
	<!--签署成功后的弹框提示 -->
	<div class="modal fade bs-example-modal-sm" tabindex="-1" role="dialog" aria-labelledby="mySmallModalLabel" id="qs_success" > 
	  <div class="modal-dialog modal-sm" role="document" style="margin-top: 130px;" >
	    <div class="modal-content" style="padding: 30px 0 20px;" >
	      <div class="text-center">
	      	<img src="<%=basePath %>images/success.png" alt="">
	      	<p style="margin-top: 5px;">合同签署成功</p>
	      	<button type="button" class="btn btn-orange" onclick="qsSuccess();" style="margin-top: 20px;" >确认</button>
	      </div>
	    </div>
	  </div>
	</div>
</body>
</html>