# Sina Visitor System

- 原始链接: https://passport.weibo.com/visitor/visitor?entry=miniblog&a=enter&url=https%3A%2F%2Fs.weibo.com%2Fweibo%3Fq%3D%25E7%2588%25B8%25E7%2588%25B8%25E5%25AB%258C%25E5%25BC%2583%25E7%2588%25B7%25E7%2588%25B7%25E5%2581%259A%25E9%25A5%25AD%25E9%259A%25BE%25E5%2590%2583%25E8%25A2%25AB6%25E5%25B2%2581%25E9%2597%25BA%25E5%25A5%25B3%25E8%25AF%25B4%25E5%2593%25AD&domain=.weibo.com&sudaref=&ua=php-sso_sdk_client-0.6.29&_rand=1781467030.6679
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
        var return_url = "https://s.weibo.com/weibo?q=%E7%88%B8%E7%88%B8%E5%AB%8C%E5%BC%83%E7%88%B7%E7%88%B7%E5%81%9A%E9%A5%AD%E9%9A%BE%E5%90%83%E8%A2%AB6%E5%B2%81%E9%97%BA%E5%A5%B3%E8%AF%B4%E5%93%AD";
        var request_id = "4bb930bd36288920a47a9c5e52e