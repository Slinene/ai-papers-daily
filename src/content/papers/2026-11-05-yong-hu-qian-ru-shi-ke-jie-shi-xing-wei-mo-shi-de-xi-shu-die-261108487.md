---
title: User Embeddings are Superpositions of Interpretable Behavioral Modes
title_zh: 用户嵌入是可解释行为模式的稀疏叠加
authors:
- Jonathan Kozaczuk
- Zheng Dong
- Noyan Evirgen
- Keivan Majidi
- Eddie K. H. Ng
- Chris Porter
- Qi Zhao
- Jia Geng
- Changmao Li
- Brandon R. Feng
affiliations:
- Amazon
arxiv_id: '2611.08487'
url: https://arxiv.org/abs/2611.08487
pdf_url: https://arxiv.org/pdf/2611.08487
published: '2026-11-05'
collected: '2026-11-06'
category: RecSys
direction: SAE 分解用户嵌入 · 可解释受众检索
tags:
- Sparse Autoencoders
- User Embeddings
- Interpretability
- Audience Retrieval
- Superposition
- Recommender Systems
one_liner: 用稀疏自编码器事后分解用户嵌入为可解释行为模式，实现零样本自然语言受众检索
practical_value: '- 对现有用户 embedding 做 post-hoc SAE 分解，无需改上游模型；建议 4x overcomplete，L1
  penalty 用 decoder-orthogonality 准则选 λ，可低成本获得稀疏可解释行为模式，适用于电商 SVD/Transformer 用户表示。

  - 复用自然语言受众检索流程：对每个 SAE latent 用 LLM 做 auto-interpretation（输入激活/非激活用户历史），保留名称+描述+confidence；query
  时让 LLM 对 feature 打 0-10 分，保留 ≥5，按用户激活加权和排序。confidence≥0.6 过滤不可靠 latent，可替代需 seed
  的 lookalike 受众扩展。

  - 与 K-Means encoding 对比结论：K-Means 聚类中心重叠、特征冗余、覆盖率低；SAE 字典近正交、特征多样性高、coverage 显著高。做可解释受众/用户画像时优先
  SAE 而非 K-Means。

  - 工程细节：遇到 feature splitting 可按 decoder cosine>0.45 合并；transformer 用户嵌入建议 mean-pool
  最后层而非 last-token/CLS，便于 mode 级叠加；注意隐私风险：可自然语言查询敏感生命事件，需检测/剔除或隔离敏感 latent。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**：用户嵌入是推荐、个性化系统的核心，但密集且不透明，难以解释推荐原因、审计嵌入携带的信息，也无法直接用自然语言查询。传统方案要么需要预先定义 taxonomy + 原始交互数据，要么逐用户 LLM 标注成本过高。论文将 mechanistic interpretability 的叠加假设迁移到用户嵌入：把用户嵌入看作可解释行为模式的稀疏叠加，用稀疏自编码器事后恢复。

**方法关键点**：
- 生成模型推导：用户行为是少量行为模式的混合；当嵌入函数为样本均值时，用户嵌入近似等于模式质心的稀疏线性组合。非线性 transformer 通过叠加假设近似成立。
- 对预训练用户嵌入训练 ReLU SAE：4x overcomplete，L1 稀疏惩罚；用 decoder-orthogonality 准则选择 λ，支持对 feature splitting 的合并。
- LLM 自动解释：对每个 latent 输入激活/非激活用户及交互历史，生成名称、描述、confidence；query 时 LLM 对 latent 打分，保留高相关特征，按用户激活加权和排序，实现零样本 NL 受众检索。
- 验证数据：合成数据（75 个 ground-truth 模式、100k 用户）；真实数据 Open e-commerce 1.0（SVD 用户嵌入）和 MovieLens 1M（SASRec/BERT4Rec 序列嵌入）。

**关键结果**：
- 合成数据：在高叠加态 m<75 时，SAE 匹配或超过 PCA/ICA/NMF/K-Means encoding；m=128 时合并后中位 per-feature r 从 0.35 升至 0.70；transformer 嵌入上 SAE code-GT alignment 0.58，恢复 73/75 模式。
- Open e-commerce：SAE category Lift 1.93 vs text baseline 1.39，life-event Lift 5.30 vs 2.13；AUROC 0.705/0.715。
- MovieLens：SAE 与 K-Means 排名相当，但 coverage 98% vs 81-85%，FVU 0.032-0.041 vs 0.108-0.136；SAE 特征显著更少冗余，受众表征更多样。

最值得记住的一句话：用户嵌入本身就是稀疏叠加，用 SAE 后处理是低成本打通可解释行为模式与自然语言受众检索的入口，无需修改上游系统。
