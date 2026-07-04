---
title: Bringing Agentic Search to Earth Observation Data Discovery
title_zh: 将 Agentic Search 引入地球观测数据发现
authors:
- Minghan Yu
- Youran Sun
- Chugang Yi
- Yixin Wen
- Haizhao Yang
affiliations:
- University of Maryland, College Park
- University of Florida
arxiv_id: '2607.02387'
url: https://arxiv.org/abs/2607.02387
pdf_url: https://arxiv.org/pdf/2607.02387
published: '2026-07-02'
collected: '2026-07-04'
category: Agent
direction: Agent 驱动的搜索与重排序
tags:
- Agentic Search
- Reranking
- Domain Adaptation
- Retrieval Evaluation
- Hybrid Retrieval
- Knowledge Graph
one_liner: 利用论文-数据集引用图构建超大评估集，并通过 NN-SSC 域修正+BM25 融合及 Agentic 工具调用将检索精确率提升超 5 倍
practical_value: '- 借鉴引用图谱构造评估集：如将用户实际购买/点击的物品作为 silver label，构建百万级 query-item 对，低成本获得高质量的离线评测数据。

  - NN-SSC 轻量域适应：冻结通用 Encoder，仅训练一个 3 层 MLP 头（46 万参数）修正域偏移，可快速部署到任何已有向量召回服务上，成本极低。

  - 混合检索的解析融合权重：利用训练集上各检索支路的性能之比（π_n/(π_ℓ+π_n)）自动计算融合系数 α，无需网格搜索，直接用于 BM25+向量分数的凸组合。

  - Agentic 重排序提升 GMV：在候选集确定后，让 LLM 自主调用商品百科、用户问答、外部网页等工具补充上下文，可有效解决长尾 query 和歧义商品的排序问题，尤其适合高客单价决策场景。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
地球观测数据分散在数十个 DAAC 及工具中，即便领域专家也很难为研究问题快速匹配到最合适的数据集。通用 LLM 直接用于领域搜索面临两大挑战：预训练语料缺乏地学知识，且 RAG 的上下文窗口有限，重排序质量成为瓶颈。然而，该领域一直缺乏可信、可量化的大规模评测基准。

### 方法关键点
1. **NASA-EO-Bench 基准**：从 NASA EO-KG 的论文-数据集引用边（USES DATASET）出发，将论文摘要经 LLM 改写成 “I want to…” 形式的查询，构建了 47,654 个 query-dataset 正例对（21k 条查询，均 ta 均 2.24 个引用数据集）。训练/测试按论文级切分，避免泄露。
2. **三阶段搜索流水线**：
   - 路由层：若请求能被 NASA 官方工具（Harmony/SDE/WorldView）直接响应则提前结束；
   - 混合检索：BM25 锚定精确术语 + 领域适配的语义评分（NN-SSC 或微调编码器），凸融合得分。NN-SSC 在冻结的 backbone 上只训练一个 1536→256→256→1 的 MLP，学习 pair-specific 的偏置校正。
   - 重排序：先以 LLM 零样本列表式重排 top-K；再引入**Agentic 重排序**，LLM 可自主调用网络搜索与 arXiv 查阅，用 live 外部知识消歧和补充上下文。
3. **融合权重解析计算**：α = π_n/(π_n+π_ℓ)，其中 π_n, π_ℓ 分别为神经检索与 BM25 在训练集上的平均检索指标，避免超参网格调优。

### 关键结果
- 在 NASA-EO-Bench 测试集上，**NN-SSC + BM25 混合检索**较未适应的余弦基线，R@10 与 MRR 均提升 **5 倍以上**（R@10: 0.0755→0.4275，MRR: 0.0538→0.2918）。
- 零样本 LLM 重排序在所有五款模型上均使 MAP/MRR 稳定提升（最强 GPT-5.5 将 MRR 从 0.302 提至 0.383）。
- **Agentic 重排序**相比单次 LLM 重排带来方向性增益：Opus 4.7 的 MAP 从 0.317→0.323，MRR 从 0.367→0.388；DeepSeek v4 pro 同样正增益。且 Opus 仅在 41% 的查询上调用工具，收益反而更大，暗示“何时调用工具”是关键。
