# 峰哥教大学生区分鹅腿鸭腿_哔哩哔哩_bilibili

- 原始链接: https://www.bilibili.com/video/av116736741480387/
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

峰哥教大学生区分鹅腿鸭腿

全站排行榜最高第33名

217.9万

6087

2026-06-12 18:55:23

未经作者授权，禁止转载

10.6万

1.0万

1.2万

2.0万

分享给你清华北大的同学，分享分享分享！

发现《蜜桃物语》

生活记录

清华

北大

鸭腿

烧鹅

峰哥

大学生

探店

Vlog

鹅腿

峰哥亡命天涯

发消息

纪录片导演，极限旅行家，国家一级登山运动员，自由潜运动员，滑翔伞飞行员，水下摄影师，B站知名孩子王

关注 271.0万

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
