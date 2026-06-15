# Sina Visitor System

- 原始链接: https://passport.weibo.com/visitor/visitor?entry=miniblog&a=enter&url=https%3A%2F%2Fs.weibo.com%2Fweibo%3Fq%3D10%25E5%25AE%25B6A%25E8%2582%25A1%25E5%2585%25AC%25E5%258F%25B8%25E9%2580%2580%25E5%25B8%2582%2B%25E8%25B6%258525%25E4%25B8%2587%25E8%2582%25A1%25E6%25B0%2591%25E8%25B8%25A9%25E9%259B%25B7&domain=.weibo.com&sudaref=&ua=php-sso_sdk_client-0.6.29&_rand=1781467011.8591
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
        var return_url = "https://s.weibo.com/weibo?q=10%E5%AE%B6A%E8%82%A1%E5%85%AC%E5%8F%B8%E9%80%80%E5%B8%82+%E8%B6%8525%E4%B8%87%E8%82%A1%E6%B0%91%E8%B8%A9%E9%9B%B7";
        var request_id = "7c7dbd08b1b23977b7ccf4bd994abb62";
        var webdriver =