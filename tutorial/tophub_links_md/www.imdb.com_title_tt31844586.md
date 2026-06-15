# Untitled

- 原始链接: https://www.imdb.com/title/tt31844586/
- 来源页面: https://tophub.today/
- 状态码: 202

## 抽取文本预览

AwsWafIntegration.saveReferrer();
        AwsWafIntegration.checkForceRefresh().then((forceRefresh) => {
            if (forceRefresh) {
                AwsWafIntegration.forceRefreshToken().then(() => {
                    window.location.reload(true);
                });
            } else {
                AwsWafIntegration.getToken().then(() => {
                    window.location.reload(true);
                });
            }
        });

JavaScript is disabled

In order to continue, we need to verify that you're not a robot.
        This requires JavaScript. Enable JavaScript and then reload the page.