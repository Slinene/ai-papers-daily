---
title: 'GUT: Quantifying and Optimizing the Reasoning Uncertainty of LLMs via Graph
  Complexity'
title_zh: GUT：基于图复杂度量化与优化 LLM 推理不确定性
authors:
- Shuang Liang
- Xin-Yu Hu
- Xiang-Jun Ou
- Shao-Qun Zhang
affiliations:
- National Key Laboratory for Novel Software Technology, Nanjing University
- School of Intelligent Science and Technology, Nanjing University
arxiv_id: '2609.05284'
url: https://arxiv.org/abs/2609.05284
pdf_url: https://arxiv.org/pdf/2609.05284
published: '2026-09-04'
collected: '2026-09-07'
category: Reasoning
direction: LLM 推理不确定性量化与优化
tags:
- LLM
- Uncertainty Quantification
- Graph Complexity
- Reinforcement Learning
- Reasoning
one_liner: 用有向无环图表征推理分支，以图复杂度量化推理不确定性并通过强化学习降低不确定性。
practical_value: '- 在 Agent 多步规划或推理场景中，对同一输入采样多条推理链构建 DAG，用图复杂度（节点/边/分支比）作为不确定性分数，可触发重试、请求用户澄清或降低自动决策阈值。

  - 将“负不确定性”作为奖励信号加入 RLHF/DPO 等优化流程，能训练模型生成更聚焦、更少发散的推理路径，适用于需要稳定输出的推荐解释、搜索 query 改写等场景。

  - 图结构相比单链采样更能捕获分支覆盖，可作为在线评估指标，监控生成式推荐/Agent 的推理稳定性，及时发现漂移。

  - 该方法属于通用推理层优化，不依赖具体业务数据，但落地时需重新定义领域图结构与复杂度度量。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：LLM 推理过程常因温度采样产生大量发散分支，即使输入相同也会出现明显不可信甚至荒谬的推理链，影响推理可靠性。

**方法**：提出 Graph-complexity-based UncerTainty (GUT) 方法。核心思路是用有向无环图（DAG）表征每条推理链的潜在分支，确保图空间全面覆盖所有可能分支；GUT-Q 模块通过图复杂度近似推理空间复杂度，实现对推理不确定性的量化；GUT-O 模块以负不确定性作为奖励函数，通过强化学习优化模型，降低推理不确定度。

**结果**：在四个 LLM 和五个数据集上的实验验证了 GUT 的有效性，表明该方法能够量化并降低 LLM 的推理不确定性。
