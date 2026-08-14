---
title: 'RAGSieve: Self-Referenced Local Contrast for Knowledge-Poison Detection in
  Retrieval-Augmented Generation'
title_zh: RAGSieve：检索增强生成中知识投毒的自引用局部对比检测
authors:
- Xinlong Xu
- Yoshua Y. Li
affiliations:
- Nanjing University of Information Science and Technology
- Meituan
arxiv_id: '2608.13010'
url: https://arxiv.org/abs/2608.13010
pdf_url: https://arxiv.org/pdf/2608.13010
published: '2026-08-13'
collected: '2026-08-14'
category: RAG
direction: RAG安全 · 自引用局部对比检测
tags:
- RAG
- Poisoning Detection
- Security
- Self-supervised
- Contrastive Learning
- Retrieval
one_liner: 提出自引用局部对比检测框架，在查询时和语料入库时无需投毒标签识别RAG投毒文档
practical_value: '- 在RAG检索后、生成前增加轻量检测层：对同一次检索的 top-5 与 rank 6-20 候选做分布对比（如相似度集中度、排名跃迁），发现异常文档直接过滤，不需要全局阈值，适合多品类电商检索结果分布差异大的场景。

  - 语料入库阶段构建文档局部邻域图，检测与语义相似但词法不同邻居的密度异常，可提前拦截协同注入的商品描述、评论或UGC内容，降低在线风险。

  - 方法无需投毒标注或可信参考语料，适合业务冷启动或无标注数据时快速上线防御。

  - 联合部署查询时和入库时检测，攻击成功率从67.4%降至14.0%，且对干净检索F1影响有限，可作为RAG安全模块直接嵌入现有pipeline。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：RAG将外部语料作为推理证据，攻击者只需注入少量文档即可操纵生成答案。现有检测依赖可信参考、特定攻击痕迹或全局阈值，对语料拓扑敏感，泛化性差。

**方法关键点**：提出RAGSieve自引用检测框架，从被检测系统自身构建参照。RSQ在查询时做局部对比：对同一次检索的top-5与rank 6-20候选打分，捕获答案锚定集中度和载体跃迁异常。RSG在语料入库时做局部对比：比较文档与其语义相似但词法不同邻居的密度，识别协同投毒。两者均无需投毒标签或可信语料。

**关键结果**：在三个QA数据集和六种投毒构造上，RSQ AUROC达95.2%，5%干净文档移除下检出82.2%投毒，优于GMTP的81.1%/52.5%；RSG达93.3%/79.8%，优于CleanBase的79.4%/37.6%。联合部署将攻击成功率从67.4%降至14.0%，同时未中毒检索F1保持41.3%。
