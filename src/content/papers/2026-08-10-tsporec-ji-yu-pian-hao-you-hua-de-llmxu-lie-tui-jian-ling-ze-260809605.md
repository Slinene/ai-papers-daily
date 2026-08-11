---
title: 'TSPORec: Token Selection via Preference Optimization for LLM-Based Sequential
  Recommendation'
title_zh: 'TSPORec: 基于偏好优化的LLM序列推荐令牌选择'
authors:
- Wenqiao Zhu
- Chao Xu
- Haipang Wu
- Ji Liu
arxiv_id: '2608.09605'
url: https://arxiv.org/abs/2608.09605
pdf_url: https://arxiv.org/pdf/2608.09605
published: '2026-08-10'
collected: '2026-08-11'
category: RecSys
direction: LLM序列推荐 · 令牌选择与偏好优化
tags:
- Sequential Recommendation
- LLM
- Token Selection
- Preference Optimization
- Proxy Reward
- Efficiency
one_liner: 通过偏好优化自动选择信息令牌，在提升序列推荐准确率31%的同时推理开销降低63%
practical_value: '- 处理商品长文本描述时，可采用类似的令牌选择策略压缩输入序列，优先保留内容词（名词、形容词、实体），滤除高频功能词，在电商推荐中减少
  LLM 推理延迟。

  - chunk-level 选择提供了灵活的粒度控制，工程上可通过调节 chunk size 在性能和效率间取得平衡，离线预计算 item 令牌子集后直接用于在线服务。

  - 偏好优化的 proxy reward 设计简单有效：对比两次采样子序列的交叉熵，无需外部标注，该范式可迁移至搜索、广告创意排序等需要精简文本输入的场景。

  - 三阶段训练（预训练→策略学习→重训练）虽然额外增加训练耗时，但模型一次训练长期部署，适合推荐系统离线优化的节奏，推理效率的提升远大于训练成本。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
现有 LLM 序列推荐为降低推理成本，通常只取商品描述的前 k 个 token，丢弃了完整文本中的大量语义信息，导致推荐效果次优。论文探究能否从全文自动选出最具信息量的 token 子集，同时提升准确率和效率。

**方法关键点**
- **三阶段流程**：① 使用完整 token 序列预训练 Item LLM + User LLM（InfoNCE 损失）；② 冻结 LLM，附加策略头（用 query‑key 注意力计算每个 token 的重要性分数），通过两次采样子序列构建正负偏好对，以交叉熵比较结果作为代理奖励，最大化期望奖励训练选择策略；③ 用训练好的策略按 chunk 粒度选择信息 token，构建精简数据集，重新训练推荐模型。
- **chunk 级选择**：以连续 token 组成 chunk 为单位进行选取，既保留局部语义结构，又可灵活控制粒度。
- **代理奖励**：对同一用户交互序列采样两个子序列，计算各自对完整 item embedding 的交叉熵，较小者胜出，引导策略提升高信息 token 的概率。

**关键实验**
在 Amazon Books 和 Pixel 数据集上，以 Qwen3‑Embedding‑0.6B 和 TinyLlama‑1.1B 为骨干，对比 SASRec、HSTU、LLMinit、HLLM 等。TSPORec 在 Recall@5/10/50 和 NDCG@5/10/50 均大幅领先，Amazon 平均提升 29.43%，Pixel 提升 16.79%。仅用 64 个选中 token 即可达到或超过 HLLM 使用 256 个 token 的性能，推理时间降低 63.4%。

**核心洞察**
TSPORec 倾向于选择内容词（名词、实体）、过滤高频功能词，证明“**不是所有 token 都对推荐有益，通过偏好优化学习的选择策略能精准锁定判别性 token，实现效果与效率的双赢**”。
