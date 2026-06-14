# 挑战给历史故事打tag（标签2）_哔哩哔哩_bilibili

- 原始链接: https://www.bilibili.com/video/av116740314957040/
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

挑战给历史故事打tag（标签2）

全站排行榜最高第87名

123.0万

2202

2026-06-13 10:03:07

含虚构演绎内容

未经作者授权，禁止转载

12.6万

2516

1.3万

7402

-

学习

娱乐

历史

生活记录

挑战

故事

历史故事

混饭达人

发消息

个人就是比较擅长胡说八道
合作：2984568752@qq.com
更多请搜索【送饭达人】
微博@混饭达人是我

关注 103.3万

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
          fu