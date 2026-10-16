---
title: 'FreeSolo: Linear-time Sparse Attention with Zero-Shot Length Extrapolation'
title_zh: FreeSolo：零样本长度外推的线性时间稀疏注意力
authors:
- Zekun Shi
- Alastair James Arthur Price
affiliations:
- National University of Singapore
- University of Toronto
- Sea AI Lab, Singapore
arxiv_id: '2610.17191'
url: https://arxiv.org/abs/2610.17191
pdf_url: https://arxiv.org/pdf/2610.17191
published: '2026-10-11'
collected: '2026-10-16'
category: LLM
direction: 线性时间稀疏注意力 · 长度外推
tags:
- sparse attention
- length extrapolation
- linear attention
- long-context
- KV cache
- LLM
one_liner: 短程滑窗+长程 keypoint 选择的稀疏注意力，线性变体短 CPT 即可零样本长度外推
practical_value: '- 在电商/广告/搜索推荐中，用户行为序列可能长达数十万 token，完整 attention 成本过高；FreeSolo 的“短程滑窗
  + 长程 keypoint 选择”可直接启发用户长期记忆或 Agent 记忆模块设计：用 keypoint 表示长历史中的关键类目/商品节点，显著减少 KV cache
  和推理延迟。

  - FS-L 表明通过较短的继续预训练即可学会前缀剪枝，并获得零样本长度外推能力；已有 4k/8k 底座、需要扩展到 64k/256k 行为序列的团队，可以避免昂贵的全量长上下文
  CPT，采用类似的稀疏化微调路径。

  - FS-B 的 radix-sort + 平衡树 O(N log²N) 构建成本，为大规模商品/内容索引的层级化检索提供工程思路：离线构建可剪枝树状索引，在线做
  query 相关的 top-k 节点选择，兼顾精度与时延。

  - 可复用 S-NIAH/RULER 作为长上下文模块评估指标，相比单纯 loss 更能暴露零样本长度外推能力。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：长上下文语言建模面临 full attention 二次成本、循环模型固定状态限制召回、稀疏注意力需继续预训练且长度外推难的困境。  
**方法关键点**：FreeSolo 采用短程滑动窗口分支 + 长程 keypoint cell 选择分支，直接对 token 做稀疏注意力。线性变体 FS-L 用较短 CPT 学习前缀剪枝，再做 query 依赖选择；FS-B 借助基数排序构造平衡树，算法成本 O(N log²N)。  
**关键结果**：在 800M 模型、4k 训练长度下，Zero-shot RULER 外推测试中，FS/FS-L/FS-B 在 S-NIAH-1/2/3 与 RULER mean 上显著优于 Raven、Raven-full、GDN，覆盖 4k–256k 长度，无需长上下文微调。
