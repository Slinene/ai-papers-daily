---
title: Enhancing Multilingual Reasoning via Steerable Model Merging
title_zh: 通过可操控模型合并增强多语言推理
authors:
- Zhuoran Li
- Rui Xu
- Jian Yang
- Junnan Liu
- Zhijun Chen
- Qianren Mao
- Hongcheng Guo
- Jiaheng Liu
- Likang Xiao
- Ming Li
affiliations:
- Beijing University of Posts and Telecommunications
- Fudan University
- Beihang University
- Monash University
- Zhongguancun Laboratory
arxiv_id: '2606.19002'
url: https://arxiv.org/abs/2606.19002
pdf_url: https://arxiv.org/pdf/2606.19002
published: '2026-06-17'
collected: '2026-06-18'
category: LLM
direction: 可操控模型合并 · 多语言推理
tags:
- Model Merging
- Multilingual Reasoning
- Gated Cross-Attention
- Steerable
- LLM
one_liner: 提出可操控模型合并（ST-Merge），用门控交叉注意力动态调整多语言与推理模型的贡献，解决多语言推理中的模型冲突
practical_value: '- 在多语言业务（如跨境电商客服、多语言商品描述生成）中，可通过模型合并将领域模型与推理模型结合，避免独立部署多个模型，降低推理成本。

  - 门控交叉注意力机制可迁移至多专家模型集成，例如在推荐系统中融合用户理解模型和知识推理模型，根据请求内容动态分配权重。

  - 低资源语言表现提升明显：若业务需快速扩展小语种支持，可借助本方法合并已有高性能模型，减少微调数据需求。

  - 模型合并替代 pipeline 调用，能减少延迟与计算开销，适合对实时性要求高的 Agent 推理链路。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：多语言推理需要融合多语言模型的语言能力与推理模型的逻辑能力。简单的模型合并（如权重平均）无法动态平衡两个源模型，常因模型间冲突导致性能次优，且固定合并策略不能适应不同输入对模型偏好的差异。

**方法**：提出可操控模型合并（ST-Merge），核心是门控交叉注意力机制。该机制对两个源模型的输出表示进行加权或过滤，根据输入内容自适应地调节每个模型的贡献度，实现输入相关的“可操控”合并。训练时冻结源模型参数，仅学习门控模块。

**结果**：在4个多语言推理基准（含21种语言）上，ST-Merge一致超越多个强基线（如直接微调、固定合并方法），尤其在低资源语言上提升显著，证明了动态合并的有效性。
