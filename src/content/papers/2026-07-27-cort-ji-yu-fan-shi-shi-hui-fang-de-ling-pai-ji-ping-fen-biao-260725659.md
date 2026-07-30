---
title: 'CoRT: Counterfactual Replay for Token-Level Rubric-Guided Policy Optimization'
title_zh: CoRT：基于反事实回放的令牌级评分标准引导策略优化
authors:
- Bo-Wen Zhang
- Junwei He
- Wen Wang
- Song-Lin Lv
- Wentao Ma
- Rongyi Lin
- Shuhan Zhong
- Lan-Zhe Guo
affiliations:
- Nanjing University
- ByteDance
- University of Chinese Academy of Sciences
arxiv_id: '2607.25659'
url: https://arxiv.org/abs/2607.25659
pdf_url: https://arxiv.org/pdf/2607.25659
published: '2026-07-27'
collected: '2026-07-30'
category: Training
direction: 令牌级信用分配 · 反事实回放
tags:
- GRPO
- token-level credit assignment
- counterfactual replay
- rubric-conditioned RL
- language model training
one_liner: 提出反事实回放计算令牌级信用权重，在不引入辅助模型的情况下改进 GRPO 的令牌级优势分配
practical_value: '- **令牌级信用分配可直接用于对话/推荐理由生成训练**：在电商客服或推荐文案生成中，常根据语义、格式等多条标准打分，将优势信号均匀广播到所有
  token 会导致噪声。CoRT 的令牌级加权方法可复制到类似场景，提升训练效率和生成质量，无需额外评分模型。

  - **反事实回放思路可迁移到评估对齐任务**：在搜索推荐系统的 LLM 评估（如 RAG 生成质量评价）时，可通过构造“有评分标准 vs. 无评分标准”的提示对比，自动获取每个
  token 对评分标准的依赖程度，作为细粒度奖励信号。

  - **纯推理侧实现，工程成本低**：CoRT 仅用两次前向传播（带与不带评分标准提示）计算 log-likelihood 差异，无需训练单独的 token 评分器，可直接插入现有
  GRPO 训练流程，适合资源受限的团队快速实验。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：基于评分标准的强化学习（如 GRPO）将多维评价压缩为单一标量奖励，并将响应级优势均匀分配到所有 token，忽略了不同 token 对不同评分标准的贡献差异。这导致信用分配不精确，影响训练效率与最终效果。

**方法关键点**：提出 CoRT，一种令牌级信用加权方法。核心思想是**反事实回放**——对同一采样响应，分别使用原始评分标准提示和无评分标准提示进行重打分，计算两者的 token 级对数似然差，作为每个 token 对评分标准依赖度的代理。该差异经有界响应归一化后，用于重新分配 GRPO 带符号优势，从而实现对不同 token 的差异化权重，整个过程无需额外训练 token 评分模型，也不改变响应级奖励。

**关键结果**：在指令微调模型及不同奖励粒度上的实验显示，CoRT 在绝大多数对比中优于响应级 GRPO 基线，平均胜出 4.4 个百分点。与需要单独学习 token 相关性的基线方法相比，CoRT 保持了竞争力，同时避免了额外的训练阶段。
