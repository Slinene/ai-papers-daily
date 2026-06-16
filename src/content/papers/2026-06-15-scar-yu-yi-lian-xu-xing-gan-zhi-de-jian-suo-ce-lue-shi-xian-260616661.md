---
title: 'SCAR: Semantic Continuity-Aware Retrieval for Efficient Context Expansion
  in RAG'
title_zh: SCAR：语义连续性感知的检索策略实现RAG高效上下文扩展
authors:
- Nathanaël Langlois
affiliations:
- Horizon Flow
arxiv_id: '2606.16661'
url: https://arxiv.org/abs/2606.16661
pdf_url: https://arxiv.org/pdf/2606.16661
published: '2026-06-15'
collected: '2026-06-16'
category: RAG
direction: 语义连续性感知的自适应上下文扩展
tags:
- RAG
- Semantic Continuity
- Context Expansion
- Retrieval Efficiency
- Adaptive Chunking
one_liner: 提出自适应扩展相邻块的检索策略，以更少的块数达到高召回并减少 token 开销
practical_value: '- 在电商知识库、客服RAG中，可借鉴SCAR的自适应扩展逻辑，通过权衡查询相关性与结构连续性，避免静态窗口造成的token浪费，用更少的上下文块保持高召回。

  - 方法对嵌入模型具有尺度不变性，同一超参数可直接跨模型迁移，减少多业务场景下的调参成本，适合快速部署。

  - 对于需要跨段落重组证据的长文档（如产品规格书、法律条款），SCAR可提升边界分割后的证据链完整性，避免人工调整分块策略。

  - 在Agent的记忆检索或工具调用文档检索中，引入结构连续性惩罚项，能有效缓解因固定分块带来的信息碎片化，提升下游生成质量。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：固定长度分块常将关键证据切分到相邻块中，导致检索召回下降（边界碎片化问题）。现有静态窗口或父块检索虽改善召回，但引入大量冗余token开销。

**方法关键点**：SCAR 提出自适应检索策略，在检索到初始块后，选择性扩展其相邻块。扩展决策基于查询与邻居的相关性评分，并引入结构连续性惩罚项，通过相对阈值（与当前块自身查询相关性绑定）动态决定是否拼接邻居。该规则近似尺度不变，跨嵌入模型无需重新标定超参数。

**关键结果**：在 RFC、GDPR、10-K报告、并购协议四个语料（共320个查询，其中160个边界分割查询）上，SCAR 对边界分割查询的召回率达 92.8%，平均仅使用 7.84 个块，相对于静态窗口（10.16 块）减少 22.9% 的块开销。Bootstrap 检验（B=10000）确认块减少高度显著（p<0.0001，Cohen's d=-1.49），召回差异较小（Cohen's d=-0.33）。使用 text-embedding-3-large、BGE-large-en-v1.5、zembed-1 三个嵌入模型，均采用同一组超参数，无需重新调整。下游 RAGAS 评估表明，SCAR 在保持生成忠实度的同时，上下文 token 减少 27.1%。
