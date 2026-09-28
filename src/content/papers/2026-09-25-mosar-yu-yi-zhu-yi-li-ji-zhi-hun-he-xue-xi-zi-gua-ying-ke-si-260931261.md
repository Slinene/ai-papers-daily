---
title: 'MoSAR: Mixture of Semantic Attention Regimes for Learning Adaptive and Approximable
  Attention Geometries'
title_zh: MoSAR：语义注意力机制混合，学习自适应可近似注意力几何
authors:
- Michele Paolicelli
- Alessandro Petruzzelli
- Alessandro Franceso Maria Martina
- Cataldo Musto
- Giovanni Semeraro
affiliations:
- Università degli Studi di Bari Aldo Moro
arxiv_id: '2609.31261'
url: https://arxiv.org/abs/2609.31261
pdf_url: https://arxiv.org/pdf/2609.31261
published: '2026-09-25'
collected: '2026-09-28'
category: LLM
direction: LLM 高效注意力 · 自适应几何
tags:
- Efficient Attention
- Long Context
- RoPE
- Sparse Attention
- Learnable Decay
- Routing
one_liner: 在 RoPE 后通过 query/key 路由器混合短中全局 regime，学习可离散化的距离衰减注意力几何，500M 预训练外推最优
practical_value: '- 在电商搜索/推荐的长用户行为序列建模中，可借鉴「可学习距离衰减 + 轻量路由器」替代固定窗口或硬截断：用 query/key
  双侧路由选择短/中/全局 regime，让不同 token/item 自适应选择交互范围，既保留长程依赖又降低注意力成本。

  - 推理时采用 top-1 离散化先把 attention support 确定，再计算稀疏 QK。论文显示 support density 随上下文长度下降（0.154→0.104），说明在商品描述、会话历史等长序列场景中，这种路由可带来亚二次的注意力开销，适合在线扩容。

  - 若需要显式压成本，可参考 MoSAR-Cost：在 LM loss 上加入归一化期望 reach 正则，以很小的困惑度代价换取更低的预期注意力范围；在推荐排序
  loss 里也可以加入类似 expected attention cost 项，实现推理成本可控。

  - 结论「平滑可控衰减优于硬 mask」可直接用于改进用户长期兴趣序列的 RoPE 截断或滑动窗口设计，避免硬截断带来的语义不连续。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**  
Dense self-attention 的二次复杂度是长上下文 LLM 的核心瓶颈，现有稀疏/局部方法多在训练前固定模式，难以适配不同 token、层和上下文。RoPE 提供相对位置几何，但并没有显式的距离衰减。论文认为注意力近似本质是几何问题：应从数据学习交互几何，让模型自己决定哪里局部、哪里保留更广交互，而不是先验规定稀疏性。

**方法关键点**  
- 在 post-RoPE 的 query 和 key 后分别插入轻量 MLP 路由器，输出对短/中/全局三种 semantic regime 的概率分布。
- 每个 regime 定义距离衰减函数 g_mn(d)：包含 locality 区（保持 RoPE 交互）、transition 区（平滑衰减到 e^{-B}）和 low-relevance 区（有限下限）。默认 reach 为 (δ_S, δ_M, δ_G)=(128,512,2048)，plateau 分数为 (0.75,0.5,1)，全局 regime 无衰减，所以 MoSAR 包含 dense RoPE 特例。
- query regime 与 key regime 的几何取平均得到 pair 几何，注意力偏置 B_θ=log W_θ，W_θ 是 query/key 路由概率与 regime 矩阵的 bilinear 混合。
- 训练时 soft routing 稠密计算，可学习连续衰减场；推理时可 top-1 离散化，先基于路由输出构建 causal support Ω_θ，再做稀疏 QK 计算。
- MoSAR-Cost 额外加入归一化期望 reach 正则，显式偏置模型选择更短的计算范围。

**关键实验与数字**  
8 个 Gemma2-style 500M 模型从头预训练，序列长度 2048，约 10B tokens，共享种子、数据和优化，对比 RoPE、ALiBi、0.75-RoPE、Fixed-S/M、RoPE-M-mask 等。训练上下文 PPL@2k：MoSAR 12.269，与最佳 Fixed-M 12.267 基本持平，但期望 reach 仅 0.221，远低于 dense。长度外推到 8k 时，MoSAR PPL 12.208 为所有变体最优，优于 ALiBi 12.232 和 RoPE 15.176；0.75-RoPE 则退化到 29.594。Top-1 离散化后 8k PPL 12.872，相对软路由仅增加 5.4%，support density 从 0.154 降到 0.104，注意力成本呈亚二次增长。RoPE-M-mask 表现明显更差，说明平滑可控衰减优于硬 mask。

**最值得记住的一句话**  
注意力近似应从几何出发，让模型学习位置相关性的衰减尺度，而不是预先固定稀疏模式。
