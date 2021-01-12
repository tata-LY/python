<%@ page language="java" import="java.util.*" pageEncoding="UTF-8"%>
<link href="jquery_file_upload/css/jquery.fileupload-ui.css" rel="stylesheet" />  
<link href="jquery_file_upload/css/jquery.fileupload.css" rel="stylesheet" />  
<script src="jquery_file_upload/js/vendor/jquery.ui.widget.js"></script>
<script src="jquery_file_upload/js/jquery.fileupload.js"></script>
<script src="jquery_file_upload/js/jquery.fileupload-process.js"></script>
<script src="jquery_file_upload/js/jquery.fileupload-validate.js"></script>

<!-- 进度条 -->
  <div class="abcdefg" style="display: none;z-index: 99999;position: fixed;top: 0px;left: 0px;width: 100%;background-color: rgba(0,0,0,0.7);height: 100%;text-align: center;">
	<div class="progress progress-striped active" role="progressbar" 
	 aria-valuemin="0" aria-valuemax="100" aria-valuenow="0" style="position: relative;top: 200px;width: 50%;left: 25%;">
		<div class="progress-bar progress-bar-warning" style="width:0%;"></div>
	</div>
      </div>