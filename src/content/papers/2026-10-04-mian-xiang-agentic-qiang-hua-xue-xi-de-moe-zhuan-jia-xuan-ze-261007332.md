---
title: Structuring MoE Expert Selection for Agentic Reinforcement Learning
title_zh: 面向 Agentic 强化学习的 MoE 专家选择结构化
authors:
- Bolian Li
- Ting-Yao Hu
- Cheng-Yu Hsieh
- Sanjoy Chowdhury
- Oncel Tuzel
- Raviteja Vemulapalli
affiliations:
- Apple
- Purdue University
arxiv_id: '2610.07332'
url: https://arxiv.org/abs/2610.07332
pdf_url: https://arxiv.org/pdf/2610.07332
published: '2026-10-04'
collected: '2026-10-08'
category: Agent
direction: Agent RL · MoE 专家路由控制
tags:
- MoE
- Agentic RL
- Expert Routing
- GRPO
- Entropy Gate
- Long-horizon Agent
one_liner: 提出分层路由控制框架，用操作感知互信息与令牌级一致性约束，提升 Agentic RL 成功率与推理吞吐
practical_value: '- MoE 专家选择可以用 agent 轨迹中的 operation 语义（READ/CREATE/UPDATE）做监督，电商搜索/推荐
  agent 也可以按意图或工具类别进行专家对齐，提升长程任务成功率和推理速度。

  - token 级一致性控制用“相邻 top-k 专家集 Jaccard 距离阈值”选择性回拉，比强制统一更稳定；可搬进多轮 search/agent rollout
  中降低专家切换开销、提高吞吐。

  - 添加辅助路由 loss 容易引发 RL 训练崩溃，可用 policy entropy 高低门控关闭路由梯度；这个工程 trick 对 MoE 后训练很实用。'
score: 8
source: huggingface-daily
depth: full_pdf
---

Long-horizon LLM agent 通常用 MoE 架构承载，但标准 RL 后训练只优化 policy 输出，不管 router 的专家选择，导致已有 operation 专业化被噪声破坏，限制任务成功率和推理效率。现成 MoE 模型已经具备按 operation 分组的专家使用结构，同 operation 的 turn 内专家分布更相似，token 级同 field 专家重合也更高，但这种结构在 RL 中没有被显式保护。

方法关键点：
- Turn 级 operation-aware 控制：对每个 turn 的 thinking / tool-use 字段，将 token 级 router 概率平均为 turn 分布，最大化其与 operation label 的互信息，鼓励相同 operation 共享专家、不同 operation 分离专家集。
- Token 级局部一致性控制：计算相邻 token 的 top-k 专家集 gap，仅当 gap 小于阈值时拉高当前 token 对前一 token 所选专家的 softmax 概率；跨字段/跨 turn 不加约束，避免抑制语义转换。
- Entropy-gated 控制：监控 policy entropy，当超出目标区间（如 [0, 0.2]）时关闭路由控制梯度，防止辅助 loss 干扰 policy 优化导致崩溃。

关键结果：
- AppWorld 上，GRPO + Ours 相对 GRPO 提升 test-normal TGC 5.4、SGC 8.9，test-challenge TGC 8.6、SGC 12.2；LOOP 方案最高提升 12.9 点。
- AutomationBench 上，LOOP + Ours 提升 11.34 点。
- 路由结构上 token Jaccard 提升 7.7%，turn 级互信息提升 23.5%；推理吞吐从 224 提升到 316 tokens/GPU/s（+41.1%），rollout wall time 降低 22.3%。

最值得记住的一句话：agentic trajectory 中的 operation 结构是 MoE 路由的有效监督信号，用互信息 + 局部一致性约束后可以同时提升成功率和推理吞吐。
