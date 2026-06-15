---
title: 'ADORE: Iterative Query Expansion with Retrieval-Grounded Relevance Feedback'
title_zh: ADORE：检索反馈驱动的迭代查询扩展
authors:
- Amin Bigdeli
- Negar Arabzadeh
- Radin Hamidi Rad
- Sajad Ebrahimi
- Charles L. A. Clarke
- Ebrahim Bagheri
affiliations:
- University of Waterloo
- Mila – Quebec AI Institute
- University of Toronto
- University of California, Berkeley
arxiv_id: '2606.13905'
url: https://arxiv.org/abs/2606.13905
pdf_url: https://arxiv.org/pdf/2606.13905
published: '2026-06-11'
collected: '2026-06-15'
category: QueryRec
direction: 检索增强的迭代查询改写
tags:
- query expansion
- retrieval-grounded feedback
- relevance assessment
- iterative refinement
- LLM-as-judge
one_liner: 将检索结果转化为结构化相关性反馈，在迭代中不断纠正扩展方向，显著提升查询扩展的检索效果
practical_value: '- **检索结果作为显式反馈信号**：不直接把召回文档喂给生成器，而是让 LLM 先对文档做分级相关性评估（0-3 分），再将正负例中的有效词汇和噪声词汇显式告诉模型，指导下一轮生成。电商搜索或推荐场景中的
  query 改写、自动补全可借鉴此范式，用点击/转化信号自动生成结构化反馈。

  - **分级反馈池与词汇锚定**：从高分文档中提取 named entity、数字、单位等“词汇锚点”，在下一轮伪文档生成时要求模型原样复用，避免同义词置换导致匹配失败。该
  trick 可直接用于电商商品搜索的 query 扩展，确保扩展词与库存索引的精确匹配，减少召回漂移。

  - **自适应终止策略**：通过质量饱和（所有 top-10 已获最高分）和覆盖率饱和（连续两轮新文档数低于阈值）自动停止迭代，避免固定轮次浪费算力。Agent
  或多步推理系统中可复用此思想，在规划或检索循环中设置早期停止条件，平衡效果与延迟。

  - **解耦生成与评估**：将 reformulator 和 relevance assessor 角色分离，并使用同一 LLM 但不同 prompt，即使换用开源模型也能保持稳定。推荐系统中可借鉴此分离设计，用单独的评估模块对生成的推荐理由或扩展
  query 打分，提升可控性和可解释性。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
现有 LLM 驱动的查询扩展大多仅依赖生成，不观察检索结果，无法判断生成的扩展词是否真的提升了检索质量。部分方法开始引入语料信号，但只把召回文档作为上下文喂给生成器，并未将其转化为显式的反馈信号。迭代式方法如 ThinkQE 虽多次检索，但缺少对每轮效果的验证，可能强化错误词语导致漂移。因此，亟需一种能将检索结果转化为可指导下一步生成的结构化反馈机制，让查询扩展成为一个迭代的、由检索效果驱动的修正过程。

**方法关键点**
- **三阶段循环**：每轮包含（1）Adapt：根据前一轮反馈生成伪文档；（2）Observe：用生成文本构造新查询，在目标语料上检索 top-K 文档；（3）Evaluate：用 LLM 评估检索结果与原始查询的相关性，将文档分为 4 级（0~3）。
- **反馈池构建**：按得分将文档归入“强化证据”（得分 3）、部分相关（2）、漂移/不相关（1/0），并在下一轮的 prompt 中要求模型复用高分文档的精确词汇（如技术术语、数字、命名实体），同时避免低频噪声词。
- **原始查询锚定**：所有相关性评估始终以原始查询为准，防止迭代导致语义漂移。
- **自适应终止**：当新检索文档已全为最高分，或连续两轮未出现足够新增文档时提前停止，至多运行 5 轮。

**关键实验**
- 数据集：TREC DL 2019/2020/DL-Hard（段落检索）、BEIR 5 个子集（跨域）、BRIGHT 7 个子域（推理密集检索）。
- 基线：BM25、BM25+RM3，以及 GenQR、Query2Doc、MUGI、ThinkQE 等 SOTA 扩展方法，全部使用 GPT-4.1 作为 backbone，以 BM25 作底层检索器。
- 主要结果：在 BEIR 上平均 nDCG@10 比 BM25 提升 24.5%，比最强基线 ThinkQE 提升 3.6%；在 BRIGHT 上分别提升 122.9% 和 9.2%；在 TREC DL 和 BEIR 上 BM25 经 ADORE 扩展后整体超越强稠密检索器 BGE-base-en-v1.5。
- 消融：迭代收益主要在前 2~3 轮，R2 贡献最大；更换评估器或改写器为 DeepSeek-V3 或 Llama-3.3-70B 效果稳定；扩展后的 query 同样能提升 BGE/Contriever 稠密检索效果。

**核心一句**：ADORE 通过让 LLM 评估检索结果并将分级反馈注入下一轮生成，使查询扩展从“一次生成”转变为“检索结果驱动的迭代修正”，大幅提升了跨域和推理密集场景下的检索精度。
