---
title: 'WebRetriever: A Large-Scale Comprehensive Benchmark for Efficient Web Agent
  Evaluation'
title_zh: WebRetriever：大规模全方位Web Agent高效评估基准
authors:
- Wei Dong
- Tianyu Fu
- Zhe Yu
- Hanning Wang
- Anyang Su
- Zhizhou Fang
- Yuyang Chen
- Shuo Wang
- Minghui Wu
- Ping Jiang
affiliations:
- Mininglamp Technology
- University of Chinese Academy of Sciences
- Institute of Automation, Chinese Academy of Sciences
arxiv_id: '2607.06118'
url: https://arxiv.org/abs/2607.06118
pdf_url: https://arxiv.org/pdf/2607.06118
published: '2026-07-07'
collected: '2026-07-08'
category: Agent
direction: Agent 评估基准 · 多域导航
tags:
- Web Agent
- Benchmark
- LLM-as-Judge
- Interaction Context
- Evaluation Protocol
one_liner: 提出涵盖800网站1550任务的多域Web Agent基准与基于交互上下文的评估框架，揭示导航成功率不足以衡量真实效果
practical_value: '- 评估 Agent 时不能只看导航成功率，参考文中三个协议：纯导航、知识辅助交互、端到端信息抽取，可分层诊断 Agent 在搜索/推荐场景中的真实能力。

  - LLM-as-Judge 不应仅依赖页面截图，NavEval 强调记录并输入 query 构造、过滤/点击序列等交互上下文，能更准确评判 query 改写、筛选器使用等细粒度动作，可直接迁移至电商搜索
  Agent 的自动评测。

  - 构建多领域任务集（消费者、专业、企业站点）确保泛化测试，电商/广告推荐 Agent 可借鉴其意图覆盖方法，将用户需求细化为搜索、对比、属性过滤等原子任务。

  - 基准提供 1,550 个真实任务，可作为强化学习或 Prompt 优化的 reward 信号源，工程上可利用其诊断结论针对性提升 Agent 在复杂信息提取中的鲁棒性。'
score: 7
source: arxiv-cs.MM
depth: abstract
---

**动机**：现有 Web Agent 评估基准规模小、领域单一，且常用 LLM-as-Judge 仅依赖截图，无法捕捉 query 构造、过滤等细粒度交互语义；同时指标过分偏重导航成功率，忽略真实部署中知识辅助、信息抽取等关键维度。  
**方法**：构建 **WebRetriever** 基准，涵盖 800 个网站、1,550 个任务，覆盖消费者、专业、企业等多领域，系统梳理用户意图模式。提出 **NavEval** 评估框架，将交互上下文（动作序列、查询历史、过滤操作等）作为 LLM 输入，提升评估与人类判断的一致性，并在多个数据集上达到 SOTA。设计三种互补评估协议：**(1) 导航熟练度**（纯导航任务）、**(2) 知识辅助交互**（需领域常识的查询/过滤）、**(3) 端到端任务完成与信息提取**（含结果抽取）。  
**关键结果**：实验显示不同协议间 Agent 表现存在巨大差异，单纯导航成功率无法预测全链路效能；NavEval 与人类评估的对齐度显著优于基线方法。WebRetriever 为 Agent 能力提供细粒度诊断，揭示了跨领域泛化的薄弱环节。
