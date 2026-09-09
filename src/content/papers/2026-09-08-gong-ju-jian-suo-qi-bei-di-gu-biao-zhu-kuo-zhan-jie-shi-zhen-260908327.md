---
title: 'Tool Retrievers Are Underestimated: Annotation Expansion Reveals True Capability'
title_zh: 工具检索器被低估：标注扩展揭示真实能力
authors:
- Yanyu Zhu
- Chenheng Zhang
- Shaoshen Chen
- Hoilam Pao
- Yufei zhang
- Jiajun Chai
- Dongnian Wang
- Zhaoyu Hu
- Guojun Yin
- Wei Lin
affiliations:
- Shenzhen International Graduate School, Tsinghua University
- Peking University
- Meituan, Beijing
arxiv_id: '2609.08327'
url: https://arxiv.org/abs/2609.08327
pdf_url: https://arxiv.org/pdf/2609.08327
published: '2026-09-08'
collected: '2026-09-09'
category: Eval
direction: 工具检索评估 · 标注扩展
tags:
- Tool Retrieval
- Benchmark
- Annotation Expansion
- Evaluation
- Agent
- Functional Equivalence
one_liner: 提出ToolEX自动发现功能等效工具组合，扩展基准为ToolEQ，证明一对一标注系统性低估检索器，微调增益中30-47%是评估伪迹
practical_value: '- 评估召回/检索系统时，若 query 存在多个等价结果（如同义商品、替代品、功能相同工具），单一 ground truth
  会低估模型；可借鉴 ToolEX 做等价扩展，构建更公平的测试集，避免误杀有效召回。

  - 微调收益评估需警惕标注缺陷：论文发现 30-47% 的微调提升是评估伪迹。建议上线前用扩展后的多正例评估集复测，量化真实增量，尤其当训练数据与测试标注同源时。

  - ToolEX 自动发现等价工具组合的流程（生成候选 + 功能等价验证）可迁移到电商搜索/推荐：对同一 query 挖掘多条等价商品、广告或服务组合，用于多正例学习或评估鲁棒性。

  - 如果业务中做 Agent 工具检索或 API 推荐，注意同一功能通常有多个实现，检索评估与训练不能基于一对一的刚性标注，需支持一对多映射。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：工具增强的 LLM Agent 依赖检索器从大规模工具库中召回相关工具。由于工具库常含功能重叠但命名/接口不同的工具，同一 query 可由多个功能等价工具组合解决，形成天然的一对多映射。但现有工具检索基准（如 Tool-DE）只标注单一相关组合，将一对多压成一対一，导致有效检索被误判为失败。

**方法关键点**：提出 ToolEX（Tool Equivalent eXpansion）框架，自动发现并标注与已标注组合功能等价的工具组合。应用于 7,360 查询的 Tool-DE 基准，发现 67.9% 的子查询存在等价替代，平均每个 query 扩展到 5.3 个有效组合，构建新基准 ToolEQ。该流程同样应用于 SkillRet 技能检索，证实一对多问题普遍存在。

**关键结果数字**：在 ToolEQ 上重评估 8 个基础检索器与 2 个微调变体，指标较 Tool-DE 大幅上升；一对一标注系统性低估检索器能力；之前报告的微调增益中 30-47% 是评估伪迹，而非真实提升。
