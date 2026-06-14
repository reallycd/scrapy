# 景泰蓝_哔哩哔哩_bilibili

- 原始链接: https://www.bilibili.com/video/av116725265795009/
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

景泰蓝

全站排行榜最高第60名

81.7万

1354

2026-06-11 21:00:00

未经作者授权，禁止转载

8.7万

2.5万

1.0万

1236

景泰蓝，学名铜胎掐丝珐琅，因兴盛于明代景泰年间而得名，距今已有六百多年历史

发现《重门暮雪香——金庸小说人物群像》

手工

原创

手工艺

非物质文化遗产

记录

景泰蓝

彭南科

发消息

守一方天地，拥一颗匠心，做乡村守护人

关注 87.1万

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
          function 