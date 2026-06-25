---
title: Why Multi-Step Tool-Use Reinforcement Learning Collapses and How Supervisory
  Signals Fix It
title_zh: 多步工具使用强化学习的崩溃分析与监督信号修复
authors:
- Yupu Hao
- Zhuoran Jin
- Huanxuan Liao
- Kang Liu
- Jun Zhao
affiliations:
- 中国科学院自动化研究所复杂系统认知与决策重点实验室
- 中国科学院大学人工智能学院
arxiv_id: '2606.26027'
url: https://arxiv.org/abs/2606.26027
pdf_url: https://arxiv.org/pdf/2606.26027
published: '2026-06-24'
collected: '2026-06-25'
category: Agent
direction: 多步工具调用 RL 的稳定化训练
tags:
- RL collapse
- tool-use
- interleaved SFT-RL
- control token
- process supervision
- BFCL
one_liner: 揭示 RL 训练中控制 token 概率畸变导致的结构性崩溃，系统性对比 6 种监督信号并以交错训练实现稳定工具调用
practical_value: '- **RL 训练前务必先用 SFT 注入工具调用格式**：直接对未见过工具调用格式的模型做 RL 极容易发生 `tool_call`
  等控制 token 的概率膨胀，导致输出退化为 `<tool_call><|im_end|>` 的空结构，需先用少量 SFT 数据建立格式基础。

  - **交错训练（interleaved SFT-RL）比同步训练稳定得多**：在 RL 探索过程中间歇插入基于失败样本的 SFT 校正，可大幅减少格式漂移，避免
  KL 散度爆炸；尤其推荐 `Erroneous Trajectory Supervision + Process Reflection Supervision`，后者将中间步骤反思转化为文本监督信号，起到逻辑正则化作用。

  - **纯 RL 的“崩溃”可能是格式伪影而非能力丧失**：OOD 评估发现，单纯 GRPO 在分布外格式下反而稳定，说明崩溃主要集中在特定控制 token 的分布敏感区，真实工具调用能力仍然保留；因此线上部署时可考虑改变
  prompt 模板来规避训练格式过拟合。

  - **学习率对交错训练极为关键**：错误轨迹监督 (ETS) 在较高学习率 (1e-5) 下提升显著，而同步方法常因共享学习率导致优化不稳定；可借鉴其逐步增加
  RL 次数 + 错误 SFT 的调度策略。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

## 动机
多步工具调用是 LLM Agent 的核心能力，但基于 RL 的训练经常出现突然崩溃，性能直接降到接近 0，工具调用结构完全瓦解。本文研究了这一现象的根本原因：并非模型推理能力退化，而是 RL 过程中特定控制 token（如 `<tool_call>`、`<|im_end|>`）的概率被异常放大，导致输出格式逐渐污染，最终退化为无意义的终止序列。因此，如何通过监督信号稳定多轮工具调用 RL 训练成为关键问题。

## 方法关键点
1. **崩溃机制分析**：将模型输出分为四类——健康工具调用、健康文本响应、格式污染、完全崩溃，发现崩溃来自控制 token 的概率再分配，而非能力丧失。
2. **六种监督信号对比**：系统研究同步（on-policy 混合）与交错（SFT 与 RL 交替）两类范式，包括：SFT→RL、Off-policy 监督（OPS）、Hint-based 引导（HBG）、错误轨迹监督（ETS）、过程反思监督（PRS）。
3. **过程反思监督 (PRS)**：用 LLM 分析失败轨迹的中间步骤，生成反思文本，与错误纠正 SFT 联合训练，将隐式过程信息转化为显式文本监督，增强格式鲁棒性。
4. **交错训练调度**：逐步增加 RL 轮次（如 50/100/150），在每轮后对失败样本进行 SFT，有效解耦格式学习与探索。

## 关键结果
- 在 BFCL-V3 数据集上，Qwen2.5-1.5B 直接 GRPO 平均得分 0.0（完全崩溃），而 **PRS 达到 25.75，ETS 达到 20.0**，相比 SFT+RL 的 17.25 提升显著。
- OOD 泛化实验（ACEBench）揭示：SFT 导致严重格式过拟合，纯 RL 却在格式 OOD 下表现更稳定，PRS/ETS 可缓解单步性能下降，并维持多步泛化。
- 学习率分析：错误轨迹监督对学习率敏感，高学习率（1e-5）下相对基础模型提升 16.5 分，而低学习率（1e-6）仅提升 13.75。
