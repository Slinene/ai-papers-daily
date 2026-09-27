---
title: 'OneTrans-V2: Unifying Retrieval, Pre-rank, and Fine-rank with One Transformer
  in Industrial Recommender'
title_zh: OneTrans-V2：用单一 Transformer 统一工业推荐中的召回、粗排与精排
authors:
- Hannan Cao
- Jun Guo
- Haolei Pei
- Zhaoqi Zhang
- Tianyu Wang
- Ziyang Wang
- Youchen Sun
- Yue Xue
- Yucheng Mao
- Lintao Yan
affiliations:
- ByteDance Global E-Commerce Recommendation Foundation Team
arxiv_id: '2609.28589'
url: https://arxiv.org/abs/2609.28589
pdf_url: https://arxiv.org/pdf/2609.28589
published: '2026-09-23'
collected: '2026-09-27'
category: RecSys
direction: 工业推荐系统级联统一 · 共享 Transformer
tags:
- One Transformer
- Cascade Unification
- Generative Retrieval
- Sparse MoE
- Sequence-Native Training
- Industrial Recommender
one_liner: 用一个 Transformer 统一召回/粗排/精排级联，共享用户上下文，结合 DCGR 与 SNT，GMV 提升 9.74%，吞吐 3.2×
practical_value: '- **统一多阶段用户表征**：在电商/广告推荐中，可将召回、粗排、精排的用户行为序列编码合并为一个共享 Transformer，通过
  stage visibility mask 隔离 stage-specific tokens，行为序列只需编码一次，显著减少重复计算，提升吞吐。

  - **生成式检索的多目标在线调控**：DCGR 的决策前缀 + 业务偏移量（βφ(z)）可以在不重新训练的情况下动态调节生成式推荐的目标倾向（如提升高客单价商品曝光），适合多业务目标共用一个生成模型。

  - **稀疏 MoE + μP 稳定扩展**：采用 DeepSeekMoE 式 fine-grained experts + shared expert，配 sigmoid
  router，结合 μP/Depth-μP 参数化，可在保持激活计算近似不变的前提下扩大模型容量，适合大规模推荐模型。

  - **SNT 训练效率优化**：按用户窗口组织训练样本，一次编码用户行为序列，该用户的所有曝光和所有 stage 复用该编码，训练加速 4.4×，适合行为序列长、曝光多的电商推荐场景。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：工业推荐系统通常采用召回、粗排、精排三级级联，但各级独立设计、训练和部署，导致用户行为序列被重复编码、优化目标孤立、工程重复、模型容量碎片化。之前的 OneTrans 只统一了单个排序模型内部组件，而级联仍割裂。为保留级联中丰富的候选特征，需要一种不消除级联、但共享用户上下文的统一方案。

**方法关键点**：
- 将三个 stage 作为单一因果 Transformer 的三个任务，共享 candidate-independent 的用户行为序列编码；每个 stage 追加自己的 stage-specific tokens，用混合参数化建模异构特征。
- 引入 stage visibility mask：行为序列 token 自注意力因果可见；stage-specific token 可看行为前缀，但 stage 间互相隔离，保证行为序列一次编码、多次复用。
- 联合训练三个任务，单模型内知识蒸馏：fine-rank 作为 teacher 指导 pre-rank，无需独立教师模型，提升两阶段一致性。
- DCGR：生成式检索在生成 SID 前先预测一个决策前缀（包含 purchase level, discovery level, supply type, spending level），再条件生成 item；业务目标通过加偏移 βφ(z) 到决策分布实现，可在线调节，无需重训；还提出 classifier-free guidance 扩展。
- 稀疏 MoE（fine-grained experts + shared expert, sigmoid router）提升容量但控制激活计算；μP/Depth-μP 稳定超参数；GQA 缩小 KV cache。
- SNT：按用户窗口组织训练，一次编码用户行为序列，该用户多个曝光和多个 stage 复用，训练加速 4.4×。

**关键实验**：在大型工业推荐系统生产日志上离线评估，部署到全部三个 stage，GMV 提升 9.74%；在相同硬件预算下，端到端 QPS 提升 3.2×；训练速度提升 4.4×。离线检索采用 HitRate@M 指标。

**最值得记住的一句话**：Unify the cascade, not eliminate it; share user context and decouple objectives via decision-conditioned generation.
