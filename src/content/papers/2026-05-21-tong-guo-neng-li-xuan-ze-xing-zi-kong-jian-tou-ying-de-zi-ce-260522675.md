---
title: Self-Policy Distillation via Capability-Selective Subspace Projection
title_zh: 通过能力选择性子空间投影的自策略蒸馏
authors:
- Guangya Hao
- Yitong Shang
- Yunbo Long
- Zhuokai Zhao
- Hanxue Liang
affiliations:
- University of Cambridge
- HKUST
- University of Chicago
arxiv_id: '2605.22675'
url: https://arxiv.org/abs/2605.22675
pdf_url: https://arxiv.org/pdf/2605.22675
published: '2026-05-21'
collected: '2026-05-23'
category: Training
direction: LLM 自蒸馏 · 能力选择性子空间
tags:
- self-distillation
- low-rank subspace
- KV cache projection
- capability selection
- LLM training
- no external signal
one_liner: 无需外部信号的自我蒸馏方法，利用低秩能力子空间投影筛选自生成数据，显著提升LLM特定能力
practical_value: '- 在无外部信号（如标注数据、奖励模型）的场景下，可通过能力子空间投影从模型自身梯度中提取任务相关特征，实现自我蒸馏，适用于电商对话、推荐理由生成等任务的低成本优化。

  - 利用 KV 缓存投影到低秩能力子空间，相当于在自生成过程中隐式施加“能力滤波器”，可稳定提升特定能力（如商品推荐的合理性、数学推理），避免无关特征干扰。

  - 方法具备良好的域外泛化性（15% 提升），可跨任务迁移，适合在电商多任务场景下统一提升模型的多方面能力。

  - 工程实现上，只需在自生成前向过程中插入一次投影操作，与标准下一 token 预测损失结合，无需修改训练目标，易于集成到现有 LLM 微调流程中。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：现有 LLM 自蒸馏方法要么依赖外部信号（正确性过滤、执行反馈、奖励搜索）来筛选自生成数据，成本高且不适用于最强前沿模型；要么直接使用原始输出，通常领域特定且难以泛化。二者都面临共同弱点：自生成输出混杂了风格、格式、模型特定错误等与任务无关特征，稀释了目标能力的提升信号。

**方法关键点**：提出 Self-Policy Distillation (SPD)，无需任何外部信号，实现可泛化的能力选择性蒸馏。首先从模型在正确性定义 token 上的梯度中提取低秩能力子空间；然后在自生成阶段，将 KV 激活投影到这个子空间，再基于生成的原始输出使用标准下一 token 预测损失进行微调。投影操作相当于引导模型在生成时更聚焦于目标能力相关的特征。

**关键结果**：在代码生成、数学推理、多选 QA 等任务上，SPD 比无外部信号的自蒸馏方法最多提升 13%，比预训练基线最多提升 16%；域外泛化场景下性能提升 15%，展现出优异的泛化性。
