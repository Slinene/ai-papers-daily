---
title: Advancing SVD-based LLM Compression via Layer-Wise Error Model Search
title_zh: 推进基于SVD的LLM压缩：逐层误差模型搜索
authors:
- Moritz Thoma
- Maximilian Groezinger
- Maximilian Forstenhäusler
- Emad Aghajanzadeh
- Manoj Rohit Vemparala
- Christos Anagnostopoulos
- Pierpaolo Mori
- Nael Fasfous
- Alexander Frickenstein
- Daniel Mueller-Gritschneder
affiliations:
- Technical University of Munich
- BMW Group
- University of Glasgow
- TU Wien
arxiv_id: '2610.32878'
url: https://arxiv.org/abs/2610.32878
pdf_url: https://arxiv.org/pdf/2610.32878
published: '2026-10-23'
collected: '2026-10-26'
category: Other
direction: LLM 低秩压缩与层级误差建模
tags:
- SVD
- LLM Compression
- Rank Allocation
- KFAC-SVD
- Layer-wise Error
- ILP
one_liner: 提出LEMS与KFAC-SVD，分别解决SVD压缩中rank分配不精确和分解rank崩溃的问题
practical_value: '- 在部署LLM用于推荐/query生成时，SVD压缩可大幅降低推理成本，但rank分配不能简单全局均匀：LEMS用逐层误差代理+ILP全局优化，能更好地保留关键层容量，值得借鉴到生成式推荐的backbone压缩。

  - KFAC-SVD利用token-wise统计替代Fisher信息估计，缓解rank collapse，提高了分解质量；若业务中需要对嵌入层或Transformer层做低秩近似，可优先考虑类似token级统计修正。

  - 层间误差传播的建模思路可迁移到多任务资源分配：在电商多目标排序模型中，不同层的敏感度不同，可仿照传播偏置做层级算力/参数预算分配。

  - 工程实现上，ILP求解rank分配虽然复杂，但离线一次性完成，对在线推理无额外开销；适合用固定压缩比部署LLM生成商品描述、搜索词润色等场景。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**  
现有SVD低秩压缩方法存在两个关键缺陷：全局rank分配依赖未校准的误差代理，无法捕捉层间复杂误差传播；基于Fisher的分解估计器易出现rank collapse，损害压缩后模型质量。  

**方法关键点**  
提出两个组件：  
- **LEMS**：引入逐层误差代理，融合局部与全局层重要性，并加入传播偏置项，然后通过整数线性规划（ILP）求解全局最优rank分配。  
- **KFAC-SVD**：改用token-wise统计进行分解，替代传统Fisher信息矩阵，有效缓解rank deficiency问题。  

**关键结果数字**  
在Mistral、Qwen3、Llama 3系列上，LEMS相比现有搜索策略取得一致提升，zero-shot准确率最高提升4.8个百分点，并可泛化至70B参数模型；KFAC-SVD带来平均15%的perplexity改善。项目代码已开源。
