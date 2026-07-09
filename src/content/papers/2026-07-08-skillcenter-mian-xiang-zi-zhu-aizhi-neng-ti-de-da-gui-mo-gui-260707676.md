---
title: 'SkillCenter: A Large-Scale Source-Grounded Skill Library for Autonomous AI
  Agents'
title_zh: SkillCenter：面向自主AI智能体的大规模源归因技能库
authors:
- Tianming Sha
- Yue Zhao
- Lichao Sun
- Yushun Dong
affiliations:
- Stony Brook University
- University of Southern California
- Lehigh University
- Florida State University
arxiv_id: '2607.07676'
url: https://arxiv.org/abs/2607.07676
pdf_url: https://arxiv.org/pdf/2607.07676
published: '2026-07-08'
collected: '2026-07-09'
category: Agent
direction: Agent 技能增强与知识基础设施
tags:
- Skill Library
- Source Grounding
- Autonomous Agents
- LLM
- Knowledge Infrastructure
- Quality Gate
one_liner: 提出迄今最大的开放技能库，含216,938个源归因结构化技能，提升AI智能体输出正确性与安全性
practical_value: '- 在电商Agent的开发中，可借鉴源归因机制，要求每个自动化决策或文案生成均关联到具体知识来源（如行业标准、历史最佳实践），从而减少幻觉输出，增强可信度和合规性。

  - 技能模板化生成结合SkillGate质量门控，可用于自动构建和维护电商运营知识库（如促销策略、商品描述规范），通过LLM初步生成后自动校验，降低人工审核成本。

  - 离线可搜索的SQLite FTS5打包方式适合集成到推荐系统流水线中，为实时决策提供毫秒级技能检索，避免外部API延迟。

  - 多源采集（学术论文+社区贡献）的融合思路，可启发构建电商领域的专家知识众包与审核闭环，持续迭代业务知识库。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：自主AI智能体在自动化执行任务时，常缺乏可靠的操作知识，导致输出虽可运行但未必正确、安全或可维护。为弥补这一缺陷，需要可检索、源可靠的技能库作为基础设施。

**方法**：提出SkillCenter，一个包含216,938个结构化技能的大规模库，覆盖24个领域。其中管道技能通过多源采集（同行评审期刊、ArXiv、超2.4万技术源），经LLM质量门SkillGate过滤、模板化生成、迭代源归因，确保每条声明均指向原文确切引用。社区技能则汇入GitHub和ClawHub上的10.2万条技能。最终所有技能打包为离线可搜索的SQLite FTS5捆绑包，便于集成。

**结果**：构建了迄今已知最大的开放技能库，源归因保障了可追溯性，为智能体提供正确、安全且可维护的操作知识，缩小了自主性与判断力之间的质量鸿沟。
