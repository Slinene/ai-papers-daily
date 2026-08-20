---
title: 'Grouping the Stochastic Machine: Precision, Not Capability, as the Frontier
  Metric for AI Systems'
title_zh: 评估前沿 AI：精度而非能力，输出一致性才是分水岭
authors:
- George Andrikopoulos
affiliations:
- Independent researcher, London, United Kingdom
arxiv_id: '2608.19140'
url: https://arxiv.org/abs/2608.19140
pdf_url: https://arxiv.org/pdf/2608.19140
published: '2026-08-19'
collected: '2026-08-20'
category: Eval
direction: LLM 系统评估 · 输出一致性
tags:
- evaluation
- reliability
- precision
- consistency
- LLM
- benchmarking
one_liner: 提出用重复请求的输出一致性（precision）而非基准能力作为前沿模型区分指标，并给出测量框架与决策方法
practical_value: '- 在电商/推荐/Agent 系统中增加**重复一致性评估**：对关键任务（query 改写、推荐理由生成、商品标题生成、Agent
  决策）固定 temperature 多次采样同一输入，用确定性规则或文本相似度计算一致率，监控输出漂移，避免只看平均指标。

  - **区分两类失败**指导调优：一致失败（集中偏离）说明是系统性 bias，可以通过规则/后处理/提示词修正；分散失败（高方差）说明模型或采样策略本身不可靠，需要换模型、降低
  temperature 或加入约束解码。

  - **低成本的 harness 设计**：复用现有多轮测试集，针对每个任务重复 N 次，用确定性评分（无需 model-in-loop grader），能快速定位哪类任务不稳定，适合接入
  CI/CD 作为回归门禁。

  - **人机协作监控**：跟踪 Agent 与人类配合过程中的输出 grouping 随时间变化，作为可靠性 KPI，累计信号帮助发现模型退化、策略失效或环境漂移。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：前沿模型的能力（平均准确率）已趋同，但实际工程中更关心重复请求下输出是否稳定一致。基准测试只报告中心趋势，系统性地忽略了方差，无法区分真正可用的工程系统。

**方法关键点**：借用射击比喻区分 capability（平均弹着点）与 precision（弹着群大小）。提出可操作测量：固定任务套件，固定 temperature，多次重复相同请求，用确定性评分（无需模型打分）计算每个任务的输出一致性。定义 grouping 指标，复用现有挑战测试基础设施即可实现。进一步区分两类失败：一致失败（集中偏离，可通过规则或操作纪律修正，类似“瞄准调整”）与分散失败（方差大，只能换模型或改变采样策略，类似“枪的问题”）。同时用于追踪人机组合随时间的 grouping，提供复合信号。

**关键结果数字**：首次实测中，一个差距被单条规则完全关闭（0/5 → 5/5）；但从规则本身构建的任务套件未发现价值，因为前沿模型已内化显式良好实践——说明纪律的价值需在真实工作中测量，而非依据规则书构造。
