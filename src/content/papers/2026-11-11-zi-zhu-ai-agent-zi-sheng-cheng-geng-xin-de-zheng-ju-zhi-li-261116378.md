---
title: Evidence-Governed Adoption of Self-Generated Updates in Autonomous AI Agents
title_zh: 自主 AI Agent 自生成更新的证据治理框架
authors:
- Subodh Lonkar
affiliations:
- Independent Researcher
arxiv_id: '2611.16378'
url: https://arxiv.org/abs/2611.16378
pdf_url: https://arxiv.org/pdf/2611.16378
published: '2026-11-11'
collected: '2026-11-16'
category: Agent
direction: Agent 自更新治理与统计校准
tags:
- autonomous agents
- evaluator calibration
- sequential inference
- non-inferiority
- AI governance
- self-evolving agents
one_liner: 统计框架治理自主 Agent 的自生成更新，含评估器校准与顺序审计
practical_value: '- 将「候选生成」与「确认上线」解耦：Agent 生成的 prompt/工具/工作流改动先冻结，不复用生成阶段交互样本做评估；必须在
  fresh paired audit 样本上比较，避免自适应选择偏差。

  - 对每个候选同时设主指标（如转化率/成交）和守护指标（如相关性、延迟、退货率）做 reference-relative non-inferiority：本地提升不足或守护劣化即拒绝上线，避免长期相对旧基线退化。

  - 引入评估器校准样本校正业务 evaluator（如 LLM-as-judge）与 prespecified reference procedure 的偏差：用
  candidate-specific calibration 校正 Hoeffding bound，降低对乐观/可操纵评估器的信任。

  - 采用 bounded canary deployment 和 bridge test：当需要更换 reference（例如从旧排序模型换成新 agent）时，做桥接测试并维护带版本号的
  reference lineage，累积退化有 bound 后再全量。'
score: 6
source: huggingface-daily
depth: abstract
---

动机：自主 Agent 持续根据交互历史修改 prompt/记忆/工具/工作流，但「能生成一个合理修改」不等于应持久化；自适应候选选择、不完备评估器和局部收益可能掩盖相对旧基线的退化。

方法关键点：EGE 把候选生成与确认式采纳分离；冻结候选在 fresh paired audit 样本上评估；要求预设主目标有实质提升，并对已声明能力做 reference-relative non-inferiority；通过治理约束后做 bounded canary deployment。统计上给出 evaluator-calibrated simultaneous lower-bound，组合候选级 Hoeffding bound 与独立 calibration samples；用 bridge test 形式化 reference replacement，并沿版本化 reference lineage 给出累积退化界；审计规划条件连接 effect margin、样本量与接收概率下界。

关键结果：Monte Carlo stress test 展示在候选依赖的评估器乐观下校准的重要性；论文明确是风格化统计实验，未在真实自主 Agent 系统做经验验证；保证依赖 bounded paired scores、fresh sampling、合法 reference-evaluation 构造和声明的评估分布。
