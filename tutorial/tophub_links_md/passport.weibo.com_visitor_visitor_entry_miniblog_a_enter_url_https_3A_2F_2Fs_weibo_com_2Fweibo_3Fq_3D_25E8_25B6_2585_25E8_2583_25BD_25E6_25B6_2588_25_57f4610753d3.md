# Sina Visitor System

- 原始链接: https://passport.weibo.com/visitor/visitor?entry=miniblog&a=enter&url=https%3A%2F%2Fs.weibo.com%2Fweibo%3Fq%3D%25E8%25B6%2585%25E8%2583%25BD%25E6%25B6%2588%25E6%25AF%2592%25E6%25B6%25B2%25E4%25B8%258D%25E8%2583%25BD%25E4%25B8%258E%25E6%25B4%2597%25E8%25A1%25A3%25E6%25B6%25B2%25E5%2590%258C%25E7%2594%25A8&domain=.weibo.com&sudaref=&ua=php-sso_sdk_client-0.6.29&_rand=1781467048.1409
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
        var return_url = "https://s.weibo.com/weibo?q=%E8%B6%85%E8%83%BD%E6%B6%88%E6%AF%92%E6%B6%B2%E4%B8%8D%E8%83%BD%E4%B8%8E%E6%B4%97%E8%A1%A3%E6%B6%B2%E5%90%8C%E7%94%A8";
        var request_id = "9708af1adbdf02b4fbd70d75ae426e11";
        var webdrive