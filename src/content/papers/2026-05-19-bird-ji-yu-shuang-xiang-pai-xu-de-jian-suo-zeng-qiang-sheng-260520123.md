---
title: 'BiRD: A Bidirectional Ranking Defense Mechanism for Retrieval Augmented Generation'
title_zh: BiRD：基于双向排序的检索增强生成防御机制
authors:
- Chengcai Gao
- Zhihong Sun
- Xiaochuan Shi
- Qiufeng Wang
- Chao Liang
affiliations:
- Wuhan University
- Naval University of Engineering
- Xi’an Jiaotong-Liverpool University
arxiv_id: '2605.20123'
url: https://arxiv.org/abs/2605.20123
pdf_url: https://arxiv.org/pdf/2605.20123
published: '2026-05-19'
collected: '2026-05-24'
category: RAG
direction: RAG安全 · 双向排序信号
tags:
- RAG
- defense
- ranking
- poisoning
- adversarial
- retrieval
one_liner: 发现毒化文档的双向排名对齐特征，提出结合前向与后向排名的双信号防御框架，兼顾效率与鲁棒性
practical_value: '- 电商 RAG 系统可借鉴双向排名一致性检查作为轻量级毒化检测：在检索后计算查询到文档的前向排名和文档到查询的后向排名的一致性分值，筛选异常文档，额外延迟
  < 1s，适合在线服务。

  - 双向排名信号不依赖特定 LLM 或检索器，可嵌入现有检索管道作为插件式过滤器，迁移成本低。

  - 该发现启示在推荐/广告系统反作弊中，可分析用户与物品的双向近邻关系来检测异常交互，例如刷单用户的邻居行为异常。

  - 实验证明该方法在强攻击下仍有效，可应用于电商问答系统防投毒，提升生成答案的可靠性和任务准确率。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：RAG 系统的语料投毒攻击日益严重，现有防御仅依赖语义相关性分析或投票，计算开销大且对强攻击鲁棒性不足，根源在于忽视了检索结果排序结构中的上下文信息。

**方法**：研究者发现毒化文档与良性文档在双向排名行为上存在差异：毒化文档的后向排名（文档最相关的查询）与查询的前向排名（查询最相关的文档）对齐度异常高。基于此提出 BiRD，构建双信号框架：利用前向排名得分评估语义相关性，后向排名得分量化排名上下文一致性，通过联合两种信号检测并过滤毒化文档。

**结果**：在三个 QA 数据集上，使用三种检索器和三种 LLM，针对两种投毒攻击（PoisonedRAG 等）评估，BiRD 将攻击成功率降低最多 54%，任务准确率提升最多 56%，平均额外延迟小于 1 秒。
