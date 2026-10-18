---
title: 'ReviewPilot: A Multi-Agent System for Screening and Data Extraction in Systematic
  Reviews'
title_zh: ReviewPilot：系统综述筛选与数据抽取的多智能体对话系统
authors:
- Zhaoqian Xue
- Shaoze Zhou
- Xuexin Li
- Junting Mu
- Haozheng Liu
- Zhongyin Wang
- Yichun He
- Renkai Ma
- Hao Zhou
- Sarah Bratt
affiliations:
- University of Arizona
- Florida International University
- Vanderbilt University
- University of California, Irvine
- New York University
arxiv_id: '2610.21042'
url: https://arxiv.org/abs/2610.21042
pdf_url: https://arxiv.org/pdf/2610.21042
published: '2026-10-15'
collected: '2026-10-18'
category: MultiAgent
direction: 多智能体协作自动化系统评价
tags:
- Multi-Agent System
- PRISMA
- Systematic Review
- LLM
- Data Extraction
- Project Memory
one_liner: 用多智能体对话系统自动化 PRISMA 流程，决策留痕可溯，筛选与抽取 F1 最高达 0.788
practical_value: '- 多智能体协作加项目记忆的架构可迁移到电商/广告的规则配置场景：把选品标准、定向规则或活动 schema 作为可对话修订的 project
  memory，运营通过自然语言迭代，而不是改代码。

  - “每个决策带理由、每个抽取带出处”是可解释性样本：推荐/广告 Agent 的每次拦截、召回或排序决策，都应绑定证据引用与理由，便于审核和 debug。

  - 对话式配置 criteria/schema 的思路适合快速将业务专家经验转为结构化筛选逻辑，例如大促选品、广告审核、商家资质筛选。

  - 评估方法可直接借用：在信息抽取任务上对比单 prompt 与多智能体系统，用 macro F1 度量，能客观量化 Agent 架构带来的收益。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：系统综述按 PRISMA 流程要求筛选大量文献并提取证据，人工耗时一年以上；现有 LLM 深度研究工具只能搜索和总结，不记录排除理由与数据出处，无法满足透明可复现要求。

**方法关键点**：提出 ReviewPilot，一个对话式多智能体系统，覆盖论文筛选到信息抽取的 PRISMA 全流程。研究者可通过对话定制纳入排除标准与抽取 schema，项目记忆保存所有配置和修订版本。系统为每个筛选决策生成理由，为每个抽取值标注来源，实现全程可追溯。

**关键结果**：在流行病学专家评审任务上，ReviewPilot 在三种 LLM 上均优于单 prompt LLM 和 AgentSLR，筛选 macro F1 最高 0.776，抽取 F1 最高 0.788。在生物医学和人机交互领域案例中与人工标注高度一致，显示跨领域迁移能力。
