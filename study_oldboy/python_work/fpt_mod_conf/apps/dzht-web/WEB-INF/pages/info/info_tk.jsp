<%@ page language="java" import="java.util.*" pageEncoding="UTF-8"%>
<!-- 设置密码 起-->
	<div style="display:none" class="modal fade bs-example-modal-sm" id="shezhimima" tabindex="-1" role="dialog" aria-labelledby="mySmallModalLabel" data-backdrop="static">
	  <div class="modal-dialog modal-sm" role="document">
	    <div class="modal-content">
	      <div class="modal-header">
	        <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
	        <h4 class="modal-title" id="myModalLabel">设置密码</h4>
	      </div>
	      <div class="modal-body">
	        <div class="form-horizontal">
			  <div class="form-group">
			    <label class="col-xs-3 control-label">密码</label>
			    <div class="col-xs-8">
			      <input type="password" class="form-control" placeholder="" 
			      id="passwd" name="passwd" onfocus="clearmsgHideName('errormsg');">
			    </div>
			  </div>
				<!-- 引入密码公用样式 -->
				  <div class="form-group">
				 	<div class="col-xs-offset-4 col-xs-8">
				 		<%@ include  file="/WEB-INF/pages/common/pwd.jsp"%>
				   </div>
				   <div class="clearfix"></div>
				 </div>
			  <div class="form-group">
			    <label class="col-xs-3 control-label">确认密码</label>
			    <div class="col-xs-8">
			      <input type="password" class="form-control" placeholder="" 
			      id="passwd2" name="passwd2" onfocus="clearmsgHideName('errormsg');">
			    </div>
			  </div>
			  <div class="text-error" name="errormsg_mm" style="display:none">${errormsg}</div>
			  <div class="form-group">
			    <div class="col-xs-offset-3 col-xs-8">
			      <button type="submit" class="btn btn-orange" onclick="setPasswd();">提交</button>
			    </div>
			  </div>
			</div>
	      </div>
	    </div>
	  </div>
	</div>
<!-- 设置密码 止-->

<!-- 修改密码 起-->
	<div class="modal fade bs-example-modal-sm" id="mima" tabindex="-1" role="dialog" aria-labelledby="mySmallModalLabel">
	  <div class="modal-dialog modal-sm" role="document">
	    <div class="modal-content">
	      <div class="modal-header">
	        <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
	        <h4 class="modal-title" id="myModalLabel">修改密码</h4>
	      </div>
	      <div class="modal-body">
	        <div class="form-horizontal">
			  <div class="form-group">
			    <label class="col-xs-3 control-label">原密码</label>
			    <div class="col-xs-8">
			      <input type="password" class="form-control" placeholder="" id="mm_oldpass" onfocus="clearmsgHideName('errormsg');">
			    </div>
			  </div>
			  <div class="form-group">
			    <label class="col-xs-3 control-label">新密码</label>
			    <div class="col-xs-8">
			      <input type="password" class="form-control" placeholder="" maxlength=16
			      id="mm_passwd" name="mm_passwd" onfocus="clearmsgHide('errormsg');">
			    </div>
			  </div>
				<!-- 引入密码公用样式 -->
				<div class="form-group">
				 	<div class="col-xs-offset-4 col-xs-8">
				 		<%@ include  file="/WEB-INF/pages/common/pwd.jsp"%>
				   </div>
				   <div class="clearfix"></div>
				 </div>
			  <div class="form-group">
			    <label class="col-xs-3 control-label">确认密码</label>
			    <div class="col-xs-8">
			      <input type="password" class="form-control" placeholder="" 
			      id="mm_passwd2" name="mm_passwd2" onfocus="clearmsgHide('errormsg');">
			    </div>
			  </div>
			  <div class="text-error" name="errormsg_mm" style="display:none">${errormsg}</div>
			  <div class="form-group">
			    <div class="col-xs-offset-3 col-xs-8">
			      <button type="submit" class="btn btn-orange" onclick="updatePasswd();">提交</button>
			    </div>
			  </div>
			</div>
	      </div>
	    </div>
	  </div>
	</div>
<!-- 修改密码 止-->

<!-- 修改手机号 起-->
	<div class="modal fade bs-example-modal-sm" id="shoujihao" tabindex="-1" role="dialog" aria-labelledby="mySmallModalLabel">
	  <div class="modal-dialog modal-sm" role="document">
	    <div class="modal-content">
	      <div class="modal-header">
	        <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
	        <h4 class="modal-title" id="myModalLabel">修改手机号</h4>
	      </div>
	      <div class="modal-body">
	        <div class="form-horizontal">
			  <div class="form-group">
			    <label class="col-xs-3 control-label">新手机号</label>
			    <div class="col-xs-9">
			      <input type="text" class="form-control" placeholder=""
			       id="sjhm" name="sjhm" value="${sjhm}" onfocus="clearmsgHideName('errormsg');" maxlength=11
		        		onblur="value=value.replace(/[^0-9]/g,'')"
			      >
			    </div>
			  </div>
			  <div class="form-group">
			    <label class="col-xs-3 control-label">验证码</label>
			    <div class="col-xs-3" style="padding-right:0px;">
			      <input type="text" class="form-control" style="padding-right:6px 3px;" placeholder=""
			      id="sjyzm" name="sjyzm" onfocus="clearmsgHideName('errormsg');"
		        		onblur="value=value.replace(/[^0-9]/g,'')"
			      >
			    </div>
			    <div class="col-xs-6" style="padding: 0px 15px 0px 5px;">
			      <button type="button" class="btn btn-empty btn-full" style="padding: 6px;" onclick="getCode('1');" name="yzmBut">发送验证码</button>
			    	
			    </div>
			  </div>
			  <div class="text-tips"> ※ 验证码将发送至新手机进行验证</div>
			  <div class="text-error" name="errormsg_sjh" style="display:none">${errormsg}</div>
			  <div class="form-group">
			    <div class="col-xs-offset-3 col-xs-8">
			      <button type="submit" class="btn btn-orange" onclick="sjhmChange();">提交</button>
			    </div>
			  </div>
			</div>
	      </div>
	    </div>
	  </div>
	</div>
<!-- 修改手机号 止-->


<!-- 修改邮箱号 起-->
	<div class="modal fade bs-example-modal-sm" id="email" tabindex="-1" role="dialog" aria-labelledby="mySmallModalLabel">
	  <div class="modal-dialog modal-sm" role="document">
	    <div class="modal-content">
	      <div class="modal-header">
	        <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
	        <h4 class="modal-title" id="myModalLabel">修改邮箱号</h4>
	      </div>
	      <div class="modal-body">
	        <div class="form-horizontal">
			  <div class="form-group">
			    <label class="col-xs-3 control-label">新邮箱号</label>
			    <div class="col-xs-9">
			      <input type="email" class="form-control" placeholder=""
			       id="zhmc" name="zhmc" value="${zhmc}" onfocus="clearmsgHideName('errormsg');" maxlength=60
			      >
			    </div>
			  </div>
			 <div class="form-group">
			    <label class="col-xs-3 control-label">验证码</label>
   			    <div class="col-xs-3" style="padding-right:0px;">
			      <input type="text" class="form-control" style="padding-right:6px 3px;" placeholder=""
			      id="yxyzm" name="yxyzm" onfocus="clearmsgHideName('errormsg');"
		        		onblur="value=value.replace(/[^0-9]/g,'')"
			      >
			    </div>
			    <div class="col-xs-6" style="padding: 0px 15px 0px 5px;">
			      <button type="button" class="btn btn-empty btn-full" style="padding: 6px;" onclick="getCode('2');" name="yzmBut">发送验证码</button>
			    </div>
			  </div>
			  <div class="text-tips"> ※ 邮箱变更后，后续需使用新邮箱地址作为本账户登录名。</div>
			  <div class="text-error" name="errormsg_yxh" style="display:none">${errormsg}</div>
			  <div class="form-group">
			    <div class="col-xs-offset-3 col-xs-8">
			      <button type="submit" class="btn btn-orange" onclick="zhmcChange();">提交</button>
			    </div>
			  </div>
			</div>
	      </div>
	    </div>
	  </div>
	</div>
<!-- 修改邮箱号 止-->



	<!-- 邮箱修改成功后的弹框提示 -->
	<div class="modal fade bs-example-modal-sm" tabindex="-1" role="dialog" aria-labelledby="mySmallModalLabel" id="email_change_success"> 
	  <div class="modal-dialog modal-sm" role="document">
	    <div class="modal-content">
	      <div class="text-center">
	      	<img src="<%=basePath %>images/success.png" alt="">
	      	<p>邮箱修改成功，请重新登录</p>
	      	<button type="button" class="btn btn-orange" onclick="emailChangeSuccess();">确认</button>
	      </div>
	    </div>
	  </div>
	</div>

	<!-- 手机号码修改成功后的弹框提示 -->
	<div class="modal fade bs-example-modal-sm" tabindex="-1" role="dialog" aria-labelledby="mySmallModalLabel" id="sjhm_change_success"> 
	  <div class="modal-dialog modal-sm" role="document">
	    <div class="modal-content">
	      <div class="text-center">
	      	<img src="<%=basePath %>images/success.png" alt="">
	      	<p>手机号码修改成功</p>
	      	<button type="button" class="btn btn-orange" onclick="sjhmChangeSuccess();">确认</button>
	      </div>
	    </div>
	  </div>
	</div>