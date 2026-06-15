# Gemini 3.5 发布｜Google I/O 2026 全整理 | 人人都是产品经理

- 原始链接: https://www.woshipm.com/ai/6399044.html
- 来源页面: https://tophub.today/
- 状态码: 200

## 抽取文本预览

首页

培训课程

名师辅导课

AI产品经理转岗特训营

BAT大厂产品运营体系课

B端C端全栈产品经理私教课

查看更多

个人自学课

互联网运营能力进阶

业务产品经理能力进阶

电商产品经理从入门到进阶

查看更多

企业内训课

数字化产品经理课

商业化产品实战课

数字化营销体系课

B端运营实战课

私域流量实战课

数据分析体系课

查看更多

分类浏览

业界动态

30982篇文章

产品设计

19414篇文章

产品运营

15261篇文章

产品经理

9583篇文章

职场攻略

5382篇文章

营销推广

4908篇文章

交互体验

3940篇文章

分析评测

3593篇文章

创业学院

2256篇文章

用户研究

1904篇文章

数据分析

1805篇文章

原型设计

1436篇文章

活动讲座

问答

企业培训

AI社区

摸鱼

HarmonyOS

搜索

APP

起点课堂会员权益

职业体系课特权

线下行业大会特权

个人IP打造特权

30+门专项技能课

1300+专题课程

12场职场软技能直播

12场求职辅导直播

12场专业技能直播

会员专属社群

荣耀标识

{{ userInfo.member ? '查看权益' : '开通会员' }}

发布

注册 | 登录

登录人人都是产品经理即可获得以下权益

关注优质作者

收藏优质内容

查阅浏览足迹

免费发布作品

参与提问答疑

交流互动学习

立即登录

首次使用？

点我注册

Gemini 3.5 发布｜Google I/O 2026 全整理

赛博禅心

2026-05-20

0 评论

5140 浏览

6 收藏

22 分钟

Google I/O 2026以「agentic era」为主题，带来了一场AI技术盛宴。从Gemini 3.5 Flash的速度突破到Omni多模态世界模型，从Antigravity 2.0的agent开发平台到Gemini Spark私人助理，Google正在重塑AI生态。本文深度解析9大产品矩阵如何重构搜索、电商、创意工具与科研边界，揭示下一代AI基础设施的竞争逻辑。

今天凌晨，Google 的年度发布会 I/O 2026，主题为「agentic era」，发布了大量新品。在看完整场发布会后，带来了如下整理，九个章节逐个展开

✦

Gemini 3.5 Flash

·谷歌家的最新模型，全面超越 3.1 Pro，速度 4 倍于同级模型

✦

Gemini Omni

·世界模型，从任意输入生成任意输出，Omni Flash 今天上线

✦

Antigravity 2.0

·agent-first 开发平台，桌面应用 + CLI + SDK + Managed Agents

✦

Gemini Spark

·私人 AI agent，7×24 后台执行，新 $100/月 Ultra 计划

✦

Search 改版

·新搜索框、Search Agents、Generative UI

✦

电商三件套

·UCP 协议 + AP2 支付 + Universal Cart 统一购物车

✦

Gemini App + 创意工具

·Neural Expressive 重设计、Daily Brief、Flow、Pics、Stitch、Docs Live

✦

智能眼镜

·Samsung + Gentle Monster + Warby Parker，音频眼镜秋季上市

✦

DeepMind 科学 + 安全

·Gemini for Science、WeatherNext、SynthID 扩展

01 Gemini 3.5 Flash

Gemini 3.5 Flash 是今天新发布的模型，同步上线进了 Gemini app、Search AI Mode、Gemini API 并成了的默认模型

至于 3.5 Pro，目前还在内测中，预计下个月放出

Benchmark

Terminal-Bench 2.1 编码

: 76.2%(3.1 Pro 70.3%)。

GDPval-AA 真实任务

: 1656 Elo(3.1 Pro 1314)，跳了一档。

MCP Atlas 工具调用

: 83.6%(3.1 Pro 78.2%)。

CharXiv 多模态推理

: 84.2%。几乎所有指标都超过了自家上一代旗舰 3.1 Pro

Gemini 3.5 Flash vs 3.1 Pro 各项 benchmark 对比

速度

输出速度

289 tok/s

，是同级别 frontier 模型的四倍。在 Antigravity