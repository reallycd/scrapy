# 我以为我们大了 会看些成熟的东西_哔哩哔哩_bilibili

- 原始链接: https://www.bilibili.com/video/av116714595420698/
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

我以为我们大了 会看些成熟的东西

第377期每周必看

349.1万

1542

2026-06-08 21:01:24

27.1万

9412

4.0万

2.0万

-

拉力赛

WRC

QQ飞车

rc拉力

断空飘

RC

rc遥控车

拉力漂移

车瓶人虹泽RC

发消息

RC蚊车玩家 RC群➕v16616651305

关注 2.9万

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
         