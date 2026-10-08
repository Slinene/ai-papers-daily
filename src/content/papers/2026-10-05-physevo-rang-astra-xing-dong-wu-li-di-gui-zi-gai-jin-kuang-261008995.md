---
title: 'PhysEvo: Astra Can Act, Let It'
title_zh: PhysEvo：让 Astra 行动，物理递归自改进框架
authors:
- Wenqing Tian
- Zeyu Zhang
- Zhaocheng Liu
- Fengwei Liu
- Qiang Liu
- Liang Wang
affiliations:
- University of Chinese Academy of Sciences
- Institute of Automation, Chinese Academy of Sciences
- Tsinghua University
- Independent Researcher
arxiv_id: '2610.08995'
url: https://arxiv.org/abs/2610.08995
pdf_url: https://arxiv.org/pdf/2610.08995
published: '2026-10-05'
collected: '2026-10-08'
category: Agent
direction: 具身智能 · 递归自改进 Agent
tags:
- Recursive Self-Improvement
- Embodied AI
- Meta-Agent
- Tool Revision
- Robot Manipulation
- Frozen Model
one_liner: 冻结模型上通过元代理诊断失败、修订工具与技能，大幅提升机器人操作成功率
practical_value: '- **Agent 自改进闭环可迁移**：将执行轨迹作为诊断数据，让 meta-agent 分析失败原因、生成工具/技能修订，再通过测试验证后保留，这套「执行-诊断-修订-验证-保留」流水线可直接用于推荐/搜索
  Agent 的策略迭代，无需更新底层 LLM 权重。

  - **工具层迭代优于模型层重训**：PhysEvo 证明在冻结模型上只改工具和技能就能显著提升成功率，对业务 Agent 来说，维护可复用的工具库和技能模板，比频繁微调模型更经济、更可控。

  - **测试驱动修订**：meta-agent 会先测试候选修订再决定保留，避免把坏的工具引入生产环境；在推荐 Agent 中可以对新的召回/排序工具进行离线评估或
  A/B 测试后再上线。

  - **可复用技能沉淀**：修订后的技能被保留并支持后续任务，类似推荐系统的可复用策略模块，如用户意图识别、动态 query 改写等，通过累积有效修订形成领域知识库。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**
直接使用大模型（Astra）进行机器人操作时，可靠操控受限于观察与控制系统：一次性代理难以处理复杂操纵任务，缺乏从执行反馈中持续改进的能力，而模型权重更新或单独训练动作策略成本高、泛化差。

**方法关键点**
PhysEvo 围绕一个冻结模型构建物理递归自改进闭环：任务代理（task agent）执行机器人任务；元代理（meta-agent）利用执行轨迹诊断失败原因，修订工具与技能，并通过测试验证修正；元代理还能改进自身的诊断工具，使保留的修订同时支持后续行动和后续自我改进。整个过程无需模型权重更新，也不依赖单独训练的动作策略。它通过丰富观察证据、扩展控制能力、优化反馈可靠性，将动作后果转化为持久、可测试的改进。

**关键结果数字**
在 42 个 RoboDojo 任务的 held-out 布局评估中，保留的任务特定部署版本平均得分 68.14/100，成功率 62.00%，对比最强公开参考 RoboDawn 一次性 Astra 的 47.17%；在 8 个对直接 Astra 困难的操纵任务上，PhysEvo 成功率 55.00%，而直接 Astra 仅 1.25%。将模拟演化的 harness 部署到 AgileX PiPER 并继续技能修订，在 5 个真实世界任务的 25 次试验中平均得分 90.60/100，成功率 84.00%。
