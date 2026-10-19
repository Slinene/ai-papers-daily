---
title: 'FC-SWE: Failure-Conditioned RL for Long-Horizon Software Engineering Agents'
title_zh: FC-SWE：面向长程软件工程智能体的失败条件强化学习
authors:
- Jia Liufu
- Bin Hu
- Linglin Jing
- Terry Kong
- Yuki Huang
- Ashwath Aithal
- Wenming Yang
- Jun Yang
affiliations:
- NVIDIA
- Tsinghua University
arxiv_id: '2610.07898'
url: https://arxiv.org/abs/2610.07898
pdf_url: https://arxiv.org/pdf/2610.07898
published: '2026-10-05'
collected: '2026-10-19'
category: Training
direction: Agent 强化学习训练 · Failure-Conditioned RL
tags:
- RL
- SWE Agent
- GRPO
- Failure-Conditioned
- Long-Horizon
- Tool Use
one_liner: 引入失败条件 RL 框架，将失败补丁与验证反馈作为恢复轨迹上下文，SWE-bench Verified Resolved@1 从 GRPO 的
  38.9% 提升至 41.7%
practical_value: '- 失败反馈作为条件上下文：在电商搜索/推荐 Agent 中，可以把用户负反馈、工具调用失败或验证不通过的结果作为后续恢复轨迹的输入，训练模型主动修复而非重新独立采样，提升多轮交互成功率。

  - Trajectory-local rewards：将每次尝试的验证结果单独作为奖励，避免恢复成功错误归因到之前的失败补丁，适合多轮对话或工具调用中每轮独立评估的场景。

  - Active-set advantage estimation：只把同一 issue 下实际执行的初始和恢复轨迹纳入比较组，排除未执行的轨迹，可迁移到变长、条件依赖的轨迹训练，改善
  GRPO 在复杂 Agent 任务中的优势估计。

  - 测试时扩展尝试次数：训练只用最多两次尝试，但测试时用 11 次尝试 Resolved@11 达 70.7%，说明部署阶段可以配合验证器多次尝试，显著提升最终解决率。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：仓库级软件工程是典型长程任务，智能体需要多轮工具调用并适应有状态环境。现有 GRPO 训练独立采样多个轨迹，只比较终端奖励，忽略了失败补丁中的诊断信息。将失败反馈作为后续尝试上下文进行恢复训练，能更接近真实问题解决过程。

**方法关键点**：FC-SWE 在补丁验证失败后，将仓库恢复到原始任务状态，把失败补丁和验证反馈作为恢复轨迹的条件上下文。为适配完整的、多轮工具调用链，引入两个机制：trajectory-local rewards 保留每次尝试的验证结果，防止恢复成功奖励早期失败补丁；active-set advantage estimation 从同一 issue 下实际执行的所有初始和恢复轨迹中构建比较组，失败尝试保留、未执行尝试排除。

**关键结果**：在全部 500 个 SWE-bench Verified 任务上，使用 Qwen3.5-4B 和 SWE-agent，FC-SWE 达到 41.7% Resolved@1 和 52.8% Resolved@2，对比 GRPO 的 38.9% 和 48.5%。测试时允许 11 次尝试，FC-SWE 达到 70.7% Resolved@11。
