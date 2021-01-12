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
					$('.partner .col-xs-4').find("img").each(function(){
						$(this).parent().css("background-image","url(images/partnerbg.png)");
					})
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
					break;
				case 2:
					var tx_bt = $(".tx_bt"),
						tx_btnew = tx_bt.clone(true);
						tx_bt.before(tx_btnew);
					$("." + tx_bt.attr("class") + ":last").remove();
					var tx_tb = $(".tx_tb"),
						tx_tbnew = tx_tb.clone(true);
						tx_tb.before(tx_tbnew);
					$("." + tx_tb.attr("class") + ":last").remove();
					break;
				case 3:
					var dztitle = $(".dztitle"),
						dztitlenew = dztitle.clone(true);
						dztitle.before(dztitlenew);
					$("." + dztitle.attr("class") + ":last").remove();
					var dzsming = $(".dzsming"),
						dzsmingnew = dzsming.clone(true);
						dzsming.before(dzsmingnew);
					$("." + dzsming.attr("class") + ":last").remove();
					var dzqmf_nr = $(".dzqmf_nr"),
						dzqmf_nrnew = dzqmf_nr.clone(true);
						dzqmf_nr.before(dzqmf_nrnew);
					$("." + dzqmf_nr.attr("class") + ":last").remove();
					break;
				case 4:
					var partner_bt = $(".partner_bt"),
						partner_btnew = partner_bt.clone(true);
						partner_bt.before(partner_btnew);
					$("." + partner_bt.attr("class") + ":last").remove();
					var partnerlogo = $(".partnerlogo"),
						partnerlogonew = partnerlogo.clone(true);
						partnerlogo.before(partnerlogonew);
					$("." + partnerlogo.attr("class") + ":last").remove();
					break;
				default:

					break;
			}
		}
		
	});
});
