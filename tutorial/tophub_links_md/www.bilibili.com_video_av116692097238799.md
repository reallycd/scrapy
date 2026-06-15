# 城市大富翁（5）_哔哩哔哩_bilibili

- 原始链接: https://www.bilibili.com/video/av116692097238799/
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

城市大富翁（5）

第377期每周必看

492.0万

4.8万

2026-06-05 11:05:00

未经作者授权，禁止转载

19.9万

14.5万

5.0万

6051

城市大富翁第五期来了！全新的超有意思工厂地图！！
超刺激的6小时极限赚钱挑战！！
点赞30W，出发拍摄下一期！！！

搞笑小剧场

游戏

综艺

大富翁

生活

竞技

搞笑

挑战

鬼魂

爱回收

创作团队

4人

雨哥到处跑

UP主

啊吗粽

参演

力元君

参演

自来卷三木

参演

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
 