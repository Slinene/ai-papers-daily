---
title: Efficient LLM-based Subgraph Retrieval for Multi-Hop Knowledge Base Question
  Answering
title_zh: 基于 LLM 的高效子图检索用于多跳知识库问答
authors:
- Duanyang Yuan
- Sihang Zhou
- Xiaoshu Chen
- Haoyuan Chen
- Ke Liang
- Jian Huang
arxiv_id: '2610.39667'
url: https://arxiv.org/abs/2610.39667
pdf_url: https://arxiv.org/pdf/2610.39667
published: '2026-10-29'
collected: '2026-11-01'
category: Reasoning
direction: MCTS + LLM 图检索 · 多跳 KBQA
tags:
- MCTS
- LLM
- KBQA
- Subgraph Retrieval
- Multi-hop Reasoning
- Graph Search
one_liner: 用 MCTS 将子图探索转为树搜索，结合 LLM 引导节点筛选，在 WebQSP 上 Hits@1 达 78.88% 并提升效率
practical_value: '- 在电商商品知识图谱的多跳推理或可解释召回中，可借鉴 MCTS 将子图扩展变成树搜索：对每个候选节点计算 relevance
  score 并回传剪枝，避免按 hop 全量扩张带来的候选爆炸，显著降低线上推理延迟。

  - LLM 不做最终答案生成，而是作为搜索方向 refine 器：每一步用 LLM 判断当前节点/关系是否与 query 相关，可减少纯符号搜索的盲目性；类似思路可用于
  RAG 的图索引检索或 query 到 KG 的映射，控制 LLM 调用成本。

  - 节点评分反馈机制可作为召回阶段的 hard filtering：先粗召回，再用轻量打分/LLM 过滤不相关节点，适合 latency 敏感场景；在商品图谱问答或导购
  Agent 中可先 MCTS 缩小候选，再进精排。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：IR-based 多跳 KBQA 方法从整个知识库抽取子图时，常包含大量与问题弱相关或无关的节点；缺少节点过滤机制时，无关节点数量随跳数增加而膨胀，造成计算资源浪费。

**方法**：提出 M-ER 框架，用 Monte Carlo Tree Search (MCTS) 将子图探索转化为树结构搜索。在 MCTS 选择阶段，优先纳入与问题高度相关的节点，避免遍历 KB 所有节点；引入 LLM 细化搜索方向，保证探索聚焦于相关节点；对选中节点做定量打分，并将分数反馈到节点选择过程，过滤不相关候选，提升子图质量。

**结果**：在 WebQSP 基准上，M-ER 达到 78.88% Hits@1，同时提升计算效率，验证了性能与效率的平衡。
