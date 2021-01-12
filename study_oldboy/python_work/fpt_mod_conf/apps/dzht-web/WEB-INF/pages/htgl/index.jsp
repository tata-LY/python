<!DOCTYPE html>
<%@ page language="java" import="java.util.*" pageEncoding="UTF-8"%>
<html>
<head>
    <%@ include  file="/WEB-INF/pages/common/head.jsp"%>
    <!-- end head.html -->
    <title>电子合同-签大大</title>
    <link rel="stylesheet" href="<%=basePath %>css/pages.css">
    <link rel="stylesheet" href="<%=basePath %>css/bootstrap-datetimepicker.css">
    <script src="<%=basePath %>js/bootstrap-datetimepicker.js"></script>
    <script src="<%=basePath %>js/bootstrap-datetimepicker.zh-CN.js"></script>
    <script src="<%=basePath %>js/common.js"></script>
    <script src="<%=basePath %>js/paginator.js"></script>
    <script src="<%=basePath %>js/htgl/htgl.js"></script>
</head>
<body>
<!-- 头部 -->
	<jsp:include page="/WEB-INF/pages/common/head_top.jsp">
     	<jsp:param value="5" name="top_menu_id"/>
   </jsp:include>
<!-- banner -->
<div id="carousel-example-generic" class="carousel slide" data-ride="carousel">
    <!-- Wrapper for slides -->
    <div class="carousel-inner" role="listbox">
        <div class="item active">
            <img src="<%=basePath %>images/banner_guanli.jpg" alt="">
        </div>
    </div>
</div>
<!-- 全部文件 -->
<div class="hetong">
    <div class="container">
        <h3>全部文件</h3>
        <div class="search ">
            <form action="" class="form-inline search-form">
            <div class="form-inline">
                <div class="form-group">
                    <label class="sr-only">合同名称/合同编号</label>
                    <input type="text" class="form-control" placeholder="合同名称/合同编号" name="HTMC">
                </div>
                <div class="form-group">
                    <label>合同发起时间：</label>
                    <input type="data" class="form-control" placeholder="" name="beginDate" id="beginDate">
                    -
                    <input type="data" class="form-control" placeholder="" name="endDate" id="endDate">

                </div>
                <div class="form-group">
                    <button type="button" class="btn btn-moren" onclick="bthChangeDate(1)">一周内</button>
                    <button type="button" class="btn btn-default" onclick="bthChangeDate(2)">一月内</button>
                </div>
                <div class="form-group">
                    <button type="button" class="btn btn-orange" onclick="searchForm()">搜索</button>
                </div>
            </div>
            </form>
        </div>
        <div class="biaoge" id="contentk">
            <table class="table table-striped table-condensed">
                <thead>
                <tr>
                    <th>合同编号</th>
                    <th>文件名称</th>
                    <th>发件人</th>
                    <th>发起时间</th>
                    <th>签署状态</th>
                    <th class="text-right">操作</th>
                </tr>
                </thead>
                <tbody  id="itembox">
                </tbody>
            </table>
        </div>
    </div>

    <!-- 拒签 -->
    <div class="modal fade bs-example-modal-sm" id="juqian" tabindex="-1" role="dialog" aria-labelledby="mySmallModalLabel">
        <div class="modal-dialog modal-sm" role="document">
            <div class="modal-content">
                <form class="juqian-modal">
                <div class="modal-header">
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                    <h4 class="modal-title" id="myModalLabel">请填写拒签理由</h4>
                    <input type="hidden"  id="htId"/>
                    <input type="hidden"  id="htBh"/>
                </div>
                <div class="modal-body">
                    <textarea class="form-control modal-jqyy" rows="5" maxlength="120" placeholder="请填写拒签理由"></textarea>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-empty" data-dismiss="modal">取消</button>
                    <button type="button" class="btn btn-orange"  onclick="jqsubmit();">提交</button>
                </div>
                </form>
            </div>
        </div>
    </div>

</div>
<!--footer-->
<%@ include  file="/WEB-INF/pages/common/footer.jsp"%>


</body>
</html>