# Sina Visitor System

- 原始链接: https://passport.weibo.com/visitor/visitor?entry=miniblog&a=enter&url=https%3A%2F%2Fs.weibo.com%2Fweibo%3Fq%3D%25E5%258F%25B0%25E5%2585%25AC%25E5%25BC%2580%25E8%25A7%25A3%25E6%2594%25BE%25E5%2586%259B%25E6%2597%25A0%25E4%25BE%25A610%25E5%25BD%25B1%25E5%2583%258F%25E7%2596%2591%25E4%25BC%25BC%25E5%259C%25A8%25E5%25A3%25AE%25E8%2583%2586&domain=.weibo.com&sudaref=&ua=php-sso_sdk_client-0.6.29&_rand=1781467045.7769
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
        var return_url = "https://s.weibo.com/weibo?q=%E5%8F%B0%E5%85%AC%E5%BC%80%E8%A7%A3%E6%94%BE%E5%86%9B%E6%97%A0%E4%BE%A610%E5%BD%B1%E5%83%8F%E7%96%91%E4%BC%BC%E5%9C%A8%E5%A3%AE%E8%83%86";
        var request_id = "a653c9d819fc78c3969940fcf321899b";
