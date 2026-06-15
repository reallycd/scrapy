# 还能再来一次吗…嘻嘻_哔哩哔哩_bilibili

- 原始链接: https://www.bilibili.com/video/av116719964133557/
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

还能再来一次吗…嘻嘻

第377期每周必看

337.2万

3.6万

2026-06-10 12:00:00

未经作者授权，禁止转载

25.9万

12.5万

7.9万

4874

点赞40W更新下一期！
希望观众朋友们喜欢这个系列！
（希望你们喜欢，记得素质三连！）

京东618跟着UP买买买到夯

生活记录

搞笑

生活

高能

恶作剧

UP主综艺

京东618

来我家玩

小潮team

小潮院长

发消息

希望给你带来快乐 ｜ 商务合作请联系QQ2284771898

关注 1523.8万

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
  