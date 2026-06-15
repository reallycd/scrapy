# Claude Code 2026年最新保姆级安装指南 | 人人都是产品经理

- 原始链接: https://www.woshipm.com/ai/6337198.html
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

Claude Code 2026年最新保姆级安装指南

别惹CC

2026-02-03

0 评论

10267 浏览

10 收藏

10 分钟

Claude Code的官方限制正在被技术爱好者们逐个击破。本文手把手教你通过Node.js环境搭建、密钥配置修改、VS Code插件联动三大步骤，实现第三方模型的无缝接入。从DeepSeek到Poe API的实战配置，这套方法论将彻底释放AI编程工具的潜力。

本文将带各位读者一步步完成Claude Code的安装，并通过“魔改”配置解锁第三方端点支持，让你摆脱官方的限制，实现更灵活的 AI 编程体验。

一、环境准备：安装 Node.js

Claude Code 依赖 Node.js 环境，首先需要确保你的系统已正确安装 Node.js。

1.下载

访问 Node.js 官网 (https://nodejs.org/en/download)，下载适合你操作系统的版本。

2.验证安装

安装完成后，打开PowerShell (Windows) 或终端 (macOS/Linux)，输入以下命令检查版本，出现版本号即表示成功。

node -v

npm -v

二、安装Claude Code

截止本文发布的时候，最新版本2.1.19已经放弃了npm安装方式，所以通过npm安装的后续也不再自动更新。如果你以前是通过npm安装的，可以通过官方的命令升级成最新的原生版本。

claude install

最新的原生版本的安装方式大家根据自己的系统选择对应的命令即可（记得开启科学上网）。

# Mac用户

brew install claude-code

# Linux用户

curl -fsSL https://claude.ai/install.sh | bash

# Windows PowerShell用户

irm https://claude.ai/install.ps1 | iex

查看版本号

Claude –version

三、开启第三方端点配置

这是最关键的一步。默认情况下，最新版的Claude Code 仅支持官方模型。我们需要手动创建配置文件来通过“验证门槛”并开启第三方模型支持。此步骤包含两个部分的配置：

1.key类型配置

我们需要在 .claude文件夹中创建一个config.json文件。

文件路径如下

：

Windows

:

C:\Users\你的用户名\.claude\

macOS/Linux

:

~/.claude/

文件内容如下

：

{

“primaryApiKey”: “any-string-is-ok-here”

}

快速创建命令 (PowerShell)：

你也可以直接复制以下命令在 PowerShell 中运行，一键创建该文件：

$path = “$HOME\.claude”; if (!(Test-Path $path)) { New-Item -ItemType Directory -Path $path -Force }; Set-Content -Path “