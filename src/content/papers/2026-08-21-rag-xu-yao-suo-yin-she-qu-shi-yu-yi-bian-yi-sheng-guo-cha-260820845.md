---
title: 'RAG Deserves an Index: Why Ingest-Time Compilation Beats Query-Time Interpretation'
title_zh: RAG 需要索引：摄取时语义编译胜过查询时解释
authors:
- Kyle Wild
- Yusuke Takahashi
- Asako Uraki
affiliations:
- Endgame Labs, Inc.
- Asia AI Institute, Musashino University
- Faculty of Data Science, Musashino University
- AIx, Inc.
arxiv_id: '2608.20845'
url: https://arxiv.org/abs/2608.20845
pdf_url: https://arxiv.org/pdf/2608.20845
published: '2026-08-21'
collected: '2026-08-24'
category: RAG
direction: RAG · 摄取时语义编译与索引
tags:
- RAG
- semantic compilation
- provenance
- incremental maintenance
- indexing
- agent memory
one_liner: 提出摄取时语义编译 ISC，将语料编译为带验证来源的原子声明，查询时读取成本降低约21倍且准确率更高
practical_value: '- 电商知识库/客服对话场景：将商品卖点、用户评价、客服承诺提前编译为原子事实（claim），每条事实携带 verbatim span、说话人、位置；RAG
  时直接返回事实而非原始段落，可显著降低读取 token 并提升答案准确率，尤其适合高频查询。

  - Agent 记忆/生成式推荐中写入 provenance 门禁：对从评论、对话中提取的每一条声明做精确字符串匹配，无法定位原文 span 的不写入，避免幻觉传播到下游答案或推荐理由。

  - 成本模型 R* 指导编译决策：热门商品描述、政策文档、常见问题可提前编译；长尾、易变内容保留查询时解释，不要默认全量编译。

  - 索引维护上借鉴增量低秩更新：频繁更新的商品语料不要每次全量重算 embedding，可考虑增量更新；模型升级用 Procrustes 对齐，只重新嵌入少量样本，降低迁移成本。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

动机：RAG 系统每次查询都让 LLM 对原始语料重新做语义解释（指代消解、归属判断、结构重建），然后丢弃；这类似数据库全表扫描，token 成本高，且上下文增长反而降低准确率。数据库的解法是索引：把昂贵工作写入时做一次，读取时便宜。

方法关键点：
- 提出 ingest-time semantic compilation (ISC)，把语料编译为双层语义 substrate：几何层维护 embedding；符号层存储原子声明（claims），每条携带 verbatim source span、作者、位置，编译时验证。
- 实现为 PostgreSQL，claims 表与 fact_evidence 表通过外键关联，验证门做精确字符串匹配，无法定位原文的候选 claim 直接丢弃。
- 引入四个合约：编译合约（语义 DDL）、维护合约、迁移合约、成本模型（break-even read count R*）；维护用增量低秩更新，迁移用 orthogonal Procrustes。

关键结果：
- 合成维护试验：增量更新 8.4ms/update vs 全重建 283ms，约 33.7× 便宜，最大主角度漂移 <1e-11 度，recall@10=1.0。
- MediaSum 500 段访谈、499 问题上，编译 claims 在 32 个 budget/model 组合全部胜出：2,048-token 预算下 85.2% 正确（约 2.2k 读取 token），最佳 chunk 配置仅 72.5%（约 16.3k）。唯一追平的 contextualized-chunk + hybrid retrieval + rerank 需要约 47.7k token（约 21×），且统计不显著。
- 20 文档重放验证门拒绝 1.1% 候选 claim；编译 500 文档约 $32，等价于该 stack 约 580 次查询的额外 token 成本，R* ≈ 580。

最值得记住的一句话：所有在查询时解释的配置都明显落败；唯一能保持准确率的配置已经开始编译，并以约 21 倍查询时 token 成本为代价。
