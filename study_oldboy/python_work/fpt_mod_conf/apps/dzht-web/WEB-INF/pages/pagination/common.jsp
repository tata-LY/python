<%@ page language="java" import="java.util.*" pageEncoding="UTF-8"%>
<input type="hidden" name="pageCount" id="pageCount" value="${pageCount }"/>
<input type="hidden" name="total" id="total" value="${total }"/>
<input type="hidden" name="currentPage" id="currentPage" value="${ currentPage}"/>
<input type="hidden" name="isFirst" id="isFirst" value="${isFirst }"/>
<input type="hidden" name="isLast" id="isLast" value="${isLast }"/>
<div class="holder ifrm_footer">
	<c:choose>
		<c:when test="${isFirst eq true}">
			<a class="jp-first jp-disabled disabled" >首页</a>
			<a class="jp-previous jp-disabled disabled" >&lt;&lt;</a>
		</c:when>
		<c:otherwise>
			<a class="jp-first jp-disabled" onclick="page('first');">首页</a>
			<a class="jp-previous jp-disabled" onclick="page('pre');">&lt;&lt;</a>
		</c:otherwise>
	</c:choose>
	<a class="jp-current">${currentPage }</a>
	
	
	<c:choose>
		<c:when test="${isLast eq true}">
			<a class="jp-next jp-disabled disabled" >&gt;&gt;</a>
			<a class="jp-last jp-disabled disabled" >末页</a>
		</c:when>
		<c:otherwise>
			<a class="jp-next jp-disabled" onclick="page('next');">&gt;&gt;</a>
			<a class="jp-last jp-disabled" onclick="page('last')">末页</a>
		</c:otherwise>
	</c:choose>
	<a class="pages">共${pageCount }页,${total}条记录</a>
	<input class="tiaoye form-control" type="text" id="pagination_current_page">
	<input class="btn btn-danger" value="跳转" type="button" onclick="changeCurrentPage();">
</div>