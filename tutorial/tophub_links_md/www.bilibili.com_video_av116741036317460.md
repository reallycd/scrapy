# 华强买瓜，但是艺术家_哔哩哔哩_bilibili

- 原始链接: https://www.bilibili.com/video/av116741036317460/
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

华强买瓜，但是艺术家

全站排行榜最高第83名

126.9万

1308

2026-06-13 13:01:47

含AI生成内容

未经作者授权，禁止转载

6.5万

1.2万

1.3万

5851

内容AI生成，仅供娱乐，请勿过度解读

AI音乐宇宙

搞笑

艺术家

鬼畜

有一个人前来买瓜

AI整活

AI名场面

抽象

华强买瓜

快乐阿托

发消息

主做鬼畜剧场，仅在b站投稿

关注 25.4万

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
            })
          }
          function getP