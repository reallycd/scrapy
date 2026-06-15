# Sina Visitor System

- 原始链接: https://passport.weibo.com/visitor/visitor?entry=miniblog&a=enter&url=https%3A%2F%2Fs.weibo.com%2Fweibo%3Fq%3D%25E5%25B9%25BC%25E5%25B9%25B4%25E5%25BD%25A2%25E6%2580%2581%25E5%25B0%25B1%25E5%25B7%25B2%25E7%25BB%258F%25E8%2583%25BD%25E7%259C%258B%25E6%2587%2582%25E8%25BF%2599%25E4%25B9%2588%25E5%25A4%259A%25E4%25BA%2586&domain=.weibo.com&sudaref=&ua=php-sso_sdk_client-0.6.29&_rand=1781467022.9516
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
        var return_url = "https://s.weibo.com/weibo?q=%E5%B9%BC%E5%B9%B4%E5%BD%A2%E6%80%81%E5%B0%B1%E5%B7%B2%E7%BB%8F%E8%83%BD%E7%9C%8B%E6%87%82%E8%BF%99%E4%B9%88%E5%A4%9A%E4%BA%86";
        var request_id = "a214b678d28e860e12d7535f987d03a5";
        var