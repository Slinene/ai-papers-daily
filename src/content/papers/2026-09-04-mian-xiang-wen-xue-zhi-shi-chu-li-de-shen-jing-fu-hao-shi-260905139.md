---
title: 'NS-ST-GraphRAG: Neuro-Symbolic Spatio-Temporal GraphRAG for Literary Knowledge
  Processing'
title_zh: 面向文学知识处理的神经符号时空 GraphRAG 框架
authors:
- Zheng Kui Lin
affiliations:
- Joint Laboratory for Port Big Data and Intelligent Applications, Dalian Ocean University
arxiv_id: '2609.05139'
url: https://arxiv.org/abs/2609.05139
pdf_url: https://arxiv.org/pdf/2609.05139
published: '2026-09-04'
collected: '2026-09-08'
category: RAG
direction: 神经符号时空 GraphRAG 与可验证 QA
tags:
- RAG
- Knowledge Graph
- Spatio-Temporal
- Neuro-Symbolic
- Multi-hop QA
- Hallucination Mitigation
one_liner: 提出整合时空约束与动态子图检索的 NS-ST-GraphRAG，并发布红楼梦多跳 QA 基准
practical_value: '- **按查询时空范围选择有效图状态**：电商/推荐场景中，商品属性、价格、库存、活动规则都有明确时效；可以借鉴论文思路，按时间戳/空间/场景对知识图谱做切片，检索时动态加载匹配版本，避免
  RAG 返回过期或冲突信息。

  - **本体引导抽取 + 确定性约束检查**：在商品知识、活动规则、导购问答等场景，先定义轻量本体（类目、属性、关系、时效），用 LLM 抽取实体关系后，再用规则校验时间范围、数值区间、空间限制等硬约束，降低生成幻觉；适合构建可解释的导购
  Agent 或政策问答。

  - **可审计的多跳评估方法**：论文的机械答案复现、引用忠实度检查、每部分证据跨度设计，可以迁移到内部知识问答或推荐解释评估中；建议对关键业务 QA 采用“规则校验答案
  + 独立语义判断”双轨，而不是只依赖 LLM 主观打分。

  - **警惕过度设计**：实验显示时空 GraphRAG 相比简单窗口基线只有方向性优势但统计不显著；业务上应先用严格 AB 和统计检验验证复杂架构的必要性，避免为了图而图。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**  
长篇叙事（如《红楼梦》）对 RAG 构成特殊挑战：证据分散在各章，人物关系随时间变化，答案可能依赖时间、空间和关系约束的联合推理。现有静态语料级图检索无法处理这种时空有效性。

**方法关键点**  
NS-ST-GraphRAG 将本体引导抽取、确定性约束检查、双时间坐标、空间场景属性与动态子图检索结合。与固定全量图不同，系统根据 query 的时空范围选择有效的图状态，并基于可追溯证据生成答案。同时发布 Red-Chamber-QA，首个古典中文文学多跳问答基准，包含 104 题初版与 120 题 held-out，设置时间/空间/一般问题类别、逐部分证据跨度和确定性快捷控制。

**关键结果**  
Held-out 120 题：机械答案复现率 0.733，高于冻结窗口基线 0.675、闭卷模型 0.083；McNemar 精确检验 p=0.092，方向有利但不显著。语义判断准确率 0.866 vs 0.850，无可靠差异。预注册的约束类别条件未获支持。整体验证了时空图表示、受限抽取与可审计评估的整合路径，但优势尚需更大规模验证。
