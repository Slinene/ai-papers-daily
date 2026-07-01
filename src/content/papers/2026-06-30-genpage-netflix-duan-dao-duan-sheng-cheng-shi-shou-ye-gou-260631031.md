---
title: 'GenPage: Towards End-to-End Generative Homepage Construction at Netflix'
title_zh: GenPage：Netflix 端到端生成式首页构建
authors:
- Lequn Wang
- Jiangwei Pan
- Fengdi Che
- Linas Baltrunas
affiliations:
- Netflix
- University of Alberta
arxiv_id: '2606.31031'
url: https://arxiv.org/abs/2606.31031
pdf_url: https://arxiv.org/pdf/2606.31031
published: '2026-06-30'
collected: '2026-07-01'
category: GenRec
direction: 生成式推荐 · 页面级自回归生成
tags:
- Generative Recommendation
- End-to-End
- LLM Training Recipe
- Reinforcement Learning
- Homepage Construction
- Custom Tokenization
one_liner: 用单个 Transformer 自回归生成整个多行首页，线上核心指标+0.24% 同时延迟降 20%
practical_value: '- 自定义 tokenization 大幅压缩行为序列长度：将用户行为、属性、上下文映射为固定词汇 token，显著降低输入长度和推理成本，适合搜索/推荐场景中的序列建模。

  - 页面级自回归生成 + 混合行解码：只自回归生成每行前几个关键实体，其余通过一次前向评分补全，平衡推理质量与延迟；电商首页、频道页或搜索结果页布局生成可复用。

  - 预训练+WBC 后训练范式：先用正反馈页面做 next-token 预训练，再用加权二分类直接预测每个 token 的即时价值，实现端到端生成式推荐器，替代传统多级模型。

  - 约束解码实现业务规则硬约束：利用 token 与实体/行的一一映射，通过 logit 掩码强制满足布局、去重、分类要求，适用于生成式推荐的可控输出。

  - 上下文注入与语义嵌入融合解决冷启动：对新物品通过注入元数据和内容语义嵌入，让模型在没有交互数据时也能生成合理推荐。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：Netflix 首页是由多行和多个实体组成的复杂布局，传统多阶段推荐流水线（召回、排序、重排）模块多、目标不一致，难以整体优化页面的交互效应（如不同行的“停止力”平衡、多样性）。GenPage 将首页构建视为一个生成式序列建模问题，用单个 Transformer 端到端地同时优化整页，以提升用户满意度和系统简洁性。

**方法关键点**：
- *统一序列表示*：用户上下文（历史行为、画像、请求特征）和首页（行和实体）均 token 化为域内词汇，行为序列经过大幅压缩（如一次播放用 4 个 token），页面按布局顺序线性化。
- *训练配方*：借鉴 LLM 的预训练-后训练流程。预训练用 positive 交互的页面做 next-token prediction；后训练有两种：加权二分类（WBC）在每个 token 预测该位置实体的即时奖励（符号和幅度），训练效率高，直接对齐 token 级目标；RL（Dr. GRPO）用页面级奖励模型优化整体回报，捕捉行/实体间交互，实验中带来额外多样性收益。
- *冷启动与新鲜度*：通过上下文注入新实体元数据、语义嵌入融合（打标时随机替换 fallback token）让模型利用内容信息；多节奏增量训练（每周全量重训+每日增量微调）和 fallback token 保持模型新鲜。
- *工程优化*：约束解码通过 token mask 强制业务规则；混合行解码仅自回归生成每行前少数实体，其余通过一次前向评分补全，大幅减少解码步数。

**关键结果**：
- 在线 A/B 测试：200M 参数的 WBC 模型对比成熟多阶段生产基线，核心用户参与指标提升+0.24%（p<0.001），端到端服务延迟降低 20%。
- 离线消融：预训练对 WBC 后训练有明显增益；在 120M–900M 参数范围内，损失呈幂律下降；丰富 prompt 带来的损失降幅（~6.9%）远超模型容量扩展（~1.3%），提示信息充分度是当前瓶颈；RL 后训练使得页面多样性在不影响主目标的情况下自发提升。

**值得记住的一句话**：在工业级生成式推荐中，**用自定义 tokenization 将整个页面序列化，并采用预训练+WBC/RL 后训练范式，能同时取得业务指标和延迟的双重收益，而丰富 prompt 信息往往比盲目扩模型更划算。**
