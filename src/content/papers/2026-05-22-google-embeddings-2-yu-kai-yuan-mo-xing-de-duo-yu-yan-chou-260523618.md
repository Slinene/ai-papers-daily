---
title: Benchmarking Google Embeddings 2 against Open-Source Models for Multilingual
  Dense Retrieval and RAG Systems
title_zh: Google Embeddings 2 与开源模型的多语言稠密检索及 RAG 系统基准评测
authors:
- Stefano Cirillo
- Domenico Desiato
- Giuseppe Polese
- Giandomenico Solimando
affiliations:
- University of Salerno
- University of Bari
arxiv_id: '2605.23618'
url: https://arxiv.org/abs/2605.23618
pdf_url: https://arxiv.org/pdf/2605.23618
published: '2026-05-22'
collected: '2026-05-25'
category: RAG
direction: 多语言稠密检索模型评测
tags:
- dense retrieval
- multilingual embeddings
- RAG
- benchmark
- chunking
- latency
one_liner: 系统对比 GE2 与 5 款开源嵌入模型，揭示 GE2 质量最优但延迟高，mE5-L 在短文本几乎持平，LaBSE 完全不适合检索。
practical_value: '- **绝对不要用 LaBSE 做检索**：它的训练目标是跨语言句子对齐，与 top-k 相关性排序天然不兼容，BEIR 上 nDCG@10
  仅 0.188，FiQA 上低至 0.069，比随机还差。当前仍有很多教程将其用作多语言检索 backbone，应立即替换为 mE5-L 或 GE2。

  - **短文本、单语场景优先用 mE5-L**：在意大利语短篇章（平均 60 token）上，mE5-L 的 nDCG@10=0.279，与 GE2 的 0.282
  几乎无差异，但延迟仅 31 ms，比 GE2 快 7.5 倍，适合对 <100ms SLA 敏感的实时检索或在线推荐服务。

  - **长文档或 query–doc 严重不匹配时切换 GE2**：对于法律文本、医疗文献等长篇幅内容，GE2 的 2048 token 上下文窗口避免了 BERT
  系模型的截断损失；其`RETRIEVAL_QUERY`/`RETRIEVAL_DOCUMENT` 的非对称条件编码能系统性地处理 query 与文档的词汇风格差异，在
  TREC-COVID 等任务上优势明显（0.799 vs 0.702）。

  - **分块策略可大幅简化**：在短篇章体裁（平均 60 token）中，所有模型在 32 token 即达性能饱和，进一步增大分块无增益；可优先使用固定 256-512
  token 的窗口，仅在 token 极度受限（16 token）时语义分块才有效果。这可以将分块调优成本降为零。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

## 动机
RAG 系统的性能上限由检索阶段决定——漏检的段落无法被生成模型利用，且错误不可恢复。但实践中，嵌入模型的选择常被简化，例如大量教程将基于对称句子相似度的 LaBSE 用于非对称的 query–passage 检索，导致严重的质量损失。同时，Google 的闭源 Embeddings 2 (GE2) 发布后缺乏独立评测，其 2048 token 上下文与任务类型条件机制的实际收益不明。此外，分块策略对检索质量的影响也缺少跨模型、跨大小的系统性消融实验。

## 方法关键点
- **模型对比**：GE2（text-embedding-004，768 dim，2048 上下文，支持`RETRIEVAL_QUERY`/`RETRIEVAL_DOCUMENT`非对称编码）与 5 种开源模型：BGE-M3、E5-large、mE5-L、LaBSE、mMPNet。
- **评测协议**：零 shot 设定，采用 BEIR 的四个子集（FiQA-2018、NFCorpus、SciFact、TREC-COVID）及自建的意大利语 IT-RAG-Bench（3200 段落、640 条模板查询，源自维基百科、行政 FAQ、民法条文）。指标包括 nDCG@10、MRR、Recall@k。
- **分块消融**：针对 IT-RAG-Bench，比较固定大小、滑动窗口（50% 重叠）和语义分割三种策略，分别在 8、16、32、64、128 token 粒度下评估，揭示饱和点与策略优劣。
- **延迟测量**：单查询 CPU 端到端耗时（Apple M 系列），报告中位数、标准差与 p95。

## 关键结果
- GE2 在 BEIR 平均 nDCG@10 达到 0.638，领先 mE5-L 0.092 点；但在 IT-RAG-Bench 上仅高出 0.003，可视为持平。
- LaBSE 在所有检索任务中垫底，BEIR 平均 0.188，FiQA 仅 0.069，暴露其对称相似度目标与检索排序的根本冲突。
- mE5-L 延迟 31 ms，GE2 为 231.6 ms（p95 达 575.5 ms），前者可在绝大多数实时场景中替换 GE2。
- 分块实验中，所有模型在 32 token 时达到 95% 以上峰值 nDCG，再增大无益；语义分块仅在 16 token 时产生可测量增益（约 +0.075 nDCG）。

## 一句话记忆点
GE2 在长文档与 query–doc 高度不匹配的检索中拥有结构优势，但在常见的短篇章、低延迟场景下，mE5-L 以几乎同等的质量和 1/7 的延迟成为更务实的引擎，同时 LaBSE 绝对不应被用于任何 RAG 检索通路。
