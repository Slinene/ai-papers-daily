---
title: Group-Aware Adaptive Retrieval for Evidence Navigation
title_zh: 群组感知的自适应证据导航检索
authors:
- June Park
- Jun Kwon
- Jonghyo Kim
- Jongwuk Lee
affiliations:
- Sungkyunkwan University
arxiv_id: '2609.02188'
url: https://arxiv.org/abs/2609.02188
pdf_url: https://arxiv.org/pdf/2609.02188
published: '2026-09-02'
collected: '2026-09-05'
category: RAG
direction: 自适应检索 · 组级扩展 · 推理密集检索
tags:
- adaptive retrieval
- corpus graph
- group-level expansion
- explore-then-exploit
- reasoning-intensive retrieval
- LLM reranker
one_liner: 用组级方向评估替代文档级扩展，结合探索-利用策略提升推理密集检索中的有界召回问题
practical_value: '- 在电商/内容推荐中，可借鉴离线对物品图做社区检测得到语义簇，并用LLM为每个簇生成摘要，作为粗粒度召回方向。相比逐item扩展，簇级信号能更早发现远处相关物品，减少初期弱信号下的迷航。

  - 采用explore-then-exploit策略：召回初期用round-robin从多个高分组簇各取少量物品，避免过早集中在单一簇；后期集中到强相关簇。该策略适合搜索推荐中的多路召回融合，前期保多样性，后期聚焦头部。

  - 分离粗粒度方向评估与细粒度相关性排序：navigator用较小的reranker模型（如Qwen3-Reranker-4B）评估组摘要，主reranker用大模型精排文档。工程上可并行执行，且实验表明小模型足够做方向判断，可节省大量推理成本。

  - group-driven evidence propagation后处理：对同簇内高排名文档赋予衰减权重，并传播给簇内其他文档。可类比电商推荐中的类目内协同过滤，利用头部商品带动长尾商品得分，提升召回排序质量。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
推理密集检索中，相关文档常因非表面匹配而无法出现在初始召回池，导致有界召回问题（bounded recall）。现有自适应检索方法基于corpus graph逐文档扩展邻居，但在检索初期，当前文档级相关性信号弱且噪声大，易沿错误方向扩展并传播误差。核心问题：如何从弱信号中辨识能导向相关文档的扩展方向？

**方法关键点**
- **组构建（离线）**：在文档语义近邻图上用Leiden社区检测划分语义一致且相互区分的组；对每组用LLM生成摘要，作为该扩展方向可获取信息的粗粒度预览。
- **组感知自适应检索（在线）**：每轮迭代先用文档级reranker对当前窗口重排，保留top-h文档；然后navigator对候选组（当前窗口文档邻域所属组）打分，依据query与组摘要的相关性。采用**explore-then-exploit**策略：前τ_switch轮从多个高分組中轮询选取未观测文档（广度优先），之后集中从最高分组深度选取，减少早期决策错误传播。
- **组驱动证据传播（后处理）**：对最终top-10文档赋予RBP衰减权重，将同组内高排名文档的权重按α参数传播给组内其他文档，提升同组相关但未被精排充分提升的文档。

**关键实验**
在BRIGHT（12个子集）、R2MED、BEIR上评估。对比Retrieve-and-Rerank、SlideGAR、RGS、REPAIR。在BRIGHT非推理设置下，GAREN平均nDCG@10达28.3，比最强baseline RGS高7.2%；推理设置下31.2，比RGS高7.9%（摘要提及最高提升8.0%）。在R2MED和BEIR上也取得最优或次优。消融显示navigator、explore-then-exploit、propagation均必要，移除navigator改用连接度启发式导致nDCG@10下降25.1%。距离分析表明gold doc离初始窗口越远，GAREN优势越明显，因为组图可将文档图上的多跳压缩到3跳内。

**最值得记住的一句话**：将扩展单元从文档提升到语义组，用小型navigator评估组级方向，配合探索-利用策略，能在弱信号下可靠地导航至远处相关文档。
