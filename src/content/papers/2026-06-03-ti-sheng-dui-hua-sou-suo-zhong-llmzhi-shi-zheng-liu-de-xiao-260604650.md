---
title: Improving the Efficiency and Effectiveness of LLM Knowledge Distillation for
  Conversational Search
title_zh: 提升对话搜索中LLM知识蒸馏的效率与效果
authors:
- Stan Fris
- Jan Hutter
- Jan Henrik Bertrand
- Simon Lupart
- Mohammad Aliannejadi
affiliations:
- University of Amsterdam
arxiv_id: '2606.04650'
url: https://arxiv.org/abs/2606.04650
pdf_url: https://arxiv.org/pdf/2606.04650
published: '2026-06-03'
collected: '2026-06-04'
category: QueryRec
direction: 对话搜索 · LLM知识蒸馏 · 稀疏检索效率优化
tags:
- Conversational Search
- Knowledge Distillation
- KL Divergence
- Sparse Retrieval
- Contrastive Learning
- Regularization
one_liner: 通过引入加权对比损失、优化负采样策略和强正则化，在稀疏检索中平衡效果与推理效率
practical_value: '- **蒸馏损失中加入小权重对比项**：在电商搜索的 query 重写或对话式推荐场景，若使用 KL 散度蒸馏（如 DiSCo），可混入
  5%-20% 的 InfoNCE 损失，不增加推理开销，就能稳定提升 MRR 和 nDCG—直接替换损失函数即可。

  - **负采样数量需要谨慎选择**：虽然理论上更多负样本能逼近真实 KL 期望，但在做检索相似度蒸馏时，正样本容易被大量负样本“淹没”，造成梯度分散。实验表明
  16 个负样本是平衡点（TopiOCQA 上），这一结论可迁移到商品搜索的稀疏蒸馏中，避免盲目增加 batch 内负例。

  - **利用 KL 蒸馏的松弛特性做强力稀疏正则化**：KL 损失对表示空间的约束比 MSE 更松，因此可以加大 L1 或 FLOPS 正则化强度，将推理 FLOPS
  降低 50% 以上，而召回率下跌 <2%。这对有延迟要求的电商搜索尤为实用，可快速压缩稀疏索引模型。

  - **长会话中特别注意稀疏退化并提供解决方案**：对话轮次增加会导致激活维度急剧膨胀（L0 分数恶化），强力正则化能有效抑制这一趋势，使长对话仍保持高度稀疏，适合部署在客服
  Agent 或多轮对话推荐等场景。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
对话搜索需要根据多轮上下文检索文档，常用 LLM 改写查询但推理成本高。知识蒸馏（KL 散度）可将 LLM 的写作能力迁移到轻量稀疏模型，但现有工作在损失设计、采样策略和稀疏效率方面仍存空白。本文系统研究如何进一步提升 KL 蒸馏的效果与效率。

**方法关键点**  
- **目标函数融合**：将 KL 散度蒸馏损失与 InfoNCE 对比损失加权组合（λ∈[0.05,0.20]），赋予模型显式的排序激励。  
- **采样策略分析**：从理论（大数定律、重要性采样）和实验角度考察负采样数量对 KL 近似质量及下游性能的影响，揭示正样本欠表示导致边际收益递减。  
- **强力正则化**：针对 KL 蒸馏的松弛特性，大幅提高 L1 与 FLOPS 正则化系数（最高 λ_d=5e-2, λ_q=1e-1），显著压缩激活维度，尤其改善长对话的稀疏退化。  

**关键实验**  
在 TopiOCQA 数据集上，以 SPLADE++ 为骨架，对比 DiSCo（纯 KL 蒸馏）基线。  
- 加入 10% InfoNCE 时，MRR 从 0.409 升至 0.421，nDCG@3 从 0.396 升至 0.408；  
- 负采样数从 1 增到 70，KL 散度从 3.501 降至 3.221，但 16 个样本时 MRR/R@10/R@100 均最高，更多反而下降；  
- 使用“Higher”正则化后，FLOPS 从 3.790 降至 1.370（约 2.8 倍），Recall@100 仅从 0.879 降至 0.859（<2.3%），且长对话的稀疏性显著改善。  

**核心 insight**  
“对 KL 蒸馏的稀疏检索模型，小量对比损失可大幅提升排序精度，而强力正则化能在几乎不损害召回的前提下成倍降低推理成本，为工业级对话搜索提供了可落地的效率优化路径。”
