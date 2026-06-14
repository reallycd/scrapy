# 谁是猜价超人？_哔哩哔哩_bilibili

- 原始链接: https://www.bilibili.com/video/av116696325033953/
- 来源页面: https://tophub.today/
- 状态码: 200

## 抽取文本预览

首页

番剧

直播

游戏中心

会员购

漫画

赛事

投稿

谁是猜价超人？

第377期每周必看

244.5万

2220

2026-06-05 17:00:00

未经作者授权，禁止转载

11.3万

1.5万

1.6万

969

本节目是5月31日小潮院长直播幕后采访！
视频内容纯属娱乐，不要当真～
欢迎关注！一键三连也拜托了！！

上淘宝用国补买数码家电

搞笑

#天猫趣测实验室#

#天猫618发新券现货低至73折#

小杨

小潮院长

啊吗粽

Lks

伢伢gagako

杜海皇

创作团队

3人

小杨Johnson

UP主

杜海皇

参演

天猫

赞助商

var vd = window.__INITIAL_STATE__ && window.__INITIAL_STATE__.videoData
        var user = window.__INITIAL_STATE__ && window.__INITIAL_STATE__.user
        if (typeof window['nano'] === 'undefined') {
        } else {
          function gqs(name) {
            var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)");
            var r = window.location.search.substr(1).match(reg);
            if (r != null) {
              return unescape(r[2])
            }
            return null
          }
          function getTidInfo(channel, tid) {
            if (!channel || !tid) return null
            const len = channel.length
            for (let i = 0; i < len; i++) {
              if (!channel[i] || !channel[i].sub) continue
              const sLen = channel[i].sub.length
              for (let j = 0; j < sLen; j++) {
                if (tid === channel[i].sub[j].tid) {
                  return {
                    name: channel[i]['name'],
                    route: channel[i]['route'],
                    tid: channel[i]['tid'],
                    url: channel[i]['url'],
                    subName: channel[i].sub[j]['name'],
                    subRoute: channel[i].sub[j]['route'],
                    subUrl: channel[i].sub[j]['url'],
                    subTid: channel[i].sub[j]['tid']
                  }
                }
              }
            }
            return null
          }
          function getUpStaffs(staffData) {
            if (!staffData || !staffData.length) return null
            return staffData.map(item => {
              return {
                mid: item.mid,
                name: item.name,
                face: item.face,
           