---
title: 'FashionChameleon: Towards Real-Time and Interactive Human-Garment Video Customization'
title_zh: FashionChameleon：实时交互式人衣视频定制
authors:
- Quanjian Song
- Yefeng Shen
- Mengting Chen
- Hao Sun
- Jinsong Lan
- Xiaoyong Zhu
- Bo Zheng
- Liujuan Cao
affiliations:
- Xiamen University
- Alibaba Group
arxiv_id: '2605.15824'
url: https://arxiv.org/abs/2605.15824
pdf_url: https://arxiv.org/pdf/2605.15824
published: '2026-05-14'
collected: '2026-05-18'
category: Multimodal
direction: 交互式服装视频生成
tags:
- video generation
- garment customization
- autoregressive model
- KV cache
- real-time
- interactive
one_liner: 利用上下文学习和KV缓存调度实现单GPU 23.8FPS的实时流式服装切换视频生成
practical_value: '- **实时换装交互**：KV cache重调度（服装KV刷新、历史KV撤回、参考KV解缠）支持生成中途切换服装，可应用于电商直播换装、虚拟试衣间，无需重新生成整个视频。

  - **单服装数据训练**：通过故意制造参考图与服装图不匹配的Context Learning，仅需单服装视频即可学习运动一致性，降低多服装数据采集成本，适用于商品视频生成的快速冷启动。

  - **长视频外推一致性**：流式蒸馏中使用梯度重加权分布匹配，可借鉴于生成式推荐长序列行为建模，提升自回归生成稳定性。

  - **实时性工程参考**：单GPU 23.8FPS，比现有方法快30-180倍，为在线部署交互式生成提供了可行性设计思路，如商品流中动态换装展示。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：服装视频定制在电商直播、内容创作中具有商业价值，但现有方法无法实现低延迟、交互式换装，制约了实时应用。  
**方法**：提出FashionChameleon，核心为三项技术：(i) 在单服装视频上，通过In-Context Learning训练教师模型：保留图像到视频的训练范式，但让参考图与服装图内容不匹配，迫使模型隐式学习运动一致性；(ii) 流式蒸馏（Streaming Distillation with In-Context Learning）：结合上下文Teacher Forcing微调，并引入梯度重加权的分布匹配蒸馏，提升长视频外推一致性；(iii) 免训练的KV Cache重调度：生成过程中通过服装KV刷新、历史KV撤回和参考KV解缠，实现无缝服装切换，保持动作连贯。  
**结果**：首次支持交互式多服装视频定制和一致的长视频外推，单GPU上达23.8 FPS，比基线快30-180倍，生成质量保持与离线方法可比。
