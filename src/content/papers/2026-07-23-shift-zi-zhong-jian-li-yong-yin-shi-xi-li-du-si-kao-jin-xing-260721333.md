---
title: 'SHIFT: Self-reconstruction Harnesses Implicit Fine-grained Thinking for Retrieval'
title_zh: SHIFT：自重建利用隐式细粒度思考进行检索
authors:
- Yuxiao Luo
- Da Li
- Mingjie Zhang
- Zhentao He
- Shikun Zhang
- Wei Ye
affiliations:
- Peking University
- Institute of Computing Technology, Chinese Academy of Sciences
- Beihang University
arxiv_id: '2607.21333'
url: https://arxiv.org/abs/2607.21333
pdf_url: https://arxiv.org/pdf/2607.21333
published: '2026-07-23'
collected: '2026-07-24'
category: RAG
direction: 隐式推理检索器 · 细粒度自重建
tags:
- implicit reasoning
- self-reconstruction
- contrastive learning
- next-token prediction
- LLM retriever
one_liner: 用细粒度自重建缓解对比学习与隐式推理的目标错配，提升推理密集型检索性能
practical_value: '- **隐式推理检索可直接用于电商搜索/推荐召回**：在双塔模型里插入少量软 token 做隐式查询理解，替代显式改写，既保留推理能力又降低在线延迟。

  - **细粒度 NTP 重建可作为对比学习的有效正则**：在训练检索器时加入 next-token-prediction 重建 query 或 item 文本，能缓解对比目标与生成能力之间的冲突，提升表征的语义对齐度，适合复杂意图的查询-商品匹配。

  - **残差投影与双向注意力的适配方案**：将 LLM 转换为检索器时，用残差投影层和按任务定制的双向注意力聚合，可稳定保留预训练语义知识，这为利用大模型做召回模型提供了一套轻量、稳定的改造范式。

  - **对 Agent 中检索工具的优化意义**：若 Agent 需要调用多跳推理检索，可微调一个隐式推理检索器，在低延迟下实现接近显式推理的效果，适合实时决策场景。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：现有基于 LLM 的检索器往往采用「先改写后检索」引入显式推理，或通过软 token 实现隐式推理（如 GIRCSE、LaSER）以提升效率。但隐式推理方法普遍存在对比学习目标和生成推理目标之间的错配，导致检索性能受限。

**方法**：提出 SHIFT 训练框架，将 LLM 转化为高效推理检索器。包含两个关键设计：
1. **推理高效的检索骨干**：在 LLM 隐空间中引入残差投影层和任务导向的双向注意力聚合，使模型能够高效凝聚推理信息，输出适合检索的表征。
2. **细粒度自重建任务**：利用 next-token-prediction 方式对输入文本进行逐 token 重建，作为对比学习的辅助任务，缓解对比损失与隐式推理之间的目标冲突，迫使模型在表征中保留细粒度语义。

**结果**：在多项推理密集型检索基准上，SHIFT 一致超越主流检索器，并取得新的 SOTA 效果。消融分析验证了残差投影、双向注意力聚合及细粒度重建各自的作用。
