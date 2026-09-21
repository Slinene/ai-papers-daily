---
title: 'MoME: Mixture-of-Memory Embeddings for Context-Aware Sparse Lookup'
title_zh: MoME：上下文感知稀疏查找的混合记忆嵌入
authors:
- Muchen Li
- Leonid Sigal
- Renjie Liao
affiliations:
- University of British Columbia
- Vector Institute for AI
- Canada CIFAR AI Chair
- NSERC CRC Chair
arxiv_id: '2609.15126'
url: https://arxiv.org/abs/2609.15126
pdf_url: https://arxiv.org/pdf/2609.15126
published: '2026-09-13'
collected: '2026-09-21'
category: Training
direction: 上下文感知稀疏记忆嵌入
tags:
- Mixture-of-Memory
- Sparse Memory
- Context-Aware
- LLM Pretraining
- Memory Embeddings
- Scaling
one_liner: MoME 用上下文门控选择 M 个记忆槽的混合，取代单一行记忆，在 iso 参数/FLOP 下优于现有稀疏记忆基线，并改善 scaling 趋势。
practical_value: '- 在 LLM4Rec / Query 推荐等场景，可将类目、品牌、高频 query 模板等静态知识注入 token 级条件记忆：用
  MoME 式混合门控取代固定 embedding lookup，按上下文选择多个 slot，能区分“苹果”手机与水果等多义 token，提升下游意图理解。

  - 在线 serving 需要低延迟稀疏查找时，条件记忆比 MoE 更便宜；MoME 的推理开销接近简单 embedding lookup，适合在推荐/搜索模型里增加轻量领域记忆，而无需承担
  expert 路由与全激活成本。

  - 对于搜索 query 生成/改写，可借鉴其多槽分离机制，将同一 surface token 的多种语义分开存储，由 learned gate 自动识别意图；定性结果显示路由具有可解释性，有助于后续分析或人工干预。

  - 工程实现上注意 slot 数 M 与训练 FLOP 的平衡：MoME 在 sub-billion 规模下 memory-size scaling 趋势更优，说明在中小规模模型上增加记忆容量比扩大
  dense 参数更具性价比。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**
LLM 高效扩展常依赖稀疏容量机制。现有 conditional memory 方法通过 token surface form 的确定性函数检索，导致同一 token 的不同上下文语义（如 python 语言 vs. 动物）塌缩为单一固定条目，削弱记忆的区分能力。

**方法关键点**
MoME 把每个 token 的单条 memory row 替换为 M 个 slot 的混合，引入基于 hidden state 的 learned gate，在每个位置选择读取哪些 slot，从而实现上下文感知的稀疏 lookup。该设计保留 conditional memory 的便宜参数查找特性，同时避免 surface form 塌缩。

**关键结果数字**
在 nanochat、Llama-3/MobileLLM、Qwen3 多个骨干的受控预训练实验中，MoME 在 iso-parameter 和 iso-training-FLOP 设置下均优于 Value Embedding、Bigram、STEM 基线；在 sub-billion 规模观察到的 memory-size scaling 趋势更具前景；训练与推理开销保持高效。对多义词的定性路由分析显示，同一 surface token 在不同语义下被分配到不同 memory slot，表明学到的混合具备一定语义可解释性。
