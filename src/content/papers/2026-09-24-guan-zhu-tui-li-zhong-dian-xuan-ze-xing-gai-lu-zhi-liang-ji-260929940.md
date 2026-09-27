---
title: 'Mind What Matters for Reasoning: Aligning Cross-Modal Attention via Selective
  Probability Mass Concentration'
title_zh: 关注推理重点：选择性概率质量集中的跨模态注意力对齐
authors:
- Jiaqi Deng
- Zonghan Wu
- Zhan Heng
- Xiaoshui Huang
- Huan Huo
- Guandong Xu
affiliations:
- University of Technology Sydney
- East China Normal University
- The University of New South Wales
- Shanghai Jiaotong University
- The Education University of Hong Kong
arxiv_id: '2609.29940'
url: https://arxiv.org/abs/2609.29940
pdf_url: https://arxiv.org/pdf/2609.29940
published: '2026-09-24'
collected: '2026-09-27'
category: Multimodal
direction: 多模态训练 · 注意力对齐
tags:
- MLLM
- Visual Grounding
- Attention Regularization
- Reasoning
- Probability Mass Concentration
one_liner: 提出 sPMC 训练框架，仅对少量视觉grounding敏感注意力头做概率质量集中正则，零样本平均提升3%
practical_value: '- **少而精的头选择正则**：不全局约束所有注意力头，而是先识别对视觉证据 grounding 敏感的少数头（3%-15%），再做任务相关正则；可迁移到电商多模态商品理解/推荐理由生成，保留语言先验与通用能力，避免过正则导致性能下降。

  - **用弱监督区域先验引导注意力**：借助 segmentation mask / 商品主体框等空间先验，让文本到图像注意力概率质量向语义相关区域集中；无需大规模推理标注，对图文匹配、多模态搜索相关性建模有直接借鉴价值。

  - **训练成本低、推理零开销**：sPMC 只在训练阶段施加正则，不改推理架构，适合作为现有 MLLM 流程的插件式训练技巧；在电商 Agent 或多模态搜索中可较快验证。

  - **注意力头功能分析可复用**：Adaptive Head Selection 的思路可迁移到任何多模态 LLM 或推荐模型中，先探测头功能再定向优化，减少无效训练。'
score: 6
source: arxiv-cs.CV
depth: abstract
---

**动机**：MLLM 在视觉推理任务上仍容易出现幻觉、过度依赖语言先验，生成答案时未充分使用任务相关视觉证据。已有方法多靠推理监督或推理时策略，本文从“不直接监督推理过程、强化隐式视觉 grounding”切入。

**方法关键点**：提出 Selective Probability Mass Concentration (sPMC)。基于注意力头功能分工，先识别对视觉证据 grounding 响应最强的头；将文本到图像注意力归一化为空间概率分布，利用 segmentation 派生的空间先验，鼓励概率质量集中到语义相关区域。Adaptive Head Selection 只对少量视觉响应头施加正则，其余头保持不变，以保留其互补功能。

**关键结果**：在 6 个多模态基准上，sPMC 使多个 MLLM 平均零样本提升 3%，最高提升 11.3%，且仅正则化 3%-15% 的注意力头。表明对稀疏、隐式视觉证据通路做定向引导，可直接改善多模态推理。
