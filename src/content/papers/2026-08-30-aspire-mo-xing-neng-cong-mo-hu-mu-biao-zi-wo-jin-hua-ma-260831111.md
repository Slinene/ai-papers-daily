---
title: 'Aspire: Can Models Self-Evolve from Vague Goals?'
title_zh: Aspire：模型能从模糊目标自我进化吗？
authors:
- Yuhao Wu
- Jingyuan Zhang
- Jiajun Shi
- Yuxuan Zhang
- Xinping Lei
- Junting Zhou
- Zexuan Wang
- Yuchen Wu
- Huan Zhou
- Duo Wang
affiliations:
- ByteDance Seed
- Singapore University of Technology and Design
- M-A-P
- TokenWave.AI
arxiv_id: '2608.31111'
url: https://arxiv.org/abs/2608.31111
pdf_url: https://arxiv.org/pdf/2608.31111
published: '2026-08-30'
collected: '2026-09-04'
category: Eval
direction: LLM 自我进化基准与评估
tags:
- self-evolution
- LLM agents
- benchmark
- vague goals
- agent harness
one_liner: 提出 Aspire 基准，考察 LLM 在仅给定模糊目标时的自主进化能力；当前代理权重级提升稀疏且不稳定
practical_value: '- 在电商/推荐场景，模糊需求（如“提高转化率”）常被直接简化为单一指标优化；可借鉴 Aspire 的目标解释步骤：先显式拆解能力缺口、选择数据与验证信号，再启动训练或
  Agent 编辑，避免初始搜索空间偏差。

  - 自进化循环中，模型/代理容易信任狭窄的自评估，导致局部提升不迁移到线上；应保留一个与线上分布一致的隐藏评估集，并在每次更新后监控线上业务指标，避免过拟合自建验证数据。

  - 持续训练会擦除早期改进（遗忘）；在线上模型持续更新或 Agent 迭代时，需要 checkpoint 回滚、阶段性评估与 early stop 策略，不能盲目多轮训练或搜索。

  - 权重更新不稳定时，优先改进 harness（prompt/工具编排）是更稳路径；在搜索推荐 Agent 中可先用工作流、记忆或工具适配提升效果，待稳定后再考虑微调模型权重。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有 LLM self-evolution 依赖人类指定任务和指标，本质是优化明确目标，未覆盖“模糊目标”下的自主决策。Aspire 通过只给自然语言能力目标、隐藏下游评估任务，要求 agent 自主决定学什么、怎么学和如何验证。

**方法关键点**：基准支持权重级和 agent-harness 两种进化路径，提供统一交互环境；下游评估为隐藏专家标注的 520 道题目，覆盖 6 个能力目标。Agent 需选择数据与更新方法、构造训练/验证信号并决定何时评估。

**关键结果**：模糊目标使搜索重心转向目标解释；当前 agent 能完成训练和 harness 编辑循环，但权重级提升稀疏且不稳定；最强进化 harness 仍低于工程 Qwen-Agent 参考。常见失败模式包括训练错配数据、过度信任窄自评估，局部提升无法迁移到隐藏评估，且持续搜索/训练会擦除早期改进。
