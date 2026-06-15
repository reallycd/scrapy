# Sina Visitor System

- 原始链接: https://passport.weibo.com/visitor/visitor?entry=miniblog&a=enter&url=https%3A%2F%2Fs.weibo.com%2Fweibo%3Fq%3D%25E7%2594%25B7%25E5%25AD%2590%25E5%258E%25BB%25E4%25B8%2596%25E6%25AC%25A049%25E4%25B8%2587%25E6%2588%25BF%25E8%25B4%25B7%25E7%2588%25B6%25E6%25AF%258D%25E6%2594%25BE%25E5%25BC%2583%25E7%25BB%25A7%25E6%2589%25BF&domain=.weibo.com&sudaref=&ua=php-sso_sdk_client-0.6.29&_rand=1781467081.7576
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
        var return_url = "https://s.weibo.com/weibo?q=%E7%94%B7%E5%AD%90%E5%8E%BB%E4%B8%96%E6%AC%A049%E4%B8%87%E6%88%BF%E8%B4%B7%E7%88%B6%E6%AF%8D%E6%94%BE%E5%BC%83%E7%BB%A7%E6%89%BF";
        var request_id = "6d04a1401b2c0b21a14cc74d0752f9b8";
        v