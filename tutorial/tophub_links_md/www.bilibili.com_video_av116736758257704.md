# 路边一块，经过雕刻，包你看了过目不忘！愿你成为自己的太阳，无需借谁的光_哔哩哔哩_bilibili

- 原始链接: https://www.bilibili.com/video/av116736758257704/
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

路边一块，经过雕刻，包你看了过目不忘！愿你成为自己的太阳，无需借谁的光

全站排行榜最高第4名

409.5万

6694

2026-06-12 18:53:49

未经作者授权，禁止转载

22.9万

1.3万

2.3万

7625

祝你快乐！

手工

手工艺

雕刻

捡玉

小梨家的和田玉

发消息

拾荒创意雕刻 | 专业和田玉甄选
娱乐看视频，品质看直播
承蒙厚爱，被你喜欢
每晚9:30直播，么么哒❤️

关注 10.2万

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
          func