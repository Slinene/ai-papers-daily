---
title: 'Understanding AI from the Inside: The State of Mechanistic Interpretability
  for AI Safety'
title_zh: 从内部理解AI：面向安全的机制可解释性现状
authors:
- Fazl Barez
- Tung-Yu Wu
- Hunar Batra
- Gabriele Dominici
- Florent Draye
- Yanai Elazar
- Damiano Fornasiere
- Antía García
- Abir Harrasse
- Riley Harris
affiliations:
- University of Oxford
- Martian
- MIT
- Anthropic
- EleutherAI
arxiv_id: '2611.08438'
url: https://arxiv.org/abs/2611.08438
pdf_url: https://arxiv.org/pdf/2611.08438
published: '2026-11-05'
collected: '2026-11-08'
category: Other
direction: 机制可解释性与AI安全综述
tags:
- Mechanistic Interpretability
- AI Safety
- Circuits
- Feature Extraction
- Causal Verification
- Survey
one_liner: 系统综述机制可解释性方法，提出统一评估框架，并探讨其对AI安全编辑、控制与监控的作用和局限
practical_value: '- 用 probing 或 sparse autoencoder 分析推荐/排序模型的隐藏状态，定位价格敏感度、类目偏好等特征的编码位置，辅助特征归因与
  debug。

  - 借鉴 activation patching / causal tracing 做因果验证，判断某注意力头或 MLP 子层是否对推荐同质化、违规内容等行为负责，再定向干预或知识编辑。

  - 将电路发现方法迁移到多 Agent 推荐流程：定位 Agent 链中导致错误决策或幻觉的模块，避免全局重训，降低迭代成本。

  - 建立基于内部激活的线上监控指标，捕获分布漂移和越狱风险，作为行为监控的补充，提升 LLM 推荐/搜索改写系统的安全性。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：神经网络可能成为史上最重要人造物，能力增强但内部机制不透明，安全风险上升。机制可解释性通过研究内部表征和计算，试图评估、预测和控制行为，但需要回答：理解模型内部是否真的让模型更安全。

**方法关键点**：介绍基础概念（特征、多义性、Transformer 计算、电路）；综述特征提取与分析、电路发现与因果验证、中间表示用自然语言解释、学习动力学、训练数据归因等方法；提出统一评估框架，并刻画六种研究取向的目标、假设与权衡；还讨论了与行为评估的互补关系。

**关键结果**：机制证据比单纯行为评估更细粒度，可用于知识编辑、模型 steering 和监控；但仍有局限和失败模式，需结合行为安全措施。开放问题包括规模化、可靠性等。随附代码 notebooks 复现关键发现。
