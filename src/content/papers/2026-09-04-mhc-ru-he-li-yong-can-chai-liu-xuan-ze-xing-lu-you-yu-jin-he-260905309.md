---
title: How Does mHC Use Its Residual Streams? Selective Routing and Near-Identity
  Mixing
title_zh: mHC 如何利用残差流：选择性路由与近恒等混合
authors:
- Pengxiang Zhao
- Xing Li
- Xianzhi Yu
- Wei Guo
- Zhenhua Dong
affiliations:
- Huawei Technologies Co., Ltd.
arxiv_id: '2609.05309'
url: https://arxiv.org/abs/2609.05309
pdf_url: https://arxiv.org/pdf/2609.05309
published: '2026-09-04'
collected: '2026-09-08'
category: LLM
direction: 多流残差架构机制分析
tags:
- mHC
- Residual Streams
- Sparse Routing
- LLM Architecture
- Model Analysis
- DeepSeek-V4-Flash
one_liner: 揭示 DeepSeek-V4-Flash 四流 mHC 路由集中、晚期混合近恒等，稀疏化与恒等替换几乎不损性能
practical_value: '- 若团队在推荐/搜索/Agent 中采用或预研 Hyper-Connections/mHC 等多流残差 LLM，可直接尝试“逐
  token 保留 top-3 路由权重”做稀疏化推理：在 DeepSeek-V4-Flash 上 PPL 最多上升 2.7%，平均分变化 ≤0.4 分，延迟/显存可降，适合线上排序或生成式推荐的低延迟约束。

  - 对深层（22-42）多流混合器，可考虑替换为恒等或单流结构，C4 PPL 仅 +1.9% 且六任务平均分不变；可用于模型压缩、蒸馏学生模型或减少多流通信，尤其适合广告/电商场景中需要轻量部署的
  LLM。

  - 早期混合器的“站点结构”比 token 级动态更重要（固定到诊断均值 PPL +0.2%、平均分 -0.25pp），意味着在量化、缓存或离线计算中，可对早期混合器按层预计算固定权重，减少在线
  token-wise 计算。

  - 注意：该结论来自 DeepSeek-V4-Flash 单一模型，迁移前应先在自己的模型上做 effective stream counts 与 cosine
  诊断；若未使用多流残差架构，可借鉴的分析方法较有限，主要是模型冗余与路由稀疏化的诊断思路。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

动机：Hyper-Connections/mHC 将残差流从 1 扩到 n，但训练后模型是否真正利用多流容量、路由模式如何、晚期混合是否必要，尚未明确。
方法关键点：以 DeepSeek-V4-Flash 四流为例，用 effective stream counts、跨流残差权重、流间 cosine similarity 度量读写广度、混合强度与表示差异；并通过替换混合器为恒等、固定混合器到均值、保留 top-3 路由权重等干预实验验证功能。
结果：典型注意力/FFN 站点有效使用约 2 个流，主导流随层变化，流表示保持方向差异；残差混合早期较强，22-42 层近似逐流独立传递。晚期混合器换恒等后 C4 困惑度仅 +1.9%，六任务平均分基本不变；早期混合器换恒等则 PPL +41%。固定早期混合器到诊断均值 PPL +0.2%、平均分 -0.25pp，说明站点结构比 token 级变化更重要。每个 token 保留 top-3 路由权重，PPL 最多 +2.7%，平均分变化 ≤0.4 分。
