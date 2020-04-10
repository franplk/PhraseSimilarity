layui.use(['jquery', 'element'], function() {
    element = layui.element;
    var $ = layui.jquery;

    window.addTab = function(title, url, id) {
        for (var i = 0; i < $('.x-iframe').length; i++) {
            if($('.x-iframe').eq(i).attr('tab-id')==id){
                element.tabChange('xbs_tab', id);
                return;
            }
        };
        element.tabAdd('xbs_tab', {
            id: id, title: title,
            content: '<iframe tab-id="'+id+'" frameborder="0" src="'+url+'" scrolling="yes" class="x-iframe"></iframe>'
        });
        element.tabChange('xbs_tab', id);
    };

    $(".layui-tab-title").on('contextmenu', 'li', function(event) {
        var tab_left = $(this).position().left;
        var left = $(this).position().top;
        this_index = $(this).attr('lay-id');
        $('#tab_show').show();
        return false;
    });

    $('.page-content,#tab_show,.container,.left-nav').click(function(event) {
        $('#tab_show').hide();
    });

    $('.container .left_open i').click(function(event) {
        if($('.left-nav').css('left')=='0px') {
            $('.left-nav').animate({left: '-221px'}, 100);
            $('.page-content').animate({left: '0px'}, 100);
            $('.page-content-bg').hide();
        } else{
            $('.left-nav').animate({left: '0px'}, 100);
            $('.page-content').animate({left: '221px'}, 100);
            if($(window).width()<768){
                $('.page-content-bg').show();
            }
        }
    });

    $('.page-content-bg').click(function(event) {
        $('.left-nav').animate({left: '-221px'}, 100);
        $('.page-content').animate({left: '0px'}, 100);
        $(this).hide();
    });

    // 关闭Tab
    $('.layui-tab-close').click(function(event) {
        $('.layui-tab-title li').eq(0).find('i').remove();
    });

    //左侧菜单效果
    $('.left-nav #nav').on('click', 'li', function(event) {
        var index = $('.left-nav #nav li').index($(this));
        if($(this).children('.sub-menu').length){
            if($(this).hasClass('open')){
                $(this).removeClass('open');
                $(this).find('.nav_right').html('&#xe697;');
                $(this).children('.sub-menu').stop().slideUp();
                $(this).siblings().children('.sub-menu').slideUp();
            } else {
                $(this).addClass('open');
                $(this).children('a').find('.nav_right').html('&#xe6a6;');
                $(this).children('.sub-menu').stop().slideDown();
                $(this).siblings().children('.sub-menu').stop().slideUp();
                $(this).siblings().find('.nav_right').html('&#xe697;');
                $(this).siblings().removeClass('open');
            }
        } else {
            var url = $(this).children('a').attr('_href');
            var title = $(this).find('cite').html();
            addTab(title,url,index+1);
        }
        event.stopPropagation();
    });
});