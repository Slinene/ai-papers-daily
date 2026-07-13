---
title: 'Long-Horizon-Terminal-Bench: Testing the Limits of Agents on Long-Horizon
  Terminal Tasks with Dense Reward-Based Grading'
title_zh: 长周期终端基准：密集奖励检验长任务智能体极限
authors:
- Zongxia Li
- Zhongzhi Li
- Yucheng Shi
- Ruhan Wang
- Junyao Yang
- Zhichao Liu
- Xiyang Wu
- Anhao Li
- Yue Yu
- Ninghao Liu
affiliations:
- Tencent HY LLM Frontier
- University of Maryland, College Park
- University of Georgia
- Indiana University
- Lehigh University
arxiv_id: '2607.08964'
url: https://arxiv.org/abs/2607.08964
pdf_url: https://arxiv.org/pdf/2607.08964
published: '2026-07-08'
collected: '2026-07-13'
category: Eval
direction: 长程终端智能体评估 · 密集奖励
tags:
- Long-Horizon Agent
- Terminal Benchmark
- Dense Reward
- Sub-task Decomposition
- LLM Evaluation
one_liner: 提出长周期终端基准LHTB，细粒度子任务与密集奖励评估智能体长程能力，最强模型仅15.2% pass@1
practical_value: '- 子任务分解与密集奖励：在构建多步自动化 Agent（如广告优化、商品文案测试）时，可借鉴将复杂任务拆解为可评分的子任务，设计中间奖励信号，支持逐步改进和部分成功。

  - 长上下文与记忆管理：任务平均消耗9.9M tokens，提示在实际Agent中需要处理超长上下文，可引入检索增强（RAG）或层次化记忆，避免关键信息遗忘。

  - 迭代调试与容错机制：论文发现Agent失败多因环境错误和调试不足，业务系统应加入自动重试、错误恢复和环境状态检查，提升长流程稳定性。

  - 过程性评估：从只看最终结果转向细粒度过程评估，帮助定位Agent瓶颈，适合用于评估复杂推荐或运营Agent的中间决策质量。'
score: 6
source: huggingface-daily
depth: abstract
---

现有终端基准主要面向短程任务，仅以最终结果评估，忽略中间进展，奖励信号稀疏。为此，论文推出Long-Horizon-Terminal-Bench (LHTB)，包含46个长周期终端任务，覆盖实验复现、软件工程、多模态分析、交互游戏等9类。每个任务在Terminal-Bench风格基础上，细分为多级可评分子任务，提供参考解或模拟引擎，实现密集中间奖励与部分得分，能衡量智能体在多步开放式工作流中的推进程度。

评估15款前沿模型显示，任务平均消耗9.9M tokens、231个episode、85.3分钟，远超以往基准。最强模型在部分奖励阈值0.95时pass@1仅15.2%，完美奖励1.0时10.9%，所有模型均值分别为4.3%和1.7%，暴露出长程规划、上下文管理、迭代调试的巨大短板。失败模式分析指出环境错误和调试能力不足是主要障碍。

该基准为长程终端智能体提供了更细粒度的评估标尺，为后续研究指明了方向。
