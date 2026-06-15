# Sina Visitor System

- 原始链接: https://passport.weibo.com/visitor/visitor?entry=miniblog&a=enter&url=https%3A%2F%2Fs.weibo.com%2Fweibo%3Fq%3D%25E4%25B8%2596%25E7%2595%258C%25E9%25A5%25AE%25E9%25A3%259F%25E7%25BE%258E%25E5%259B%25BD%25E5%258C%2596%25E5%258F%25AA%25E6%259C%2589%25E4%25B8%25AD%25E5%259B%25BD%25E6%25B2%25A1%25E5%258F%2598&domain=.weibo.com&sudaref=&ua=php-sso_sdk_client-0.6.29&_rand=1781467058.819
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
        var return_url = "https://s.weibo.com/weibo?q=%E4%B8%96%E7%95%8C%E9%A5%AE%E9%A3%9F%E7%BE%8E%E5%9B%BD%E5%8C%96%E5%8F%AA%E6%9C%89%E4%B8%AD%E5%9B%BD%E6%B2%A1%E5%8F%98";
        var request_id = "601d1f1ab8eb1c2d4d1f61ce661dbbc6";
        var webdrive