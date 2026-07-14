---
title: 'Metacognition in LLMs: Foundations, Progress, and Opportunities'
title_zh: 大语言模型中的元认知：基础、进展与机遇
authors:
- Gabrielle Kaili-May Liu
- Areeb Gani
- Jacqueline Lu
- Jordan Thomas
- Mark Steyvers
- Arman Cohan
affiliations:
- Yale University
- University of California, Irvine
arxiv_id: '2607.11881'
url: https://arxiv.org/abs/2607.11881
pdf_url: https://arxiv.org/pdf/2607.11881
published: '2026-07-13'
collected: '2026-07-14'
category: Reasoning
direction: LLM 元认知能力评估与增强
tags:
- Metacognition
- Self-Reflection
- Uncertainty Estimation
- Calibration
- LLM Evaluation
one_liner: 系统综述 LLM 元认知研究，提出监控与控制双过程框架，总结评估与增强技术
practical_value: '- **推荐置信度过滤**：在生成式推荐或对话 Agent 中，利用模型的校准（calibration）和不确定性估计能力，对推荐结果进行置信度评分，过滤低质量输出，提升推荐可靠性。

  - **自我反思增强 Agent 决策**：借鉴元认知监控-控制循环，在搜索/推荐 Agent 中加入自我评估步骤，让模型判断信息是否充分、是否需要调整查询或调用工具，提高任务完成率。

  - **提示工程激发元认知**：通过特定提示（如要求模型先解释推理过程再给出答案）诱导模型的自我反思，改善复杂推荐任务（如动态查询改写、广告文案生成）的准确性和可解释性。

  - **减少幻觉与错误累积**：在多步推理或序列推荐场景，引入元认知监控可以及时检测和纠正逻辑错误，防止错误传播，特别适用于需要长链条规划的购物助手或营销策略生成。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

**动机**：元认知（监控自身认知并据此调控）是可靠智能系统的关键，但 LLM 是否具备或如何被赋予有效的元认知能力尚未明晰，亟需系统梳理。

**方法**：该综述首次全面归纳 LLM 元认知研究，定义双过程框架——**监控**（如不确定判断、任务表现评估）与**控制**（如策略调整、资源重分配）。从两方面分类现有工作：(1) **测量与评估**：分析校准（Calibration）、置信度估计、自我评估等指标，总结专用基准（如 TruthfulQA、SelfCheckGPT 变体）；(2) **激发与改进**：探讨提示工程（如思维链、自我反思提示）、训练干预（微调、强化学习）、解码策略（如束搜索置信度惩罚）等技法。

**关键发现**：现有 LLM 普遍存在过度自信，校准误差随模型增大可能加剧；但通过分步推理、外部反馈或对比解释等元认知提示，可显著提升自我评估准确率（部分场景 ECE 降低 30%–50%）。应用涵盖规划、推理、医疗问答等，揭示元认知是提升可解释性与鲁棒性的可行路径。综述最后指出开放问题：多语言泛化、长程任务中的元认知维持、以及与 Agent 架构的深度融合。
