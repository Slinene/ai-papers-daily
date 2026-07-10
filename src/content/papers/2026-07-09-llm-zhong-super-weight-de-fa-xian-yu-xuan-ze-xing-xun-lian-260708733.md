---
title: Super Weights in LLMs and the Failure of Selective Training
title_zh: LLM 中 Super Weight 的发现与选择性训练之败
authors:
- Shreyas Subramanian
- Adewale Akinfaderin
- Akarsha Sehwag
affiliations:
- Amazon Web Services
arxiv_id: '2607.08733'
url: https://arxiv.org/abs/2607.08733
pdf_url: https://arxiv.org/pdf/2607.08733
published: '2026-07-09'
collected: '2026-07-10'
category: Training
direction: 参数高效微调 · Super Weight 分析
tags:
- Super Weights
- LoRA
- Sparse Training
- PEFT
- Intrinsic Dimensionality
- LLM Fine-tuning
one_liner: 证明重要性不等于可孤立训练性：微调 Super Weight 完全失效，而全层低秩更新（LoRA）成功且对位置限制鲁棒
practical_value: '- **微调策略选择**：不要试图仅训练少量重要参数（基于幅度或剪枝后的子集），即使它们对模型质量至关重要；实验显示训练100–8192个
  Super Weight 准确率跌至随机，同样大小的随机稀疏训练（避开 Super Weight）却能超过基线。在电商/推荐场景微调 LLM 做 query 理解、商品描述生成时，直接使用
  LoRA 等全层低秩更新，无需特意挑选重要参数。

  - **LoRA 位置冻结的冗余性**：在 attention 层中冻结与 down_proj Super Weight 坐标对应的位置（占 LoRA 参数的
  0.5–6.8%）对性能统计无影响（10 seeds p>0.05），且 LoRA 自身更新中最高幅值位置也不是瓶颈。这意味着部署 LoRA 时，不需要针对下游关键权重的位置做
  mask 或缩放，低秩结构本身已提供协调性。

  - **结构化分解的指导意义**：理论证明稀疏更新只捕获微调子空间的 k/N，而低秩分解的覆盖维度是稀疏的 256×。在设计参数高效微调方案时，应优先选择具有层级别协调的结构（如低秩、SVD
  基冻结），避免坐标对齐的稀疏选择，无论那些坐标看起来多重要。

  - **异常权重的处理**：若模型通过激活尖峰识别出 Super Weight 存在，标准 LoRA 微调足以成功，且 Super Weight 在微调期间几乎不变（幅度变化仅
  0.03%），LoRA 通过重新路由表征来利用固定的高增益放大器。在需要持续适配推荐模型时，可信任 LoRA 的隐式正则，无需额外冻结或特殊约束 Super Weight
  参数。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**：
Super Weight 是 LLM 中极少数参数，移除会导致困惑度飙升数个数量级。直觉上，微调这些最重要的参数应能高效适配下游任务，但本文验证了这一直觉完全错误。研究旨在厘清：参数重要性是否等同于可孤立训练性？

**方法关键点**：
- 在 OLMo-1B 与 OLMo-7B 上进行严谨对照实验，以 ARC‑Easy 为主要基准。
- Super Weight 识别：通过幅度排序，绝大部分集中于 MLP 的 `down_proj` 层，并验证跨 1000 条 WikiText‑2 样本的激活一致性（9 个权重在所有样本中均引发最大尖峰）。
- 实验组：
  - 直接训练 top‑k SW（k=100 ~ 8192），其余冻结；
  - 邻域训练（包含 SW 周围 3×3 区域，最多 36864 参数）；
  - 两个关键对照：同层随机稀疏训练（避开 SW）与同层低秩更新（LoRA on `down_proj`）；
  - LoRA‑dproj‑SW‑freeze：在 attention 层的 LoRA 更新中，冻结与 `down_proj` SW 坐标对应的行/列，缩放因子 s=0.0～1.0；
  - LoRA‑ΔW‑SW‑freeze：冻结 LoRA 学习到的 ΔW 中最高幅值的前 1000 个位置。
- 理论分析：内在维度框架下，稀疏更新捕获微调子空间的期望比例为 k/N（k=4096 时仅为 6.4×10⁻⁶），而低秩流形维度是稀疏的 256 倍；孤立训练 SW 时梯度放大引发崩溃。

**关键结果**：
- 直接训练 SW 的准确率全部跌落随机（～25%），邻域扩展无效（表 2,3）。
- 回避 SW 的随机稀疏训练 alcanzable（64.18% vs 基线 60.65%），同层 LoRA 达 68.77%，排除了稀疏性或模块未适配的干扰（表 6）。
- Vanilla LoRA（0.16% 参数）提升至 66.88%，且对 attention 位置冻结不敏感：s=0.0 冻结 6.8% LoRA 参数，10 种子测试与 vanilla 无统计差异（62.90%±0.45%，p>0.05）。
- 冻结 LoRA 自身高幅值 ΔW 位置也未见性能退化（表 5）。
- Winogrande 上模式一致：SW 训练崩溃至机会，LoRA 保持基线附近。
- SW 在 LoRA 训练中几乎不变（平均变幅 0.03%），而直接训练时平均变幅 8.19%，证实大更新摧毁序列。

**最值得记住的一句话**：参数的关键性不等于其可分离训练性；有效的参数高效微调必须依赖全层范围的结构化分解（如 LoRA），而非针对个别重要权重的稀疏更新。
