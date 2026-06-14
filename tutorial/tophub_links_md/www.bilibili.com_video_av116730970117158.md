# 当你因为上学几年没玩手机_哔哩哔哩_bilibili

- 原始链接: https://www.bilibili.com/video/av116730970117158/
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

当你因为上学几年没玩手机

全站排行榜最高第49名

273.3万

383

2026-06-11 18:23:35

含虚构演绎内容

18.9万

1368

8778

2111

-

搞笑小剧场

原创

手机

学生

刘鸿哥哥

发消息

全网同名：刘鸿
商务（个人）：Cartier75052

关注 58.9万

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
          function getPlayerViewInfo(state) {
            if (!state) re