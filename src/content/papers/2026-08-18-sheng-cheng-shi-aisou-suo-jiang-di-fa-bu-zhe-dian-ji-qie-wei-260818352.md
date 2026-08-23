---
title: 'AI in Search Reduces Publisher Referrals Without Improving User Experience:
  Experimental Evidence'
title_zh: 生成式AI搜索降低发布者点击且未改善体验：实验证据
authors:
- Stephanie T. Wang
- Jeffrey Gleason
- Yakov Bart
- Christo Wilson
- Danaé Metaxa
affiliations:
- University of Pennsylvania
- Northeastern University
arxiv_id: '2608.18352'
url: https://arxiv.org/abs/2608.18352
pdf_url: https://arxiv.org/pdf/2608.18352
published: '2026-08-18'
collected: '2026-08-23'
category: LLM
direction: 生成式AI搜索的因果效应评估
tags:
- generative AI
- web search
- field experiment
- publisher traffic
- click-through rate
- user experience
one_liner: 基于1,100人的预注册田野实验，证明Google AI搜索减少发布者点击，AI Mode还损害体验与信任
practical_value: '- 在搜索/推荐结果页引入LLM摘要或对话式回答时，必须同时观测下游详情页、广告、商家页的CTR和GMV；本实验显示AI Overviews会系统性蚕食外部点击，不能只看搜索侧满意度。

  - 完全“无链接”的AI Mode会显著降低用户信任与体验，电商搜索应保留原文链接、商品卡片等可点击出口，采用混合UI而非纯答案界面。

  - 可复用其预注册现场实验设计：在真实搜索引擎上通过浏览器扩展随机屏蔽/保留AI功能，估计因果效果；对AI搜索/推荐功能灰度可用类似RCT，避免观察性偏差。

  - 生成式推荐/Agent回答场景需监控“答案终结率”和后续跳转率，防止Agent直接给结论抑制用户探索和交易路径，必要时加入引用、相关推荐、追问按钮来平衡信息效率与商业流量。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：生成式AI被整合进搜索后，用户可能更多停留在答案页而不再点击第三方发布者，威胁内容供给生态；但此前缺乏因果证据。

**方法**：在Google Search上开展预注册的现场实验（N=1,100），通过浏览器扩展控制被试看到AI Overviews、AI Mode或传统搜索结果，测量点击行为、主观体验和信任。

**关键结果**：移除AI Overviews和AI Mode会提升发布者CTR；仅保留AI Mode的对话式搜索会降低发布者点击，同时恶化用户体验和对Google信息的信任。说明生成式AI搜索重塑了注意力分配，对上游内容方有直接经济后果。
