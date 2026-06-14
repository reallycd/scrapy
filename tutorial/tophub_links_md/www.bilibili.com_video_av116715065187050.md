# 呃 你有点太重力了_哔哩哔哩_bilibili

- 原始链接: https://www.bilibili.com/video/av116715065187050/
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

呃 你有点太重力了

全站排行榜最高第50名

80.5万

705

2026-06-12 17:15:00

未经作者授权，禁止转载

7.9万

2.1万

3.5万

2712

专辑「二次元凶」收录曲《那太重了》 take it easy
作曲&编曲&混音&母带：Evalia-爱娃 
作词：小驴&Hanser
演唱：Hanser 
视频：瓷小鱼    画：小猪码头

发现《那太重了》

原创曲

二次元凶

hanser

音乐mv

创作团队

5人

hanser

UP主

Evalia-爱娃

作曲

瓷小鱼

视频制作

小猪码头

曲绘

围巾和棉服挂一起

作词

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
                f