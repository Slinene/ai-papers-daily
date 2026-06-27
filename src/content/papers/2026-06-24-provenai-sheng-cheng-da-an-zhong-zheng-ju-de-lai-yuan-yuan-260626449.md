---
title: 'ProvenAI: Provenance-Native Traces of Evidence in Generated Answers'
title_zh: ProvenAI：生成答案中证据的来源原生追踪
authors:
- Mohammad Faizan
- Dalal Alharthi
affiliations:
- University of Arizona
arxiv_id: '2606.26449'
url: https://arxiv.org/abs/2606.26449
pdf_url: https://arxiv.org/pdf/2606.26449
published: '2026-06-24'
collected: '2026-06-27'
category: RAG
direction: RAG归因 · 多跳问答透明度
tags:
- RAG
- Attribution
- Multi-hop QA
- Transparency
- Citation Influence
- Provenance
one_liner: 提出三层透明度框架，独立测量答案正确性、引用忠实度与文档影响力，揭示引用-影响差距
practical_value: '- **推荐解释的可信度评估**：借鉴 leave-one-resource-out 消融方法，量化推荐理由（如商品评论、属性）对最终推荐的实际影响，避免“引用了但没起作用”的虚假解释。

  - **Agent 多步推理审计**：在多步搜索或决策 Agent 中，对每步检索结果进行消融，度量每条知识对最终动作的因果贡献，构建真正可追溯的决策链。

  - **引用忠实度作为线上指标**：设计答案与引用内容的一致性得分，作为 RAG 系统生成质量的持续监控指标，及时捕捉生成幻觉或引用虚标。

  - **多层透明度框架迁移**：将透明度拆分为结果质量、解释正确性和信息实际影响力三个独立维度，分别测量，可用于电商搜索排序的解释面板或 Agent 调试工具。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：RAG 系统常附带引用，但引用存在不代表该来源真正影响了答案生成，多跳 QA 中这一问题更突出，需要量化的透明度度量。

**方法**：ProvenAI 针对 HotpotQA 设计七阶段流水线，将透明度解耦为三层独立指标——答案正确性、引用忠实度（与基准支撑证据的一致性）、文档影响力（leave-one-resource-out 消融下输出的变化）。通过归因审计与 token 级 KL 散度目标的形式化，桥接表面代理与忠实性条件。

**关键结果**：在 7,405 验证样本上，答案准确率 53.53%，平均引用忠实度 71.55%。工作案例揭示“引用-影响差距”：表面引用审计干净，但一个引用来源仅弱影响输出，而七个未引用源显著改变了输出。框架表明，有意义的透明度需要三个独立层次的可追踪链接。
