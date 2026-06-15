# 深度分析Sorry勒索软件的加密实现与行为特征-安全KER - 安全资讯平台

- 原始链接: https://www.anquanke.com/post/id/315390
- 来源页面: https://tophub.today/
- 状态码: 200

## 抽取文本预览

首页

阅读

安全资讯

安全知识

安全工具

活动

社区

学院

安全导航

内容精选

专栏

精选专题

安全KER季刊

360网络安全周报

深度分析Sorry勒索软件的加密实现与行为特征

阅读量

706643

发布时间 : 2026-04-29 13:32:51

x

译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

Sorry勒索软件攻击事件

Sorry勒索软件自今年3月现身以来，利用各类常见企业软件漏洞发起攻击，能够远程加载攻击载荷，并展现出跨平台的勒索攻击能力。

本周，360反病毒团队持续收到与Sorry勒索软件相关的样本反馈与攻击告警信息，本轮勒索攻击的峰值集中爆发于4月中旬的两个周末。

结合样本逆向分析、加密文件结构还原及攻击行为链追踪，本次事件呈现出明显的“利用漏洞自动批量投放”与“目标文件定向加密”的攻击模式。从技术实现角度看，该家族采用分层密钥封装设计。即以RSA+RSA+AES-GCM 的算法组合方案实现文件加密与密钥保护操作。这一设计在兼顾了批量加密速度的同时，也大幅提高了受害者在无密钥的情况下想要破解算法直接恢复文件的难度。

此外，样本在运行时会主动收集主机标识信息，包括但不限于主机名称与基于当前设备环境特征计算出的“host_hash”值，并将其写入相关数据结构中，供攻击运营侧对受害主机与加密会话进行追踪管理。

综合来看，该变种具备完整的工程化实现。

其整体完成度较高，建议广大安全厂商将本次事件列为中高危等级的勒索事件，启动相应的分级响应流程。同时结合其在周末假期较为活跃的特性，对五一假期期间极有可能出现的新一轮攻击高峰做好安全防护预案。

本轮勒索事件攻击流程

本轮的Sorry勒索软件的典型攻击进程链如下：

图1. 攻击进程链示例

而该勒索软件的加密逻辑流程则如下图所示：

图2. 加密流程示意图

我们的分析人员综合完整的入侵、加密链条并结合我们的技术分析与解决方案，厘清了Sorry勒索家族完整的加/解密流程示意图，供大家更加直观地理解本轮攻击的总体情况。

图3. Sorry勒索软件攻击概况

勒索样本技术分析

环境初始化

我们以一个典型的勒索软件样本为例，其在运行后会首先停止MSSQL的相关服务。在诸多数据库服务中，勒索软件唯独停止了MSSQL相关服务，可见其勒索目标对服务器系统的针对性极强。

图4. 定向关闭MSSQL服务

而该样本所要加密的文件扩展名完整列表如下：

db、db3、db_journal、dbf、dbx、fdb、mdb、mdf、ndf、sql、sqlite、sqlite3、sqlitedb、ldf、sdf、3db、accdb、accde、accdr、accdt、bdb、edb、adf、dbb、bak、doc、docx、docb、docm、dot、dotm、dotx、pdf、txt、rtf、odt、ods、odp、ott、xls、xlsx、xlsb、xlsm、xlt、xltm、xltx、ppt、pptm、pptx、pot、potm、potx、pps、ppsm、ppsx、ppam、psd、ai、eps、svg、png、jpg、jpeg、gif、bmp、tiff、tif、ico、raw、cr2、nef、orf、dng、raf、arw、webp、fpx、dwg、dxf、skp、indd

在加密扩展名的列表外，为避免不必要的系统异常导致加密失败，勒索软件还排除了部分文件的路径、文件名及扩展名。

被排除的文件名及扩展名如下：

thumbs.db, netuser.dat, autorun.inf, iconcache.db, bootfont.bin, desktop.ini, pagefile.sys, .ds_store, .sorry, readme.md

被排除的目录、路径关键词如下

:\windows, \git\mingw64, \git\usr, \go\src, \go\pkg\mod, \java\jdk, \vmware\drivers, \program files\vmware, \inetpub\temp\apppools, programdata, efi.boot, efi.microsoft, all users, node_modules, .git, recycle.bin, system volume information, .trash, .cache, __pycache__, ieidcache, \appdata, .recovery, local settings, site-packages, test_importlib

图5. 前期初始化代码