# 微信今日视频榜 - 今日热榜

- 原始链接: https://tophub.today/n/W1VdJPZoLQ
- 来源页面: https://tophub.today/
- 状态码: 200

## 抽取文本预览

今日热榜

首页

日报

动态

追踪

榜中榜

热文库

话题

日历

综合

科技

娱乐

社区

购物

财经

开发

简报

AI

更多















.tag-group{padding:5px 0;margin-bottom:5px;text-align:left}
.tag-group .F-gb{padding:2px 5px;margin:2px;overflow:hidden;color:#4a4a4a;opacity:.8;height:auto;line-height:20px;text-align:center;font-size:13px;display:inline-block!important;position:relative;border-radius:8px;background-color:#f5f5f5;transition:all .2s ease;float:none;font-weight:500}
.tag-group .F-gb:hover{opacity:1;background-color:#e8e8e8;color:#333}
.tag-group .F-gb-jb{background-color:#1e88e5;color:#fff;opacity:1;font-weight:500;box-shadow:0 1px 3px rgba(0,0,0,.12)}
.tag-hr{height:1px;background-color:#f4f4f4;margin:2px 0}
.kb-more-dropdown{left:40%}
/* 深色模式样式 */
.dark .tag-group .F-gb{color:#e0e0e0;background-color:#333;opacity:.9}
.dark .tag-group .F-gb:hover{background-color:#444;color:#fff}
.dark .tag-group .F-gb-jb{background-color:#0d47a1;color:#fff;box-shadow:0 1px 3px rgba(0,0,0,.3)}
.dark .tag-hr{background-color:#444}

报刊

设计

校务

政务

专栏

苹果

公众号

小部件

自定义分组

更多作品推荐

今日简报 AI

总结全网10000+热榜，让阅读更高效！

即时写作 AI

人工智能让每个人都可以自信地写作！

今日历

全球最全的日历，日历届的航空母舰！

今日解忧

赛博修行，舒缓静心，21世纪解压神器！

今日热卖

淘宝京东拼多多等热卖热榜线报聚合

百晓生 AI

人工智能聊天兼全能创作助手

榜眼数据

今日热榜官方数据 API 开放平台



登录



夜间模式



关于我们



App 下载



使用指南



赞助商广告



API 开放平台

$(document).ready(function() {
    // 点击搜索按钮时
    $("#search-button").click(function() {
        // 隐藏导航栏
        $(".kb-lb-ib-c").hide();
        // 显示搜索框
        $(".I-J").show();
        
        // 聚焦到搜索输入框
        $(".I-K-L").focus();
    });
    
    // 点击搜索框以外的区域或按ESC键时取消搜索
    $(document).click(function(event) {
        if (!$(event.target).closest('#search-button, .I-J').length) {
            $(".kb-lb-ib-c").show();
            $(".I-J").hide();
        }
    });
    
    $(document).keyup(function(e) {
        if (e.key === "Escape") {
            $(".kb-lb-ib-c").show();
            $(".I-J").hide();
        }
    });
    
    // 阻止点击搜索框时触发document的click事件
    $(".I-J"