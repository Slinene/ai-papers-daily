---
title: 'DarwinX: Evolving Agent Harnesses Through Natural Selection'
title_zh: DarwinX：通过自然选择进化 Agent 外壳
authors:
- Yifan Zhang
- Yutong Dai
- Juntao Tan
- Luyu Yang
- Rishi Mullur
- Thai Hoang
- Zhiyuan Hu
- James Zhu
- Phil Mui
- Silvio Savarese
affiliations:
- Salesforce AI Research
- Salesforce Agentforce
arxiv_id: '2608.07545'
url: https://arxiv.org/abs/2608.07545
pdf_url: https://arxiv.org/pdf/2608.07545
published: '2026-07-30'
collected: '2026-08-14'
category: Agent
direction: Agent 群体选择与 harness 进化
tags:
- Agent Evolution
- Harness Optimization
- Population Search
- Preserve-and-Extend
- LLM Agents
- Natural Selection
one_liner: 冻结模型下把 Agent 自改进变成对 harness 变体的群体选择，用保留-扩展契约和档案重组，在四个基准平均提升约 17 个点
practical_value: '- 在电商/广告/搜索的 Agentic 产品中，可以冻结 LLM 只进化 harness（prompt、tool、skill、control
  flow），用 preserve-and-extend 契约做上线门禁：只接受新增能力且回归有界的编辑，避免推荐或 query 改写质量出现全局抖动。

  - 保留档案中的弱势变体而非只留单最优：不同 specialist 可能分别擅长 query 推荐、商品推荐、多轮对话等子任务，merge 互补变体可覆盖更多场景，类似多策略/多智能体协作。

  - 把失败轨迹、teacher 演示、自身 pass/fail 对比三种信号统一成 harness 编辑接口；业务中可用人工标注的 good/bad case
  或用户反馈作为 teacher/failure 信号，不微调模型，降低迭代成本和风险。

  - Agentic 推荐系统评测噪声大，用 avg@k 和 preservation probe 确认而非单次 lucky rollouts，可避免假阳性、防止过度优化某个子集。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
现代 LLM Agent 的能力很大程度由 harness（提示词、工具、记忆、控制流）决定，但单线自改进容易路径依赖且跨任务干扰，一个任务上的局部改进可能悄悄伤害其他任务。需要一个选择过程而不是训练过程，让进化在群体层面展开。

## 方法关键点
- 冻结模型权重，只编辑 harness 的两层：skill（prompts、memory、distilled knowledge）和 code（tools、control flow、agent loop）。
- 核心是 preserve-and-extend 契约：子节点必须在至少一个任务上净增益且回归有界（R ≤ δ），防止顾此失彼。
- 档案树保留所有变体，包括全局更差但持有独特解的 stepping stones，支持跨 lineage 继承和合并互补 specialists。
- 学习信号模块化：failure-derived（失败轨迹）、teacher-derived（参考解轨迹）、self-derived（自身 pass/fail 对比），统一转成 harness 编辑。
- 探索与确认分离：探索阶段宽松 promote bounded-risk 变体；确认阶段严格 avg@k 和 preservation probe 后才允许引导后续搜索。

## 关键实验
在四个演化信号与测试分离程度递增的基准上做 matched-model 比较，模型全程冻结：
- Terminal-Bench 2.1：GPT-5.5 上 75.5% → 83.2%（+7.7），GPT-5.6 Sol 上 84.7% 达到验证榜前沿。
- TerminalWorld held-out：68.3%，高于所有 off-the-shelf agent；合并后的 harness 超过所有 specialist。
- WebArena-Infinity：audit-clean pass@1 43.5% → 93.0%（+49.5），invalid 轨迹从 293 降到 17。
- 跨基准迁移：TB2.1 进化 harness 原样跑 SWE-bench Verified 得 84.2%。
- Ablation 显示 evolved skills 集中在 verification/artifact-contract 家族，即先明确验收契约再自查，而非注入领域知识。

## 最值得记住的一句话
冻结的模型不必是固定 Agent：harness 是仍可移动的表面，对其做选择能把评估算力转化为持久能力。
