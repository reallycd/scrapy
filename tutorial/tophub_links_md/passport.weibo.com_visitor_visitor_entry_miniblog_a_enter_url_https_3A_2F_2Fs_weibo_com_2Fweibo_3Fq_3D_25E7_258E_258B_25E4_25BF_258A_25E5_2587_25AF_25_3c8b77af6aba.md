# Sina Visitor System

- 原始链接: https://passport.weibo.com/visitor/visitor?entry=miniblog&a=enter&url=https%3A%2F%2Fs.weibo.com%2Fweibo%3Fq%3D%25E7%258E%258B%25E4%25BF%258A%25E5%2587%25AF%25E5%2588%2598%25E6%2598%258A%25E7%2584%25B6%25E5%2590%25B4%25E7%25A3%258A8%25E5%25B9%25B4%25E5%2589%258D%25E5%2590%2588%25E7%2585%25A7&domain=.weibo.com&sudaref=&ua=php-sso_sdk_client-0.6.29&_rand=1781467063.9511
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
        var return_url = "https://s.weibo.com/weibo?q=%E7%8E%8B%E4%BF%8A%E5%87%AF%E5%88%98%E6%98%8A%E7%84%B6%E5%90%B4%E7%A3%8A8%E5%B9%B4%E5%89%8D%E5%90%88%E7%85%A7";
        var request_id = "2c39122437c3ee4443d81bdb7d8c0183";
        var webdriver = navi