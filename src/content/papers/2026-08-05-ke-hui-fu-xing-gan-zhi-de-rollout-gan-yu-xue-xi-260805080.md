---
title: 'Optimizing What Policies Learn From: Recoverability-aware Rollout Intervention
  Learning'
title_zh: 可恢复性感知的 Rollout 干预学习
authors:
- Zheyuan Zhang
- Manqing Mao
- Hong Wang
- Zhuoer Wang
- Samson Koelle
- Jie Yuan
- Yanjun Lin
- James Feng
- Nikki Lijing Kuang
- Yanfang Ye
affiliations:
- University of Notre Dame
- Amazon
arxiv_id: '2608.05080'
url: https://arxiv.org/abs/2608.05080
pdf_url: https://arxiv.org/pdf/2608.05080
published: '2026-08-05'
collected: '2026-08-06'
category: Training
direction: LLM Agent 后训练 · 可恢复性感知的 rollout 干预
tags:
- Reinforcement Learning
- LLM Post-training
- Rollout Intervention
- GRPO
- Agentic Reasoning
- Contextual Bandit
one_liner: 将 rollout 干预建模为在线 bandit，从 reward contrast 增益学习在何处、如何分支，提供更强的训练信号并节省算力
practical_value: '- **用 reward contrast 增益代替固定启发式作为干预信号**：在对话推荐或商品搜索 Agent 训练中，不用固定的熵或成功率来分配分支预算，而是预测一次额外
  rollout 能带来的 reward 方差增益（recoverability），并将其作为在线 bandit 的反馈，学习动态分支策略。

  - **Shadow-to-Live 双阶段部署**：先用高熵 anchor 检测 + 迭代分支收集 (state, action, gain) 轨迹，训练一个轻量控制器；在线训练时用
  utility gate 过滤低增益分支，并用 recency‑weighted 滑动窗口持续更新控制器。这种「先暖场再上场」的范式可直接迁移到线上 Agent
  训练系统。

  - **结构化干预空间**：不要只调 rollout 数量，同时联合选择 branch budget 和 decoding 温度（exploit / explore），让控制器学到「增加采样数」和「增加采样多样性」的组合策略，在稀疏奖励的交互推荐场景中尤其有效。

  - **在训练流程中实现算力与效果的 Pareto 改善**：实验表明 RAIL 用不到半数的 rollout 即可超越 GRPO‑32，在成本敏感的线上推荐
  Agent 训练中，可以用更少的交互获得更好的策略，显著降低环境交互开销。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**

基于 GRPO 的 LLM 后训练通常为每个输入均匀分配 rollout 预算，但不同任务和轨迹状态的学习价值差异巨大：某些状态能从额外探索中获得丰富奖励对比，而另一些已饱和或不可恢复，继续采样只会稀释梯度信号。现有自适应方法依赖固定的熵或难度启发式，无法适应策略演变（非稳态性），且只调整 rollout 数量而无法协同决定“在哪里分支”与“如何分支”（非标量性）。

**方法**

RAIL 将 rollout 干预转化为在线 contextual-bandit 学习：
- 定义 recoverability 为某一状态应用干预措施后 rollout 组 reward variance 的期望增益，以此衡量干预价值。
- 构建结构化干预空间：联合选择 branch budget（额外 rollout 数量）与 decoding 策略（温度控制探索程度）。
- Shadow 阶段：用高熵 anchor 检测候选分支点，以迭代接受‑或‑停止的方式收集 (state, action, gain) 轨迹，训练 recoverability controller。
- Live 阶段：控制器为每个候选状态预测干预收益，仅当收益超过 utility gate 时才执行分支；同时用 recency‑weighted 滑动窗口和 Huber 损失持续在线更新，跟踪策略演变。
- 策略模型维持 GRPO 原始优势计算，仅通过 reshape 后的 rollout 组获得更强学习信号。

**关键结果**

在 AgentBench‑OS、AgentBench‑DB、WebShop、ToolQA‑Coffee 四个 agentic 推理基准上，RAIL 在使用平均 10‑13 次 rollout（远低于 GRPO‑32 的 32 次）的情况下，整体成功率超越所有 baseline：例如 OS 任务 33.30% vs. 最佳 baseline 31.25%，DB 任务 61.67% vs. 60.25%，困难子任务（如 WebShop L2、ToolQA Hard）提升更为显著。消融表明，结构化干预（同时选择分支大小与温度）优于仅调数量的标量干预，且在线控制器比离线冻结控制器更低 MAE、更高符号一致性，验证了在线跟踪非稳态 recoverability 的必要性。

> **最值得记住的一句话**：让 rollout 生成过程本身成为一个根据 reward contrast 增益在线学习的 bandit 问题，比任何固定启发式都更适应训练中的策略漂移，并能用更少算力激发更强的学习信号。
