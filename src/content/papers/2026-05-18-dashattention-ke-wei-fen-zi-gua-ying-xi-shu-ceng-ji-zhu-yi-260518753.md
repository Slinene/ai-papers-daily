---
title: 'DashAttention: Differentiable and Adaptive Sparse Hierarchical Attention'
title_zh: DashAttention：可微分自适应稀疏层级注意力
authors:
- Yuxiang Huang
- Nuno M. T. Gonçalves
- Federico Alvetreti
- Lei Li
- Xu Han
- Edoardo M. Ponti
- André F. T. Martins
- Marcos V. Treviso
affiliations:
- Tsinghua University
- Instituto Superior Técnico, Universidade de Lisboa
- Carnegie Mellon University
- Sapienza University of Rome
- University of Edinburgh
arxiv_id: '2605.18753'
url: https://arxiv.org/abs/2605.18753
pdf_url: https://arxiv.org/pdf/2605.18753
published: '2026-05-18'
collected: '2026-05-19'
category: LLM
direction: 自适应稀疏层级注意力 · α-entmax 路由
tags:
- sparse attention
- α-entmax
- long context
- differentiable routing
- hierarchical attention
- LLM
one_liner: 用 α-entmax 替代 top-k 实现可微分、自适应块选择，在长上下文任务中同时提升精度与速度。
practical_value: '- 在推荐系统的长用户行为序列中，可借鉴分块摘要 + α-entmax 路由的设计：先学习每个块的轻量表示，再用 α-entmax
  动态选择相关块，替代固定 top-k，使模型能按需关注任意数量的历史块，提升长序列建模的灵活性。

  - α-entmax 的可微稀疏性让块选择能够端到端训练，避免硬截断带来的梯度断裂，适合需要可学习稀疏门控的生成式推荐（如 Semantic ID 序列建模）或
  Agent 记忆检索模块。

  - 两阶段“粗筛+细读”范式具有工程复用价值：第一阶段用廉价摘要快速评分，第二阶段仅在保留块内计算完整 token 级注意力，可在推理时大幅降低计算量，同时保持精度，适用于工业级推荐模型的服务优化。

  - 论文的局部注意力摘要初始化技巧（从均值池化平滑过渡）及 GPU 友好的 Triton 实现策略（块摘要缓存、位掩码压缩、单次融合 pass）可直接启发推荐系统在处理超长序列时的特征工程和系统实现。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
长上下文语言模型需要同时具备高选择性和灵活性：既要忽略无关信息，又要精确检索到任意数量的重要位置。密集 softmax 注意力会分散概率质量，而基于 top-k 的硬路由固定了预算、切断了梯度流，无法根据不同查询自适应调整稀疏模式。该工作旨在设计一种可微分、自适应稀疏的层级注意力，端到端可训练，并保持高效推理。

### 方法关键点
- **三阶段设计**：Stage 0 用局部注意力学习每个分块的可微分摘要向量，初始化为均值池化，逐步增强表达力；Stage 1 用 α-entmax 代替 top-k，根据查询自适应产生稀疏的块级路由分布，块数动态变化并保持可微；Stage 2 在选中的块上执行带先验偏差的 token 级 softmax 注意力，全局可微且兼容 FlashAttention。
- **先验引入**：将 Stage 1 的块路由概率变换为先验分布，控制 KL 散度强度，使第二阶段 softmax 在路由块内精细缩放，未路由块完全屏蔽，同时保留梯度回传至摘要与路由参数。
- **理论保证**：证明 α-entmax 头聚合非分散，而 softmax 头聚合会重新引入分散，因此在困难检索任务上优势明显。
- **高效 GPU 实现**：基于 Triton 的三核融合，采用块摘要缓存、位掩码压缩、单次融合迭代，适配预填充和解码两种场景。

### 关键实验
在 MiniCPM-4 (1B/3B/8B) 上继续训练 16K 长文本，对比 NSA 和 InfLLMv2。在 RULER 和 HELMET 基准上，75% 稀疏度的 DashAttention 准确率接近全注意力，且在更高稀疏度下（如 90%）显著领先基线（HELMET 整体精度高 9% 以上）。推理速度最高达到 FlashAttention-3 的 3.36 倍、InfLLMv2 的 1.35 倍。动态稀疏分析显示不同层自适应分配密度，浅层更密、中层更稀，类似手动预算分配效果。

### 关键洞察的一句话
以 α-entmax 为路由的层级注意力，既实现了根据查询自适应稀疏化，又保持了端到端可微，将稀疏注意力的准确度和效率推向了新的 Pareto 前沿。
