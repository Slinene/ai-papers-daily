---
title: Maximizing Capacity Utilization of LoRA Adapters for Mitigating the Learning-Forgetting
  Trade-off
title_zh: 最大化LoRA适配器容量利用以缓解学习-遗忘权衡
authors:
- Tomohiro Sawada
- Kartik Goyal
affiliations:
- School of Interactive Computing, Georgia Institute of Technology
arxiv_id: '2611.17191'
url: https://arxiv.org/abs/2611.17191
pdf_url: https://arxiv.org/pdf/2611.17191
published: '2026-11-12'
collected: '2026-11-14'
category: Training
direction: LoRA 有效秩正则化与持续学习
tags:
- LoRA
- effective rank
- regularization
- continual learning
- PEFT
one_liner: 发现LoRA有效秩远低于配置秩，提出Rényi-2有效秩正则化提升容量利用并改善持续学习遗忘
practical_value: '- 在电商/搜索场景用 LoRA 微调 LLM 做生成式推荐、query 改写或 Agent 工具时，可在语言模型损失中加一个
  Rényi-2 有效秩正则项（λ≈0.01），无需 SVD，即可提升高秩 adapter 的容量利用率，且训练困惑度几乎不降。

  - 多领域/多任务持续微调同一基座模型时，该方法能缓解灾难性遗忘；有效秩可作为训练监控指标，帮助发现 adapter 容量浪费。

  - 对已有 LoRA 变体（如 DoRA、rsLoRA 等）也适用，可作为互补正则化组件嵌入现有 PEFT 流程，改动成本低。

  - rank 至少 16 时收益明显，适合广告/推荐领域语料混杂、持续更新的场景。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

动机：LoRA 在异构和持续学习设置下遗忘严重，学习-遗忘权衡差，常低于全参微调。作者发现标准 LoRA 更新的有效秩远低于配置秩，尤其高秩 adapter 未能充分利用容量，更新能量分布过窄。

方法：提出在语言模型损失中加入 Rényi-2 有效秩正则项，最大化 adapter 有效秩；该正则简单、稳定、可微、无需 SVD。同时建立容量最大化与范数有界更新的联系。

结果：在三模型混合域 rank 扫描（多随机种子）中，λ=0.01 使 Wiki 困惑度在 rank≥16 时均低于无正则 LoRA；训练困惑度改善或最多增加 0.02；单任务和调度实验显示学习与保留平衡依赖配置；多个已有 LoRA 变体也存在容量问题，本方法提供互补改进。结论：有效秩不仅是事后诊断指标，还可作为可训练目标，改善学习-遗忘前沿。
