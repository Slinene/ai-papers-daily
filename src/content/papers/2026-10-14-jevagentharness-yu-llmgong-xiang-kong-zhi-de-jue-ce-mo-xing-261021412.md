---
title: 'JevAgentHarness: Benchmarking, Deploying and Training Decision Models That
  Share Control with LLMs'
title_zh: JevAgentHarness：与LLM共享控制的决策模型基准、部署与训练
authors:
- Kunlun Zhu
- Tao Feng
- Xu Han
- Heng Wang
- Ling Yang
- Xiangru Tang
- Jiaxuan You
- Heng Ji
affiliations:
- University of Illinois Urbana-Champaign
- Princeton University
- Google
arxiv_id: '2610.21412'
url: https://arxiv.org/abs/2610.21412
pdf_url: https://arxiv.org/pdf/2610.21412
published: '2026-10-14'
collected: '2026-10-16'
category: Agent
direction: Agent决策模型与LLM级联降本提速
tags:
- agent harness
- decision models
- cascade delegation
- JEV
- cost-latency optimization
- benchmark
one_liner: 以置信度阈值将Agent常规多选决策委派给4B决策模型，最高降本89%、提速2.5倍，成功率损失<3点
practical_value: '- 在电商/推荐 Agent 的 tool call 与参数选择中，可以把大量常规多选决策（查订单、选参数、退款原因、确认动作）交给
  4B 级 decision model，按置信度级联；阈值需按 decision point 在 shadow 轨迹上单独拟合，不要用全局固定阈值（论文固定0.5掉21.5点）。

  - 评测决策模型不能只看离线准确率：StartLux-9B 离线最好但在 task-level 仅 69.5%；建议建立 step-level/task-level
  回归集，特别是包含错误后状态和 must-ask 状态，否则会误判上线收益。

  - 训练专属小决策模型时，用业务 agent 自己的轨迹做 SFT 非常划算（Qwen3-4B shifted task 成功率 13.5%→96.0%，仅 2.2
  GPU-hours）；数据里要刻意注入错误后状态（论文30.9%），否则模型无法应对 agent 自身失误后的局面。

  - 不可逆/高风险动作（取消订单、支付、发送消息）不要只交给 decision model 或 guard；对新增业务规则需重新训练/重新拟合阈值，否则成功率可能从88%跌到3%。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
LLM agent 每步都调用大模型，长任务慢且贵；但大部分调用最终落到 multiple-choice 决策（选哪个 tool、参数、是否 stop）。JEV 等 decision model 直接对选项打分，一次调用只需 LLM 的 28% 时间、2.6% 价格。问题在于：决策模型在隔离题上高分，不代表在 agent 闭环里可用；错误会跨步传导，且 agent 会遇到自己犯错后的状态。因此需要一套在 agent 内部测试、按置信度使用、并在 agent 自身轨迹上训练的机制。

**方法关键点**
- AgentDecisionBench：三层评测 L1 隔离选择、L2 记录运行逐步评分、L3 实际控制 running agent；新增 Decision Gym 环境，提供每个状态可接受下一步的 answer key。
- JevAgentHarness：把工具/参数选择拆成 typed multiple-choice 问题；每个 decision point 在 shadow-mode 轨迹上拟合置信度阈值 τ_d，只有 confidence ≥ τ_d 才用决策模型，否则 LLM 兜底；支持 REPLACE/CASCADE/ASSIST/GUARD/TRIGGER 五种模式。
- AgentDecision-4B：Qwen3-4B + LoRA，先用 agent 自身轨迹 SFT，包含 30.9% 错误后状态；目标混合 one-hot 和 JEV 概率分布，加 Brier 校准项；再用 GRPO 在 agent loop 中 RL。

**关键实验结果**
- 隔离题最佳模型 StartLux-9B（BFCL 92.2%）在 task-level 只解决 69.5% 任务；AgentDecision-4B 解决 91.5%，JEV 82.0%。离线圈分误导排名。
- 拟合阈值保护成功率：工具/参数 cascade 省 14.2% 成本，500 任务成功率无损失；固定阈值 0.5 掉 21.5 点。
- 部署效果：AgentDecision-4B 使 Decision Gym agent 降本 86.3%、提速 2.5 倍；ALFWorld 4B 训练后降本 89%，成功率不损。
- 训练收益：Qwen3-4B shifted task 成功率从 13.5% SFT 后到 96.0%；StartLux-4B 从 49.0% 到 98.0%；GRPO 无显著增益，SFT 是主因。

**最值得记住的一句话**：决策模型要在 agent 闭环里评估和训练；按决策点拟合置信度阈值，是把常规多选决策从 LLM 外包给小模型、安全降本提速的关键。
