---
title: 'CFPO: Counterfactual Policy Optimization for Multimodal Reasoning'
title_zh: 面向多模态推理的反事实策略优化
authors:
- Zhangyuan Yu
- Wanran Sun
- Guangjing Yang
- Xiaohu Wu
- Qicheng Lao
affiliations:
- Beijing University of Posts and Telecommunications
arxiv_id: '2606.23206'
url: https://arxiv.org/abs/2606.23206
pdf_url: https://arxiv.org/pdf/2606.23206
published: '2026-06-22'
collected: '2026-06-23'
category: Multimodal
direction: 多模态推理 · 反事实策略优化
tags:
- Counterfactual Policy Optimization
- Multimodal Reasoning
- Reinforcement Learning
- Vision-Language Models
- Causal Consistency
- Hallucination Reduction
one_liner: 通过跨模态反事实增强正则化，强制视觉与文本因果一致性，显著减少多模态推理中的视觉忽略与幻觉漂移
practical_value: '- CFPO 的反事实正则化可直接用于多模态商品理解：训练时随机遮盖商品图片关键区域，最大化模型输出与遮盖后预测的差异，强制依赖视觉特征，减少对标题文本的偏倚，适合电商搜索/推荐中的视觉质量评估。

  - 在生成式推荐（GenRec）中使用多模态 LLM 生成 item 表示时，CFPO 的因果一致性训练可抑制视觉幻觉，提升 item 语义 ID 或描述的准确性，降低错误推荐风险。

  - 方法无需外部奖励模型，可与 GRPO、DAPO 等现有 RL 流程无缝集成，工程实现成本低，可直接插入现有强化学习微调管线，快速验证对多模态推理任务的效果。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：多模态大模型（LVLM）在强化学习优化时普遍缺乏反事实增强与因果学习机制，导致视觉推理严重依赖语言先验、忽略图像证据，并在长链思维中出现幻觉漂移。现有 RL 范式仅奖励最终答案正确性，未强制跨模态因果一致性。  
**方法**：提出 CFPO，引入跨模态反事实增强机制。在训练时构造反事实状态（抑制关键视觉线索），计算模型在该状态下的预测，并最大化其与标准预测的差异作为正则项。该正则项迫使模型必须利用视觉信息才能做出正确预测，从而内化视觉—文本因果约束。CFPO 与 GRPO、DAPO 等标准 RL 算法无缝集成，无需额外奖励模型或监督。  
**结果**：在多个多模态推理基准上，CFPO 比标准 RL 基线提升 3.17%–6.25% 的推理保真度，比最新感知感知方法 PAPO 提升 1.32%–2.13%，且有效减少幻觉和视觉忽略现象。
