# Sina Visitor System

- 原始链接: https://passport.weibo.com/visitor/visitor?entry=miniblog&a=enter&url=https%3A%2F%2Fs.weibo.com%2Fweibo%3Fq%3D%25E5%2588%2598%25E6%2598%258A%25E7%2584%25B6%25E8%2591%25A3%25E5%25AD%2590%25E5%2581%25A5%25E7%25A8%258B%25E6%25BD%2587%25E9%2583%25BD%25E5%259C%25A8%25E6%25B1%2582%25E5%25B7%25A5%25E4%25BD%259C&domain=.weibo.com&sudaref=&ua=php-sso_sdk_client-0.6.29&_rand=1781467074.5322
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
        var return_url = "https://s.weibo.com/weibo?q=%E5%88%98%E6%98%8A%E7%84%B6%E8%91%A3%E5%AD%90%E5%81%A5%E7%A8%8B%E6%BD%87%E9%83%BD%E5%9C%A8%E6%B1%82%E5%B7%A5%E4%BD%9C";
        var request_id = "f9c33e2a5800a44e33f1a09c1d9748a7";
        var webdrive