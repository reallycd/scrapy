# 温 柔 的 洛 恩_哔哩哔哩_bilibili

- 原始链接: https://www.bilibili.com/video/av116730030458484/
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

温 柔 的 洛 恩

全站排行榜最高第26名

67.4万

610

2026-06-11 14:37:13

未经作者授权，禁止转载

13.4万

1.8万

4.1万

5740

我这把匕首可是涂了剧毒的。
感谢配音老师们！
洛恩：

@凉水咕咕咕

布伦妮、荧：

@云生s

米卡：

@赛可_Cykal

派蒙：

@青提Mio

绘画

手书

米卡

同人

搞笑

动画

布伦妮

二创

原神

洛恩

鼎芸

发消息

早睡觉！多出门！

关注 26.1万

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
       