---
title: Joint Agent Memory and Exploration Learning via Novelty Signals
title_zh: 通过新颖信号联合学习智能体记忆与探索
authors:
- Shizuo Tian
- Xiaohong Weng
- Rui Kong
- Yuxuan Chen
- Guohong Liu
- Yuebing Song
- Jiacheng Liu
- Yuchen Li
- Dawei Yin
- Ting Cao
affiliations:
- Tsinghua University
- Sun Yat-sen University
- Baidu Inc.
- Tongji University
- Peking University
arxiv_id: '2606.01528'
url: https://arxiv.org/abs/2606.01528
pdf_url: https://arxiv.org/pdf/2606.01528
published: '2026-05-31'
collected: '2026-06-02'
category: Agent
direction: 智能体记忆与探索的联合学习
tags:
- Agent Memory
- Exploration
- Latent Memory
- Novelty
- GUI
- Code Coverage
one_liner: 利用代码覆盖率等持久新颖信号，联合训练智能体潜在记忆与探索策略，显著提升探索效率并减少 token 消耗
practical_value: '- **无监督的记忆训练信号**：在 GUI 或可嵌入环境中，利用代码覆盖率、新状态发现等持久新奇信号作为内在奖励，为记忆模块提供无需人工标注的训练目标。这可以迁移到电商
  App 自动化测试、Agent 探索冷启动等场景，用环境固有指标替代昂贵的人工反馈。

  - **轻量级历史压缩**：使用一个冻结的视觉语言模型将每一步（观测，动作）压缩为一个向量 token，大幅减少长对话的 token 开销。在电商客服 Agent
  或推荐对话系统中，可以类似地压缩多轮交互历史，避免上下文窗口膨胀，同时保持关键信息。

  - **自然课程式训练**：随着会话进行，奖励自然变得稀疏，迫使策略学习更深层的探索行为。在构建 Agent 的训练环境时，可以设计类似“先易后难”的奖励衰减机制，无需手动设计课程。

  - **联合训练记忆与策略**：将记忆压缩和对齐与策略梯度联合优化，避免解耦带来的次优解。对于需要记忆的推荐 Agent 或多智能体协作场景，可考虑将记忆模块的学习与任务目标直接对齐，而非单独训练或使用静态规则。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
开放环境中，智能体需要依靠记忆来区分已探索的行为与未知区域，但现有 LLM agent 的探索能力薄弱，且记忆训练缺乏明确的步级监督信号。作者观察到探索与记忆相互依赖：记忆帮助避免重复行为，而探索过程揭示哪些历史信息对决策有用。因此提出用持久的新奇信号（如 GUI 领域的代码覆盖率）作为无监督奖励，联合训练记忆压缩与探索策略。

## 方法关键点
1. **记忆压缩架构**：冻结的视觉语言模型（Qwen3-VL-2B）将每个（观测，动作）对压缩为一个向量 Token，形成线性对齐后注入策略模型的输入前缀，实现长历史的紧凑表示。
2. **新奇奖励定义**：以代码覆盖率提升作为二元奖励（触发至少一条未执行路径则+1），保证奖励的持久性，避免循环累积奖励；奖励随时间自然稀疏，形成课程式训练。
3. **数据收集与训练**：部署通用 LLM 在 86 个 Web 应用中执行探索，收集 24k 条样本；仅保留包含至少一步正奖励的轨迹片段，通过最大化动作似然联合更新对齐矩阵和策略模型。

## 关键实验
在 ScaleWoB 的 10 个未见过应用上评估 50 步探索，指标为累积覆盖奖励（累计触发新路径的步数）。JAMEL-9B（2B 压缩器 + 7B 策略）取得 20.7 分，超越所有开源基线（MAI-UI 8.4、Mobile-Agent 5.9），接近闭源 Gemini 3.1 Flash-Lite 的 ReAct-vision（20.9 分），且输入 Token 消耗仅为 ReAct-vision 的约 4.5%（1.06M vs 23.26M）。局部方案因上下文裁剪导致探索停滞，而 JAMEL 的潜在记忆保持持续上升曲线。

## 核心结论
持久的新奇信号可以为智能体记忆提供免费且有效的训练监督，使探索策略和记忆压缩在同一个循环中互相促进，既提升了探索深度，又大幅降低了计算开销。
