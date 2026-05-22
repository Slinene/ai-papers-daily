---
title: 'From Reasoning Chains to Verifiable Subproblems: Curriculum Reinforcement
  Learning Enables Credit Assignment for LLM Reasoning'
title_zh: SCRL：子问题课程强化学习实现LLM推理细粒度信用分配
authors:
- Xitai Jiang
- Zihan Tang
- Wenze Lin
- Yang Yue
- Shenzhi Wang
- Gao Huang
affiliations:
- LeapLab, Tsinghua University
- Qiuzhen College, Tsinghua University
arxiv_id: '2605.22074'
url: https://arxiv.org/abs/2605.22074
pdf_url: https://arxiv.org/pdf/2605.22074
published: '2026-05-20'
collected: '2026-05-22'
category: Reasoning
direction: 课程RL · 子问题分解与信用分配
tags:
- Curriculum Learning
- Credit Assignment
- GRPO
- Mathematical Reasoning
- RLVR
- Subproblem
one_liner: 通过可验证子问题构建难度课程，结合子问题级归一化把部分推理进展转化为细粒度学习信号，显著提升困难数学题的RL训练效率
practical_value: '- **多步推理任务的训练范式**：当业务问题可分解为可独立验证的子步骤（如电商长链决策、多轮Agent交互），可借鉴**子问题课程+进度感知奖励校正**，将稀疏最终奖励转化为密集的中间信号，避免梯度死区。

  - **细粒度信用分配**：**子问题级归一化**在每个子步骤位置独立计算优势，再映射到回答 span 的 token，无需额外奖励模型或过程标注。可直接用于多步推荐对话或规划模型，为每个中间决策分配细粒度学习信号。

  - **混合训练保持分布一致性**：采用一半课程 rollout、一半原始 rollout 的混合训练，防止 prompt 不匹配，保证模型在推理时能处理原始问题，适合在线
  on-policy 训练场景。

  - **降低生成器依赖**：实验表明即使使用较弱模型生成子问题，SCRR 依然有效，仅需有参考解即可分解，不要求完美构造，工程实现成本低。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：基于可验证奖励的强化学习（RLVR，如 GRPO）在困难数学题上常因正确样本稀少导致组内归一化失效，且样本级信用分配无法利用部分正确的进展。如何从困难题中提取更细粒度的学习信号，使模型在保持 on-policy 探索的同时有效利用中间步骤，成为关键。

**方法**：SCRL 包含三步。①**子问题构建**：给定题目与参考解，用外部 LLM 将推理链拆解为 K 个可验证的子问题，难度递增，最后一个子问题固定为原题，形成课程。②**在线滚动**：模型在一个 rollout 中批量回答所有子问题，用 `<pj>...</pj>` 标签标记答案 span；验证答案得到奖励向量，经**进度感知校正**（只保留最长连续成功前缀）得到最终子问题奖励。③**训练算法**：**子问题级归一化**在每个子问题位置独立计算优势，再映射回对应 span 的 token，实现 token 级信用分配；训练采用**混合组**：一半课程 rollout + 一半原题 rollout，共同优化。

**理论**：从 Fisher 信息几何证明，原题在低成功率时陷入梯度死区，而子问题分解将优化提升到乘积流形，恢复非退化的梯度信号，且恢复比随题目难度增大而增大。

**实验**：在 7 个数学推理基准上，SCRL 在 Qwen3-4B-Base 上平均准确率 35.0%，比 GRPO 的 30.9% 高出 4.1 个点（Qwen3-14B 上 +1.9）；在 AIME24/25、IMO-Bench 三个困难集上，pass@1 和 pass@64 分别提升 3.7 和 4.6 个点。消融证实：子问题数 K=4 最优；弱生成器仍能带来 2.7 点提升；奖励校正和位置归一化都是有效设计。

**核心 insight**：通过将困难题系统性拆解为可验证子问题，并用位置感知的归一化给予中间步骤独立信用，RLVR 得以跳出奖励稀疏的困境，而模型始终在自己的滚动中探索，避免引入外部前缀造成的分布偏移。
