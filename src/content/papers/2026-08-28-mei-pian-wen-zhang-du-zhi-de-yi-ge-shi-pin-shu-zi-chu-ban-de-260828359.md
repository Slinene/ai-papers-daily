---
title: 'Every Article Deserves a Video: Contextual Video Matching for Digital Publishers'
title_zh: 每篇文章都值得一个视频：数字出版商的上下文视频匹配
authors:
- Arnaud Corone
- Brice Pierre de la Briere
- Gladys Roch
- Samuel Leonardo Gracio
- Yassine Bouher
- Parvati Chauchaix
affiliations:
- Dailymotion
arxiv_id: '2608.28359'
url: https://arxiv.org/abs/2608.28359
pdf_url: https://arxiv.org/pdf/2608.28359
published: '2026-08-28'
collected: '2026-08-31'
category: RecSys
direction: 基于 LLM 与文本嵌入的文章-视频匹配
tags:
- LLM
- Video Recommendation
- Text Embeddings
- HyDE
- Content Matching
- Production System
one_liner: 用 LLM 与文本嵌入为文章自动匹配相关视频，已在 Dailymotion 生产环境规模化落地
practical_value: '- 可借鉴 HyDE 思路：用 LLM 把长文本商品描述/文章页面改写成搜索式 query 或假设段落，再做向量召回，比直接拿原文
  embedding 更可控，适合电商详情页与短视频/直播切片匹配。

  - 两阶段匹配架构：先文本 embedding 粗召回，再用 LLM 做相关性校验或重排，能低成本扩展到千万级 SKU 与视频库；线上可异步处理新文章/新商品。

  - 把“文章到视频”看成跨模态配对任务，不需要用户行为数据，冷启动友好；在广告落地页与创意素材匹配、SEO 内容推荐等场景可直接复用。

  - 生产部署需缓存 LLM 生成结果、对同义视频做 embedding 预计算，降低推理成本和延迟；与现有推荐链路解耦，作为内容侧增强模块上线。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

动机：数字出版商需要在文章内嵌相关视频以提升广告变现和用户留存，但面对海量文章和视频库，人工选择不可扩展。Dailymotion 需在自有平台及全网视频库中为不同出版商文章自动匹配视频。

方法：系统基于 LLM 与文本嵌入构建。针对文本密集型网页，先利用 LLM 生成文章的假设摘要或查询表示（Hypothetical Document Embeddings），将长文章压缩为可匹配的语义向量；同时为候选视频生成或复用文本描述。两部分通过文本嵌入进行语义相似度匹配，再结合规则或轻量排序输出最相关视频。系统强调可扩展性与生产环境部署，避免逐篇人工标注。

结果：该系统已在 Dailymotion 生产环境上线，被数百家出版商采用，用户参与度显著提升，视频与文章的相关性体验更优。论文讨论了系统动机、架构、评测与部署细节。
