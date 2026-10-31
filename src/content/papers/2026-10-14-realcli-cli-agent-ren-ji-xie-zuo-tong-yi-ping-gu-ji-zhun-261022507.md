---
title: 'RealCLI: Toward a Unified Evaluation of Human-Agent Collaboration for CLI
  Agents'
title_zh: RealCLI：CLI Agent 人机协作统一评估基准
authors:
- Yunqi Liu
- Peiyu Wang
- Bingli Wang
- Leo Luo
- Xuanwu Song
- Xudong Ma
- Hongxin Li
- Yaxin Du
- Weicheng Gu
- Fanglin Xu
affiliations:
- Beihang University
- Renmin University
- IQuest Research
arxiv_id: '2610.22507'
url: https://arxiv.org/abs/2610.22507
pdf_url: https://arxiv.org/pdf/2610.22507
published: '2026-10-14'
collected: '2026-10-31'
category: Eval
direction: CLI Agent 人机协作评估基准
tags:
- CLI Agent
- Human-Agent Collaboration
- Benchmark
- Evaluation
- Steerability
- Safety
one_liner: 提出 REALCLI 双模式基准，统一评估 CLI Agent 任务执行与协作质量，揭示前沿模型协作能力严重不足
practical_value: '- 电商/运营 Agent 常执行长链路任务（如批量改价、选品、报表生成），可借鉴 REALCLI 的“执行模式 + 协作模式”双评估：既测任务完成，又用
  scripted user 模拟渐进需求与授权，防止只优化结果而忽略用户体验。

  - 五维框架中的 steerability、trust calibration、safety boundary 可直接迁移为客服/自动报价 Agent 的评测
  rubric，例如检查 Agent 是否在修改价格、发优惠券前请求确认、是否过度自信。

  - 对于需要人机协同的推荐/搜索 Agent（如自动生成 query 或调整策略），可参考“约束修订”场景模板，设计测试用例评估模型在用户中途改变目标时能否平滑重规划。

  - 工程上，scripted user 成本低，适合作为 CI 回归测试，避免每次都要真实人工参与，可先小规模试点。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有 CLI agent 基准或固定用户指令、或只看任务完成，忽视运行时人机协作质量，无法反映真实长程任务中用户修正、授权等交互。

**方法关键点**：REALCLI 提供配对评估两种模式：REALCLI-EXEC 一次性给全规格；REALCLI-COLLAB 引入 scripted user 逐步给出信息、纠错、约束修订和授权决策。构建五维协作框架，细化为 22 子维度和 51 交互场景模板。提出联合协作分数 J_collab，同时度量任务有效性和协作质量。

**关键结果**：前沿 agent 最佳配置平均分仅 49.2%，J_collab 峰值仅 37.6%。任务有效性远高于协作质量，模型在可引导性（steerability）、信任校准（trust calibration）、安全边界管理上普遍薄弱。
