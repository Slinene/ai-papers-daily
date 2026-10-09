---
title: What Did the Agent Actually Do? Evidence-Grounded Oversight for Long-Horizon
  Agents
title_zh: Agent实际做了什么？面向长程Agent的基于证据监督方法
authors:
- Zhongxiang Sun
- Jiahao Yan
- Hongkang Zhao
- Haojie Ding
- Boheng Zhang
- Fan Yang
- Xiao Zhang
- Jun Xu
affiliations:
- Gaoling School of Artificial Intelligence, Renmin University of China
- Kuaishou Technology
arxiv_id: '2610.06406'
url: https://arxiv.org/abs/2610.06406
pdf_url: https://arxiv.org/pdf/2610.06406
published: '2026-10-04'
collected: '2026-10-09'
category: Agent
direction: Agent行为监控与证据定位
tags:
- Agent Oversight
- Evidence Localization
- Behavior Graph
- Long-Horizon Agents
- Benchmark
one_liner: 提出EBG训练无关方法，将证据按行为分组并构图为任务导向视图，提升长程Agent关键决策识别与证据定位
practical_value: '- 在电商/广告Agent自动化流程中，可将EBG作为轻量监控层：把Agent动作日志按源链证据聚类为行为节点并构建依赖图，在审核UI中呈现任务导向视图，帮助运营快速定位需要人工验证的环节，避免阅读完整trace。

  - EBG训练无关、即插即用，且证据定位增益在长上下文和不同超参数下保持稳定，可直接嵌入现有Agent监控模块，无需额外训练或微调，适合快速上线。

  - 借鉴AgentMonBench的两个评估维度（需求-行为对齐、自主决策需验证的意识），在内部构建Agent可靠性测试集，重点考察Agent是否做了需求外的事、是否在关键节点主动请求确认。

  - 对搜索/推荐系统中由LLM Agent生成的query或策略，可用EBG将决策与证据（用户日志、商品信息）显式链接，增强可解释性与审计能力，提升人对自动决策的信任。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：用户与长程Agent的关系正从逐决策执行转向监督代理执行，但Agent活动量大、证据碎片化，难以判断哪些决策需要人工验证。现有监控方法多依赖完整上下文，缺乏结构化证据组织。

**方法**：引入AgentMonBench基准，包含三个子集覆盖两个互补维度：需求与行为对齐、自主决策需验证的意识。提出Evidence-Grounded Behavior Graph（EBG），一种训练无关方法：将源链接证据分组为行为节点，并组织其关系为图；随后根据任务呈现图的任务导向视图，帮助监控模型在上下文中解释行为。

**结果**：在8个模型上的实验显示，EBG在多数设置下相比直接使用原始上下文，显著提升决策识别与证据定位能力；证据定位的增益在不同输入规模和超参数设置下稳定；实际应用展示了其对人工监督的实用价值。
