---
title: 'TrialAtlas: Multi-Agent Research Organization for Clinical Trial Design and
  Optimization'
title_zh: TrialAtlas：面向临床试验设计与优化的多智能体研究组织
authors:
- Jiacheng Lin
- Zifeng Wang
- Zheng Chen
- Erick Scott
- Ziwei Yang
- Fanyang Yu
- Sheng Zhong
- Jimeng Sun
affiliations:
- University of Illinois Urbana-Champaign
- Keiji AI Inc
- The University of Osaka
- University of Pennsylvania
- AbbVie Inc
arxiv_id: '2609.21859'
url: https://arxiv.org/abs/2609.21859
pdf_url: https://arxiv.org/pdf/2609.21859
published: '2026-09-18'
collected: '2026-09-21'
category: MultiAgent
direction: 多智能体协作优化复杂决策
tags:
- Multi-Agent
- Memory-Augmented
- Clinical Trial
- Regulatory Science
- LLM
- Benchmark
one_liner: 提出记忆增强的多智能体系统 TrialAtlas，通过文献、竞品、法规先例及历史 NDA 学习提升临床试验缺陷检测与成功预测
practical_value: '- 多智能体分工可借鉴：文献合成、竞品情报、政策/法规先例分析、综合推理，类似电商场景中的市场分析、竞品监控、平台规则合规、策略生成，可将复杂决策拆解为专业子
  agent 协同。

  - 记忆增强机制：用历史真实案例（NDA/CRL）作为经验库，在推理时检索相关先例，可迁移到广告投放历史 campaign 复盘、商品推荐中的相似场景检索，提升决策可解释性和复用性。

  - 构建领域真实业务评测集：用 291 个 FDA 拒批信做 benchmark，比合成数据更有业务可信度；电商可借鉴用投放失败案例、申诉案例或用户投诉构建回归评测集，评估
  agent 的缺陷发现能力。

  - 输出可操作建议而非仅风险评分：TrialAtlas 生成具体设计改进点，类似商品推荐解释、广告审核意见，提升生成结果在业务上的直接落地价值。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

动机：近 90% 药物临床开发失败，临床开发计划（CDP）依赖多专家协作获取、综合、推理异质证据，劳动密集且主观。

方法关键点：TrialAtlas 是一个记忆增强的多智能体研究组织，协调四类专业 agent：文献合成、竞争性试验情报、法规先例分析、综合推理；同时从历史临床试验和 NDA 监管结果中积累经验，用于支撑决策。

关键结果数字：在 291 个 FDA Complete Response Letters 构建的 TrialAtlasBench 上，缺陷检测 F1 达到 50.0%，超最强基线 6.1 点；技术和监管成功预测 balanced accuracy 85.3%、F1 84.7%，较最佳基线分别提升 6.7 点和 Cohen's kappa 12.0 点；专家评估中 86.4% 生成关注点被判定有效，高于 OpenAI DeepResearch（83.1%）和 Gemini DeepResearch（59.3%）。
