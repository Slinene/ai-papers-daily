---
title: Cross-platform epistemic verification for improving factual reliability in
  AI-generated news summarization
title_zh: 跨平台多源证据共识验证提升AI新闻摘要事实可靠性
authors:
- Zhuo Xie
- Haoze Ni
affiliations:
- Bank of Changsha Co., Ltd.
- Boston University
arxiv_id: '2608.05302'
url: https://arxiv.org/abs/2608.05302
pdf_url: https://arxiv.org/pdf/2608.05302
published: '2026-08-05'
collected: '2026-08-08'
category: RAG
direction: 多源验证与共识仲裁提升事实一致性
tags:
- Hallucination Correction
- Multi-source Verification
- Consensus Scoring
- Retrieval-Augmented Generation
- Factual Consistency
- Multi-LLM Jury
one_liner: 提出MECV框架，通过异构多源检索与多LLM陪审团共识打分修正摘要幻觉
practical_value: '- **多源证据交叉验证**：在商品描述生成或评论摘要等场景，可借鉴从商品库、百科、用户问答等多源检索证据，交叉验证事实性声明，减少单一信源偏差。

  - **多LLM陪审团共识机制**：对关键商品属性（如材质、功能）或广告文案的事实陈述，采用不同LLM独立验证，通过矛盾感知的共识打分识别不可靠内容，提升可信度。

  - **迭代最小编辑修正**：对生成式推荐文案或推送消息中的可疑事实片段，采用小步迭代修改，既修正错误又尽量保留原有结构和风格，降低改写成本。

  - **异构检索引擎编排**：在涉及多平台商品信息核验时，可设计类似架构，组合内部知识库、第三方API和开放网络搜索，并利用协调器控制修正流程。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：LLM生成的新闻摘要常包含幻觉事实，现有事后校验方法大多依赖单一检索源，易受检索偏差、证据不全和平台不一致的影响，可靠性不足。

**方法**：提出多源证据共识验证框架MECV。首先从源文档、维基百科和开放网络等多个异构渠道检索证据；然后引入多LLM陪审团（GPT-4o-mini、DeepSeek-Chat）对每条声明进行独立的事实校验，通过矛盾感知的共识打分综合判断可靠性；被标记为可能无据的声明交由协调器（Qwen-Plus）进行迭代最小编辑修正，直至通过验证或达到最大迭代次数。

**结果**：在SummEdits基准上，MECV在保持原文语义结构的同时显著提升事实一致性。实验表明，跨源证据的一致程度可作为识别事实不确定性的有效信号，在金融新闻聚合等信息敏感领域尤为有用。
