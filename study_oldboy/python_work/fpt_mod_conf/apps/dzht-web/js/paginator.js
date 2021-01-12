/** ajax分页 */
(function ($) {
    "use strict";

    var BootstrapPaginator = function (element, options) {
    	this.setOptions(options);
        this.init(element);
    };

    BootstrapPaginator.prototype = {

        init: function (element) {
        	this.$element = $(element);
        	var params = {};
        	if(this.options.searchClass){
        		params = getFormData(this.options.searchClass);
        	}
        	params.currentPage = 1;
        	postData(this.options.pageUrl, params, this.successCallback.bind(this), null, true);
        },
        
        setOptions: function(options){
        	this.options = $.extend({}, (this.options || $.fn.bootstrapPaginator.defaults), options);
        },
        
        pageChange: function(currentPage){
        	var params = {};
        	if(this.options.searchClass){
        		params = getFormData(this.options.searchClass);
        	}
        	params.currentPage = currentPage;
        	postData(this.options.pageUrl, params, this.successCallback.bind(this),null, true);
        },
        
        render: function(){
        	if(typeof this.options.buildTable==='function')
        		this.options.buildTable(this.options.data, this.$element);
            var page = {
            	currentPage: this.options.currentPage,
            	total: this.options.total,
            	pages: this.options.pages
            };
            this.$element.append(this.buildPageItem(page));
        },
        
        successCallback: function(data) {
    	    if (!data) return;
    	    this.setOptions({
    	    	currentPage: data.currentPage, //当前页
    	        total: data.total, //总记录数
    	        pages: data.pages, //总页数
    	        data: data.list //分页数据
    	    });
    	    this.render();
        },

        onPageClicked: function (event) {
        	var data = event.data, type = data.type;
            switch (type) {
            case "first":
            	this.pageChange(data.page);
                break;
            case "prev":
            	this.pageChange(data.page - 1);
                break;
            case "next":
            	this.pageChange(data.page + 1);
                break;
            case "last":
            	this.pageChange(data.page);
                break;
            case "page":
            	this.pageChange(data.page);
                break;
            case "jump":
            	var jumpPage = event.currentTarget.previousSibling.value;
            	this.pageChange(jumpPage);
            	break;
            }
        },

        buildPageItem: function (page) {
            var itemContainer = $('<div class="holder ifrm_footer"></div>');
            
            var itemFirstContent = $('<a class="jp-first">首页</a>');
            if(page.currentPage==1) itemFirstContent.addClass("jp-disabled");
            else itemFirstContent.on("click", null, {type: 'first', page: 1}, $.proxy(this.onPageClicked, this));
            itemContainer.append(itemFirstContent);
            
            var itemPrevContent = $('<a class="jp-previous">&lt;&lt;</a>');
            if(page.currentPage==1) itemPrevContent.addClass("jp-disabled");
            else itemPrevContent.on("click", null, {type: 'prev', page: page.currentPage}, $.proxy(this.onPageClicked, this));
            itemContainer.append(itemPrevContent);
            
            if(page.pages <= 3){
        		for(var i=1;i<=page.pages;i++){
        			var itemContent = $('<a>'+i+'</a>');
        			if(page.currentPage==i) itemContent.addClass("jp-current");
        			else{
            			itemContent.on("click", null, {type: 'page', page: i}, $.proxy(this.onPageClicked, this));
        			}
        			itemContainer.append(itemContent);
        		}
        	}else{
        		var i = -1;
        		if(page.currentPage==1) i = 0;
        		if(page.currentPage==page.pages) i = -2;
        		for(var j=0;j<3;j++){
        			var itemContent = $('<a>'+(page.currentPage+i)+'</a>');
        			if(i==0) itemContent.addClass("jp-current");
        			else{
            			itemContent.on("click", null, {type: 'page', page: page.currentPage+i}, $.proxy(this.onPageClicked, this));
        			}
        			itemContainer.append(itemContent);
        			i++;
        		}
        	}
            
            var itemNextContent = $('<a class="jp-next">&gt;&gt;</a>');
            if(page.currentPage==page.pages) itemNextContent.addClass("jp-disabled");
            else itemNextContent.on("click", null, {type: 'next', page: page.currentPage}, $.proxy(this.onPageClicked, this));
            itemContainer.append(itemNextContent);
            
            var itemLastContent = $('<a class="jp-last">末页</a>');
            if(page.currentPage==page.pages) itemLastContent.addClass("jp-disabled");
            else itemLastContent.on("click", null, {type: 'last', page: page.pages}, $.proxy(this.onPageClicked, this));
            itemContainer.append(itemLastContent);
            
            var sumary = '共'+page.pages+'页,'+page.total+'条记录';
            itemContainer.append($('<a class="pages">'+sumary+'</a>'));
            itemContainer.append($('<input type="text" class="tiaoye form-control" />'));
            
            var jumpContent = $('<input type="button" class="btn btn-danger" value="跳转" />');
            jumpContent.on("click", null, {type:'jump'}, $.proxy(this.onPageClicked, this));
            itemContainer.append(jumpContent);
            return itemContainer;
        }
    };
    
    $.fn.bootstrapPaginator = function (option) {
        var args = arguments,
            result = null;

        $(this).each(function (index, item) {
            var $this = $(item),
                data = $this.data('bootstrapPaginator'),
                options = (typeof option !== 'object') ? null : option;

            if (!data) {
                data = new BootstrapPaginator(this, options);

                $this = $(data.$element);

                $this.data('bootstrapPaginator', data);

                return;
            }

            if (typeof option === 'string') {

                if (data[option]) {
                    result = data[option].apply(data, Array.prototype.slice.call(args, 1));
                } else {
                    throw "Method " + option + " does not exist";
                }

            } else {
                result = data.setOptions(option);
            }
        });

        return result;

    };

    $.fn.bootstrapPaginator.defaults = {
    	pageUrl: null,  //分页数据请求url
        searchClass: '', //分页查询参数form的class
        buildTable: null //构造列表数据的方法
    };

    $.fn.bootstrapPaginator.Constructor = BootstrapPaginator;
    
}(window.jQuery));


