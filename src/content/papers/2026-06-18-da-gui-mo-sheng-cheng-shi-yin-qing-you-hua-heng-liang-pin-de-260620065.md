---
title: 'Generative Engine Optimization at Scale: Measuring Brand Visibility Across
  AI Search Engines'
title_zh: 大规模生成式引擎优化：衡量品牌在AI搜索引擎中的可见性
authors:
- Pratyush Kumar
affiliations:
- Ranqo
arxiv_id: '2606.20065'
url: https://arxiv.org/abs/2606.20065
pdf_url: https://arxiv.org/pdf/2606.20065
published: '2026-06-18'
collected: '2026-06-20'
category: Other
direction: 生成式引擎优化 · AI搜索品牌可见性测量
tags:
- GEO
- AI_Search_Visibility
- Brand_Visibility
- LLM
- Content_Strategy
- Citation_Analysis
one_liner: 首次对AI搜索引擎中的品牌可见性进行大规模测量，揭示品牌知名度三层阶梯与引用模式
practical_value: '- 品牌权威性可用于生成式推荐的冷启动：论文量化了品牌知名度对提及率的巨大影响，电商平台内部LLM推荐产品时，可引入品牌层级特征，或主动补充中长尾品牌信息以缓解曝光马太效应。

  - “best-of”榜单内容的高引用率启示：在生成商品描述或推荐理由时，可模仿榜单格式输出结构化推荐清单，提升信息密度和用户采纳率。

  - 情感不稳定性警示：AI生成品牌相关文本时情感容易翻转，建议在面向用户的生成式推荐文案中加入实时情感校验或平滑机制，避免品牌形象波动。

  - 多引擎差异化监控：不同AI引擎背后模型偏好不同，若业务中接入了多个LLM服务，需建立品牌展示的跨引擎对比看板，及时发现偏差。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

动机：AI搜索引擎逐渐取代传统搜索，品牌亟须从传统SEO转向生成式引擎优化(GEO)，但缺乏测量品牌在AI引擎中可见性的大规模基准，尤其对中小企业、D2C品牌和初创公司更具挑战。

方法：通过Ranqo平台收集2026年3月至5月间100+品牌在ChatGPT、Claude、Perplexity、Gemini等引擎上的100K+次提示-响应对，分析品牌提及率、引用来源、内容格式及情感，首次系统量化品牌AI可见性。

关键结果：1) 形成清晰的三层品牌知名度阶梯——全球知名品牌在相关AI回答中提及率达73%，中端品牌44%，小众品牌仅11%，每级差距约30个百分点。2) 引用源中78%指向企业网站，非企业源里YouTube被引最多，其次Reddit、编辑媒体和Wikipedia。3) “最佳榜单”(best-of listicle)是最常被引用的页面格式，占全部引用的21%。4) 品牌情感信号极不稳定，正负面翻转频率是提及翻转的6.7倍，表明AI引擎对品牌描述缺乏一致性。基于这些发现，研究者提出七项可验证的改进协议，旨在因果性提升AI可见性。
