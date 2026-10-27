---
title: 'ProAS: A Progress-Aware Advantage Shaping Framework for Multi-Turn Agentic
  Reinforcement Learning'
title_zh: 面向多轮智能体强化学习的进度感知优势塑形框架 ProAS
authors:
- Bowen Ding
- Mingda Wan
- Yuhan Chen
- Jiyao Yuan
- Qi Zhu
- Futing Wang
- Heyuan Deng
- Fei Mi
- Lifeng Shang
- Tao Lin
affiliations:
- Zhejiang University
- Westlake University
- Westlake Institute for Advanced Study
- Huawei Noah's Ark Lab
arxiv_id: '2610.18683'
url: https://arxiv.org/abs/2610.18683
pdf_url: https://arxiv.org/pdf/2610.18683
published: '2026-10-24'
collected: '2026-10-27'
category: Training
direction: 多轮 Agent RL 信用分配 · 优势塑形
tags:
- GRPO
- advantage shaping
- credit assignment
- agentic RL
- multi-turn agents
- LLM
one_liner: 用动态任务参考图对轨迹级优势做非对称掩码和惩罚重分配，解决 critic-free 智能体 RL 的均匀信用分配问题
practical_value: '- 在基于 GRPO/DAPO 的智能体 RL 中，避免把轨迹级 advantage 均匀广播；可构造任务进度参考图（如电商购物流程：搜索→商品页→选规格→结算）给动作打
  reasonable/progress-advancing 标签，在优势侧做掩码和重加权。

  - 建议优先使用优势塑形而非奖励塑形：论文消融显示直接加 progress-aware reward 比 advantage shaping 低 14.1 个成功率点，简单
  mask 合理动作或按 suffix 长度加权也不如 Future-Drift 归一化重分配。

  - 工程上可以用历史成功会话自动构建/更新参考图，无需完美人工标注；即使剪枝 40% 或由教师模型蒸馏，只要保留在线演化，仍能带来显著提升，适合快速落地。

  - 对负优势轨迹，按动作引起的下游停滞程度（Future-Drift）对惩罚做比例再分配，优先惩罚早期偏航动作，比均匀惩罚更公平，能加速收敛（最高 2.44×）。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
多轮 LLM 智能体用 RL 训练时，critic-free 的 GRPO 把整条轨迹 reward 归一化后得到的 advantage 直接广播到每个 token/action，导致两个问题：正优势轨迹里无效动作被强化，负优势轨迹里早期关键动作和后期被污染动作都被同样惩罚。作者对 ALFWorld/WebShop 统计发现成功轨迹中不合理动作约占 40%，失败轨迹中非推进动作占 76-93%，说明均匀信用分配导致噪声被强化和真实偏差被忽略。需要一种无 critic 的细粒度信用分配方法。

## 方法关键点
- 构造 ARG（Agentic Reference Graph）：用成功轨迹抽象出有序子目标 DAG，每个子目标是一组状态等价类，动作是边。训练中动态演化，合并新成功轨迹的状态和动作。
- 用 ARG 对每个动作标注两个二进制属性：Reasonable（动作是否构成合法转移）和 Progress-Advancing（是否到达新子目标且不重复历史状态）。
- 优势塑形公式：正优势轨迹用 MUI（把不合理动作的 local advantage 置零）；负优势轨迹用 APR（按 Future-Drift 即从当前步到末尾非推进动作的包含计数做归一化，对早期引起下游停滞的动作施加更大负惩罚）。
- 无需训练 critic，仅需图查询和少量重新加权，可插拔到 GRPO/DAPO/GiGPO。

## 关键结果
- ALFWorld 上，GiGPO+ProAS 在 1.5B/7B 分别达到 91.9%/94.3% SR，超过 MiGPO 和 GPT-5.6-Sol（78.9%）。
- WebShop 上，1.5B 的 DAPO/GiGPO+ProAS 达 66.7% SR，比 MiGPO 高 13.1 分；7B GRPO+ProAS 达 70.8%。
- GRPO+ProAS 在 ALFWorld 1.5B 上比原始 GRPO 提升 16.7 分；训练收敛加速最高 2.44×（7B ALFWorld GiGPO+ProAS）。
- 消融：去掉 MUI 导致 ALFWorld 降 15.4 点；去掉 APR 降 3.7 点；用 progress-aware reward 而非 advantage shaping 低 14.1 点；随机 ARG 标签导致灾难性下降 39.3 点；40% 剪枝或蒸馏 ARG 仍有效，但在线演化重要。

**最值得记住的一句话**：对 multi-turn agent RL，与其用更稠密的 reward 或均匀 advantage，不如用任务结构图对 advantage 做非对称塑形：屏蔽不合理动作、按下游停滞程度重分配负惩罚。
