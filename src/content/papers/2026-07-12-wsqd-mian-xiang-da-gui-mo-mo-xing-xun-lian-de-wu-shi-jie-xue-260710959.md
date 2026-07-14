---
title: 'WSqD: A Horizon-Free Learning Rate Schedule for Large Model Training'
title_zh: WSqD：面向大规模模型训练的无视界学习率调度
authors:
- Jianhao Ma
- Yuxin Chen
affiliations:
- University of Pennsylvania
arxiv_id: '2607.10959'
url: https://arxiv.org/abs/2607.10959
pdf_url: https://arxiv.org/pdf/2607.10959
published: '2026-07-12'
collected: '2026-07-14'
category: Training
direction: 训练优化 · 学习率调度
tags:
- learning rate schedule
- continued training
- stochastic convex optimization
- LLM pretraining
- horizon-free
- Warmup-Stable-Decay
one_liner: 提出结合逆平方根基底与线性退火的 WSqD 调度，理论证明其最优 O(1/√T) 收敛，并在 LLM 续训中无需重调优就能超越调优的 WSD
practical_value: '- **长时间递进式训练/增量训练可直接复用**：在电商搜索、推荐模型的持续训练场景中（如每天新增日志继续训练），WSqD 的根基底与训练时长相独立，同一峰值学习率可跨越不同续训长度，避免每次续训重调学习率。

  - **设置建议**：将 shift 参数 T0 设为初始短跑时长（如 5000 或 10000 步），基学习率由短跑网格搜索确定一次后即可用于后续所有更长工期，工程成本极低。

  - **退火阶段的长度**：线性退火占比 α 固定为 20%，实践可照搬；续训时从退火前检查点恢复，仅丢弃退火部分的计算，性价比高。

  - **适配优化器**：论文给出 Adam-style 和 Muon-style 的镜像下降视角诊断，在实际推荐模型训练中可监控梯度 L1 范数或块核范数作为双范数缩放因子的稳定性，以便将实用优化器方向近似视为镜像下降步骤，增强调度理论指导。'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
现代大语言模型（LLM）训练常需在预算耗尽后继续训练或加域适应。传统余弦退火将学习率与固定训练终场强绑定，WSD（Warmup-Stable-Decay）虽支持续训，但其最优峰值学习率仍依赖训练总长，续训时需重新调优。为此，作者受随机凸优化启发，设计了一种真正无视界的学习率调度。

### 方法关键点
- **WSqD 调度**：后预热的调度由两阶段组成：阶段 1 采用平移逆平方根基底 `c₀ / √(t+T₀)`，全程不依赖总步数 T；阶段 2 在最后 αT 步线性衰减到零。
- **理论保证**：在标准随机凸优化（非光滑）框架下，证明随机镜像下降配合 WSqD 的最后迭代达到极小化最优 `O(1/√T)` 收敛速率，且最优的 `c₀` 与 T 无关，只需 `T ≥ max{2T₀, 4/α}`。逆平方根基底避免了 WSD 常量阶段的信息停滞，最终线性退火消除了逆平方根自身对数因子的次优性。
- **续训协议**：从阶段 1 的检查点恢复，仅丢弃原退火区间，无需重调根底学习率，完成灵活续训。

### 关键实验结果
- 在 SlimPajama 语料上预训练 213M 参数的 LLaMA 风格模型，使用 AdamW。
- 续训从 15000 步延长至 60000 步，WSqD 复用短跑（10000 步）搜索得到的同一根底学习率，始终匹配或优于精心调优的 WSD，在最长工期优势约达 1.05×。
- 对比两级调优 WSD（含第二阶重搜峰学习率）和幂律调度，WSqD 表现相当或更优，而计算开销更小。
- 消融实验表明 shift 参数 T₀≥5000 后不敏感，推荐设为初始短跑长度。

### 最值得记住的一句话
WSqD 用逆平方根基底解耦了续训灵活性与最优收敛，凭借一个仅需短跑调优的根底学习率即可覆盖多种续训长度，实现真正的‘一次调参，处处续训’。
