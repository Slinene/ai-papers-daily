---
title: Incremental Pooled LLM Evaluation for Cost-Effective Retrieval Model Selection
title_zh: 增量池化 LLM 评估：低成本检索模型选择
authors:
- Max Nelson
- Hanoz Bhathena
- Aviral Joshi
- Saket Sharma
affiliations:
- JPMorganChase
arxiv_id: '2609.02745'
url: https://arxiv.org/abs/2609.02745
pdf_url: https://arxiv.org/pdf/2609.02745
published: '2026-09-02'
collected: '2026-09-03'
category: Eval
direction: 检索模型评估 · LLM 评判
tags:
- LLM-as-judge
- Pooled evaluation
- Retrieval model selection
- RAG
- Incremental evaluation
- Cost-efficiency
one_liner: 增量池化 LLM 评估复用已有相关性判断，仅对新系统新增文档做 LLM 评判，大幅降低 RAG 检索模型选型成本
practical_value: '- 在电商搜索/推荐召回模型选型中，用 LLM 做 pooled relevance judgment：维护一个已标注文档池，新召回模型上线前只标注其新增文档，复用旧
  qrels 计算完整指标，适合快速迭代。

  - 对于有大量召回重叠的候选系统（如不同 embedding、混合检索），池化方案能获得 65-80% 标注复用，等价于数倍评估成本节省，可工程化为自动化评估
  pipeline。

  - 采用 bootstrap 估计 qrels 不确定性，避免在小样本或 LLM 判断噪声下对模型排序做出错误结论；对比模型时报告置信区间而非单一数值。

  - 在 Agent 检索工具选择或多路召回对比中，同样可复用增量池化思路，让 LLM 仅评判增量文档，支撑低成本、持续的多候选评估。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**  
生产 RAG 系统需要为领域选择最佳检索引擎，但传统 human relevance judgments 成本高且难随新模型迭代。逐系统独立让 LLM 评判也存在大量冗余，因为不同检索系统召回文档高度重叠。

**方法**  
采用池化 LLM 评估：LLM 只评判当前候选系统检索结果文档的并集，形成 qrels；新系统加入时，池子增量扩充，仅评判新系统带来的新文档。所有系统基于同一套 qrels 计算标准 IR 指标。在四个检索基准 11 个系统上验证，并部署于金融新闻 QA 系统比较 62 个检索配置。

**结果**  
pooled LLM 排名与 gold-standard 高度相关；考虑 qrels bootstrap 不确定性后，97% 的成对系统排序保持。生产中，文档重叠带来 65-80% 判断复用，成本最多降 4.9 倍，使团队无需重新标注即可评估新检索候选。
