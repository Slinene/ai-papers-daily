---
title: Do Sequential Recommendation Benchmarks Really Require Higher-Order Sequence
  Modelling?
title_zh: 序列推荐基准是否需要高阶序列建模？
authors:
- Aleksandr V. Petrov
- Praveen Chandar
- Paul N. Bennett
- Hugues Bouchard
- Mounia Lalmas
affiliations:
- Spotify
arxiv_id: '2608.19833'
url: https://arxiv.org/abs/2608.19833
pdf_url: https://arxiv.org/pdf/2608.19833
published: '2026-08-20'
collected: '2026-08-21'
category: RecSys
direction: 序列推荐基准评测 · 容量探针
tags:
- Sequential Recommendation
- Benchmark Evaluation
- Capacity Probes
- Transformer
- Pairwise Transition
- eSASRec
one_liner: 用 recency 加权成对转移探针发现多数基准无需高阶建模，Transformer 增益被高估
practical_value: '- 在电商/广告序列推荐中，先实现一个强 pairwise transition 基线（如 PCTM 或 SeqRules）作为“照妖镜”，避免被
  Transformer 在弱基准上的虚假增益误导；尤其当数据规模小、用户行为以短会话为主时，简单模型可能足够。

  - 评估新模型时，务必使用 full-catalogue ranking + seen-item filtering 的严格协议，不要用 sampled softmax
  或 paper-to-paper 比较；否则像 TIGER 这类生成式推荐在 Beauty/Sports/Toys 上可能被简单探针反超 65-70%，说明基准本身不支撑
  SOTA 宣称。

  - PCTM 的工程实现很轻：离线统计有向转移计数（距离衰减），在线做加权 log-prob 求和；无 embedding、无序列编码器，适合作为召回通道或冷启动兜底，尤其适合需要快速上线的场景。

  - 当你要引入 Transformer/LLM 做序列推荐时，先检查数据集是否“pairwise-sufficient”：如果成对转移+recency 已经解释了大部分
  NDCG，那么高阶建模的增量有限，应优先投入特征工程或更真实的工业数据。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
序列推荐领域大量采用 Transformer 架构捕捉高阶序列依赖，但现有基准（Amazon Beauty/Sports/Toys、MovieLens）是否真的需要高阶交互并不清楚。此前虽有研究发现部分数据集主要呈 Markov 性质或 recency 主导，但缺少一个系统的容量探针来检验“高阶建模增益”是否可测。

**方法关键点**  
- 提出两个 recency-weighted pairwise probes：SeqRules 和 PCTM，均不学习高阶序列表示，仅聚合历史中的成对转移证据。  
- SeqRules 是稀疏序列规则模型，调整距离衰减、行剪枝、历史长度和 IDF 权重。  
- PCTM 为每个历史 item 估计有向 next-item 分布，使用距离加权因果计数和 Bayesian 平滑；推荐时对近历史 item 加权 log-prob 求和，并加入 popularity 校正项。  
- 将两个探针的较好分数定义为 pairwise envelope；若 Transformer 模型无法超过该包络，则该基准不能证明高阶建模增益。  
- 全部使用 eSASRec 发布的 full-catalogue ranking、seen-item filtering 协议，复现 SAS+ 和 eSASRec 结果。

**关键实验与数字**  
- 在 Amazon Beauty/Sports/Toys 上，pairwise envelope 分别超过 eSASRec 复现 21.3%、14.8%、38.4%；在 ML-1M 上超过 4.4%。  
- 仅 ML-20M 上 eSASRec 保持明显优势：0.1969 vs 0.1431，留有 27.3% NDCG 未解释。  
- FMC+（只用最后一项的 full-softmax 模型）在 Toys 上超过两个 Transformer 基线，在 Sports 上达到 eSASRec 的 84%。  
- 按论文间比较，PCTM 在 Beauty/Sports/Toys 上比 TIGER 报告值高 65.4%/63.5%/70.8%，但因无官方实现无法验证，说明 paper-to-paper 比较不可靠。

**最值得记住的一句话**  
强 recency-weighted pairwise 探针是检验序列推荐基准是否真能衡量高阶建模增益的试金石；多数小基准不通过该检验。
