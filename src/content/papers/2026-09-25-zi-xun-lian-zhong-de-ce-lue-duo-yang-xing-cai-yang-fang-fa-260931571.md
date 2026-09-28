---
title: Strategically Diverse Sampling for Self-Training
title_zh: 自训练中的策略多样性采样方法
authors:
- Alexander Gurung
- Esmeralda S. Whitammer
- Mirella Lapata
affiliations:
- School of Informatics, University of Edinburgh
arxiv_id: '2609.31571'
url: https://arxiv.org/abs/2609.31571
pdf_url: https://arxiv.org/pdf/2609.31571
published: '2026-09-25'
collected: '2026-09-28'
category: Training
direction: LLM 自训练数据构建与采样
tags:
- self-training
- strategic diversity
- sampling
- LLM
- reasoning
one_liner: 提出策略多样性采样，证明解法多样性比正确性和教师规模对自训练更关键
practical_value: '- 构建 SFT/蒸馏数据时不要只按正确性过滤，可以先用模型生成多个高层策略（例如基于价格、用户画像、场景），再展开成完整轨迹，避免同一策略的表面变体；在电商训练
  LLM 生成推荐理由、query 改写或 Agent 规划时，能显著提升困难 case 上的泛化。

  - 错误但多样的轨迹也有价值：如果缺乏大规模教师标注，可以用小模型自己采样并保留多样化的错误中间步骤，经过筛选或与正确样本混合训练，可能比直接蒸馏大模型更有效，降低
  API 成本。

  - 对 RLHF/GRPO 在线采样，策略多样性原则说明仅靠提高温度不够，需要显式鼓励策略分支；可以在 reward 中加入策略多样性项，或在 prompt 中要求给出多种解法，提升
  rollout 组的信息量。

  - 在生成式推荐中构建 Semantic ID 或多路径推理数据时，可将策略多样性作为数据增强与负样本构造的指导思想。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：LLM 训练与推理中的重复采样只有在响应具有实质差异时才有效，但自训练数据通常 IID 采样并按正确性过滤，导致模型已偏好策略被过度代表。

**方法关键点**：提出策略多样性（strategic diversity）作为构造自训练数据的原则；设计 GROOT，通过构建方法的分层树并采样不同路径生成策略多样数据；将 Verbalized Sampling 适配为产生无结构方法集。在竞争编程和 Next-Chapter Prediction 两个领域训练模型。

**关键结果**：策略采样训练的模型在困难任务上优于 IID 训练对照组，并提供更强的 RL 和 test-time scaling 初始化；最突出的是，Qwen3-4B 自训练在策略多样但错误的 traces 上，性能超过 235B 教师的 IID 蒸馏。这挑战了自训练数据有用性的传统假设，表明方法多样性可能比正确性或教师规模更重要。
