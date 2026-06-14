# OpenClaw：高强度使用两周，这个 AI 工具颠覆了我的工作流 - 少数派

- 原始链接: https://sspai.com/post/106232
- 来源页面: https://tophub.today/
- 状态码: 200

## 抽取文本预览

共创

PRIME

Matrix

栏目

Pi Store

无需申请，自由写作

任何用户都可使用写作功能。成功发布 3 篇符合基本规则的内容，可成为正式作者。

了解更多

共创

PRIME

Matrix

栏目

Pi Store

OpenClaw：高强度使用两周，这个 AI 工具颠覆了我的工作流

主作者

关注

Vanilla

少数派作者

whoops

Vanilla

关注

Vanilla

少数派作者

whoops

联合作者

关注

Vanilla

少数派作者

whoops

Vanilla

关注

Vanilla

少数派作者

whoops

02/11 17:47

我相信很多人在最近一个月都被一款叫作 OpenClaw 的 AI 工具刷屏了。据社交平台发布和社区早期讨论，这款工具曾经历过多次命名调整，最终定名为 OpenClaw。在更名期间，还发生了社交平台账号被恶意抢注，并通过发行名为 $CLAWD 的 meme 币来「割韭菜」的事情，让 OpenClaw 这款工具的诞生过程更加充满了戏剧性。

对于像我种典型的移动互联网时代用户，遇到问题时的下意识举动就是寻找各种软件来满足自己的需求。在使用了两周多的 OpenClaw 后，我发现自己的习惯悄然发生了变化，一步一步成功地将自己的工作流在 OpenClaw 上重新构建后，OpenClaw 已经成为了我解决数字生活需求的第一选择。

在这篇文章中，我将从 OpenClaw 是什么、怎么装开始说起，并分享一些我自己使用的场景和技巧，希望对有兴趣尝试的人能提供一些帮助。

OpenClaw 是什么？

OpenClaw 并非一个单纯的大语言模型，也不是一个单纯的 Coding CLI，它其实是一个运行在本地的「数字生命中枢」，可以成为我们的个人 AI 助手，也可以胜任公司中的部分工作岗位。它支持通过 Skills / 工具集成扩展能力（含 MCP 场景），通过驻留在 Mac mini 或服务器上的 Gateway 实现跨平台接入与异步调度。无论身处何地，你都能通过各种即时通讯工具与之即时互动。

与此同时，所有在 OpenClaw 中产生的记忆、文件索引和个人习惯都储存在你自己的本地工作区（Memory.md、索引数据库、Skills 脚本等）中，在本地部署场景下，你对数据有更高的可控性，也更容易做权限和备份管理。

OpenClaw 怎么装？

安装 OpenClaw 的容器有很多种选择，目前最热门的是 Mac mini，原因主要有三个：一是支持 7×24 小时不间断运行且功耗低；二是在 Apple 生态中可以方便地调用 Apple Reminders、Apple Notes、Apple Calendar 等相关 Skill；三是硬件配置本身性价比较高，16 + 256GB 的版本在电商平台的售价虽然常有波动，但是截至写作时，不少渠道已接近 3000 元档，而 M4 芯片和 16GB 起步的统一内存也让电脑性能有上佳的表现。

除了 Mac mini，OpenClaw 其实也支持安装到 Windows、Linux 等不同操作系统的设备上。如果你不想把 OpenClaw 安装到本地，各大云服务厂商（比如说腾讯云、阿里云、Cloudflare、Digital Ocean 等）都推出了专属的云服务器镜像，同样支持快速部署 OpenClaw。

OpenClaw 总体上分为了 One-liner、npm、Hackable 和 macOS 客户端四种安装方式，其中 One-liner 可以切换 macOS / Linux 和 Windows 等平台，npm 可以分为 npm 和 pnpm 两种方式，Hackable 也分为 installer 和 pnpm 两种方式，每种分发途径都对应了不同的终端指令，大家根据自己的需求选择安装即可。

安装完成后，OpenClaw 会自动执行

openclaw onboard --install-daemon

指令来进行具体配置，一般情况下选择默认选项即可，而需要你具体配置的主要是四个部分：

第一个部分，选择 AI 服务提供商和具体使用的模型。大部分服务提供商提供了 OAuth 授权认证和直接输入 API 这两种方式，对应了不同的计费方式。

以 Google Gemini 模型为例，如果你选择 OAuth 认证，那么就可以通过 Antigravity 来使用 Google Gemini 3 Pro、Google Gemini 3 Flash、Claude Opus 4.5 和 Claude Sonnet 4.5 等模型，每五个小时刷新一次额度；如果你选择了 Google API，那么就需要到 