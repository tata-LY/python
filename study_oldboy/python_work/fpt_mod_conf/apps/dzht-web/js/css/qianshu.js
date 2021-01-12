//加载jquery
jQuery(document).ready(function ($) {

	var jssor_1_SlideshowTransitions = [
	  {$Duration:1200,$Zoom:1,$Easing:{$Zoom:$Jease$.$InCubic,$Opacity:$Jease$.$OutQuad},$Opacity:2},
	  {$Duration:1000,$Zoom:11,$SlideOut:true,$Easing:{$Zoom:$Jease$.$InExpo,$Opacity:$Jease$.$Linear},$Opacity:2},
	  {$Duration:1200,$Zoom:1,$Rotate:1,$During:{$Zoom:[0.2,0.8],$Rotate:[0.2,0.8]},$Easing:{$Zoom:$Jease$.$Swing,$Opacity:$Jease$.$Linear,$Rotate:$Jease$.$Swing},$Opacity:2,$Round:{$Rotate:0.5}},
	  {$Duration:1000,$Zoom:11,$Rotate:1,$SlideOut:true,$Easing:{$Zoom:$Jease$.$InExpo,$Opacity:$Jease$.$Linear,$Rotate:$Jease$.$InExpo},$Opacity:2,$Round:{$Rotate:0.8}},
	  {$Duration:1200,x:0.5,$Cols:2,$Zoom:1,$Assembly:2049,$ChessMode:{$Column:15},$Easing:{$Left:$Jease$.$InCubic,$Zoom:$Jease$.$InCubic,$Opacity:$Jease$.$Linear},$Opacity:2},
	  {$Duration:1200,x:4,$Cols:2,$Zoom:11,$SlideOut:true,$Assembly:2049,$ChessMode:{$Column:15},$Easing:{$Left:$Jease$.$InExpo,$Zoom:$Jease$.$InExpo,$Opacity:$Jease$.$Linear},$Opacity:2},
	  {$Duration:1200,x:0.6,$Zoom:1,$Rotate:1,$During:{$Left:[0.2,0.8],$Zoom:[0.2,0.8],$Rotate:[0.2,0.8]},$Easing:{$Left:$Jease$.$Swing,$Zoom:$Jease$.$Swing,$Opacity:$Jease$.$Linear,$Rotate:$Jease$.$Swing},$Opacity:2,$Round:{$Rotate:0.5}},
	  {$Duration:1000,x:-4,$Zoom:11,$Rotate:1,$SlideOut:true,$Easing:{$Left:$Jease$.$InExpo,$Zoom:$Jease$.$InExpo,$Opacity:$Jease$.$Linear,$Rotate:$Jease$.$InExpo},$Opacity:2,$Round:{$Rotate:0.8}},
	  {$Duration:1200,x:-0.6,$Zoom:1,$Rotate:1,$During:{$Left:[0.2,0.8],$Zoom:[0.2,0.8],$Rotate:[0.2,0.8]},$Easing:{$Left:$Jease$.$Swing,$Zoom:$Jease$.$Swing,$Opacity:$Jease$.$Linear,$Rotate:$Jease$.$Swing},$Opacity:2,$Round:{$Rotate:0.5}},
	  {$Duration:1000,x:4,$Zoom:11,$Rotate:1,$SlideOut:true,$Easing:{$Left:$Jease$.$InExpo,$Zoom:$Jease$.$InExpo,$Opacity:$Jease$.$Linear,$Rotate:$Jease$.$InExpo},$Opacity:2,$Round:{$Rotate:0.8}},
	  {$Duration:1200,x:0.5,y:0.3,$Cols:2,$Zoom:1,$Rotate:1,$Assembly:2049,$ChessMode:{$Column:15},$Easing:{$Left:$Jease$.$InCubic,$Top:$Jease$.$InCubic,$Zoom:$Jease$.$InCubic,$Opacity:$Jease$.$OutQuad,$Rotate:$Jease$.$InCubic},$Opacity:2,$Round:{$Rotate:0.7}},
	  {$Duration:1000,x:0.5,y:0.3,$Cols:2,$Zoom:1,$Rotate:1,$SlideOut:true,$Assembly:2049,$ChessMode:{$Column:15},$Easing:{$Left:$Jease$.$InExpo,$Top:$Jease$.$InExpo,$Zoom:$Jease$.$InExpo,$Opacity:$Jease$.$Linear,$Rotate:$Jease$.$InExpo},$Opacity:2,$Round:{$Rotate:0.7}},
	  {$Duration:1200,x:-4,y:2,$Rows:2,$Zoom:11,$Rotate:1,$Assembly:2049,$ChessMode:{$Row:28},$Easing:{$Left:$Jease$.$InCubic,$Top:$Jease$.$InCubic,$Zoom:$Jease$.$InCubic,$Opacity:$Jease$.$OutQuad,$Rotate:$Jease$.$InCubic},$Opacity:2,$Round:{$Rotate:0.7}},
	  {$Duration:1200,x:1,y:2,$Cols:2,$Zoom:11,$Rotate:1,$Assembly:2049,$ChessMode:{$Column:19},$Easing:{$Left:$Jease$.$InCubic,$Top:$Jease$.$InCubic,$Zoom:$Jease$.$InCubic,$Opacity:$Jease$.$OutQuad,$Rotate:$Jease$.$InCubic},$Opacity:2,$Round:{$Rotate:0.8}}
	];

	var jssor_1_options = {
	  $AutoPlay: false,
	  $MinDragOffsetToSlide: false,
	  $SlideshowOptions: {
		$Class: $JssorSlideshowRunner$,
		$Transitions: jssor_1_SlideshowTransitions,
		$TransitionsOrder: 1
	  },
	  $ArrowNavigatorOptions: {
		$Class: $JssorArrowNavigator$
	  },
	  $ThumbnailNavigatorOptions: {
		$Class: $JssorThumbnailNavigator$,
		$Rows: 2,
		$Cols: 4,
		$SpacingX: 14,
		$SpacingY: 12,
		$Orientation: 2,
		$Align: 4
	  }
	};

	
	var jssor_1_slider = new $JssorSlider$("jssor_1", jssor_1_options);
	
	
	/*responsive code begin*/
	/*you can remove responsive code if you don't want the slider scales while window resizing*/
	function ScaleSlider() {
		var refSize = jssor_1_slider.$Elmt.parentNode.clientWidth;
		if (refSize) {
			refSize = Math.min(refSize, 1170);
			refSize = Math.max(refSize, 300);
			jssor_1_slider.$ScaleWidth(refSize);
		}
		else {
			window.setTimeout(ScaleSlider, 30);
		}
	}
	ScaleSlider();
	$(window).bind("load", ScaleSlider);
	$(window).bind("resize", ScaleSlider);
	$(window).bind("orientationchange", ScaleSlider);
	/*responsive code end*/

	$("div#pdfimg > div").css({"overflow-y":"scroll","width":"100%","height":"100%"});
	$("div#pdfimg > div img").css({"height":"auto","width":"100%"});
	// $(".ht_yeqian > .jssort01-99-66").css({"width":"90%"});
	// $(".ht_yeqian > .jssort01-99-66 > div").css({"width":"90%","left":"5%","height":"100%"});
	// $(".ht_yeqian > .jssort01-99-66  div[data-u='slides']").css({"width":"100%","left":"0","height":"100%"});
	// $(".ht_yeqian > .jssort01-99-66  div[data-u='slides'] > div").css({"width":"100%"});
	// $(".ht_yeqian > .jssort01-99-66  div[data-u='slides'] > div > div+div.p").css({"right":"0","left":"auto"});
	// $(".ht_yeqian > .jssort01-99-66 div.p").css({"height":"100%"});

	
	// if(document.body.offsetWidth < 1170){
	// 	$(".ht_yeqian > .jssort01-99-66  div[data-u='slides'] > div").css({"height":"110px"});
	// }

	
	//拖拽复制体
    $('.htqz').draggable({
	   helper:"clone",
	   cursor: "move",
	   cursorAt: {top:0,left:0},
	   revert: "invalid"
	});
	// 找到当前显示页面
	jssor_1_slider.$On($JssorSlider$.$EVT_PARK,function(slideIndex){
		var slidesum = slideIndex + 1;

		$("#pdfimg div[data-u='thumb'] span").each(function(){
			var pagesum = $(this).text();
			if(slidesum == pagesum){
				$(this).parent().parent().css("z-index","999");
				var htqz = $(this).parent().parent().find(".current");
				var image = htqz.find("img[data-u='image']");
				var signature = htqz.find(".ui-draggable-handle");
				//释放后
				$(htqz).droppable({
					drop:function(event,ui){
					var imageSrc = image.attr("src");
					if(imageSrc.indexOf("blank.png")!=-1){//这个名字，是空白页对应的图片的名字，切记和jsp页面的要一致
					    　　alertMsg("该页面不允许签章");
					    return false;
					　　}
						// clone印章到页面
						var source = ui.draggable.clone();
						// 删除印章的图标及事件
						$('<img/>', {
							src: 'images/btn_delete.png',
							class: 'delete',
							style:'display:none',
							click: function() {
							  source.remove();
							}
						}).appendTo(source);
					
						source.mouseenter(function () { 
							$(this).find("img.delete").show();
							$(this).find("img").attr("data-nodrag","true");
						}); 

						source.mouseleave(function () {
							$(this).find("img.delete").hide();
						}); 

						$(this).append(source);

						// 获取签章释放时的位置
						var scrolltop = $(this).parent().scrollTop(); //获取单页div滚动的高度
						var dywidth = $(this).parent().width(); // 获取单页div的宽度
						var dyheight = $(this).height(); // 获取单页div的高度
						var qz_left = ui.position.left + dywidth; //鼠标释放时，左边的距离，坐标原点是右上角
						var qz_top = ui.position.top + scrolltop;  //鼠标释放时，上边的距离，坐标原点是右上角
						if(qz_left >= (dywidth - 120)){
							qz_left = dywidth - 120;
						}else if(qz_left < 0){
							qz_left = 0;
						};
						if(qz_top < 0){
							qz_top = 0;
						}else if(qz_top >= (dyheight - 120)){
							qz_top = dyheight - 120
						};
						$(this).find('.htqz:last-child').css({"top":qz_top,"left":qz_left});
						
						var scqz_top = dyheight - qz_top - 120; //生成已签章合同签章距离页面上边的距离
						$(this).find('.htqz:last-child').css({"top":qz_top,"left":qz_left}).attr("alt",scqz_top);
						// 签章隐藏，验证显示
						$(".ht_qz").slideUp();
						$(".ht_sf").slideDown();
					},

				});

			}else{
				$(this).parent().parent().css("z-index","");
			}
		})
	})

});
// 输入页码跳页
$(function(){
	$(".page-btn").click(function(){
		$(".jssort01-99-66 div[data-u='slides'] span").each(function(){
			var pagesum = $("#pagesum input").val();
		    var pages = $(this).text();
			if(pagesum == pages){
				$(this).parent().parent().parent().click();
				$(this).parent().parent().parent().click();
			}
		});
	});
});	
// 点击继续签名
$(function(){
	$(".ht_sf .btn-orange").click(function(){
		$(this).parent().slideUp();
		$(".ht_qz").slideDown();
		$("#sjyzmQs").val("");
	})
});

$(function(){
	$(".jssora05r").click(function(){//向右
		var buqueys = $("#buqueys").val();
		var preIndex = $(".pav").find("span[name^='spanDiv']").html();//当前页码
		preIndex = parseInt(preIndex);
		if(preIndex>=buqueys){
			$("#pageIndex").val(1);
		}else{
			$("#pageIndex").val(preIndex+1);
		}
	});
	$(".jssora05l").click(function(){//向左
		var buqueys = $("#buqueys").val();
		var preIndex = $(".pav").find("span[name^='spanDiv']").html();//当前页码
		preIndex = parseInt(preIndex);
		if(preIndex==1){
			$("#pageIndex").val(buqueys);
		}else{
			$("#pageIndex").val(preIndex-1);
		}
	});
	
	
});
