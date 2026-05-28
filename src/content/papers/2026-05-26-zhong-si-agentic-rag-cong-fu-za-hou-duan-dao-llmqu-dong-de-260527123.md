---
title: 'Rethinking Agentic RAG: Toward LLM-Driven Logical Retrieval Beyond Embeddings'
title_zh: 重思Agentic RAG：从复杂后端到LLM驱动的逻辑检索
authors:
- Yuqi Zeng
- Qixiang Deng
- Yulei Wan
- Ruiquan Jiang
- Xiaoqing Zheng
- Xuanjing Huang
affiliations:
- Fudan University
- Shanghai Kingstar Software Technology Co., Ltd.
arxiv_id: '2605.27123'
url: https://arxiv.org/abs/2605.27123
pdf_url: https://arxiv.org/pdf/2605.27123
published: '2026-05-26'
collected: '2026-05-28'
category: Agent
direction: Agent RAG的检索接口与控制权设计
tags:
- Agentic RAG
- Logical Retrieval
- Inverted Index
- Query Refinement
- Hallucination Reduction
- Efficiency
one_liner: 提出LLM用布尔逻辑直接操控倒排索引，匹配混合检索性能同时大幅降低构建与推理成本
practical_value: '- 电商搜索/Agent RAG可借鉴“LLM生成结构化查询+倒排索引”的组合，用AND/OR/NOT精确控制召回，避免稠密检索的语义漂移与冗余结果，尤其在多轮澄清场景下能显著降低无效重试。

  - 当知识库规模大、更新频繁时，跳过离线Embedding与FAISS索引，用OpenSearch等倒排引擎直接响应LLM的布尔表达式，可节省41倍构建时间与约3倍在线延迟，适合高频变动商品库。

  - 答案不可用时的幻觉降低（0.128→0.083）源于显式约束失败可被LLM解读为“证据缺失”，这一信号可借鉴到Agent的拒绝回答策略中，提高推荐或问答系统的可靠性。

  - “重脑轻手”架构将复杂推理留给LLM，检索端仅做确定性执行，该边界划分可简化整个系统迭代——检索索引成为无状态工具，更易维护和扩展。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
当前Agentic RAG普遍依赖稠密/混合检索后端，但在多轮交互中，语义相近的改写查询常导致检索结果高度重叠，LLM难以通过修正查询来修复失败检索（图1）。同时，构建与维护复杂的向量或图索引成本高昂。为此，作者主张将检索控制权交还给LLM，让检索后端退化为一个可精确执行逻辑意图的轻量工具。

**方法关键点**  
- 设计原则：接口需满足**意图忠实性**（LLM指定的约束直接反映在候选集）和**可控性**（LLM能主动拓宽、收紧、排除或调整匹配粒度）。  
- LOGICALRAG实例：LLM生成支持AND/OR/NOT、短语、字段限定的Lucene查询语法，底层用倒排索引检索，BM25仅做排序，不参与约束执行。  
- Agent流程：LLM先规划信息需求，迭代发出逻辑查询，观察结果后决定下一步或生成答案，上下文仅追加历史查询与结果，无额外控制器。

**关键实验与数字**  
- 数据集：HotpotQA、2WikiMultiHopQA、MuSiQue，分中规模（~9K–11K passages）与KILT大规模开放域。  
- 基线：Agentic Hybrid（同流程但用混合检索）、HippoRAG2（图）、MA-RAG（多Agent）。  
- 大规模下，LOGICALRAG与Agentic Hybrid的LLM评测准确率几乎持平（0.717 vs 0.716），但离线构建仅需1.27小时（混合需52.02小时），在线QPS 152.5 vs 66.6，平均延迟74.9ms vs 230.5ms。  
- 答案缺失场景，幻觉率从0.128降至0.083，拒绝率从0.767升至0.828。  
- 模型缩放显示，弱Agent（Qwen3.5-4B）时逻辑检索落后约3%，强Agent（Qwen3.5-Plus）时达到均势，说明高控制接口需足够强的推理能力驱动。

**核心结论**  
“重脑轻手”范式——将复杂推理集中在LLM，检索端仅做透明的确定性执行——既能匹配复杂后端的准确率，又能大幅降低成本并减少幻觉，为Agentic RAG设计提供了新方向。
