---
title: 'EvalResearchBench: Can AI Agents Build Their Own Feedback for Recursive Self-Improvement?'
title_zh: EvalResearchBench：让 AI Agent 自主设计评测反馈，支持递归自我改进
authors:
- Yaolun Zhang
- Tianyi Xu
- Yujie Zhao
- Jishen Zhao
- Qingyun Wu
- Huazheng Wang
affiliations:
- Oregon State University
- University of California, San Diego
- Pennsylvania State University
- AG2 AI
arxiv_id: '2610.04184'
url: https://arxiv.org/abs/2610.04184
pdf_url: https://arxiv.org/pdf/2610.04184
published: '2026-10-15'
collected: '2026-10-24'
category: Eval
direction: AI Agent 自动化评测设计
tags:
- Agent
- Evaluation
- Benchmark
- Recursive Self-Improvement
- LLM-as-Researcher
- Cost-Efficient Measurement
one_liner: 首个系统评估 AI agent 在固定预算下自主设计、迭代并冻结评测器的基准
practical_value: '- 在电商/广告/搜索推荐场景中，如果已有一套昂贵的线上 A/B 或离线评估集（如用户满意度、转化率、长期留存），可以借鉴 ERB
  的思路，让一个 LLM agent 用固定预算从已有标注/日志中挑选或合成一个小而精的「代理评测集」，通过 pilot 迭代修正 grader 和权重，再用 sealed
  候选模型验证其排序能力。

  - 评测器的构建成本与执行成本要分开账本管理：研究/开发预算和最终评估预算独立，防止 agent 在思考阶段消耗光测试资源。在业务中可对应「离线实验预算」和「在线评估配额」的隔离。

  - 关注 aggregation 的权重设计：Grok 的案例显示，按 development 候选排序拟合出的权重可能严重依赖少数几个高分题目，导致有效信号被稀释；用
  equal weight 重新计算后 Score 明显提升。业务中设计离线离线指标加权时，应避免过度拟合历史模型的排序，定期用新模型反查权重是否稳定。

  - 题目数量对评估一致性和稳定性有直接影响：从 10 题到 90 题，Score 均值上升且方差下降。若业务要做轻量级模型评估，建议保证每 domain 至少
  30-60 个有区分度的样本，否则容易高估/低估某个模型。'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
递归自我改进（RSI）依赖评估反馈来判断改进方向，但反复跑完整 benchmark 成本过高。人类专家会挑选代表性子集或设计轻量 proxy（如 tinyBenchmarks），但自动化闭环仍依赖人预先设计评测协议。

### 方法关键点
EvalResearchBench (ERB) 让一个 researcher agent 在固定时间（3 h）、推理预算（$100）、开发测试预算（$100）内，基于目标描述、任务素材、历史 traces、可见的开发集模型 API，自主完成：
- 选择或合成编码/协同工作/推理三域任务（至少 100 个可评分问题）；
- 实现 grader 与聚合权重，并通过 pilot 测试观察候选模型回答、成本和与可见目标的排序一致性，迭代修改任务、grader、答案长度上限、权重；
- 冻结一个可执行 evaluator，不再依赖候选身份或参考标签；
- 冻结后独立评估 13 个可见/密封候选模型，与 14 个目标基准（DeepSWE、SciCode、GDPval、BrowseComp、HLE 等）做 Score（100 × Lin's CCC）和 Pairwise Agreement（PA）比较。

### 关键实验结果
- 8 个有效 submitted evaluators 中，GPT-6 Astra 的 overall Score 最高（22.79），Grok 4.7 的 overall PA 最高（74.87%）。
- 最佳 PA 仍显著低于目标基准之间的 self-agreement ceiling（91%），说明单一代理评测器难以同时复现多个异构目标的全部排序。
- 开发集上 Fable 5.1 最好，但密封目标上 Grok 最好，说明 fit visible reference 不保证 transfer。
- 人类设计的 Random120 公共任务采样 baseline 很强：7/8 agent 在 Score 上超过它，但只有 4/8 在 PA 上超过。
- 执行成本最低的 evaluator 获得最高 PA，说明成本效率与测量质量可以兼得。

### 最值得记住的一句话
Agent 能通过 pilot repair 改进任务和 grader，但真正决定评估质量的是任务对候选模型的目标相关区分度，而不是任务难度或迭代次数。
