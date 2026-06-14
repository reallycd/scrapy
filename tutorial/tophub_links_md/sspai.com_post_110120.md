# 来自九年前的远古音频兵器 - Xperia XZ Premium - 少数派

- 原始链接: https://sspai.com/post/110120
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

来自九年前的远古音频兵器 - Xperia XZ Premium

主作者

关注

纳兰音韵

新手上路

太阳伞下天然文静素材

纳兰音韵

关注

纳兰音韵

新手上路

太阳伞下天然文静素材

联合作者

关注

纳兰音韵

新手上路

太阳伞下天然文静素材

纳兰音韵

关注

纳兰音韵

新手上路

太阳伞下天然文静素材

05/25 05:43

Matrix 首页推荐

Matrix

是少数派的写作社区，我们主张分享真实的产品体验，有实用价值的经验与思考。我们会不定期挑选 Matrix 最优质的文章，展示来自用户的最真实的体验和观点。

文章代表作者个人观点，少数派仅对标题和排版略作修改。

前言

Android 设备的音频质量，一直是一个被人们津津乐道的话题。从早年的低质量 AudioFlinger 强制重采样和低精度音频衰减，到现如今的专用 AAudio 高性能输出。但因为 SoC 制造商和 OEM 仍然对 HAL 有较大的自定义能力，不同设备上的音频质量区别仍旧非常巨大。比如联发科的某些设备会将 audioeffect 集成进 vendor 挂载在 AudioFlinger 上而无法关闭，高通设备的 Direct HD 可以在受支持的设备上绕过 effect chain 输出原始音频。

换句话说，Android 早已具备高质量音频输出的能力，但真正愿意保留声音原貌的厂商，却越来越少了。现在更流行的做法，则是先将所有音频统一送入 mixer 与 DSP 处理链路，再进行输出，在这里进行处理之后再输出。所谓的处理，大多是一些所谓的杜比音效，响度均衡，系统 EQ 甚至 OEM 音效。初衷确实是为了提升用户体验，但为此强行放弃了高保真音频，真的值得吗？

正巧在几个月前，我购入了一台银色镜面的 Sony Xperia XZ Premium。也正是从那时开始，我重新开始思考 Android 的声音到底应该是什么样子。

一睹机皇的风采：硬件配置

XZP 搭载了高通 msm8998 SoC，也就是高通骁龙 835。它的硬件基础或许算不上优秀，它没有专用的 DAC，而是使用了高通 Aqstic™ WCD9335 作为 DAC。

这颗 DAC 本身支持的最高音频规格来到了 32bit/384 KHz (PCM) 。支持 DSD64/128、FLAC、ALAC、LPCM 等常见的无损格式。

如果你对硬件感兴趣，这是一些来自其它网站的数据：

44.1kHz

48kHz

96kHz

Z3

测试项目,dB（A）

-96.0

-96.7

-100.5

-86.6

噪声水平，DB（A）

95.8

96.6

105.1

86.5

总谐波失真,%

0.0016

0.0069

0.0067

0.012

互调失真，%

0.0055

0.0050

0.0023

0.019

立体声分离度，dB

-90.0

-90.3

-88.5

-86.4

上述数据以及更详细的硬件测试，见

Soomal

我并不是太懂这方面，所以不说太多了，本文重点也不在此。

DIRECT 和 MIXER：把原始音频送进 HAL

这里测试了三 (四) 种不同的播放器，分别是：

Apple Music（集成解码器）

Sony Music（MediaFramework）

Poweramp（集成 FFmpeg）

Sony Music Center（Exclusive）

经过对比，发现输出类型大概可以分为四类：

MIXER

DIRECT，经过了索尼的 effectchain

DIRECT，高通 DIRECT HD，跳过了 effect chain

OFFLOAD，非 PCM 且支持的格式会被直接送进 DSP

这是来自

audio_output_policy.conf

的原始信息：

outputs {
  default {
    flags AUDIO_OUTPUT_FLAG_PRIMARY
    formats AUDIO_FORMAT_PCM_16_BIT
    sampling_rates 48000
    bit_width 16
    app_type 69937
  }
  proaudio {
    flags AUDIO_OUTPUT_FLAG_FAST|AUDIO_OUTPUT_FLAG_RAW
    fo