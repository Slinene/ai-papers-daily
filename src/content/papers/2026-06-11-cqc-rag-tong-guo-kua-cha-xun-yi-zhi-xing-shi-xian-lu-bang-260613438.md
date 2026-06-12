---
title: 'CQC-RAG: Robust Retrieval-Augmented Generation via Cross-Query Consistency'
title_zh: CQC-RAG：通过跨查询一致性实现鲁棒检索增强生成
authors:
- Yanjia Sun
- Sifan Liu
- Jie Shao
affiliations:
- University of Electronic Science and Technology of China
arxiv_id: '2606.13438'
url: https://arxiv.org/abs/2606.13438
pdf_url: https://arxiv.org/pdf/2606.13438
published: '2026-06-11'
collected: '2026-06-12'
category: RAG
direction: RAG 鲁棒性 · 交叉查询一致性
tags:
- RAG
- Cross-Query Consistency
- Hallucination Mitigation
- Multi-Query
- Self-Assessment
one_liner: 提出跨查询一致性假说，通过生成多样等价查询并评估答案信心稳定性来过滤幻觉，无需外部监督即可提升 RAG 鲁棒性
practical_value: '- **查询变体注入与一致性筛选**：在 RAG 管道中，对同一用户意图生成多个语义等价但句法不同的查询，通过对比各查询下答案的置信度稳定性，可以自动过滤噪声导致的幻觉，直接提升问答或知识检索的可靠性，无需额外标注数据。

  - **证据-答案配对自评估协议**：将答案与支撑其的证据片段强绑定，要求模型同时输出答案和对应证据，再利用跨查询稳定性筛选，这种方法可迁移到 Agent 的多步推理或工具调用验证环节，用于剔除不可靠的中间结果。

  - **共享文档池与重排序策略**：不依赖扩大检索覆盖，而是先召回一个共享候选文档集合，再针对每个查询变体重新排列文档顺序，构建差异化的推理上下文，在有限检索计算下实现多样化证据视角，适合低延迟、资源受限的业务场景。

  - **生成式推荐的鲁棒性借鉴**：当用户 query 或产品描述存在多种表达方式时，可通过生成多个语义等价变体、分别生成推荐理由或纠偏候选，再依据一致性选出最稳定的推荐，减少因表述差异导致的推荐结果波动。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：RAG 的可靠性高度依赖于外部证据的检索与使用方式，同一意图的不同句法表述可能导致不同检索结果，且无关或误导性文档会进一步诱发幻觉。现有多路径推理方法通过解码随机性注入多样性，但不可控，且答案评估局限在单一查询诱导的证据视角。为此，作者提出**交叉查询一致性假说**：正确答案在语义等价但句法多样的查询下会维持高置信度，而噪声诱导的幻觉则会在查询变体下波动。

**方法**：CQC-RAG 框架协同设计查询级多样性注入与跨查询一致性评估。首先将原始问题改写为多个语义等价但表达多样的查询；接着基于共享文档池为每个查询重排序，构造查询条件化的推理上下文；然后采用证据绑定协议，要求模型同时输出答案和支撑证据片段，形成答案-证据对；最后计算每个答案在多个上下文中的置信度稳定性，选择最稳定的答案作为最终输出。整个过程是一种无需外部监督的自我评估机制，且不依赖扩大检索覆盖。

**结果**：在 TriviaQA、MuSiQue 等四个开放域问答基准上，CQC-RAG 全面超越最强多查询基线，在 TriviaQA 上 EM 提升 4.76 pp，在 MuSiQue 上提升 9.12 pp，验证了跨查询一致性对过滤噪声幻觉的有效性。
