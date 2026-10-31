---
title: 'Investor''s Last Exam: Can AI Agents Do Equity Investment Without Seeing the
  Future?'
title_zh: 投资者的最后考试：AI智能体能否在未见未来时做股权投资？
authors:
- Huangfei Jiang
- Anning Hu
- Kai Sheng
- Yuchen Cai
- Rui Ge
- Xiangyu Kong
- Jianghao Lin
- Shuzi Chen
- Jiyi Weng
- Junchi Yan
affiliations:
- Prophetlab
- RethinkLab
- Antai College of Economics and Management, SJTU
- USTC
- Foresight Fund
arxiv_id: '2610.38342'
url: https://arxiv.org/abs/2610.38342
pdf_url: https://arxiv.org/pdf/2610.38342
published: '2026-10-27'
collected: '2026-10-31'
category: Eval
direction: 金融 Agent 评估 · 证据-假设-判断链
tags:
- Financial Agents
- Benchmark
- LLM Evaluation
- Forecasting
- Investment Research
one_liner: 提出 ILE 股权投资基准，用冻结信息集与财务依赖图评估 AI 代理研究、预测与投资表现
practical_value: '- 构建版本化、时间戳严格的信息库，避免未来信息泄漏；电商/推荐系统离线评估可借鉴此思路，在实时推荐、召回排序评估时按行为前特征快照严格取数。

  - 将评估单元从单一指标扩展到“证据—假设—判断”链，利用财务依赖图定位失败环节（检索、计算、假设、决策），适合对搜索推荐 Agent 做可解释性归因与短板诊断。

  - 专家定义任务分类与评分依赖图，拆解复杂 Agent 能力，可以迁移到电商 Agent 工作流：把任务分解为类目、证据来源、计算步骤，定位“研究强但预测弱”的瓶颈。

  - 采用冻结信息集 + 模拟业务绩效（如投资回报）联合评估，对推荐系统 Agent 的线上效果预估与离线仿真有借鉴价值，能同时衡量过程质量和结果收益。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机：** 现有金融 Agent 基准只验证知识、流程或预测，未在严格冻结信息集下评估完整投研流程，无法定位研究能力为何无法转化为预测和投资判断。

**方法关键点：** ILE 由三部分组成：版本化金融数据库含 343 万文档版本、九类来源，时间戳验证；按专业分析师交付物组织的任务分类；专家主导的财务依赖图，将评分标准关联到来源、计算和假设。评测覆盖 86 个任务，联合考量研究质量、预测准确性与模拟投资表现。

**关键结果：** GPT-6 Astra 与 Claude Opus 5.5 总分领先，分别为 68.1 / 66.9（百分制），但 Astra 在 Forecast & Model 仅 52.5。最强模型仍无法把整体研究能力转化为预测性能。ILE 将评估单元从孤立能力转向“证据—假设—判断”链，可追溯定位失败环节。
