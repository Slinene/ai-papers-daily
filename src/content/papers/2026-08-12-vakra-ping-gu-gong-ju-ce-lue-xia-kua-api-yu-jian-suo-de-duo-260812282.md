---
title: 'VAKRA: Evaluating Multi-Hop Reasoning Across APIs and Retrieval Under Tool-Use
  Policies'
title_zh: VAKRA：评估工具策略下跨 API 与检索的多跳推理
authors:
- Ankita Rajaram Naik
- Anupama Murthi
- Benjamin Elder
- Siyu Huo
- Raavi Gupta
- Abhinav Jain
- Praveen Venkateswaran
- Abdulhamid Adebayo
- Danish Contractor
affiliations:
- IBM
arxiv_id: '2608.12282'
url: https://arxiv.org/abs/2608.12282
pdf_url: https://arxiv.org/pdf/2608.12282
published: '2026-08-12'
collected: '2026-08-13'
category: Eval
direction: Agent 工具调用评测基准
tags:
- Agent evaluation
- Tool use
- Multi-hop reasoning
- API retrieval
- Benchmark
- Enterprise agents
one_liner: 推出 8000+ 可执行 API 的企业 Agent 评测基准，发现模型失败集中在语言中介推理与策略约束
practical_value: '- **真实 API 重执行验证**：评测 Agent 时用可执行 API 重放预测的工具调用并验证结果，比静态答案更接近线上工具调用场景；电商搜索/推荐
  Agent 评估可借鉴，允许多条有效路径判断正确性，避免误判。

  - **关注语言中介推理而非工具调用**：论文发现失败集中在实体消歧、跨源 grounding，而非工具调用机制。电商 Agent 设计应重点优化实体链接和 schema
  映射，例如显式注入商品 ID 映射、同义词表、类目别名，减少因命名不一致导致的调用失败。

  - **策略约束下增加拒答机制**：模型在不可回答查询上准确率低至 2.4%，暴露严重幻觉。在电商客服/推荐 Agent 中，应设置明确的不可回答或信息不足分支，结合置信度阈值触发拒答或转人工，避免错误工具调用造成业务风险。

  - **固定 ReAct harness 隔离模型能力**：团队在选型基础模型或评测生成式推荐能力时，可固定同一 Agent 框架，只替换底层 LLM，快速定位模型本身的问题，避免架构干扰。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：企业 Agent 需要跨结构化 API 和文档集合进行多跳推理，但现有基准往往只孤立评估 API 调用或知识检索，无法反映真实场景中语言理解与工具使用的耦合。

**方法关键点**：VAKRA 构建了超过 8,000 个可执行 API，覆盖 62 个领域，任务分三个递进难度：多样 API 交互风格、结构化 API 多跳推理、带自然语言工具使用策略约束的多源推理。正确性通过重放预测的工具调用到真实 API 来验证，允许多条有效路径。评测使用固定 ReAct harness，隔离模型能力与 Agent 架构。

**关键结果数字**：最佳模型在单跳端点式任务上仅 70.4%，组合 API 任务降至 50–51%；推理深度增加导致性能下降超过 50%；策略约束问题暴露严重失败，不可回答查询准确率低至 2.4%。Trace 分析显示失败集中在语言中介推理——实体消歧、跨源 grounding，而非工具调用机制。
