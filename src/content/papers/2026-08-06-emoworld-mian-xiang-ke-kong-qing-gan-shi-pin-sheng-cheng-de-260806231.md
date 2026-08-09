---
title: 'EmoWorld: A Decoupled Affective Field for Controllable Emotional Video Generation'
title_zh: EmoWorld：面向可控情感视频生成的解耦情感场
authors:
- Bingyuan Wang
- Baistan Zhyldyzbekov
- Kunyu Feng
- Zeyu Wang
affiliations:
- The Hong Kong University of Science and Technology (Guangzhou)
- The Hong Kong University of Science and Technology
arxiv_id: '2608.06231'
url: https://arxiv.org/abs/2608.06231
pdf_url: https://arxiv.org/pdf/2608.06231
published: '2026-08-06'
collected: '2026-08-09'
category: Multimodal
direction: 可控情感视频生成 · 解耦情感场
tags:
- Emotion Control
- Video Generation
- Diffusion Transformer
- Decoupled Field
- Flow Matching
one_liner: 将情感因素解耦为氛围、语义线索与时间进程，在冻结视频扩散变换器中实现精细化情感控制
practical_value: '- **冻结大模型 + 轻量控制向量**：抽取 layer-wise affect directions 并注入隐藏状态，不改动生成器参数。类似思路可复用到电商文案/广告图生成，快速调节情感基调（温馨、紧迫、高端）而不重训模型。

  - **因素解耦独立调节**：VAS（氛围）、SAS（语义线索）、TAS（时间过渡）分模块控制，可借鉴到生成式商品推荐中，分别控制产品卖点、场景氛围、促销节奏的生成。

  - **可重用线索库**：准备阶段构建 reusable cue library，推理时按需组合。适用于批量生成多风格素材的场景，如节日大促自动换肤、多套广告创意快速迭代。

  - **时序情感弧线控制**：TAS 通过插值残差场实现情感平滑过渡，可启发电商直播话术或短视频脚本的情感递进设计，增强内容感染力。'
score: 6
source: arxiv-cs.CV
depth: abstract
---

**动机**：现有视频生成器将全局氛围、情感语义线索和时间演进混杂在单一文本条件中，无法精细控制同一场景的不同情感表达，限制电影预演、虚拟制作等应用。

**方法**：提出 EmoWorld，在冻结的流匹配视频扩散 Transformer（Video DiT）中解耦情感场。准备阶段从几何一致的中性与情感编辑全景图中提取 layer-specific affect directions 和 reusable cue library。推理时三个模块：① Visual Atmosphere Steering (VAS) 将氛围方向注入隐藏状态；② Semantic Affective Steering (SAS) 隔离可缩放的提示残差以强调情感语义线索；③ Temporal Affective Steering (TAS) 在去噪步与视频帧维度上插值端点残差场，实现情感平滑过渡。

**结果**：基于 Wan2.2，VAS 使目标情感对齐提升 19%，时间波动代理降低 48%；SAS 使对齐提升 37%，检测到的情感线索增加 36%；TAS 在过渡单调性上比最强基线高 15%。框架支持 27 种情感、文生视频与图生视频，可移植到多种 Video-DiT 骨干，且无需更新参数即支持相机条件组合。
