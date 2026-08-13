---
title: 'Making Collaborative Signals Count: Graph-Aware Large Language Models for
  Sequential Recommendation'
title_zh: 让协同信号发挥作用：面向序列推荐的图感知大语言模型
authors:
- Fenglin Yan
- Bohao Wang
- Jian Zhang
- Yu Cui
- Tongya Zheng
- Ye Feng
- Can Wang
- Jiawei Chen
affiliations:
- 浙江大学
- 中国科学技术大学
arxiv_id: '2608.12184'
url: https://arxiv.org/abs/2608.12184
pdf_url: https://arxiv.org/pdf/2608.12184
published: '2026-08-12'
collected: '2026-08-13'
category: GenRec
direction: 生成式推荐 · Graph-aware LLM
tags:
- Graph-Aware LLM
- Sequential Recommendation
- Collaborative Filtering
- Attention Bias
- LLM4Rec
one_liner: 将全局 item 共现关系分桶为可学习 attention bias 注入 LLM，无需外部图编码器即可联合建模语义与协同信号
practical_value: '- 在 LLM 生成推荐候选时，用「item token + item-item 共现分桶 attention bias」替代直接拼接
  CF embedding，可缓解协同表示与文本空间不对齐；工程上只加少量 bias 参数，适合 LoRA 微调。

  - 共现强度用等频分桶（如 5 桶）作为离散 relation，比原始稀疏频率更稳定，且只从训练集统计；在电商 item 候选上可直接计算 item co-occurrence
  或 query-item 共现并复用。

  - 保留 Text-Text 与 Item-Text 关系显式建模，能减少 LLM 语义能力损失；消融显示三类关系互补，缺少任一都会掉点，尤其全局 Item-Item
  关系对跨序列协同至关重要。可借鉴做「graph bias」式的知识注入，不必改 LLM 结构。

  - 推理侧采用 trie-constrained beam search 限制生成到合法 item 集合，是 LLM 电商候选生成落地的必要工程手段；item
  token 从现有 CF 模型 embedding 经 MLP 投影初始化，可复用 SASRec 等已有向量。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
LLM 做序列推荐大多依赖语言语义，难以捕获用户-物品交互中的协同过滤信号。以往方案要么把外部推荐模型学到的 CF embedding 注入 prompt，但嵌入空间错位、模型实际归因给 CF token 的注意力很低；要么用特殊 attention mask 只增强序列内 item 依赖，忽略跨序列全局共现。因此需要一种让 LLM 直接感知全局协同图的方法。

**方法关键点**  
- 混合 prompt：每个历史 item = 文本 tokens + 一个专用 item token；item token embedding 可由 SASRec 表示经 MLP 投影初始化。
- token 级协同图：定义三类边：Item-Item 基于全局 item 共现频率，等频离散化为 5 个 relation bucket；Item-Text 连接 item token 与其文本描述；Text-Text 保留文本语义依赖。
- 图感知注意力注入：在每层 Transformer 的 attention logit 上加 relation-specific 可学习 bias，保留 causal mask，不引入额外图编码器。这相当于把图结构变成轻量偏置，随层堆叠实现隐式多层图聚合。
- 训练/推理：LLaMA-3.2-3B 骨干 + LoRA rank=8；生成时用 trie-constrained beam search 约束到合法 item。

**关键结果**  
在 Amazon Toys、Clothing、Books 和 MovieLens-10M 上，GALLM 全面优于 SASRec、LightGCN、BIGRec、LLaRA、HatLLM、TCA4Rec 等 baseline。HR@5 相对最强 baseline 平均提升 9.76%，NDCG@5 平均提升 7.62%；在 1B/3B/8B 不同骨干上持续有效。消融显示删除任一 relation 都会掉点；注意力分析发现 Item-Text attention 在 Toy 上相对提升 54.2%，Item-Item attention 随共现强度单调增加，说明 bias 有效重塑了注意力。

**值得记住的一句话**  
把全局共现关系编码为 attention bias，比注入 CF embedding 更轻、更有效地让 LLM 联合建模协同与语义。
