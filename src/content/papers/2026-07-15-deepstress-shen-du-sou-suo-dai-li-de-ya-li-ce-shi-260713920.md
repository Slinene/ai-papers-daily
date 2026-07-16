---
title: 'DeepStress: Stress-Testing Deep Search Agents'
title_zh: DeepStress：深度搜索代理的压力测试
authors:
- Ismael Rousseau
- Geraldine Damnati
- Frederic Bechet
affiliations:
- Orange Research
- Aix-Marseille Univ.
- CNRS
arxiv_id: '2607.13920'
url: https://arxiv.org/abs/2607.13920
pdf_url: https://arxiv.org/pdf/2607.13920
published: '2026-07-15'
collected: '2026-07-16'
category: Agent
direction: 搜索代理鲁棒性评估与压力测试
tags:
- Search Agents
- Stress Testing
- Robustness
- Evidence Reliability
- RAG
- Multi-step QA
one_liner: 提出DeepStress框架，通过控制检索证据的可信度、相关性和事实性来测试搜索代理对低质量信息的鲁棒性
practical_value: '- 搜索/推荐Agent评估中，可构建类似DeepStress的合成检索环境，注入不同比例的不可靠文档（如虚假产品描述、无关广告），提前暴露模型脆弱点

  - 评估指标不应仅看最终答案/推荐准确率，需引入指标量化参数知识与检索知识的冲突情况，区分“被误导”与“合理拒绝”

  - 在电商Agent中，可借鉴三个扰动维度：可信度（用户评论真实性）、相关性（搜索召回噪声）、事实性（商品属性错误），针对性设计鲁棒性提升策略

  - 对于生成式推荐（如Semantic ID），当检索到的item表示被污染时，可模仿本文方法测试生成结果的偏离程度，指导训练或后处理逻辑'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：深度搜索Agent在多步问答中表现优异，但对其处理低质量证据的鲁棒性研究不足。现有基准极少出现不可靠检索结果，而实际应用中这类情况可能导致严重失败。

**方法**：提出DeepStress压力测试框架，用可控合成环境替换检索模块，直接控制返回文档的三个可靠性维度：可信度（来源是否权威）、相关性（是否与查询匹配）、事实性（陈述是否真实）。通过注入不同比例的“挑战性文档”，系统性地测试Agent的抗干扰能力。

**结果**：在HotpotQA和BrowseCompPlus上测试多个主流搜索Agent，发现不同模型在应对不可靠信息时表现差异巨大。提出新的评估指标，能够细粒度记录系统行为，尤其是参数化知识与检索知识冲突时的交互模式，揭示Agent是忽略矛盾证据、盲目信任还是有效调和。
