function page(obj){
	var currentPage=$("#currentPage").val();
	if(obj == "next"){
		currentPage++;
	}else if(obj == "pre"){
		currentPage--;
	}else if(obj == "first"){
		currentPage=1;
	}else if(obj == "last"){
		var pageCount=$("#pageCount").val();
		currentPage=pageCount;
	}
	$("#currentPage").val(currentPage);
	$("#forms").submit();
}
function changePageSize(){
	$("#currentPage").val(1);
	$("#forms").submit();
}

function changeCurrentPage(){
	var toPage = $("#pagination_current_page").val();
	var pageCount = $("#pageCount").val();
	if(toPage==""){
		alertMsg("页码不能为空");
		return false;
	}
	if(!isNumber(toPage)){
		alertMsg("请输入正确的页码");
		return false;
	}
	if(parseInt(toPage)<=0 || parseInt(toPage)>parseInt(pageCount)){
		alertMsg("页码输入有误，请重新输入");
		return false;
	}
	$("#currentPage").val(parseInt(toPage));
	$("#forms").submit();
}