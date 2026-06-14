# HuggingFace CEO力荐，Bengio团队也押注：这个1500美元训出的HRM模型，凭什么火了？ – 量子位

- 原始链接: https://www.qbitai.com/2026/06/435483.html
- 来源页面: https://tophub.today/
- 状态码: 200

## 抽取文本预览

首页

资讯

智能车

智库

活动

MEET大会

AIGC

扫码关注量子位

// $('.biaojiwei').click(function(){
            $('.biaojiwei').click(function(event){
                event.stopPropagation();
                $('#pophead').show();
            })
            $('.weixin_pop').click(function(){
                $('.weixin_pop').hide();
            })
        // })

< img id="wx_img" src="https://www.qbitai.com/wp-content/uploads/imgs/qbitai-logo-1.png" width="400" height="400">

HuggingFace CEO力荐，Bengio团队也押注：这个1500美元训出的HRM模型，凭什么火了？

鹭羽

2026-06-13

20:40:30

来源：

量子位

模型参数量只有1B

允中 发自 凹非寺

量子位 | 公众号 QbitAI

好家伙，这次不是模型圈自嗨。

一个训练成本约1500美元、参数量约1B、从零开始预训练的小模型，把

HRM

推到了下一代推理架构讨论的中心。

HuggingFace联合创始人兼CEO Clem Delangue亲自转发推荐。

图灵奖得主Yoshua Bengio作为共同作者参与的新论文，也走向了同一条latent recursive reasoning路线。

更反常的是，它不是蒸馏，不是微调，也不是在已有大模型能力上套壳。

它就是Sapient Intelligence发布的

HRM-Text

。

如果只看参数量，它很容易被写成一个熟悉的故事：“小模型又赢了。”

但HRM-Text真正值得注意的地方，不是小，也不是便宜。而是它背后那套HRM架构，正在问一个更底层的问题：

模型到底需要记住全世界，还是需要学会如何思考、如何查找、如何验证、如何行动？

过去几年，大模型行业的默认答案很简单：参数更多，数据更多，训练更久，Token更长。

HRM走的是另一条路。

它不是继续把模型做成一个越来越大的知识仓库，而是试图把模型做成一个更强的推理核心。

大模型像一个背着图书馆的学生，HRM更像一个会解题、会查资料、会复盘、会行动的人。

当然，真正让技术圈认真讨论HRM-Text的，不是一次转发，而是一组很反常的数字。

一个约

1B参数

模型，在MATH上拿到56.2，在GSM8K上拿到84.5，在ARC-Challenge上拿到81.9，在DROP上拿到82.2。

训练成本约

1500美元

，16块H100跑了不到两天。

没有post-training，没有RLHF，也没有依赖显式思维链数据。团队同步开放了论文、模型权重和预训练代码。

这意味着，HRM-Text不是在现有大模型能力上做包装，而是在基础预训练阶段，直接验证一种新的架构路线。

这不是又一个“小模型逆袭”的故事。更准确地说，它是一次推理模型的换脑实验：

不让模型说出更多思维链，而是让模型在开口之前，先在脑子里想完。

而这条路线，很快也出现在了更高层级的学术讨论中。

HRM-Text发布前后，图灵奖得主Yoshua Bengio作为共同作者参与发布了

《Generative Recursive Reasoning》

。论文提出的GRAM，在核心计算结构上高度复用了HRM的分层递归骨架：同样是高层状态、低层状态、双时间尺度、多轮递归更新，只是在此基础上进一步加入概率生成模块。

换句话说，Sapient不是等行业给出答案之后再追随，而是先把一个关键问题抛了出来，并率先拿出了可运行、可开源、可验证的模型系统：

模型能否在输出之前，通过潜空间中的多轮分层递归计算，完成更深层的内部推理？

HRM-Text的问题因此不只是：

一个1B模型为什么能做到这些benchmark？

更关键的问题是：

Sapient是否提前验证了一条下一代推理模型值得认真对待的新路线？

知识不等于智能，CoT也不等于思考

现在的推理模型，很多时候像是在“边说边想”。

Chain-of-Thought把推理过程写成一串token，让模型一步一步输出中间过程。

这当然有用，但问题也很明显：

Token越来越长，账单越来越高；中间一步错了，后面就可能一路错下去；更关键的是，推理过程被绑