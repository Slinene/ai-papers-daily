---
title: 'Look Only When Needed: Certificate-Guided Visual Routing for Efficient Diffusion
  VLMs'
title_zh: 需要时才看：基于证书引导的视觉路由实现高效扩散视觉语言模型
authors:
- Donghyeon Cho
- Joowon Kim
- Seungho Shin
- Eunho Yang
affiliations:
- KAIST
- AITRICS
arxiv_id: '2610.36671'
url: https://arxiv.org/abs/2610.36671
pdf_url: https://arxiv.org/pdf/2610.36671
published: '2026-10-26'
collected: '2026-11-01'
category: LLM
direction: 扩散视觉语言模型高效解码
tags:
- diffusion VLM
- visual routing
- efficient decoding
- token pruning
- KV cache
- certificate routing
one_liner: 提出 LOWN 解码方法，每步自适应决定是否处理图像，平均省 65% 解码 FLOPs 而保留 99.6% 分数
practical_value: '- 多模态 LLM 在商品图像理解、广告文案生成等场景中，视觉 token 占输入 90% 以上，且不是每一步都需要细看图像。可借鉴
  LOWN 的路由思想：先用无图像轻量预测，只有与历史图像条件预测产生分歧时才重新处理图像，避免重复编码视觉特征。

  - 工程实现上，LOWN 无需训练、无需调阈值，可以直接插入现有扩散解码流程，适合快速验证收益。结合 KV cache 和视觉 token pruning 可进一步降低在线推理成本。

  - 在电商搜索推荐 Agent 中，多模态状态下视觉内容不是每个 reasoning step 都要消费。可设计类似的“证书”机制，复用之前的视觉理解结果，只在置信度下降时触发视觉重算，降低长程任务推理延迟。

  - 该方法证明了自适应路由比固定 schedule 更有效，因为不同输入对视觉依赖差异很大。业务上可对商品主图、详情图、视频帧按需求动态分配算力，而不是一刀切缩图或抽帧。'
score: 6
source: huggingface-daily
depth: abstract
---

## 动机
扩散视觉语言模型（DVLMs）在每一步去噪时处理完整输入，而视觉 token 占输入的 89–97%，导致大量重复计算。视觉 token 剪枝能减少部分 token，但仍每步处理剩余图像，且丢失信息。

## 方法关键点
作者首先统计 LLaDA-V 在有无图像时预测差异，发现只有 22.8% 的步骤移除图像会改变被 unmask 的 token，说明图像并非每步必需。基于此提出 LOWN：
- 每步先用无图像输入预测掩码 token；
- 若该预测与最近一次图像条件预测一致，则“证书”之前结果可复用，无需处理图像；
- 不一致时才重新处理图像；
- 证书覆盖的 token 数量决定该步 unmask 多少 token。
该机制自适应不同 benchmark 对图像的依赖，无需训练或调阈值。

## 关键结果
在十个 benchmark 上，LOWN 平均仅用 35.3% 的解码 FLOPs，保留 LLaDA-V 99.6% 的分数；可跨 LLaDA-based DVLMs 泛化，与视觉 token pruning 正交，且在 KV cache 下进一步提速。
