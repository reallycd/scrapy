# Mongoose 搜索注入漏洞分析 - SecPulse.COM | 安全脉搏

- 原始链接: https://www.secpulse.com/archives/205921.html
- 来源页面: https://tophub.today/
- 状态码: 200

## 抽取文本预览

首页

分类阅读

脉搏文库

内网渗透

|

代码审计

|

安全文献

|

Web安全

|

移动安全

|

系统安全

|

工控安全

|

CTF

|

IOT安全

|

安全建设

业务安全

|

安全管理

|

数据分析

|

其他

资讯

|

漏洞

|

工具

|

人物志

|

区块链安全

|

安全招聘

|

安全问答

金币商城

安全招聘

活动日程

live课程

企业服务

插件社区

小程序

扫一扫

了解小程序

登录

|

注册

$(".menu-item-has-children>a").attr("href","javascript:void(0)").attr("target","_self").css("cursor","default");
$(".menu-item-has-children").hover(function(){
    $(".read_hide").show();
},function(){
    $(".read_hide").hide();
});
$(".login_self").hover(function(){
    $(".loginout_hide").show();
    $(".loginout").text("▲");
},function(){
    $(".loginout_hide").hide();
    $(".loginout").text("▼");
});
// 返回顶部
$(function(){    
    $(function(){   
        $('.icon-fanhuidingbu').click(function(){  
            $('body,html').animate({scrollTop:0},500);  
            return false;                   
        }) 
        $(".icon-fanhuidingbu-copy").click(function(){
            // console.log(document.body.clientHeight)
            // console.log(document.body.offsetHeight)
            $("html,body").animate({
                scrollTop: document.body.offsetHeight},500);
            return false; 
        })        
    })      
// 上拉显示导航栏 下拉隐藏
    var cubuk_seviye = $(document).scrollTop();  
    var header_yuksekligi = $('#header').outerHeight();    
    $(window).scroll(function() {  
        var kaydirma_cubugu = $(document).scrollTop();  
  
        if (kaydirma_cubugu > header_yuksekligi){$('#header').addClass('gizle');}   
        else {$('#header').removeClass('gizle');}  
  
        if (kaydirma_cubugu > cubuk_seviye){$('#header').removeClass('sabit');}   
        else {$('#header').addClass('sabit');}                  
  
        cubuk_seviye = $(document).scrollTop();   
     });  
});
$(".nav_small .icon-nav").on("click",function(){
    var $list =$(".nav_small_list");
    if($list.css('display') == 'none'){
        $list.slideDown();
    }else{
        $list.slideUp();
    }  
})
$(".nav_read_click")