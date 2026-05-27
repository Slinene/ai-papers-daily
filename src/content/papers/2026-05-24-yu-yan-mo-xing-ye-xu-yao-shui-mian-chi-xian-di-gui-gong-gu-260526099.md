---
title: Language Models Need Sleep
title_zh: 语言模型也需要睡眠：离线递归巩固长时记忆以支持深层推理
authors:
- Sangyun Lee
- Sean McLeish
- Tom Goldstein
- Giulia Fanti
affiliations:
- Carnegie Mellon University
- University of Maryland
arxiv_id: '2605.26099'
url: https://arxiv.org/abs/2605.26099
pdf_url: https://arxiv.org/pdf/2605.26099
published: '2026-05-24'
collected: '2026-05-27'
category: Training
direction: 序列模型记忆巩固 · 离线递归计算
tags:
- SSM
- fast weights
- depth-recurrence
- memory consolidation
- hybrid model
- reasoning
one_liner: 在SSM-Attention混合模型中引入离线递归更新快权重，将计算移出推理时，提升对已逐出上下文的深层推理能力
practical_value: '- **离线递归巩固用户长序列行为**：电商推荐中用户行为序列很长，可将sleep机制用于在上下文窗满时将历史行为压缩进SSM或fast
  weight记忆，并迭代更新几次后再清空KV缓存，后续预测只需单次前向，保证在线低延迟。

  - **Fast weight显式存储推理中间态**：在生成式推荐（如Semantic ID序列）中，可将用户兴趣演化视为一种需要“深度计算”的推理过程，利用递归快权重更新逐步聚合信息，而非仅依赖固定深度的Encoder，这与当前多智体（Agent）记忆压缩的场景可类比。

  - **递归深度可自适应难度**：根据当前交互的复杂程度（如查询涉及的hop数）自动调节sleep的递归步数N，类似动态网络深度，简单场景用N=1快速响应，复杂推理场景用更大N保证精度。

  - **训练时通过递归快权重反向传播**：在离线训练时采用类似递推跨窗的梯度回传，避免全序列并行的高内存，可处理超长用户序列，与当前推荐系统流式训练架构兼容。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：Transformer长上下文推理成本高，混合SSM-Attention模型通过将过期上下文压缩进固定大小的fast weight来降低显存，但固定深度的单次前向压缩可能无法支持对已逐出令牌的深层推理（如多跳检索、状态演化）。该工作受生物学睡眠期间海马体回放巩固记忆的启发，提出在上下文窗满时进入“睡眠”阶段，通过多次离线递归前向传播迭代更新快权重，将计算负担从推理时迁移到离线阶段，从而在保持推理低延迟的前提下提升长程推理能力。

**方法关键点**：
1. **架构**：以SSM-Attention混合模型为基础，在每L个token的硬驱逐边界，对当前上下文执行N次递归前向传播（循环整个模型或部分层），利用SSM块的局部更新规则（如Gated Delta Networks）反复精炼fast weight状态，随后清空KV缓存。
2. **训练**：端到端训练，梯度通过整个递归过程反向传播，仅根据最终预测损失优化，迫使模型学会利用睡眠循环将上下文有效编码进快权重。
3. **推理**：预测阶段仅需单次前向，不增加延迟，所有额外计算已预付在睡眠阶段。
4. **滑动窗口变体**：同样适用，每步驱逐最旧token前进行N次递归。

**关键实验与结果**：
- **规则110细胞自动机**：在L=24的硬驱逐下，要求预测t步后的状态。无睡眠的GDA混合模型准确率随t增大快速下降，在t=32时仅约10%；加入N=4循环后准确率提升至30%+，且学习速度更快。
- **Depo多跳推理**：k-hop图遍历任务，随k增大，无循环模型几乎不进步，而N=4循环在16-hop上已开始收敛，验证了递归巩固对复杂检索的增益。
- **GSM-Infinite数学推理**：在Jet-Nemotron 2B和Ouro 1.4B上微调，对6和8跳操作任务，增加睡眠循环（如N=6 vs N=1）带来9～47%的相对准确率提升，尤其在小窗口(L=512)下，2-hop任务也从59.6%提到90.5%。
- **吞吐分析**：训练吞吐因跨窗串行和深度递归线性增加，但实验表明性能提升值得该开销。

**核心结论**：仅靠增大记忆容量不足以处理深度推理，离线递归计算能将逐出的上下文转化为支持后续推理的快权重，且提升随问题深度增大而更显著。睡眠是提升长上下文模型推理效率的有效途径。
