---
title: 'Project Kaleidoscope: Contextual, Human-Aligned Evaluation for Real-World
  AI Applications'
title_zh: 万花筒：真实AI应用的情境化人本评估工作流
authors:
- Leanne Tan
- Rohan Jaggi
- Shaun Khoo
- Roy Ka-Wei Lee
affiliations:
- GovTech, Singapore
- National University of Singapore
- University of British Columbia
arxiv_id: '2607.14673'
url: https://arxiv.org/abs/2607.14673
pdf_url: https://arxiv.org/pdf/2607.14673
published: '2026-07-16'
collected: '2026-07-18'
category: Eval
direction: LLM-as-Judge · 人本对齐评估
tags:
- Evaluation
- LLM-as-Judge
- Human-Alignment
- Persona-Based Testing
- Reliability-Gating
- Contextual Rubrics
one_liner: 集成角色测试、定制化评分与人类审核的可靠性门控自动评估方法
practical_value: '- **定制化评分标准（Rubric）**：将业务目标（如广告合规、搜索相关性、推荐多样性）转化为具体可评分维度，让评估与业务对齐。

  - **角色驱动的测试生成**：用Persona模拟多类用户行为或查询意图，生成高覆盖测试用例，提前发现策略漏洞。

  - **可靠性门控自动化**：设定LLM judge与人工标注的一致性阈值，只有达到门槛才切换为自动评分，在节省成本的同时防止偏差累积。

  - **迭代评估闭环**：结合可审查的人工标签与自动打分，持续校准评分标准，适合需要频繁调整策略的Agent或推荐系统上线前评估。'
score: 6
source: arxiv-cs.HC
depth: abstract
---

**动机**：真实AI应用评估严重依赖人工，公共基准无法匹配业务特有的用户、政策与风险要求，人工审查难以规模化。

**方法关键点**：
- **集成工作流**：将基于角色的测试生成、应用专属评分标准（rubric）和人类审核结合，通过可靠性门控实现自动化评分的平滑过渡。
- **角色驱动测试**：按多类用户画像（persona）生成问答或行为样本，确保测试覆盖业务上下文。
- **可靠性门控**：先用人工标注建立 ground truth，再引入 LLM judge 评分，仅当 judge 与人工标注的一致率超过可配置阈值时，才自动接管评分，否则回退到人工。

**关键结果**：在三周试点中，覆盖四个组织用例、108 条问答对及 14 个评分维度，展示了端到端可靠自动评估的可行性，并在多处用例中达到可接受的人工一致性阈值。
