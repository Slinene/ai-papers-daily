---
title: 'BM25 Wins at Scale: A Scaling Study of Retrieval-Augmented Generation Paradigms'
title_zh: BM25在大规模上获胜：检索增强生成范式的扩展性研究
authors:
- Pengyu Wang
- Benfeng Xu
- Shaohan Wang
- Xin Zeng
- Huarui Wu
- Lei Zhang
- Licheng Zhang
affiliations:
- University of Science and Technology of China
- Metastone Technology
- Beijing Academy of Agriculture and Forestry Sciences
arxiv_id: '2607.26497'
url: https://arxiv.org/abs/2607.26497
pdf_url: https://arxiv.org/pdf/2607.26497
published: '2026-07-29'
collected: '2026-07-31'
category: RAG
direction: 检索增强生成扩展性分析
tags:
- BM25
- scaling laws
- RAG
- File-System Agent
- GraphRAG
- cost-efficiency
one_liner: 在450倍语料规模扩展实验中，BM25在大约1000万词元后全面超越文件系统Agent和图RAG，成为准确性最高且成本最低的默认检索方案
practical_value: '- **大规模知识库推荐系统检索选型**：在电商商品描述、客服知识库等百万级文档场景中，BM25应当被作为默认检索器，而不必盲目追求稠密检索或Agent搜索；BM25无需LLM构建索引，成本极低且准确率在大规模时反而领先。

  - **搜索词/问题改写中的成本控制**：File-System Agent在小规模（<1000万词元）时可获得最佳准确率，但其顺序探索导致查询成本为BM25的39倍以上；在广告搜索词推荐或用户问题重写中，应先通过全局关键词检索（如BM25）获得候选，再引入Agent推理，而不是全程依赖Agent遍历。

  - **图索引构建的门槛评估**：GraphRAG（如LightRAG、MS-GraphRAG）在构建阶段消耗极大，LightRAG在300万词元时已无法完成构建，且准确率始终不如BM25；在含有大量噪声、事实冲突的电商评价或客服记录中，图遍历更容易被语义干扰，应谨慎评估ROI。

  - **评测设计的借鉴**：论文通过固定问答集、固定对抗文档、仅增加背景语料的“嵌套语料梯”设计，可以迁移到搜索推荐系统的离线评估中，用于衡量模型在库存/内容膨胀时的鲁棒性，避免单一体量评估掩盖扩展性问题。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：现有RAG范式（词法检索、稠密检索、图RAG、Agent搜索）通常在单一语料规模上评测，其准确率–成本随规模变化的规律不明，导致企业级知识库选型缺乏依据。本文设计了一个从1144篇到51万篇文档、覆盖1.7M到601M词元的28级嵌套语料梯，固定问题、证据和对抗文档，统一读模型和裁判协议，系统比较了7种管线的扩展性。

**方法关键点**：
- 28级嵌套语料梯：从1,144篇“基石”文档开始，每级按1.25倍增长，总规模扩大约450倍，问题、黄金文档、对抗陷阱和拒答诱饵在所有级别保持不变。
- 7种管线：BM25（无LLM构建）、DenseRAG（共享嵌入）、HippoRAG 2、MS-GraphRAG、LightRAG、LinearRAG、File-System Agent（无索引，用LLM读写文件树，预算80次调用）。
- 统一读模型Qwen3.6-27B，统一裁判协议（结合答案对齐和原子事实完整性）。
- 精确计量构建和查询的token消耗与延迟。

**关键结果**：
- 在最小的几个共享级别上，File-System Agent准确率最高（77.4 vs BM25 74.7），但在约1000万词元时被BM25反超。
- 全量601M词元时，BM25领先File-System Agent近20个百分点（50.5 vs 30.7），DenseRAG为29.9。
- 图RAG遭遇构建墙：LightRAG在2826篇时已无法完成，MS-GraphRAG在8750篇中止，HippoRAG 2虽可扩展到13万篇，但准确率始终低于BM25。
- 将File-System Agent的检索原语替换为BM25后，全量Agent准确率从36.9跃升至69.4，查询token从895K降至101K，即先全局排名再Agent推理是最优组合。

**核心教训**：语料增长使得全局候选排序的作用越来越大；词法检索是强可扩展的默认项，Agent推理应放在候选发现之后，而非替代全局排名。
