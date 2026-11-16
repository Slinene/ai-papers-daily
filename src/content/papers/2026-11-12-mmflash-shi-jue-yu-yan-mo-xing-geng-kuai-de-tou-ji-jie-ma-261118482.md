---
title: 'MMFlash: Faster Speculative Decoding for Vision-Language Models'
title_zh: MMFlash：视觉语言模型更快的投机解码
authors:
- Sicheng Feng
- Zigeng Chen
- Song Wang
- Gongfan Fang
- Xinchao Wang
affiliations:
- National University of Singapore
arxiv_id: '2611.18482'
url: https://arxiv.org/abs/2611.18482
pdf_url: https://arxiv.org/pdf/2611.18482
published: '2026-11-12'
collected: '2026-11-16'
category: Multimodal
direction: 多模态 VLM 投机解码加速
tags:
- Speculative Decoding
- VLM
- Multimodal
- Inference Acceleration
- Diffusion Drafter
- Sparse Attention
one_liner: 提出 MMFlash，通过自适应加权视觉依赖 token 和稀疏注意力加速 VLM 无损解码
practical_value: '- 业务中若用 VLM 做商品图文理解、视频广告审核或直播切片分析，可借鉴 speculative decoding 降低推理延迟；尤其长视频类任务，草稿+目标模型并行验证的架构收益明显。

  - 可复用视觉依赖度指标：用有无视觉输入下 next-token 分布的 KL 散度识别高视觉依赖 token，在训练 drafter 或蒸馏时对这些 token
  上调损失权重，能直接提升草稿接受率与加速比。

  - 长视频/多帧输入场景可引入稀疏注意力减少冗余 attention 计算，同时提升 drafting quality，适合商品视频、广告创意理解等多帧 VLM
  业务。

  - 工程上可借鉴 diffusion drafter 一次生成整块 token，在 SGLang 等推理框架上实现，相较 EAGLE-3 类头扩展方案加速效果更突出。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**  
VLM 自回归生成 token 顺序依赖，推理延迟高；投机解码通过轻量 drafter 草稿+目标模型并行验证来加速。现有 diffusion drafter（如 DFlash）主要面向纯文本，多模态草稿质量未充分探索。本文发现视觉依赖度高的 token 草稿接受率明显更低：最低视觉依赖四分位接受率 46%，最高仅 22%，且多模态训练后仍存在。

**方法关键点**  
提出 MMFlash，核心是自适应上调视觉依赖 token 的损失权重，改善 drafter 对这些 token 的预测。视觉依赖度通过有无视觉输入下 next-token 分布的 KL 散度衡量。针对长视频输入，进一步引入稀疏注意力减少冗余注意力计算，同时提升 drafting quality。

**关键结果**  
在多个多模态 benchmark 上取得 lossless 解码加速最高 3.58×，相较 EAGLE-3 和 DFlash 分别提升最高 195.4% 和 17.1%。
