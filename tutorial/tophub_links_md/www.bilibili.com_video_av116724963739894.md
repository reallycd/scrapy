# 评论区摄影大赛之视觉创意篇第二弹开启，欢迎投稿好的作品会让更多人看到。_哔哩哔哩_bilibili

- 原始链接: https://www.bilibili.com/video/av116724963739894/
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

评论区摄影大赛之视觉创意篇第二弹开启，欢迎投稿好的作品会让更多人看到。

全站排行榜最高第35名

275.5万

610

2026-06-12 17:30:00

未经作者授权，禁止转载

13.7万

1346

7285

338

-

评论区摄影大赛

风景

摄影

哔哩哔哩评论区摄影展

照片点评

摄影恩哥

发消息

全网同名摄影恩哥
照片点评创作分享
职业摄影师
欢迎投稿玻璃心慎重
评论区随机挑选图片
好的作品会让更多人看到
商务yyl601781852

关注 121.5万

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
              }
            }