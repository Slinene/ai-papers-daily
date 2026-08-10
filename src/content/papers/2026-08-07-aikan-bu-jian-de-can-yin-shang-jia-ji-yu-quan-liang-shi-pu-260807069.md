---
title: 'Invisible to the Machine: Auditing AI Restaurant, Cafe, and Bar Recommendation
  Against a Complete Market Census'
title_zh: AI看不见的餐饮商家：基于全量市场普查的推荐审计
authors:
- Vladimir Pitenin
affiliations:
- Norly Research
arxiv_id: '2608.07069'
url: https://arxiv.org/abs/2608.07069
pdf_url: https://arxiv.org/pdf/2608.07069
published: '2026-08-07'
collected: '2026-08-10'
category: Eval
direction: AI推荐审计与可见性分析
tags:
- audit
- venue recommendation
- visibility bias
- LLM evaluation
- market census
one_liner: 首次在全量市场普查下审计AI餐饮推荐，发现85.6%的场所从未被推荐，可见性由评论量、网站等数字足迹驱动，而非评分。
practical_value: '- **全量审计方法可迁移**：若电商/平台拥有完整商品或商家目录，可按此方法全面评估推荐系统的覆盖偏差，而非依赖抽样审计，发现长尾曝光不足的真实程度。

  - **可见性双阶段洞察**：入场（召回）由文档丰富度（评论量、价格信息、网站）决定，排序才由评分主导。启示：提升新品/冷启动物品的召回率应优先填充文本属性与外部引用，而非单纯追求评分。

  - **陈旧信息风险**：AI系统易推荐已关闭/下架商品（93次 vs. 编造仅0.08%），要求业务侧确保知识库或商品状态的实时更新，防止无效推荐损害体验。

  - **多系统协同不确定性**：不同AI之间一致性低（Jaccard 0.33-0.54），商户依赖单一系统引流风险高；平台若使用LLM生成推荐内容，需测试多个模型的一致性，或进行后处理融合。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：AI助手正成为本地发现的主要入口，但无人知晓其推荐覆盖了哪些商家，尤其对餐饮业有直接收入影响。现有审计多为抽样，无法衡量完整市场中的可见性缺口。

**方法**：在巴厘岛两个地区（Canggu, Ubud）枚举全部4776家咖啡馆、餐厅和酒吧，构造全量市场注册表。向四个主流AI系统（ChatGPT、Claude、Gemini、Perplexity）发送96个带人称条件的查询，收集2208个回复，进行预注册协议下的对比分析。

**关键结果**：
- 85.6%的场所从未被任何系统推荐，即便在拥有50条以上评论的成熟商家中，仍有72.6%未被推荐。
- 可见性分两阶段：进入推荐列表与**文档化程度**强相关（评论量OR 1.64、自有网站OR 1.92、标价OR 1.54、第三方web提及OR 1.44），而星级评分在此阶段无效（OR 0.89）；但在已推荐场所中，评分显著预测首位排名（OR 1.17）。
- 公开POI数据集（Foursquare）的出现对两阶段均无正向影响。
- 编造极少（0.08%），但推荐了93次已永久关闭的商家，说明信息陈旧是实际故障模式。
- 系统间一致性低（top-20 Jaccard 0.33-0.54），两周重测表明波动来自采样随机性而非时移。
