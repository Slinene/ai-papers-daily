---
title: Tokenization with Split Trees
title_zh: 基于分割树的子词分词方法ToaST
authors:
- Craig W. Schmidt
- Michael Krumdick
- Adam Wiemerslage
- Seth Ebner
- Varshini Reddy
- Yuval Pinter
- Chris Tanner
affiliations:
- Kensho Technologies
- Ben-Gurion University
- MIT
arxiv_id: '2605.22705'
url: https://arxiv.org/abs/2605.22705
pdf_url: https://arxiv.org/pdf/2605.22705
published: '2026-05-21'
collected: '2026-05-23'
category: Training
direction: 分词优化 · 子词压缩
tags:
- tokenization
- compression
- integer programming
- subword
- vocabulary
- Rényi efficiency
one_liner: 通过递归分割树与整数规划直接优化压缩率，大幅减少token数量并提升下游性能
practical_value: '- 分词压缩率提升11%+，可降低推理成本、延长有效上下文，适合大规模文本处理或LLM驱动的电商描述生成、对话系统

  - 词表选择建模为整数规划，用LP松弛获得近最优解，这一思路可借鉴到推荐场景的特征离散化或Semantic ID编码优化

  - 递归分割树结构天然支持自回归推理中的动态分词决策，可探索与生成式推荐的树形索引结合，提升编码效率

  - Rényi效率大幅提升，意味着稀有token使用更均衡，可能减少OOV问题，适用于多语言电商场景或罕见商品名称编码'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：现有子词分词方法（BPE、WordPiece、UnigramLM）采用启发式压缩策略，无法达到最优压缩率，影响推理效率和上下文窗口利用率。  
**方法**：ToaST（Tokenization with Split Trees）首先依据字节n-gram统计为每个预分词构建一棵完全二叉分割树，独立于词表。推理时，从根到叶递归下降，遇到首个在词表中的节点即输出为token。词表选择被形式化为整数规划（IP）问题，目标是最小化所有分割树上的总token数；由于LP松弛在实践中接近整数解，可高效求得近最优词表。训练时间随分割树数量二次方增长。  
**结果**：在英语文本上，词汇量≥40,960时，ToaST比主流方法减少token 11%以上，有效扩展上下文长度；常用单字节token使用频率更低，Rényi效率显著改善。用1.5B参数语言模型训练实验，ToaST获得最高CORE分数，超出基线2.6%–7.6%（两个基准显著），并在22个任务中的13个上表现最佳。
