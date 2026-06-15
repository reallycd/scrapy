# Sina Visitor System

- 原始链接: https://passport.weibo.com/visitor/visitor?entry=miniblog&a=enter&url=https%3A%2F%2Fs.weibo.com%2Fweibo%3Fq%3D%25E5%2594%2590%25E5%2583%25A7%25E8%25A6%2581%25E6%2598%25AF%25E8%25A2%25AB%25E4%25BB%2596%25E6%258A%2593%25E4%25BA%2586%25E5%25AD%2599%25E6%2582%259F%25E7%25A9%25BA%25E9%2583%25BD%25E6%259D%25A5%25E4%25B8%258D%25E5%258F%258A%25E6%2595%2591&domain=.weibo.com&sudaref=&ua=php-sso_sdk_client-0.6.29&_rand=1781467053.5565
- 来源页面: https://tophub.today/
- 状态码: 200

## 抽取文本预览

window.use_fp = "1" == "1"; // 是否采集设备指纹。
    var url = url || {};
    (function () {
        this.l = function (u, c) {
            try {
                var s = document.createElement("script");
                s.type = "text/javascript";
                s[document.all ? "onreadystatechange" : "onload"] = function () {
                    if (document.all && this.readyState != "loaded" && this.readyState != "complete") {
                        return
                    }
                    this[document.all ? "onreadystatechange" : "onload"] = null;
                    this.parentNode.removeChild(this);
                    if (c) {
                        c()
                    }
                };
                s.src = u;
                document.getElementsByTagName("head")[0].appendChild(s)
            } catch (e) {
            }
        };
    }).call(url);

    var visitor_origin = function () {
        try {
            var need_restore = "1" == "1"; // 是否走恢复身份流程。

            // 如果需要走恢复身份流程，尝试从 cookie 获取用户身份。
            if (!need_restore || !Store.CookieHelper.get("SRF")) {

                // 若获取失败走创建访客流程。
                // 流程执行时间过长（超过 3s），则认为出错。
                var error_timeout = window.setTimeout("error_back()", 5000);

                tid.get(function (tid, where, confidence) {
                    // 取指纹顺利完成，清除出错 timeout 。
                    window.clearTimeout(error_timeout);
                    incarnate(tid, where, confidence);
                });
            } else {
                // 用户身份存在，尝试恢复用户身份。
                restore();
            }
        } catch (e) {
            // 出错。
            error_back();
        }
    };

    var visitor_gray = function () {
        var from = "weibo";
        var return_url = "https://s.weibo.com/weibo?q=%E5%94%90%E5%83%A7%E8%A6%81%E6%98%AF%E8%A2%AB%E4%BB%96%E6%8A%93%E4%BA%86%E5%AD%99%E6%82%9F%E7%A9%BA%E9%83%BD%E6%9D%A5%E4%B8%8D%E5%8F%8A%E6%95%91";
        var request_id = "a15318c69eda43c10c98d01c8b3a