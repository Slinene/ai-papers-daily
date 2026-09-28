---
title: 'SLCA-GRPO: Resolving Cross-Segment Credit Misattribution in Tool-Calling RL'
title_zh: SLCA-GRPO：解决工具调用强化学习中的跨段信用错配
authors:
- Yan Zhan
- Shaobo Liu
- Qiunan Liu
- Yuanjun Shi
- Siqi Xu
- WeiYi Hou
- Xiang Xu
- Zekang Li
- Weizhou Pan
- Jiahong Yan
affiliations:
- Peking University
- Shenzhen University
- Tencent PCG QQ Team
arxiv_id: '2609.29050'
url: https://arxiv.org/abs/2609.29050
pdf_url: https://arxiv.org/pdf/2609.29050
published: '2026-09-23'
collected: '2026-09-28'
category: Training
direction: 工具调用 RL · 分段信用分配
tags:
- GRPO
- credit assignment
- tool calling
- RL
- agent training
one_liner: 将工具段与总结段优势解耦路由，从结构上阻断 summary 奖励对工具 token 的梯度泄漏
practical_value: '- 在工具调用 agent 的 RL 训练中，若总 reward 同时包含工具执行质量与最终回答质量，标准 GRPO 的统一 advantage
  会把 summary 噪声传到 tool token。可将轨迹按 token mask 自动分为工具段与总结段，分别做组内 z-score 并只路由到对应 token；几乎零额外成本，适合电商客服、订单查询等多
  API 场景。

  - 用 Schema-Guided LLM Simulator 替代真实 API 做 RL 探索：schema 校验给出确定性错误反馈，跨模型 LLM mock
  生成合理响应，降低真实 API 成本与不稳定；这可以作为离线 RL 基础设施，尤其适合工具 namespace 大的 MCP 生态。

  - 设计 process reward 建议拆成格式、工具名 F1、参数 key/value、并行度等子项（HierR），而不是单一稀疏信号；对要求低工具冗余的业务，可用类似
  Success@阈值 指标优化平均工具轮数。

  - 当模型该调工具却不调时，将 omission penalty 只路由到 summary 段，避免污染工具段，比在总 reward 上全局扣分更稳定。'
score: 8
source: huggingface-daily
depth: full_pdf
---

动机：工具调用 agent 的轨迹天然分为 `y_tool`（工具调用与推理）和 `y_sum`（面向用户的自然语言总结）。标准 GRPO 把所有 token 广播同一个 trajectory-level advantage，导致 summary 奖励的梯度噪声进入工具决策 token，造成跨段信用错配：错误/多余的工具调用可能因正确总结被强化，正确工具调用可能因错误总结被惩罚。ToolPO 增加局部工具奖励但仍存在 summary→tool 泄漏；RLTR 分离 planner/summarizer 但牺牲统一 backbone。

方法关键点：
- **SLCA（Segment-Locked Credit Assignment）**：用 token mask 自动分段，最后一个连续可学习 token run 为 summary，之前所有可学习 run 为 tool；对 tool reward 和 summary reward 分别做组内 z-score 归一化，得到 `A_tool` / `A_sum`，只路由到对应 token，保证 `∂g_tool/∂R_sum=0`，无需额外 rollout。
- **HierR**：工具段用 dense process reward（格式、工具名 F1、参数 key/value、并行度五个加权分量），总结段用 terminal preference。
- **SGLS**：Schema-Guided LLM Simulator，schema 校验 + 跨模型 LLM mock 生成仿真工具响应，替代真实 API 做规模化探索。
- 目标函数 PPO-clip + per-token KL，仅替换 advantage 标量，不改变采样。

关键结果：在 Qwen2.5-3B/7B-Instruct、Qwen3-8B-Base 上，用 Toucan-1.5M 做 RL 训练，Toucan-Test/BFCL/τ2-Bench 评估。7B matched GRPO 对比：Toucan Success@0.9 +2.53pp（79.13% vs 76.60%），BFCL V3 +1.36pp，τ2-Bench +9.15pp（0.410 vs 0.319）；3B/8B 同样一致提升。训练曲线显示 SLCA-GRPO 成功率高且平均工具轮数更少。消融显示去掉 SLCA 后 Toucan 下降 2.53pp、τ2-Bench 下降 9.15pp（7B），去掉 SGLS 和 HierR 也一致变差。

最值得记住：修复跨段信用错配不是靠加局部 reward，而是把 advantage 在结构段上分开归一化与路由，阻断 summary 奖励流向工具决策 token。
