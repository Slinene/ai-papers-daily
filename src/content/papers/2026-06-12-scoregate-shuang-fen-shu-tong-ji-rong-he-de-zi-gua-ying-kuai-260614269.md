---
title: 'ScoreGate: Adaptive Chunk Selection for Retrieval-Augmented Generation via
  Dual-Score Statistical Fusion'
title_zh: 'ScoreGate: 双分数统计融合的自适应块选择'
authors:
- Karamvir Singh
- Arvind Jain
affiliations:
- HighLevel, Inc.
arxiv_id: '2606.14269'
url: https://arxiv.org/abs/2606.14269
pdf_url: https://arxiv.org/pdf/2606.14269
published: '2026-06-12'
collected: '2026-06-15'
category: RAG
direction: RAG 自适应检索块选择
tags:
- RAG
- Adaptive Retrieval
- Score Fusion
- Cross-Encoder
- Chunk Selection
one_liner: 利用 bi-encoder 和 cross-encoder 双分数四分区自适应决定 RAG 块数量，无额外推理开销
practical_value: '- 在电商 RAG 场景（客服问答、商品推荐解释）中可直接复用：利用已有的 bi-encoder 和 cross-encoder
  输出分数，按四分区规则自动决定传给 LLM 的上下文块数量，降低无关信息干扰和 token 开销。

  - 借鉴不对称阈值设计：对 cross-encoder 高、bi-encoder 低的分区（如不同术语但高度相关的商品描述）采用更低保留阈值，可显著提升词汇不匹配场景的召回，减少
  LLM 过滤器造成的假阴性。

  - 阈值可通过生产日志一次性校准（归一化分位点+网格搜索），无需模型重训练，计算增加仅 31 ms，适合实时在线服务。

  - 固定 MAX-K 护盾机制防止上下文窗口溢出，可结合业务设置上限，避免极端安全风险。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：固定 K 的 RAG 无视查询复杂度，简单查询引入过多无关块浪费 token 并增加幻觉，复杂查询可能遗漏必要信息。LLM 过滤引入额外推理延迟，单分数阈值无法处理语义相关但词汇不匹配的块（如释义、同义词），这类块 bi-encoder 低分但 cross-encoder 正确识别。

**方法关键点**：ScoreGate 是纯分数空间决策机制，不新增模型。利用标准双阶段 RAG 流水线已有的 bi-encoder 相似度 sᵢ 和 min-max 归一化的 cross-encoder 分数 rᵢ，将 (sᵢ, rᵢ) 划分到四个互斥分区：
- B1（sᵢ ≥ τₛ, rᵢ ≥ τᵣ）：无条件保留
- B4（sᵢ < τₛ, rᵢ < τᵣ）：无条件丢弃
- B2（sᵢ ≥ τₛ, rᵢ < τᵣ）：融合分数 fᵢ = 0.3sᵢ + 0.7rᵢ ≥ 0.255 才保留
- B3（sᵢ < τₛ, rᵢ ≥ τᵣ）：融合分数 ≥ 0.15 即保留，专门挽救词汇差距的语义相关块
阈值 τₛ=0.70、τᵣ=0.08 从生产日志校准，融合权重 α=0.3 和分区阈值经网格搜索 F1 最优确定，最后用 MAX-K 上限约束总块数。

**关键结果**：
- 内部 ARB 数据集（300 带标注三元组，κ=0.87）：零假阳性（95% CI [96.4%,100%]），语义相关召回 99.34%，比 LLM 过滤高 6.93 个百分点；token 消耗降 34.8%，幻觉率从 11.8% 降至 7.1%。
- MS MARCO 公开基准（200 dev queries）：重新校准阈值后 MRR@10=0.401，平均保留 6.5 块（固定 K=10），优于标准 Top-K（MRR=0.387）和 LLM 过滤（MRR=0.361）。
- 真实生产流量 1247 查询：无效查询 87% 正确返回空集，有效查询 63% 返回非空，整体正确率≈95%。
**核心记忆**：用已有的 cross-encoder 信号拯救 bi-encoder 漏掉的语义相关块，通过极简四分区规则实现自适应检索基数，是 RAG pipeline 的免费增效插件。
