---
title: Dense Structural Compression of Transformers via Gauge-Correct Channel Removal
title_zh: 通过规范校正通道移除实现 Transformer 稠密结构化压缩
authors:
- Jed A. Duersch
- Naïm Es-Sebbani
- Nathanaël Haas
- Zied Bouraoui
affiliations:
- Université d’Artois, CNRS, CRIL UMR 8188, Lens, France
arxiv_id: '2609.07264'
url: https://arxiv.org/abs/2609.07264
pdf_url: https://arxiv.org/pdf/2609.07264
published: '2026-09-07'
collected: '2026-09-09'
category: Training
direction: 训练期结构化压缩与架构搜索
tags:
- GaugeLasso
- structured pruning
- group lasso
- transformer compression
- training efficiency
- gauge symmetry
one_liner: 训练期用对称 group-lasso 惩罚解决 gauge 自由度，在保留 dense tensor 下动态压缩 Transformer，最高
  255 倍 FMA 压缩且精度不降
practical_value: '- 部署推荐/广告 Transformer 时，可优先考虑训练期自适应压缩而非后剪枝：论文证明同样的 utility 度量在后剪枝上失败或显著变差，持续压缩压力会促使网络学到更高效的表征，而不仅删除冗余。

  - 如果业务模型含 SwiGLU MLP、attention 等 gauge-connected 结构，可借鉴 additive symmetric group-lasso
  惩罚：同时对两侧 factor 做 Frobenius-norm 惩罚，避免直接惩罚 product norm 导致的梯度消失和不稳定；按每通道实际 FMA/参数规模校准
  penalty，能把「效用/算力」统一到同一尺度。

  - 工程上实现物理 channel removal 而非 mask 稀疏：用 gauge Sinkhorn 先平衡、再 trust-drop 移除整 slice，缩小后的
  dense tensor 在 GPU 上保持高吞吐，减少稀疏算子低效；这适合做粗粒度 tower 压缩或小规模重训模型。

  - 自适应 ρ 由 loss target 驱动压缩强度，实现较平滑的「先达标再压缩」过程，可作为业务中自动搜架构、控制性能下限的参考；但该理论目前只在 <150M
  FMA 从零训练任务上验证，迁移到大模型或预训练权重需谨慎。'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

**动机**
推理时每 token 能耗主要由 dense matmul 的 FMA 和访存决定。现实 Transformer 通常给所有层分配统一宽度/深度，但不同深度功能差异很大，训练所需结构也往往远大于推理所需。现有后剪枝、NAS、CoFi 等方法要么在固定表示上操作、要么搜索离散候选集、要么启发式处理 multiplicative coupling。论文希望从训练中动态压缩结构，在保持 dense tensor 高吞吐的同时最大化推理效用/算力。

**方法关键点**
- 识别 Transformer 中的 gauge 自由度：如 Wv 与 Wo 互相 rescale 不改变函数，直接惩罚 product norm 会不稳定，一方趋零时另一方梯度消失。
- GaugeLasso 用 additive symmetric group-lasso penalty：对 channel-aligned 两侧因子分别加 Frobenius-norm 惩罚，在网络到达 gauge balance 时，group norm 能衡量通道效用。
- 效率校准：不同轴参数规模和每通道 FMA 不同，按 λA=ρ r_j/√n_A、λB=ρ r_j/√n_B 设置惩罚，使平衡后的 group norm 构成 inference utility per FMA 的单调估计。
- 训练机制：coupled regularization 让 penalty 与 task gradient 一起进入优化器；adaptive ρ 根据 loss target 保守求解，只有 Loss<L* 时才压缩；gauge Sinkhorn 定期做重参数化平衡；trust-drop 在效用低于阈值时物理删除整 channel slice，模型变成更小的 dense tensor。压缩轴覆盖 attention/MLP 内部维度、残差流 D 和分类器输入 dc。

**关键实验**
- 有限域多项式长除法 F31：8 层 Transformer 13.2M FMA，无惩罚 100% 精度；压缩后在 52k–90k FMA 上保持完美 exact match，最高 255×、中位 187× 压缩。
- 字符级语言模型 PG-19：7.1× FMA 压缩模型 perplexity 2.610，优于同 FMA 的手工 baseline 2.652。
- CelebA masked autoencoding：压缩匹配 baseline；当 dk 饱和后二次设计 dk=256，loss 从 0.237 降到 0.213。
- Post-hoc pruning 用相同 utility 度量无法达到训练期压缩结构：F31 上第一个通道移除就破坏精度，LM 上同等 FMA 下 ppl 差 22%；CoFi 只压到 1.97×，达不到 7.09×。
- 重训发现的架构在 retrieval/LM 上恢复质量，但在 F31 精确算法任务上失败，说明持续压力对发现和训练某些架构是必要的。
- 压缩使训练逐步加速，最终 step 快 1.6–5×。

**最值得记住的一句话**
持续的结构压力能发现后剪枝不可达的高效 dense 架构；additive symmetric penalties 解决了 gauge pathology，使训练期稠密压缩可行。
