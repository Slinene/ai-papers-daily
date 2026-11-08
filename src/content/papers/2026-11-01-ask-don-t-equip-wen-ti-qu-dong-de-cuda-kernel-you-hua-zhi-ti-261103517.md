---
title: 'Ask, Don''t Equip: Question-Driven Coding Agents for Deep Kernel Optimization'
title_zh: Ask, Don't Equip：问题驱动的 CUDA Kernel 优化智能体
authors:
- Gabriele Oliaro
- Jaeseong Lee
- Zhaoyuan Su
- Sreeram Vennam
- Zhihao Jia
- Samyam Rajbhandari
affiliations:
- Snowflake AI Research
- Carnegie Mellon University
arxiv_id: '2611.03517'
url: https://arxiv.org/abs/2611.03517
pdf_url: https://arxiv.org/pdf/2611.03517
published: '2026-11-01'
collected: '2026-11-08'
category: Agent
direction: LLM Agent · 问题驱动优化
tags:
- LLM Agent
- Kernel Optimization
- Question-Driven
- FlashAttention
- Evolutionary Search
- Human-in-the-Loop
one_liner: 用少量关键问题替代大量工具与上下文，让 coding agent 在 FlashAttention 级 kernel 优化上超过配备型自主 agent
practical_value: '- 在复杂优化/搜索 Agent 中别只堆工具、RAG、文档：在决策点用一句不携带答案、但要求可测量的问题注入 direction，比再加
  context 更能打破 plateau。

  - 把目标写成强制 predicate（Stop hook），逐场景校验而不是看聚合分，能防止 agent 过早宣布完成或满足于容易场景，这在排序/召回/query
  优化中同样适用。

  - 问题设计坚持六原则：不直接给答案、必须用普通工具测出一个数字、跨层追问（kernel→host→benchmark）、挑战 claimed limit、低成本、反
  deference；可沉淀成 question bank，让 agent 自己问自己。

  - 与进化搜索结合时，进化负责局部搜索，但方向必须由 question/指令提供；否则变异只会在同一层打转。推荐/广告的召回策略、排序模型、query 改写等长流程
  Agent 可复用该范式。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**

GPU kernel 优化 Agent 在「结构」与「自由」之间权衡：脚本化 agent 样本效率高但方向被写死，开放型进化 agent 自由但需要上千次评估、大量错误候选。现有方法都在给 agent 配备更多信息（profiler、反汇编、文档检索、经验库），但论文认为缺失的是 **direction**——对剩余性能缺口在哪里的假设。

**方法关键点**

- KERNELSEEK：以已有 CUDA kernel 为种子，不依赖算子特定知识或更快实现。
- 最小 harness：只做输出校验、逐场景计时、目标 predicate 强制检查；Stop hook 使 agent 无法在未达标时提前结束。
- 决策点注入问题：来自人类 steerer 或 question bank；问题不携带答案，要求可测量、跨层、挑战 claimed limit。
- 问题分类：measurement check、bound differencing、benchmark validity、gap triage、challenge a limit 等八类。
- 可组合进化搜索：AVO 式 lineage，但 directive 是 question 而非 edit。

**关键实验**

- 对照 baseline ARSENAL：工具丰富的自主进化 agent，prompt 中 37% 是参考材料、82% 工具读取自己的 kernel，133 步后 geomean 仅 0.50× FA3，0/26 配置达 parity。
- 同一任务、同一 evaluator、同一 H200、同一周内，KERNELSEEK 达到 1.13× FA3，22/26 配置 ≥1.0，最差 0.87×。
- 完整 campaign：fa3_hopper.cu 在 182 场景全部正确，1.16× FA3；fa4_blackwell.cu 在 154 可跑场景正确，1.46× FA4；均不含 CUTLASS/CuTe/cuBLAS/cuDNN。
- 162 条人类消息中 17 条关键问题引发最大性能跃升；全部大 gain 都跟随「跨层提问」或「挑战 limit」，而不是提供信息。

**最值得记住的一句话**

> For deep kernel optimization the scarce resource is not information but direction. 在业务优化 Agent 中同样成立：方向 > 信息/工具。
