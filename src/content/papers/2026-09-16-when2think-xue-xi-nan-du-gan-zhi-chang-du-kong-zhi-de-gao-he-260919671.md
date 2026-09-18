---
title: 'When2Think: Learning Difficulty-Aware Length Control for Efficient Hybrid
  Reasoning Models'
title_zh: When2Think：学习难度感知长度控制的高效混合推理
authors:
- Jaejun Shim
- HyunJin Kim
- Young Jin Kim
- JinYeong Bak
affiliations:
- Sungkyunkwan University
- Microsoft
arxiv_id: '2609.19671'
url: https://arxiv.org/abs/2609.19671
pdf_url: https://arxiv.org/pdf/2609.19671
published: '2026-09-16'
collected: '2026-09-18'
category: Reasoning
direction: LLM 推理效率 · 自适应混合推理训练
tags:
- LLM
- RLVR
- Hybrid Reasoning
- Length Control
- Reward Shaping
- Reasoning Efficiency
one_liner: 用实例级难度感知奖励塑形动态分配推理深度，在数学基准上实现 AIME24 Pass@3 +10% 且 token -27.9%
practical_value: '- 用离线参考策略统计做难度/预算先验，在 RLVR 奖励中加 correctness-gated efficiency bonus，适合有确定性校验的业务任务（如商品属性抽取、意图分类、SQL
  生成），无需在线 critic/参考模型。

  - 采用 THINK / NOTHINK 模式 token 训练 system1/system2 自适应路由，可迁移到 Agent 工具调用或 RAG：简单 query
  直接回答，复杂 query 才触发多步检索/推理，降低平均延迟与 token 成本。

  - BWS 的 batch-wise reward 标准化稳定 critic-free PPO，适合小团队在不训练 reward model/critic 的情况下做后训练，且保留跨实例难度结构。

  - 难度用 reference accuracy 而非启发式长度定义，可能更 robust；业务场景可先用较大/teacher 模型对样本滚动评估得到难度标签。'
score: 8
source: huggingface-daily
depth: full_pdf
---

- **动机**：大型推理模型在简单题过度思考，在困难题思考不足；统一长度惩罚或刚性路由带来 efficiency tax，省了简单题但损失困难题准确率。论文将高效推理重新表述为 instance-adaptive computation allocation 问题。
- **方法关键点**：
  1. 基于 R1-Distill-Qwen-1.5B 做 RLVR 后训练，引入 THINK / NOTHINK 模式 token 控制是否显式推理。
  2. 离线预计算 reference statistics：用 reference policy 对每个实例采样 K=16 条轨迹，得到 α_i（参考准确率，难度代理）和 τ_i（平均 token 预算），训练中无需查询 reference model。
  3. IDAC 奖励塑形：r = V(1 + λδ) - α_i；THINK 时 λ = exp(-T·α_i/τ_i)，NOTHINK 时 λ=1。奖励既包含正确性，又按实例难度和轨迹长度给效率 bonus，α_i 做 instance-specific baseline 归一化。
  4. BWS：对 batch 内同一轨迹索引的 reward 求 μ_k 和 σ_k，计算优势 A=(r-μ)/(σ+ε)，无需 critic 即可稳定 PPO 风格裁剪目标。
  5. 重要性采样：初始 mode token 均匀采样平衡 THINK/NOTHINK 探索，后续 token 由当前策略生成，IS 权重纠正分布偏移。
- **关键实验**：训练数据为 DeepScaleR 约 40k 道竞赛数学题；评测覆盖 GSM-Plus、OlympiadBench、AIME24/25、Minerva、MATH-500。相比 R1-Distill-Qwen 基座，AIME24 Pass@3 从 46.0% 提升到 56.0%（+10.0%），token 减少 27.9%；AIME25 达到 40.0% Pass@3，优于压缩法和 routing-only 基线。MATH-500 Level 1 简单题 token 从 1199 降至 619，同时保持 95.8% 准确；Level 5 难题仍保持深度推理；THINK ratio 随难度从约 0.2 单调上升到 0.7。
- **最值得记住的一句话**：高效推理本质是 computation allocation 问题，不是 token compression；需要按实例难度动态控制“是否思考”和“思考多深”，才能避免 efficiency tax。
