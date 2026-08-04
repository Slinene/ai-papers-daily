---
title: Collaborative Memory Augmentation for Generative Recommendation
title_zh: 协作记忆增强的生成式推荐框架
authors:
- Enze Liu
- Zhen Tian
- Wayne Xin Zhao
affiliations:
- Renmin University of China
- ByteDance
arxiv_id: '2608.01315'
url: https://arxiv.org/abs/2608.01315
pdf_url: https://arxiv.org/pdf/2608.01315
published: '2026-08-02'
collected: '2026-08-04'
category: GenRec
direction: 生成式推荐 · 协同记忆增强
tags:
- Memory Bank
- Latent Compression
- Target-Aware Retrieval
- Gated Cross-Attention
- Semantic ID
- Generative Recommendation
one_liner: 提出 OMEGA 框架，通过潜在压缩记忆库和目标感知检索将全局协同信号显式注入生成式推荐
practical_value: '- **记忆增强可无痛嫁接现有 GR 模型**：OMEGA 是模型无关的框架，仅需增加跨注意力模块和记忆检索，即可对 TIGER、Pctx、SETRec
  等 backbone 带来一致提升（NDCG@5 相对提升 16%~23%）。推荐团队可在现有生成式召回/排序模型上以轻量 fine-tuning 方式接入。

  - **潜在压缩降低在线存储与检索成本**：用 C 个可学习 query token 将变长序列压缩为固定维度嵌入（C=2 时已接近无损），存储开销极小。实际部署时还可以结合聚类裁剪记忆库，只用
  1% 的记忆容量即可保持效果，适合大规模工业检索。

  - **目标感知检索提升记忆相关性**：单纯按序列相似度检索效果差，引入目标 item 相似度（加权系数 α≈0.2~0.3）能更好地抓住“与当前意图相关的行为模式”。这一思想可直接用于电商搜索/推荐中的
  RAG 或记忆增强模块。

  - **两阶段微调策略防止语义漂移**：先冻结 backbone 只训跨注意力模块，再联合微调，避免记忆信号污染预训练表示。类似做法在 Agent 引入外部工具或记忆时也可借鉴。

  - **检索器质量决定天花板**：更强的检索器（如 HSTU 优于 SASRec）能带来更大增益，但效果并非简单模型蒸馏，而是记忆提供了独立于检索器的额外上下文信息。这意味着可以单独优化检索器来提升整个记忆增强系统的效能。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
现有生成式推荐（GR）只基于单个用户的交互历史生成 semantic ID，隐式依赖模型参数捕获全局协同模式，存在信息瓶颈，尤其对稀疏行为用户推荐乏力。受 LLM 上下文学习启发，本文提出 OMEGA——一个协作记忆增强框架，显式地将其他用户的相似行为作为外部记忆信号注入生成过程，弥补个体序列与集体协同之间的鸿沟。

## 方法关键点
- **潜在压缩记忆库**：用 C 个可学习 query token 对每个行为序列的前缀–目标对进行编码，得到固定长度的压缩表示 𝒁 ∈ ℝ^{C×d}，取代原始隐状态存储，极大降低存储开销。
- **目标感知检索**：采用轻量序列推荐模型（如 HSTU）生成序列表示，检索时既考虑序列级相似度，又加入候选目标 item 的相似度，α 加权平衡，提升记忆相关性。
- **门控跨注意力融合**：按检索分数经可学习参数生成实例级门控系数，抑制噪声记忆；再通过无因果掩码的跨注意力将记忆整合进 backbone 的编码器输出，配合残差和 FFN。
- **两阶段微调**：先冻结 backbone 只训跨注意力模块（注意力对齐），再端到端联合优化，避免冷启动记忆模块扭曲预训练表示。

## 关键结果
在 Amazon Instrument、Scientific、Video Games 三个数据集上，以 TIGER 和 Pctx 为 backbone，OMEGA 带来一致显著提升：TIGER 的 NDCG@5 绝对提升 16.2%~23.7%，Pctx 提升 6.6%~15.4%。仅用 2 个压缩 token 和 1% 记忆容量即可接近满记忆效果，检索系数 α 在 0.2~0.3 间最优，记忆数 K=10 已足够。额外在 ML-1M 和 Baby 数据集验证了长序列和大用户基场景的泛化性。

> 核心 insight：将全局用户行为压缩进外部记忆，并用目标感知检索动态注入生成过程，是提升生成式推荐性能的高效实用路径。
