$(function(){
	$("#fullPage").fullpage({
		verticalCentered:false,
		anchors:['page1','page2','page3','page4'],
		navigation:true,
		afterLoad:function(link,index){
			switch(index){
				case 1:
					
					break;
				case 2:
					
					break;
				case 3:
					
					break;
				case 4:

					break;
				default:

					break;
			}
		},
		onLeave:function(link,index){
			switch(index){
				case 1:
					var banimg = $(".banimg"),
						banimgnew = banimg.clone(true);
						banimg.before(banimgnew);
					$("." + banimg.attr("class") + ":last").remove();
					var pro_jiami = $(".pro_jiami"),
						pro_jiaminew = pro_jiami.clone(true);
						pro_jiami.before(pro_jiaminew);
					$("." + pro_jiami.attr("class") + ":last").remove();
					break;
				case 2:
					var wzimg = $(".wzimg"),
						wzimgnew = wzimg.clone(true);
						wzimg.before(wzimgnew);
					$("." + wzimg.attr("class") + ":last").remove();
					var wzneirong = $(".wzneirong"),
						wzneirongnew = wzneirong.clone(true);
						wzneirong.before(wzneirongnew);
					$("." + wzneirong.attr("class") + ":last").remove();
					break;
				case 3:
					var bzimg = $(".bzimg"),
						bzimgnew = bzimg.clone(true);
						bzimg.before(bzimgnew);
					$("." + bzimg.attr("class") + ":last").remove();
					var bzneirong = $(".bzneirong"),
						bzneirongnew = bzneirong.clone(true);
						bzneirong.before(bzneirongnew);
					$("." + bzneirong.attr("class") + ":last").remove();

					break;
				case 4:
					var jmimg = $(".jmimg"),
						jmimgnew = jmimg.clone(true);
						jmimg.before(jmimgnew);
					$("." + jmimg.attr("class") + ":last").remove();
					var jmneirong = $(".jmneirong"),
						jmneirongnew = jmneirong.clone(true);
						jmneirong.before(jmneirongnew);
					$("." + jmneirong.attr("class") + ":last").remove();
					break;
				default:

					break;
			}
		}
		
	});
});






