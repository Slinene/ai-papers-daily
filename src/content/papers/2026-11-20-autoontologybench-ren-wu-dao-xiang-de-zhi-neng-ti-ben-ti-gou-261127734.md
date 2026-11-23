---
title: 'AutoOntologyBench: A Task-Grounded Benchmark for Agentic Knowledge Engineering'
title_zh: AutoOntologyBench：任务导向的智能体本体构建基准
authors:
- Minye Shao
- Chenghao Xiao
- Xingyue Zhao
- Yang Long
affiliations:
- Durham University
- Shanghai University of Finance and Economics
- Peking Union Medical College Hospital, Peking Union Medical College
- Alibaba DAMO Academy, Alibaba Group
arxiv_id: '2611.27734'
url: https://arxiv.org/abs/2611.27734
pdf_url: https://arxiv.org/pdf/2611.27734
published: '2026-11-20'
collected: '2026-11-23'
category: Eval
direction: Agent 知识工程基准评测
tags:
- Knowledge Graph
- Ontology
- LLM Agents
- Benchmark
- Knowledge Engineering
one_liner: 评估智能体构建本体解决真实任务，发现自主构建落后专家13个点
practical_value: '- 借鉴“任务导向的本体评估”思路：电商商品知识图谱/类目体系的质量不应只看结构正确性，而应直接看下游任务（搜索召回、推荐排序、问答）的指标提升。可以建立类似
  AutoOntologyBench 的评测集，用实际业务任务验证知识表示的有效性。

  - 论文结果表明 agent 自动构建的本体在检索基础上能带来 6.1 个点的任务成功率提升，但不及专家构建（差 13.0 点）。在实际业务中，可以考虑“Agent
  构建 + 人工/专家校验”的半自动流程，用 agent 生成初始版本，再由运营或领域专家修订，平衡效率与质量。

  - 任务类型拆解为 Application、Repair、Organization、Construction，对电商类目维护有直接参考：可以分别评估 agent
  在“使用本体完成查询/推荐”、“修复错误本体关系”、“整理合并冗余类目”、“从零构建新类目体系”四类操作上的能力，定位薄弱环节。

  - 关注 source-native verification：论文用原始知识源来验证任务结果，电商可以类比用商品详情页、用户行为日志、商家录入信息作为 ground
  truth，自动验证知识抽取的准确性，避免人工标注昂贵。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：Foundation-model agents 从软件工程扩展到自主科学研究，但获取和整合领域知识仍是挑战。知识图谱和本体被用来组织异构知识，但现有基准要么孤立评估本体正确性，要么孤立评估任务成功率，无法回答“自主构建的本体是否真的帮助解决任务”。

**方法**：提出 AutoOntologyBench，一个任务导向基准，包含 19,947 个审计任务，基于 18 个真实知识源，覆盖 7 个领域，支持 source-native verification。任务分为四类：Application（应用）、Repair（修复）、Organization（组织）、Construction（构建）。比较了 9 个前沿模型 agents 在匹配的知识表示下的表现，包括 agent 构建的本体、专家参考本体、无本体基线等。

**结果**：在检索基础上，agent 构建的本体使任务成功率提高 6.1 个百分点，但比专家派生的参考本体低 13.0 个百分点，表明自主知识获取仍是规模化科学研究的瓶颈。代码和资源在 GitHub 开源。
