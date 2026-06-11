---
title: 'Tail-Aware Adaptive-k: Query-Adaptive Context Selection for Retrieval-Augmented
  Generation'
title_zh: 尾部感知自适应k：查询自适应的RAG上下文选择
authors:
- Ziyu Song
- Jiaming Fang
- Kuangyu Li
- Tuo Xia
- Chuanpeng Wang
affiliations:
- AI Lab, 37 Interactive Entertainment
- School of Computer Science, Wuhan University
arxiv_id: '2606.11907'
url: https://arxiv.org/abs/2606.11907
pdf_url: https://arxiv.org/pdf/2606.11907
published: '2026-06-10'
collected: '2026-06-11'
category: RAG
direction: RAG · 自适应上下文选择
tags:
- RAG
- Adaptive Retrieval
- Extreme Value Theory
- Query-Adaptive
- Context Selection
- Knee Detection
one_liner: 利用排序相似度曲线陡-平-陡模式进行拐点检测，结合局部极值理论检验，实现高效、查询自适应的检索截断，近似oracle质量
practical_value: '- 在RAG pipeline中，可利用相似度曲线的几何特征（陡-平-陡）进行拐点检测，动态决定检索文档数量，避免固定k带来的噪声或遗漏，提升面向电商问答、知识检索的生成质量。

  - 推荐系统中，向量召回后的结果截断可借鉴该方法：根据item相似度分布自动确定top-k，替代人工经验调参，降低粗排/精排计算量，尤其在长尾查询下稳定。

  - Agent系统需要从工具或知识库中动态选取上下文时，TAA-k提供了一种无训练、低计算开销的自适应截断策略，适合线上实时决策。

  - 方法对嵌入模型和压缩维度鲁棒，可跨业务场景复用，无需重新训练或校准。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：RAG中固定Top-K检索无法适应查询间的差异和重尾相似度分布，导致上下文噪声或信息缺失。极值理论（EVT）提供了自适应截断的数学框架，但现有全局应用方式计算复杂度高达O(N²M)且统计不稳定。

**方法**：提出TAA-k，利用排序相似度曲线呈现的“陡-平-陡”模式（陡：相关文档，平：过渡带，陡：噪声），通过拐点检测定位候选区间；再在局部窗口内进行EVT拟合优度检验，精确识别尾行为（噪声）起始位置，作为自适应截断k。这种粗到精的设计将复杂度降至O(√(N log N)M)，且无需训练。

**结果**：在WebQuestions、2WikiMultiHopQA和MuSiQue三个数据集上，TAA-k的F1分数距离oracle仅有2-3%的差距，而计算效率相比全局EVT方法提升数个数量级，对不同嵌入模型和压缩维度均有鲁棒性。
