$(function(){

    $('#beginDate').datetimepicker({
        format: "yyyy-mm-dd",
        minView: "month",
        autoclose: true,
        language: "zh-CN"
    });

    $('#endDate').datetimepicker({
        format: "yyyy-mm-dd",
        minView: "month",
        autoclose: true,
        language: "zh-CN"
    });


    var options = {
          pageUrl: baseUrl + '/htgl.do?method=list',
          searchClass : 'search-form' ,
          buildTable : function (data,$element) {
              $element.find('tbody').children().remove();
              $element.children(":gt(0)").remove();
              for(var i=0;i<data.length;i++){
                  var item =  data[i] , html=[];
                  html.push('<tr class="htid'+item.HTID+'">');
                  html.push('<td>'+item.HTBH+'</td>') ;
                  html.push('<td>'+item.HTMC+'</td>') ;
                  html.push('<td>'+item.JRFMC+'</td>') ;
                  html.push('<td>'+item.HTRQ+'</td>') ;
                  var htzt ;
                  var qszt = item.QSZT;//签署状态，针对具体某个客户
                  switch (item.HTZT){
                      case '01' :
                          htzt = '未签署';
                          break;
                      case '02' :
                          htzt = '待签署完成';
                          break;
                      case '03' :
                          htzt = '已撤销';
                          break;
                      case '04' :
                          htzt = '已拒签';
                          break;
                      case '05' :
                          htzt = '已归档';
                          break;
                      default :
                          htzt = '';
                  }
                  if((item.HTZT == "01" || item.HTZT == "02") && "01"==qszt){
                      html.push('<td><span class="btn-link"><input type="hidden" value=\"'+item.HTZT+'\">'+htzt+'</span></td>') ;
                      html.push('<td class="text-right">');
                      html.push('<a href="qianshu.do?method=qs&htId='+item.HTID+'" class="btn btn-orange btn-xs" target="_blank">签署</a> ');
                      html.push('<a href="###" class="btn btn-empty btn-xs" data-toggle="modal" data-htid =\"'+item.HTID+'\" data-htbh=\"'+item.HTBH+'\" onclick="juqian(this)" data-target="#juqian">拒签</a>');
                  }else{
                      html.push('<td><span><input type="hidden" value=\"'+item.HTZT+'\">'+htzt+'</span></td>') ;
                      html.push('<td class="text-right">');
                  }
                  html.push('<a href="javascript:;" class="gaikuang glyphicon glyphicon-chevron-down" aria-hidden="true" ht-id="'+item.HTID+'" onclick="preView(this)"></a>');
                  html.push('<a href="htgl.do?method=htView&htId='+item.HTID+'" class="chakan" data-toggle="tooltip" data-placement="bottom" title="查看合同" target="_blank"><span class="glyphicon glyphicon-eye-open" aria-hidden="true"></span></a>');
                  html.push('<a href="###" class="download" data-toggle="tooltip" data-placement="bottom" title="下载合同" ht-id="'+item.HTID+'" onclick="downloadZip(this)"><span class="glyphicon glyphicon-download-alt" aria-hidden="true"></span></a>');
                  html.push('</td>');
                  html.push('</tr>');
                  var itemContent = $(html.join(''));
                  itemContent.data("data",item);
                  $element.find("tbody").append(itemContent);
              }
              $element.append('<div class="clearfix"></div>');
          }
    };
    $("#contentk").bootstrapPaginator(options);

});

function searchForm(){
    $("#contentk").data("bootstrapPaginator").pageChange(1);
}



function bthChangeDate(changeStatu){

    //changeStatu : 1 / 2

    if(!$('#endDate').val()){
        $('#endDate').datetimepicker('setDate',new Date());
    }
    //一周内
    if(changeStatu == 1) {
        $('#beginDate').val( new Date(changeDate( $('#endDate').datetimepicker('getDate'),-7)).Format("yyyy-MM-dd"));
    }
    //一月内
    if(changeStatu == 2) {
        $('#beginDate').val( new Date(changeMonth( $('#endDate').datetimepicker('getDate'),-1)).Format("yyyy-MM-dd"));
    }
}

function changeDate(date,days){
    var d = new Date(date) ;
    d.setDate(d.getDate()+ days);
    var m =  d.getMonth() + 1 ;
    return  d.getFullYear() + '-'+ m + '-' + d.getDate() ;
}

function changeMonth(date,months){
    var d = new Date(date) ;
    d.setMonth(d.getMonth() +  months   ) ;
    return  d.getFullYear() + '-'+ (parseInt(d.getMonth())+ parseInt(1)) + '-' + d.getDate() ;
}

function preView (obj){
    //第一次点击展开 获取css 为undefined  第2次进来的时候就 有了class disnone  点击展开的时候 remove   点击关闭的时候 add
    var htid = $(obj).attr("ht-id");
    var $this = $(obj);
    var gaikuang =  $this.parent().parent().next(".qs_gaikuang");
    if(gaikuang.css("display")==undefined){
        $(obj).removeClass("glyphicon-chevron-down").addClass("glyphicon-chevron-up");
    }else if(gaikuang.css("display")=="none"){
        $(obj).removeClass("glyphicon-chevron-down").addClass("glyphicon-chevron-up");
        gaikuang.removeClass("disnone");
        return ;
    } else{
        $(obj).removeClass("glyphicon-chevron-up").addClass("glyphicon-chevron-down");
        gaikuang.addClass("disnone");
        return ;
    }
    if(!htid) return ;
    var params ={"HTID":htid};
    postData(baseUrl + "/htgl.do?method=getHtqsr",params,successCallBack,commonErrorCallBack,true) ;
}

function successCallBack(resp){
    var data = getResult(resp);
    if(!data)  return ;
    var html = [],htid;
    html.push('<tr class="qs_gaikuang ">');
    html.push('<td colspan="6">');
    html.push('<table class="table table-condensed">');
    html.push('<thead>');
    html.push('<tr>');
    html.push('<th>签署人</th>');
    html.push('<th>邮箱</th>');
    html.push('<th>签署时间</th>');
    html.push('<th>签署状态</th>');
    html.push('</tr>');
    html.push('</thead>');
    html.push('<tbody>');
    for(var i = 0;i< data.length ;i++){
        var item ;
        if(typeof(data[i])=='object'){
            item = data[i] ;
        } else {
            item = JSON.parse(data[i]);
        }
        if(item){
            var qszt ;
            htid = item.HTID ;
            html.push('<tr>');
            html.push('<td>'+item.YHMC+'</td>');
            html.push('<td>'+item.ZHMC+'</td>');
            html.push('<td>'+ replaceNull2String(item.QSRQ)+'</td>');
            if(item.QSZT=='01'){
                qszt = '待签' ;
            }else if(item.QSZT=='02'){
                qszt = '拒签' ;
            }else if(item.QSZT=='03'){
                qszt = '已签' ;
            }else{
                qszt = '';
            }
            html.push('<td>'+qszt+'</td>');
            html.push('</tr>');
        }
    }
    //==========拒签理由 ======================
    html.push('<tr>');
    html.push('<th>拒签理由</th>')
    html.push('<td colspan="3">');
    html.push('<p class="text-left text-danger">'+replaceNull2String($(".table-condensed .htid"+htid).data("data").JQYY)+'</p>');
    html.push('</td>');
    html.push('</tr>');

    html.push('</tbody>');
    html.push('</table>');
    html.push('</td>');
    html.push('</tr>');
    $(".table-condensed .htid"+htid).after($(html.join('')));
}

function juqian(obj) {
        var $this =  $(obj) ;
        var htId  =  $this.attr('data-htid');
        var htBh  =  $this.attr('data-htbh');
        $('.juqian-modal').find('#htId').val(htId);
        $('.juqian-modal').find('#htBh').val(htBh);
}

function jqsubmit(){
    var jqyy = $('.juqian-modal').find('.modal-jqyy').val();
    if(!jqyy){
        tip("请输入拒签理由!");
        return ;
    }
    if(window.confirm("确定要拒签吗?")){
        var htId = $('.juqian-modal').find('#htId').val();
        var htBh =  $('.juqian-modal').find('#htBh').val();
        var params = {"HTID":htId,"HTBH" : htBh,"JQYY" : jqyy} ;
        postData( baseUrl + '/htgl.do?method=juqian',params,jqSuccessCallBack,commonErrorCallBack) ;
    }
}

function jqSuccessCallBack (resp) {
    var data = getResult(resp) ;
    if(!data) return ;
    tip("拒签成功!") ;
    $("#juqian").modal("hide");
    $("#contentk").data("bootstrapPaginator").pageChange(1);
}

function downloadZip(obj){
    var $this =  $(obj) ;
    var htId =  $this.attr('ht-id');
    var params = {"htId" : htId } ;
  //  postData( baseUrl + '/htgl.do?method=downloadPdf',params,commonSuccessCallBack,commonErrorCallBack) ;
    postForm(baseUrl + '/htgl.do?method=downloadPdf',params) ;
}

function replaceNull2String(obj){
    if(!obj)return '' ;
    else return obj ;
}