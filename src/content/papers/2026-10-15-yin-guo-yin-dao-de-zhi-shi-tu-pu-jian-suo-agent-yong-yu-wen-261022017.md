---
title: 'CARA: Causally Guided Retrieval Agent for Question Answering'
title_zh: 因果引导的知识图谱检索 Agent 用于问答
authors:
- Weicheng Liu
- Xiangcheng Wu
- Depeng Xu
- Haopeng Zhang
- Xi Niu
affiliations:
- University of North Carolina at Charlotte
arxiv_id: '2610.22017'
url: https://arxiv.org/abs/2610.22017
pdf_url: https://arxiv.org/pdf/2610.22017
published: '2026-10-15'
collected: '2026-10-16'
category: RAG
direction: Agent 因果检索 · 知识图谱 QA
tags:
- Causal Retrieval
- Agentic RAG
- Knowledge Graph
- RRF
- STaRK
- Question Answering
one_liner: 提出 CARA，以证据对回答的因果贡献替代纯文本相似，引导 KG 检索 Agent 并融合多轨迹
practical_value: '- 在电商商品知识图谱或导购 Agent 中，把召回/排序的相似度信号替换或补充为**因果相关性评分**：对候选商品/证据问“加入它是否实质性改善对用户
  query 的回答/推荐，去掉它是否损失关键证据”，可有效过滤“相关但不必要”的商品，减少推荐噪音，尤其适合长尾 query 和复杂约束场景。

  - 采用**多 Agent 并行探索 + RRF 融合**：多个 agent 用不同初始锚点和子查询独立遍历，最后用 reciprocal rank fusion
  聚合，比简单的 count-based vote 更鲁棒；可迁移到多策略召回/多路搜索融合，成本可控且提升召回稳定性。

  - **聚焦探索与成本控制**：因果评估能减少无效 hop 和工具调用，但会引入 LLM 评估延迟；业务落地时可对候选批量评估、只对 top-k 邻居调用因果模块，或用轻量模型/规则做初筛后再评估，在效果与延迟间取平衡。

  - 论文在 STaRK 的 **AMAZON 电商数据集**上验证有效，其 causal prompt 设计（明确“不是文本相似”，给出 0-0.2 无关、0.9-1.0
  决定性等评分量表）可直接参考迁移到电商 QA、导购知识库检索等场景。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：知识图谱 RAG 中，现有 agentic retriever 主要依赖文本相似性和图结构引导搜索，容易找到“与 query 相关但并非回答所需”的证据。例如问“该患者应避免哪种药”，相似检索返回当前用药列表，而真正关键的是“过敏：阿莫西林”这类短记录。因此需要识别对回答有实质因果贡献的证据，而不是仅文本匹配。

**方法关键点**：
- 提出 training-free 的 CARA（CAusally guided Retrieval Agent），在 KG 检索 Agent 中嵌入因果推理模块 C，对每个邻居候选估计 **consequentiality**（加入候选是否显著提升可回答性）和 **essentiality**（移除候选是否显著削弱可回答性），并结合 **path consistency** 评估跳转是否延续当前路径。
- 具体评分：因果分 `cau_i = λc_i + (1-λ)e_i`，最终分 `st = α·cau_i + (1-α)·p_i`；λ=α=0.5 在实验中最优。
- C 不是独立 Agent，而是评估模块，不调用工具，只输出分数影响 Agent 的下一步动作（继续 hop / re-anchor / finish）。
- 使用 GlobalSearch（BM25 全局锚定）和 Neighbors（类型过滤 + BM25 一跳探索）两个工具；多个 Agent 并行探索，最后用 **RRF** 融合证据列表，奖励高单 Agent 排名和跨 Agent 共识。
- 用 Qwen3.8-27B 作为所有 LLM 调用 backbone，3 个 Agent，Tmax=150，GlobalSearch k=30，Neighbors k=20。

**关键结果**：在 STaRK 的 AMAZON/MAG/PRIME 三个数据集上，CARA 的 Hit@1 和 MRR 均最高：MAG Hit@1 84.9 vs ARK 80.1，MRR 88.1 vs 83.1；PRIME Hit@1 59.5 vs 58.6。下游 QA 的 BERTScore 在三个数据集均最高，faithfulness 也优于 ARK，但 KAR 的 faithfulness 最高，说明贴近证据不等于正确。消融显示因果模块是主要增益，RRF 提供额外提升。效率上 CARA 的 GlobalSearch/Neighbors 调用和检查节点数均少于 ARK，但额外因果评估导致延迟较高，尤其 MAG/PRIME。

**最值得记住的一句话**：检索时不应只问“像不像”，而应问“加上它是否让答案更可答、去掉它是否让答案受损”。
