---
title: 'Skills Know Their Neighbors: Cluster-Contrastive Capability Pages for Skill
  Retrieval'
title_zh: 技能知晓其邻居：用于技能检索的聚类对比能力页
authors:
- Zifei Wang
- Wei Wen
- Qiang Ji
- Ruizhi Qiao
affiliations:
- Tencent IMA Product Center
- Tencent Youtu Lab
arxiv_id: '2608.04482'
url: https://arxiv.org/abs/2608.04482
pdf_url: https://arxiv.org/pdf/2608.04482
published: '2026-08-05'
collected: '2026-08-06'
category: Agent
direction: 技能检索 · 对比表示学习
tags:
- Skill Retrieval
- Capability Pages
- Contrastive Learning
- LLM Agent
- Routing
one_liner: 通过聚类对比生成包含正触发、负边界和判别体的能力页，在不改变在线模型的情况下提升技能检索与路由性能
practical_value: '- 当业务中存在大量语义相似但能力不同的技能/功能时，可离线编译「能力页」来增强检索区分度，避免检索器因文档描述的局限性而误召回。

  - 引入负边界 T^- 用于路由阶段的候选拒绝，能有效减少下游执行器调用错误技能的概率，可直接用于 Agent 框架中的工具选择环节。

  - 离线生成对比表示的思想可迁移到电商商品描述改写、广告文案检索等场景：通过对比邻近项自动生成更具区分性的描述字段，改善结构化信息的检索质量。

  - 该方法完全通过改写离线库实现，无需更换编码器或修改在线模型，工程改造成本极低，适合快速验证与上线。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：当 LLM Agent 的技能库扩大时，许多技能共享相同主题和词汇但执行不同能力，检索器常因文档仅描述“做什么”而缺乏“何时不应使用”的信息导致误判。该工作将技能能力形式化为可执行区域，指出文档作为该区域的有损观察会引入无法通过改进检索器消除的误差。

**方法**：提出 Capability Pages，一种聚类对比的技能表征，包含正触发 T⁺（代表性正例查询）、负边界 T⁻（最易混淆的邻居查询）和判别体 B（对比生成的自然语言描述）。离线编译器通过比较邻近技能自动生成这些字段。在线阶段，索引利用 T⁺ 和 B 进行候选召回，路由器使用 T⁻ 拒绝易混淆的候选，从而在不修改在线模型的前提下提升路由精度。

**结果**：在包含 26,262 个技能和 5,400 个问题的 SRA-Bench 上，Capability Pages 使五种检索器的 Recall@10 平均提升 2.94 个百分点；加入 T⁻ 后端到端任务成功率平均提升 3.62 个百分点。中文迁移实验 SSL-SkillDiscovery 的 MRR@50 达到 73.07%，验证了跨语言泛化能力。
