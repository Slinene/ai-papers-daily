---
title: 'Embeddings vs. Grep: Rethinking the Dense Advantage in Code Search'
title_zh: 嵌入 vs. Grep：重新思考代码搜索中密集检索的优势
authors:
- Siqiao Xue
- Ziyin Zhang
- Zihan Liao
- Jin Qin
- Yixiang Mu
- Hang Yu
affiliations:
- Ant Group
- Shanghai Jiao Tong University
arxiv_id: '2611.20455'
url: https://arxiv.org/abs/2611.20455
pdf_url: https://arxiv.org/pdf/2611.20455
published: '2026-11-15'
collected: '2026-11-20'
category: Eval
direction: 代码搜索评估与混合检索优化
tags:
- Code Search
- Dense Retrieval
- BM25
- Query Expansion
- Hybrid Retrieval
- Evaluation
one_liner: 构建真实代码搜索基准Repo-Premium，发现密集优势源于评估偏差与查询缺乏稀有标识符，LLM生成查询扩展让BM25追平密集检索
practical_value: '- 在商品搜索/推荐中，评估 embedding 召回时避免对 BM25 做不公平处理，例如不要过度切分文本、不要忽略可被词法匹配的相关项；否则会高估
  dense 模型收益。

  - 采用混合检索（dense + BM25）作为默认召回层，尤其当查询可能缺乏关键稀有词（如长尾商品型号、品牌词）时，可借鉴 generate-then-grep：先用
  LLM 生成候选关键词，再交给词法检索，低成本提升召回。

  - 构建 Agent 的检索工具时，若语料以结构化或代码类文本为主，可优先用 grep/BM25 等词法检索并配合查询扩展，延迟低、可解释性强，不必盲目引入 embedding
  索引。

  - 评估检索系统时，应采集真实用户查询（如原始工单、会话记录），并注意数据时间切片避免 LLM 泄漏；同时定期对比公平的词法基线。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有代码搜索基准显示密集编码器大幅领先 BM25，但编码 agent 实际用 grep 效果不错，密集优势可能源于基准偏差。
**方法关键点**：构建 Repo-Premium，覆盖 91 个仓库、6 种语言、2022-2026 年 PR，同时包含 curated 和 raw 查询；对比 dense 与 BM25，并分析评估选择（文件切块、相关定义）和查询特征（是否含稀有标识符）的影响；提出 generate-then-grep，用 LLM 生成标识符扩展查询。
**关键结果数字**：实验表明密集优势主要来自评估偏差和查询缺少稀有标识符；generate-then-grep 让 BM25 在所有 Python pool 追平 dense，甚至在 LLM 发布后的 PR 上依然有效；没有方法能预测哪个检索器在给定查询上获胜。推导三条指南：评估 dense 收益需公平词法基线；融合 dense 与 BM25；为缺乏代码字样的查询添加词法词项。
