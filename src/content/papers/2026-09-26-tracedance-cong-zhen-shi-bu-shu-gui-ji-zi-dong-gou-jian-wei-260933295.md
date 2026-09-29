---
title: 'TraceDance: An Automated System for Building Agent Behavior Benchmarks from
  Real-World Agent Deployment Traces'
title_zh: TraceDance：从真实部署轨迹自动构建Agent行为基准
authors:
- Dehai Min
- Daoan Zhang
- Yiming Zeng
- Huayi Zhang
- Ziyi Chen
- Yan Zhang
- Qinbo Bai
- Mengyuan Chao
- Jing Ning
- Qiyue Hua
affiliations:
- ByteDance Inc.
- University of Illinois at Chicago
arxiv_id: '2609.33295'
url: https://arxiv.org/abs/2609.33295
pdf_url: https://arxiv.org/pdf/2609.33295
published: '2026-09-26'
collected: '2026-09-29'
category: Eval
direction: Agent行为基准自动构建
tags:
- Agent
- Benchmark
- LLM
- Evaluation
- Deployment Traces
one_liner: 自动从真实Agent部署轨迹构建针对用户指定不良行为的基准，高效且评估与人类一致性高
practical_value: '- 借鉴从部署日志构建评估集的方法：在电商搜索/推荐Agent中，可以记录真实会话轨迹，自动提取负面案例（如不相关推荐、违反政策回答），构建针对特定问题的回归测试集。

  - Anchor-and-Confirm 高效构建流程：先通过规则、向量检索等可编程方法筛出候选，再用 Flash LLM（低成本）逐条确认，大幅降低人工标注成本，适合大数据量下的评估集生成。

  - decision-point continuation 评估范式：无需完整环境重放，只需在关键决策点（如 LLM 生成下一轮推荐或回复）做续写评估，结合行为特定
  rubric 自动打分，与人类一致性高，可用于线上模型行为的快速监控。

  - 针对 LLM Agent 在推荐/搜索中的不良行为（如幻觉、违规话术），可以利用此框架自动生成定制化 benchmark，纳入模型上线前的回归测试和递归自我改进循环。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：固定基准套件无法覆盖真实部署中涌现的各种不良行为，开发者需要针对特定行为的测试。

**方法**：
- TraceDance 从部署轨迹中提取决策点，构建针对用户指定不良行为的基准。
- 高效构建：Anchor-and-Confirm 先通过可编程检索（规则、向量检索等）产生候选，再用 Flash LLM 逐候选确认是否属于目标行为；Anchor Synthesis Loop 可生成并修订自定义行为规范。
- 评估方式：decision-point continuation，在记录的决策点让待测 LLM 生成下一轮，使用行为特定 rubric 自动打分，无需参考答案或环境重放。

**结果**：
- 在编码与通用工具使用数据集上，利用 252,557 个会话构建 107 个基准、4,125 个实例，满足 95.3% 的构建目标请求。
- 人类标注者确认 84% 采样实例确实包含指定行为；自动评分器与人类判断一致性等同于标注者之间的一致性。
- 9 个前沿 LLM 平均通过率仅 26.7%，暴露当前 Agent 在特定决策点上的明显弱点。
