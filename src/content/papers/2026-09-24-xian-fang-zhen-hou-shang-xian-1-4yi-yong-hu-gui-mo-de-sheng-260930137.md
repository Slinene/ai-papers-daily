---
title: 'Screen Before You Serve: Simulation for Production Customer Experience AI
  Agents at 140M Scale'
title_zh: 先仿真后上线：1.4亿用户规模的生产客户体验AI智能体筛选
authors:
- Edesio Alcoba
- Kevin Rossell
- Aman Gupta
- Shao Tang
- Jiwoo Hong
- Pabel Carrillo-Mendoza
- Wanderson Conceição Ferreira
- Alvaro Tedeschi
- Zayd Simjee
- Shreya Rajpal
affiliations:
- Nubank
- Guardrails AI
arxiv_id: '2609.30137'
url: https://arxiv.org/abs/2609.30137
pdf_url: https://arxiv.org/pdf/2609.30137
published: '2026-09-24'
collected: '2026-09-25'
category: Agent
direction: 用户仿真 · Agent 部署前筛查
tags:
- User Simulation
- Agent Evaluation
- LLM-as-a-Judge
- Tool-boundary Mocking
- Production Deployment
one_liner: 用假设驱动的工具边界用户仿真对生产CX智能体做部署前筛选，加速迭代并带来显著业务提升
practical_value: '- **把用户仿真作为上线前的标准筛查层**：在电商客服、购物助手、推荐对话机器人等场景，可以用 persona-driven
  的模拟用户和 mock 工具层开展多轮交互，提前暴露不必要转人工、工具调用失败、回复不当等问题，避免直接让真实用户承担风险。

  - **工具边界 mocking 是工程落地的关键**：模拟环境不调用生产后端，而是由 persona 代理根据工具 schema 和一致性规则返回合成结果，能保证同一对话内状态一致；这比
  mock 整个数据库更轻量，易于在 Agent 与外部 API 交互密集的业务中复用。

  - **假设驱动 + 预设筛选标准，而非追求模拟与生产完全一致**：每次只验证一个候选改动（如 prompt 修改、工具策略调整、模型替换），用同一套 evaluator
  对比 incumbent 和 candidate 的失败率，达标才进入 live A/B；模拟的价值在于指导方向，不要求精确复现生产指标。

  - **用模拟快速扫描模型与推理配置**：对 open-weight 模型、reasoning effort、量化精度进行大规模仿真实验（如 16k+ 对话），能低成本发现各模型对不同评估维度的敏感差异，再挑选候选进入线上验证，大幅缩短选型周期。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**
客户体验（CX）智能体需要检测意图、遵循复杂运营政策、可靠调用工具，在受监管行业上线风险很高。手工端到端测试覆盖有限，线上 A/B 实验则直接暴露真实客户于潜在失败，可能损害信任。因此需要一种既安全又能快速迭代的中间评估层，在部署前筛选候选智能体。

**方法关键点**
- 提出 **假设驱动的工具边界仿真工作流**：在 SnowGlobe 模拟器中，由编排器规划 use-case 和交互风格，生成携带风格、状态、话题和轨迹计划的 persona；每个 persona 与待测智能体进行多轮对话，智能体的工具调用被 mock 层拦截并返回 schema 兼容、跨调用一致的合成结果。
- 仿真聚焦于对话–工具交互，不测试后端实现；工具边界 mocking 避免触碰生产数据库。
- 定义 **四个 simulator 诊断指标**：P1 对话长度统计、P2 嵌入距离、P3 evaluator 得分关联、P4 人工盲判来源；用生产与仿真样本对比表征仿真器保真度。
- 采用 **假设驱动筛选**：固定 incumbent 基线，对候选改动生成模拟轨迹，用 LLM-as-a-Judge 产出二进制失败率，若满足预设标准则进入 live A/B，否则修改候选。

**关键实验与数字**
- 在 Nubank 的 Card Delivery（CD）和 Card Management（CM）智能体上验证。仿真与生产版本级 evaluator 得分 Pearson r=0.74，Kendall τ=0.67；模拟与生产对话嵌入余弦距离最低 0.035，显著低于 off-topic 控制组。
- CD 的 10 个版本开发周期 212 天，CM 的 5 个版本仅 22 天，迭代速度提升 4.8 倍。
- 仿真引导下开发的 CM 相比 CD 在 live A/B 中 SSR 提升 4.90 pp，tNPS 提升 36.69 分。
- 利用仿真筛选出的 open-weight 模型 Qwen3.5-122B-A10B 替换 incumbent 后，SSR 再提升 8.82 pp，p95 延迟降低 25%，tNPS 无显著变化。
- 100 条模拟轨迹平均耗时不到 10 分钟，使大规模模型配置扫描（29 个配置、16k+ 对话）成为可能。

**最值得记住的一句话**：不完美的仿真仍能方向正确地指导生产智能体改进，关键在于把仿真当作筛查层而非生产指标的精确复制品，用假设驱动的方式快速淘汰劣质候选，再让线上实验做最终裁判。
