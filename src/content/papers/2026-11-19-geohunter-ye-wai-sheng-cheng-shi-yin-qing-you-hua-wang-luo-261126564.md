---
title: 'GEOHunter: Mapping a Generative Engine Optimization Network in the Wild'
title_zh: GEOHunter：野外生成式引擎优化网络测绘
authors:
- Sean Tang
- Peiran Wang
- Ying Li
- Esha Shivakumar
- Tao Meng
- Yuan Tian
affiliations:
- University of California, Los Angeles (UCLA)
- Georgia Institute of Technology
arxiv_id: '2611.26564'
url: https://arxiv.org/abs/2611.26564
pdf_url: https://arxiv.org/pdf/2611.26564
published: '2026-11-19'
collected: '2026-11-20'
category: Other
direction: 生成式引擎优化 · 作弊网络测量
tags:
- GEO
- Generative Engine
- UGC
- Coordinated Behavior
- Web Measurement
- LLM Security
one_liner: 测绘一个跨平台 UGC 生成式引擎优化作弊网络，并量化其对 9 个 AI 助手引用和答案的影响
practical_value: '- 做商品/品牌监控时，重点盯 UGC 平台上的 listicle 榜单和“哪个品牌好”类标题：这类内容正被生成式引擎大量引用，是灰色
  GEO 操纵 AI 推荐答案的主要载体。

  - 反作弊/内容治理不要只审单篇软文，要迁移账号级与平台级信号：低粉账号批量发品牌软文、同客户多账号同周发布、标题模板共享、固定账号对跨平台同步复制。

  - 生成式推荐或 Agent 在合成答案时，应把来自同一协调簇的页面视为相关证据而非独立证据，对近重复标题和跨站副本做去重/降权，并引入发布账号历史作为排序特征，而不只依赖域名权威。

  - 评估生成式搜索/推荐质量时，除引用准确率外，要溯源内容生产者，否则“忠实引用”会掩盖有组织的来源操纵。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

**动机**：生成式引擎把检索到的网页合成答案、推荐和排名，GEO 服务通过在海量 UGC 平台发布付费推广文章来影响 AI 回答，在医疗、金融等领域风险突出。已有研究审计引擎引用了什么，或实验室验证 GEO 技巧，但从未在野外把供给端作弊网络与生成引擎的实际引用连接起来，本文填补这一空白。

**方法关键点**：
- GEOHunteR：以购买的两篇虚构公司软文为种子，在 Bilibili、Baijiahao、360kuai 三个平台用客户名搜索滚雪球，以协调发布信号（多客户、跨账号复制标题、同日 burst）判定网络账号。
- GEOPRobe：向 9 个国内外 AI 助手（文心、秘塔、DeepSeek、元宝、360AI搜索、Gemini、ChatGPT、Google AI Overviews、AI Mode）发买方问题并配对类别领导者作对照，按 strict / extended / broad 三级追溯引用页面。
- 数据：发现 3,755 个网络账号，分析 1,985 个账号及其 466,357 篇推广文章。

**关键实验与数字**：
- 供给端：96% 的 niche 推广是普通消费品；listicle 占核心 Bilibili 账号 placement 的比例从 2024 年 16% 升至 2025 年 57%；网络账号在 Bilibili 的中位粉丝仅 9 个；98/175 个 niche 客户存在超随机的同周多账号发布；跨平台标题复制中位延迟 32 分钟。
- 暴露端：9 个助手均引用可归因于该网络的文章，strict 4.5%、extended 7.2%、broad 20% 的可检索引用页来自网络；文心最高（strict 18%）；普查中客户在 52% 的答案中被提及，而类别领导者为 68%；助手还会复述网络的关键声明，并在被问及 GEO vendor 时推荐该网络推广的供应商。

**最值得记住的一句话**：内容级防御不足以对抗协调的 UGC placement，平台和助手提供者必须转向账号级与平台级协调信号。
