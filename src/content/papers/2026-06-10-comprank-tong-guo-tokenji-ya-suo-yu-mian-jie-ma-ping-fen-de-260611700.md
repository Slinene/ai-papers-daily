---
title: 'CompRank: Efficient LLM Reranking via Token-Level Compression and Decoding-Free
  Scoring'
title_zh: CompRank：通过Token级压缩与免解码评分的LLM高效重排序
authors:
- Xuan Lu
- Haohang Huang
- Yingqi Fan
- Junlong Tong
- Yuxuan Zhang
- Ping Nie
- Rui Meng
- Xiaoyu Shen
affiliations:
- Shanghai Jiao Tong University
- Eastern Institute of Technology (Ningbo)
- University of British Columbia
- University of Waterloo
arxiv_id: '2606.11700'
url: https://arxiv.org/abs/2606.11700
pdf_url: https://arxiv.org/pdf/2606.11700
published: '2026-06-10'
collected: '2026-06-12'
category: RecSys
direction: LLM高效重排序
tags:
- LLM Reranking
- Token Compression
- CopyNet
- Attention Scoring
- Efficiency
one_liner: 提出CompRank，通过文档表示解耦、分段式token压缩和CopyNet式监督，仅保留10.2%文档token即接近全量重排序性能，并实现显著加速。
practical_value: '- **用稀疏注意力代替全量文档token**：在重排序时，仅保留文档中10%的token（如每10个取1个）即可保持性能，大幅降低交互成本。电商搜索/推荐中候选列表长，可直接应用此分段式压缩策略减少LLM重排序延迟。

  - **免解码式评分避免生成错误**：训练时用CopyNet直接优化注意力得分，推理时无需自回归生成ID，消除生成重复或超范围ID的问题。在推荐系统中，当候选集大小变化时，该方法比生成ID法更稳健，避免了分布偏移带来的解码失败。

  - **文档表示解耦实现可复用KV缓存**：将文档块与查询解耦，文档侧KV状态可预先计算并缓存，特别适合反复检索相同文档的Agent或RAG场景。在电商多轮对话或商品复筛流程中，可离线预计算商品表示，在线仅需处理查询侧计算，大幅降低在线延迟。

  - **训练与推理一致的注意力对齐目标**：使用CopyNet指针分布监督文档级得分，使训练直接服务于排序目标，优于SFT式的逐token生成。在建模用户与物品的相关性分数时，可直接采用类似pointer机制，让模型聚焦于候选集分布而非整个词表。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：LLM重排序已成为检索和RAG的关键组件，但在处理长候选列表（如top-100文档）时，自回归生成和全量token注意力计算带来极高延迟。排序信号本质稀疏，仅少数文档token对相关性有贡献，且同一批候选文档可能在不同query或推理步骤中被重复访问，产生了大量冗余计算。现有方法仍未充分消除文档侧表示和查询-文档交互中的冗余。

**方法关键点**：
- **文档表示解耦与位置无关性**：将文档块各自独立编码，共享位置偏移，禁止文档间注意力，使文档表示不依赖候选顺序和查询上下文，支持文档KV缓存复用。
- **结构化Token压缩**：在查询-文档注意力阶段，对文档侧token进行压缩，仅保留部分token参与评分。实验比较了Last-k、Segment-wise和基于内部注意力的Top-k三种策略，发现Segment-wise（每k个选1个）在覆盖率和压缩比间取得最佳平衡，Step-10仅保留10.2% token。
- **CopyNet式训练目标**：从指定Transformer层的注意力权重中聚合得到文档得分，定义候选集上的指针分布，用交叉熵优化正文档概率，训练与推理完全一致（均为免解码评分），避免生成ID错误。

**关键结果**：
- 在7个BEIR数据集上，CompRank（Segment-10）平均NDCG@10为39.2，接近全量token的39.7，但仅保留10.2%文档token。
- 在TREC-COVID上从30文档训练泛化至500文档推理，CompRank（Segment-10）比生成式列表重排序快4.9–9.5倍，比全量token CompRank快约1.3倍，且性能稳定（NDCG@10 79.5）。
- CopyNet训练准确率约70%，高于SFT解码准确率；模型在超出训练规模的候选集下无解码错误，而生成式方法出现大量缺失和重复ID错误。
