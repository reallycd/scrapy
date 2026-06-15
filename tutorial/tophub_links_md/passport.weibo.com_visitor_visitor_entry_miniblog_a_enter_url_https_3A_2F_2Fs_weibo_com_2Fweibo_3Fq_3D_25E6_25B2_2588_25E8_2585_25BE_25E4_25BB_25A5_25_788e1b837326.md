# Sina Visitor System

- 原始链接: https://passport.weibo.com/visitor/visitor?entry=miniblog&a=enter&url=https%3A%2F%2Fs.weibo.com%2Fweibo%3Fq%3D%25E6%25B2%2588%25E8%2585%25BE%25E4%25BB%25A5%25E4%25B8%25BA%25E7%25A5%259E%25E7%25BA%25A7%25E6%2595%2591%25E5%259C%25BA%2B%25E7%25BB%2593%25E6%259E%259C%25E5%2585%25A8%25E6%25BC%258F%25E4%25BA%2586&domain=.weibo.com&sudaref=&ua=php-sso_sdk_client-0.6.29&_rand=1781467077.0344
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
        var return_url = "https://s.weibo.com/weibo?q=%E6%B2%88%E8%85%BE%E4%BB%A5%E4%B8%BA%E7%A5%9E%E7%BA%A7%E6%95%91%E5%9C%BA+%E7%BB%93%E6%9E%9C%E5%85%A8%E6%BC%8F%E4%BA%86";
        var request_id = "fc7cb84c28e5d83926c15261fbfb441d";
        var webdriv