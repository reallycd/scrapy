# Sina Visitor System

- 原始链接: https://passport.weibo.com/visitor/visitor?entry=miniblog&a=enter&url=https%3A%2F%2Fs.weibo.com%2Fweibo%3Fq%3D%25E5%25A4%25A7%25E5%25AD%25A6%25E9%2587%258C%25E6%259C%2580%25E8%25A2%25AB%25E5%258A%259D%25E9%2580%2580%25E7%259A%2584%25E4%25B8%2593%25E4%25B8%259A%2B%25E5%25AE%2583%25E6%258E%2592%25E7%25AC%25AC%25E4%25B8%2580&domain=.weibo.com&sudaref=&ua=php-sso_sdk_client-0.6.29&_rand=1781467038.2953
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
        var return_url = "https://s.weibo.com/weibo?q=%E5%A4%A7%E5%AD%A6%E9%87%8C%E6%9C%80%E8%A2%AB%E5%8A%9D%E9%80%80%E7%9A%84%E4%B8%93%E4%B8%9A+%E5%AE%83%E6%8E%92%E7%AC%AC%E4%B8%80";
        var request_id = "467dd817ba766ad1b6f33fcf855d6b29";
        va