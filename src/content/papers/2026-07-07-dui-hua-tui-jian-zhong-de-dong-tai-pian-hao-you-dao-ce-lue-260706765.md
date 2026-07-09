---
title: 'When and How to Ask: Dynamic Preference Elicitation Strategies for Conversational
  Recommendation'
title_zh: 对话推荐中的动态偏好诱导策略：何时与如何提问
authors:
- Feng Xia
- Shuo Zhang
- Xi Wang
affiliations:
- University of Sheffield
- Bloomberg
arxiv_id: '2607.06765'
url: https://arxiv.org/abs/2607.06765
pdf_url: https://arxiv.org/pdf/2607.06765
published: '2026-07-07'
collected: '2026-07-09'
category: RecSys
direction: 阶段感知的对话式推荐偏好诱导
tags:
- Conversational Recommender Systems
- Preference Elicitation
- Mixture of Experts
- Stage-aware Strategy
- Dataset InPE
one_liner: 阶段感知：前期问属性，后期推物品，MoE建模策略选择提升对话推荐效率
practical_value: '- 对话推荐策略应分阶段设计：冷启动阶段多问属性，偏好明确后直接推荐商品，可大幅提升导购Agent的交互效率

  - 借鉴COPE的Mixture of Experts架构，构建一个轻量策略选择器，在线判断当前对话轮次应提问还是推荐，以及提问类型（属性/物品）

  - InPE数据集提供了细粒度标注（询问必要性、策略类型），可用于微调对话推荐模型或策略判别器，适合迁移到电商客服场景

  - 离线评估证实阶段感知策略优于静态统一策略，线上部署时可基于对话长度或状态隐式划分阶段，避免硬编码规则'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：对话推荐系统（CRS）通过自然语言交互获取用户偏好，但现有工作多采用静态策略（如固定询问属性），忽视了询问时机与类型对对话质量的动态影响。本文实证发现，最优偏好诱导策略具有阶段依赖性：对话早期属性询问更有效，当偏好逐渐明确后，物品推荐策略更优。
**方法**：构建了InPE数据集，为每轮对话标注询问必要性及策略类别（属性/物品）。提出COPE模型，基于Mixture of Experts架构，动态融合对话状态与历史信息，预测当前轮次的最佳策略（询问/推荐，并细分询问类型）。
**关键结果**：离线评估显示，上下文感知的动态策略显著优于静态基准；策略预测随对话轮次呈现一致的模式：前期倾向询问属性，后期转向推荐物品，验证了阶段感知策略的有效性。
