---
title: 'AutoIndex: Learning Representation Programs for Retrieval'
title_zh: AutoIndex：学习可执行的文档表示程序以优化检索索引
authors:
- Sam O'Nuallain
- Nithya Rajkumar
- Ramya Narayanasamy
- Hanna Jiang
- Shreyas Chaudhari
- Andrew Drozdov
affiliations:
- University of Massachusetts Amherst
- Databricks Mosaic Research
arxiv_id: '2607.18603'
url: https://arxiv.org/abs/2607.18603
pdf_url: https://arxiv.org/pdf/2607.18603
published: '2026-07-20'
collected: '2026-07-23'
category: RecSys
direction: Agent驱动的检索索引优化
tags:
- Document Representation
- BM25
- Agentic Search
- Indexing Optimization
- CRUMB
one_liner: 将文档索引视为可优化程序，用Agent迭代搜索最佳预处理代码，BM25召回提升8.4%+
practical_value: '- **把文档预处理当成可优化程序**：不只调chunk大小，而是用Agent搜索对检索最有益的文本变换（抽取、重加权、去噪），商品详情页可自动提炼标题、属性、卖点来提升搜索召回。

  - **Agent诊断失败案例驱动优化**：借鉴双Agent设计——分析Agent检查哪些查询未能召回目标商品，代码Agent生成对应预处理规则；分离关注点，避免上下文过载。

  - **离线指标指导迭代选择**：固定BM25，用Recall@100作为优化信号，每次迭代重建索引并验证，自动保留有效改进；工程上可集成到索引构建流水线，定期更新表示策略。

  - **对BM25的特化技巧可迁移**：通过重复重要字段（如电影情节、演员表）模拟字段加权，过滤特定标记（LaTeX）降低噪声，类似方法可用于处理电商文档中的重复广告语、HTML标签等。'
score: 9
source: huggingface-daily
depth: full_pdf
---

**动机**：检索系统中，文档如何切片、追加元数据、去噪等索引前处理，长期被视为固定工程选项而非优化对象。实际这些选择直接影响BM25等检索器的词汇匹配，却很少被自动调优。AutoIndex提出将文档表示映射为可执行程序，并通过Agent迭代搜索最优程序，使索引策略与检索目标对齐。

**方法关键点**：
- **程序表示**：文档预处理被定义为从原始文档到索引单元的Python代码。搜索空间包括切片、字段重复加权、LaTeX过滤、文本重排等。
- **双Agent循环**：分析Agent用`bm25_retrieve`、`read_file`等工具检查当前索引的检索失败案例（锚点、召回违反、低位正样本），生成诊断总结；代码Agent根据总结和历史记录合成新的候选预处理程序。
- **指标驱动选择**：每个候选程序被执行、重建索引、在验证集上计算Recall@100，只保留改进超过阈值的程序。若多候选有效，尝试合成混合程序。迭代5轮，固定使用BM25和MaxP文档聚合。

**关键结果**：在CRUMB（8个异构检索任务）上，用qwen3-coder做主干，AutoIndex较全文档BM25基线平均提升Recall@100 +8.4%、nDCG@10 +8.3%，其中SetOpEntity的Recall提升30.5%，LegalQA的nDCG提升43.6%。去除分析Agent或搜索历史均会导致增益大幅减小，甚至出现负优化，证实了诊断反馈和历史约束的重要性。

**一句话**：把索引前处理从静态超参数变成受指标引导的可执行程序搜索，能显著提高固定检索器的召回与排序质量，且方法不依赖特定检索器。
