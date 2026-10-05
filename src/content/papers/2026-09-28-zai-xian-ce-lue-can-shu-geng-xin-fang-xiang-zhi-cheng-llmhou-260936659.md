---
title: On-Policy Parameter Update Direction Underlies Generalization in LLM Post-Training
title_zh: 在线策略参数更新方向支撑LLM后训练泛化
authors:
- Shufan Shen
- Zhongni Hou
- Junshu Sun
- Yufei Zhang
- Wei Lin
- Guojun Yin
- Qingming Huang
- Shuhui Wang
affiliations:
- State Key Lab. of AI Safety, Institute of Computing Technology, Chinese Academy
  of Sciences
- University of Chinese Academy of Sciences
- Meituan
arxiv_id: '2609.36659'
url: https://arxiv.org/abs/2609.36659
pdf_url: https://arxiv.org/pdf/2609.36659
published: '2026-09-28'
collected: '2026-10-05'
category: Training
direction: LLM后训练·参数更新方向约束
tags:
- OPSFT
- on-policy
- SFT
- generalization
- parameter update direction
- post-training
one_liner: 提出OPSFT：约束SFT沿在线策略累积更新方向更新，仅少量在线策略步即可将泛化优势迁移给监督微调
practical_value: '- 在需要保留在线策略泛化能力但训练预算有限的场景，可先跑少量 on-policy 步骤提取累积参数更新方向，再用 OPSFT
  将大规模 SFT 更新投影到该方向，避免全量线上采样成本。

  - 对已有高质量人工标注/线上反馈轨迹的电商导购 Agent 或文案生成模型，可将这些轨迹作为 OPSFT 的 SFT 数据继续训练，不会破坏之前在线策略学到的探索与泛化能力。

  - 该方法提供了一种从在线策略到离线 SFT 的“方向蒸馏”机制，适合工业界在 RLHF/DPO 与 SFT 之间做低成本的训练范式切换。

  - 注意该方法主要针对 LLM 后训练流程，不直接改变推荐/召回模型架构；若业务中需要频繁迭代生成式模型，可在训练 pipeline 中作为正则项复用。'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
在线策略后训练泛化强但成本高；SFT 高效且可利用高质量轨迹，但泛化差。已有工作只把参数更新行为当副产物，未将其转化为可迁移的优化原则。

### 方法关键点
- 理论/实验分析发现：SFT 沿一致方向更新参数，而 on-policy 训练中不断调整方向；因此关注每个参数的累积更新方向。
- 提出 On-Policy direction-constrained Supervised Fine-Tuning (OPSFT)，先用 on-policy 训练识别累积更新方向，再约束 SFT 更新在该方向上进行。
- 仅需少量 on-policy 步即可识别支持强泛化的方向，之后可用高质量 SFT 轨迹继续训练而不破坏 on-policy 学到能力。

### 关键结果
实验表明，OPSFT 能将 on-policy 范式的泛化优势迁移到 SFT；一旦识别出有效更新方向，即使 SFT 也能获得强泛化，且训练效率高。
