---
title: Self-Evolving Search Index
title_zh: 自进化搜索索引
authors:
- Sangam Lee
- Wonjae Lee
- Sunghwan Kim
- Deogyong Kim
- Jaehoon Kim
- Daye Nam
- SeongKu Kang
- Dongha Lee
affiliations:
- Yonsei University
- Samsung Research
- University of California, Irvine
- Korea University
arxiv_id: '2609.19656'
url: https://arxiv.org/abs/2609.19656
pdf_url: https://arxiv.org/pdf/2609.19656
published: '2026-09-16'
collected: '2026-09-19'
category: Other
direction: 自进化索引优化 · LLM Agent 检索
tags:
- Self-Evolving Index
- Index Optimization
- LLM
- Retrieval
- Search Agent
- Agent Memory
one_liner: 提出 SELF-INDEX 框架，让索引自主诊断检索缺陷、选择性修订索引键并主动探索查询需求，跨语料与检索器一致提升检索性能
practical_value: '- 在电商/内容搜索中，可借鉴 SELF-INDEX 的「索引即键集合」思路：为每个商品/内容维护一组可检索键（标题、类目、属性、卖点短句），由
  LLM 根据检索反馈自动改写/增删这些键，避免人工设计 query 扩展或语义标签。

  - 用 co-retrieval profile 作为诊断信号，发现哪些商品键缺乏区分度或未覆盖用户 query 意图；Self-Validation 的 faithfulness/specificity/separation
  三准则可直接作为生成式索引质量控制，过滤幻觉或宽泛键。

  - Query Simulator 通过采样文档生成 plausible query 并用 Jaccard dissimilarity 去重，能低成本扩充优化
  query 覆盖长尾需求，适合广告关键词推荐、搜索词扩展等场景。

  - 搜索 Agent 中，优化索引键可同时提升答案准确率并减少 search calls；在电商导购 Agent 可减少与搜索中台交互次数和线上 API 成本。'
score: 8
source: huggingface-daily
depth: full_pdf
---

动机：检索质量严重依赖索引键能否充分暴露文档知识，但索引优化策略的有效性随语料类型（自然语言、代码、表格）和检索器（稀疏/密集）变化，固定策略难以跨环境稳定。人工诊断检索失败、重写策略并全库重处理成本高，阻碍索引持续进化。SELF-INDEX 提出索引自进化框架，无需人工干预即可根据检索结果自主改进索引键，并通过主动探索查询需求扩展进化范围。

方法关键点：
- Optimizer 执行三阶段循环：Self-Diagnosis 利用查询检索结果构造 co-retrieval profile，记录每个键与其他文档键的共检索频率，诊断当前键在表达和区分文档知识上的缺陷；Self-Revision 对存在短板的文档键集整体修订，避免独立改键造成冗余；Self-Validation 按 Faithfulness（忠实于文档）、Specificity（强调文档特定知识）、Separation（与其他键充分区分）三条准则过滤生成键，通过后才更新索引。
- Query Simulator 采样文档生成可能检索需求，用 Jaccard Dissimilarity 过滤与已有查询重叠的需求，持续为 Optimizer 提供新查询，推动索引主动进化。
- 检索打分对各文档的多个索引键取最大相似度，原始文本键固定保留。

关键实验：
- BRIGHT 基准覆盖自然语言、代码、数学三类语料，SELF-INDEX 在 BM25、BGE、Qwen3-Emb-8B 下平均 nDCG@10 分别较基础索引提升 40.4%、57.0%、38.8%，在所有语料类型和检索器下均获最高分。
- 表格检索三个数据集上平均提升 BM25 49.1%、BGE 17.9%、Qwen3-Emb-8B 16.2%。
- 搜索 Agent 任务 BrowseComp-Plus 中，SELF-INDEX 在四个 Agent backbone 上提升准确率并减少搜索调用：如 GPT-OSS-120B+BM25 准确率 31.08→58.92 (+89.53%)，GPT-5.4-nano+BM25 36.51→64.94 (+77.87%)，在线 API 成本降低。
- Agent memory 任务 LongMemEval-V2 中，三种检索式记忆系统准确率分别提升 13.9%、12.4%、9.2%。
- Ablation 显示去掉 co-retrieval profile、任何一条验证准则或 dissimilarity 过滤均导致明显下滑，验证了各组件的贡献。

最值得记住的一句话：让索引根据检索反馈和自生成查询持续自我进化，并用‘忠实、具体、可分离’三重校验约束生成键，能跨环境稳定提升检索和下游 Agent 性能。
