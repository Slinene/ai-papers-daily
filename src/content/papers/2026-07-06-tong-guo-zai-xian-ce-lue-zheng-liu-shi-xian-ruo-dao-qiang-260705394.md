---
title: Weak-to-Strong Generalization via Direct On-Policy Distillation
title_zh: 通过在线策略蒸馏实现弱到强泛化
authors:
- Shiyuan Feng
- Huan-ang Gao
- Haohan Chi
- Hanlin Wu
- Zhilong Zhang
- Zheng Jiang
- Bingxiang He
- Wei-Ying Ma
- Ya-Qin Zhang
- Hao Zhou
affiliations:
- SIA-Lab of Tsinghua AIR and ByteDance Seed
- Institute for AI Industry Research (AIR), Tsinghua University
- Department of Computer Science and Technology, Tsinghua University
- Peking University
arxiv_id: '2607.05394'
url: https://arxiv.org/abs/2607.05394
pdf_url: https://arxiv.org/pdf/2607.05394
published: '2026-07-06'
collected: '2026-07-07'
category: Training
direction: 弱到强知识蒸馏 · 策略偏移迁移
tags:
- RLVR
- knowledge-distillation
- weak-to-strong
- on-policy
- LLM-reasoning
one_liner: 提出 Direct-OPD，将弱模型 RL 前后策略偏移作为隐式奖励，直接提升强模型推理能力
practical_value: '- 在搜索/推荐排序中，若需对大模型做 RL 微调但资源有限，可使用小模型进行 RL（如优化 CTR），然后通过 Direct-OPD
  将策略偏移量化为 log-ratio 奖励，蒸馏到线上大模型，避免大模型直接生成海量 rollout。

  - 对生成式推荐场景，用 cheap 的小模型 RL 探索（如生成更吸引点击的标题或物品 ID），再以隐式奖励形式强化大模型，无需额外奖励模型即可提升生成质量。

  - 在 Agent 系统中，让轻量级 Agent 先探索环境并计算动作概率变化，作为密集奖励训练大型决策模型，降低试错成本并加速策略迭代。

  - 工程上可复用弱模型已有的 RL 训练信号，不必重跑昂贵 sparse-reward RL，支持增量组合多个策略改进，适合持续在线学习。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**: 基于验证奖励的强化学习 (RLVR) 虽能有效提升大模型推理，但每次对新模型进行 RL 训练都需大量 rollout，成本高昂。作者探索弱到强替代方案：先用小模型廉价完成 RL，再将其学到的东西迁移到更强模型。直接蒸馏弱模型最终策略效果不佳，因其将 RL 收益与弱模型自身能力瓶颈混在一起。

**方法关键点**: 提出 Direct On-Policy Distillation (Direct-OPD)，核心是传递 RL 引起的**策略偏移**而非最终策略。它计算弱模型 RL 前后 checkpoint 对同一动作的 log-ratio，作为密集的隐式奖励（implicit reward），并作用于强学生模型的**在线策略状态**（on-policy states）。该信号告诉学生“哪些动作在 RL 后变得更可能被采纳”。整个过程无需显式训练奖励模型，也无需在学生模型上运行稀疏奖励 RL。

**关键结果**: 在数学推理基准 AIME 2024 上，用弱教师改进 Qwen3-1.7B，仅 8 张 A100 训练 4 小时就把准确率从 48.3% 提升至 62.4%，超越相同步数的直接 RL。方法还支持顺序组合多个策略偏移，进一步叠加收益。实验表明 RL 结果可作为跨尺度的隐式奖励信号复用，而不仅仅是模仿最终模型。
