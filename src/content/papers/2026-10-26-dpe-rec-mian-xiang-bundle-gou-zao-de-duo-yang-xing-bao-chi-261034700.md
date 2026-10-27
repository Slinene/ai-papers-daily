---
title: 'DPE-Rec: Diversity-Preserving and Efficient Diffusion Language Model Recommendation
  for Bundle Construction'
title_zh: DPE-Rec：面向 Bundle 构造的多样性保持与高效扩散推荐
authors:
- Pingchuan Ma
- Bohan Jiang
- Chengshuai Zhao
- Dawei Li
- Zhen Tan
- Huan Liu
affiliations:
- Arizona State University
- Stevens Institute of Technology
arxiv_id: '2610.34700'
url: https://arxiv.org/abs/2610.34700
pdf_url: https://arxiv.org/pdf/2610.34700
published: '2026-10-26'
collected: '2026-10-27'
category: GenRec
direction: 生成式推荐 · Diffusion Semantic ID
tags:
- Diffusion Language Model
- Bundle Construction
- Semantic ID
- GRPO
- Trajectory Distillation
- Generative Recommendation
one_liner: 针对扩散语言模型在 bundle 构造中的多样性损失与并行解码质量退化，提出语义分叉感知 GRPO 与伪轨迹蒸馏，实现质量提升 63%、推理加速
  25.6 倍
practical_value: '- 在语义 ID 生成中，第一层 token 是粗粒度语义分叉，后续 token 是细粒度 refinement；可在后训练或采样时对第一层
  token 设置更高温度（如 0.6）以增加多样性，后续层设置低温度（如 0.2）保证准确率。这种 level-specific temperature 可直接迁移到电商类目/品牌/商品
  ID 生成。

  - 如需对 diffusion 模型做多样性优化，可借鉴其「autoregressive rollout + GRPO」后训练方式：仅通过推理顺序构造 AR 策略，不改动双向注意力架构，训练后仍保留并行解码能力。这比直接换因果模型成本低、兼容性好。

  - 推理加速上，伪轨迹蒸馏十分实用：用高质量顺序解码生成若干轨迹，只在这些轨迹诱导的中间状态上训练 student，使 student 能可靠地一次性并行 decode
  多个 token，降低 denoise 步数。该方法可复用到生成式推荐、query 生成等 DLM 场景，几乎不损失质量但大幅降延迟。

  - 对生成的 SID 做 legalization（映射回 catalog，非法 SID 用语义向量相似度匹配最近 item）是保证线上可用性的必要后处理，尤其在并行解码打开多
  token 时，能有效避免生成不存在的商品 ID。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
Bundle construction 是无序集合生成任务，自回归 LLM 的固定左右顺序强加了人为顺序，归纳偏置不匹配。扩散语言模型（DLM）的双向 attention 天然适合无序生成，且可每步揭示多个 token 降低推理延迟。但直接应用存在两个问题：① confidence-guided arbitrary-order 解码会优先揭示低熵的 refinement token，推迟高熵的 semantic fork（SID 第一 token），导致生成 item 高度相似、多样性差；② 每步多 token 并行解码依赖条件独立近似，容易生成非法 SID，质量和效率存在 tradeoff。

## 方法关键点
- **语义分叉感知 GRPO**：将预训练 DLM 在推理时诱导为 autoregressive 策略（不改动双向架构），按 fork-first 顺序 rollout。采样温度分层设置：semantic fork 位置温度 0.6，refinement 位置 0.2，集中探索多样分支。奖励函数采用层次 set reward，同时奖励粗粒度语义命中与精确 item 命中。GRPO 后训练只发生在 AR  rollout 阶段，模型保持双向结构，不影响后续并行解码。
- **伪轨迹蒸馏（PTD）**：用 GRPO 优化后的 teacher 以置信度引导顺序解码，生成高质量轨迹；构造轨迹诱导状态（保留前 r(t) 步，mask 其余）训练 student，并加入互补 mask 视图。训练中逐步提高 mask 比例，使学习集中在 teacher 访问的子空间。student 能可靠地并行 decode 多个 token，打破质量-效率 Pareto 前沿。
- **推理与合法化**：student 在每轮将置信度超过阈值的 mask 位置并行揭示，并用 top-q 保证在规定步数内完成。生成的 SID 通过 exact mapping 或语义相似度匹配到 catalog item。

## 关键实验
在 Spotify（30/60/90）、POG（4-item outfit）、IQON3000（8-item outfit）五个 setting 上，与 9 个 baseline（GRU4Rec、SASRec、BERT4Rec、FDSA、RecJPQ、HSTU、UniGRec、DiffGRM、DDBC）对比。DPE-Rec 在 F1/Jaccard/OAS 上平均相对提升约 63%；其 fast 变体相比三个生成式 baseline 平均推理加速 25.6 倍，质量损失很小。Ablation 显示 +GRPO 带来 F1 +28.86%、Jaccard +33.29%，+PTD 使 latency -89.52%，而三项质量指标仅下降约 2.5%。生成 item 的 pairwise cosine similarity 显著低于 DDBC、DiffGRM、UniGRec。
