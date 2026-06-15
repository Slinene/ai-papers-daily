---
title: 'ChronoID: Infusing Explicit Temporal Signals into Semantic IDs for Generative
  Recommendation'
title_zh: ChronoID：为生成式推荐注入显式时序信号的语义ID学习框架
authors:
- Dongdong Nian
- Dongqi Fu
- Chenliang Xu
- Yinglong Xia
- Hong Li
- Hong Yan
- Jian Kang
affiliations:
- University of Rochester
- Meta MRS
- MBZUAI
arxiv_id: '2606.14260'
url: https://arxiv.org/abs/2606.14260
pdf_url: https://arxiv.org/pdf/2606.14260
published: '2026-06-12'
collected: '2026-06-15'
category: GenRec
direction: 生成式推荐 · 时序语义ID
tags:
- Semantic ID
- Temporal Encoding
- Generative Recommendation
- Parallel Quantization
- Relative Time
- Sequential Recommendation
one_liner: 系统性探索如何将时间信号融入语义ID，提出相对时间编码+并行量化+晚融合的最佳方案，显著提升生成式推荐性能。
practical_value: '- 在构建语义ID时，将时间特征独立量化后与物品ID拼接（late fusion），避免异构特征被强制压缩进同一codebook，防止表示坍缩。

  - 使用相对时间间隔（用户相邻交互的时间差）替代绝对时间戳作为时间编码，更有效捕获交互节奏，提升ID判别性；业务中可直接基于事件时间差构造此类特征。

  - 并行量化比残差量化更适合融合文本与时间信息，可防止错误累积，生成解耦、高质的语义ID；在需要融合多模态信号的生成式推荐中值得尝试。

  - 构造时间敏感的离线评估集时，严格按全局时间点切分训练/测试（如指定截止日期），避免未来信息泄露，使离线评估更贴近线上真实分布；该方法简单有效，可直接用于实际系统。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：现有生成式推荐中的语义ID（Semantic ID）完全忽略交互发生的时间上下文，假设物品语义与用户意图是时间不变的，这不符合真实推荐场景的动态性。时间信息仅被隐含地用于序列顺序，而未被纳入语义抽象层面，限制了生成模型对消费节奏变化的适应能力。

**方法**：提出ChronoID框架，系统性探索三个设计维度：
- 时间编码：比较绝对时间戳（Unix timestamp）与相对时间间隔（相邻交互时间差）两种形式，发现相对时间更能刻画用户交互节奏，且避免绝对时间单调递增导致的分布偏移。
- 融合策略：比较早融合（拼接后一起量化）与晚融合（文本与时间分别量化后拼接触发ID），晚融合让异构特征保留各自特性，效果更优。
- 量化机制：残差量化（RQ-VAE）强制层次化、并行量化（多组独立codebook）更灵活地捕获解耦的多模态信息，并行量化显著优于残差量化。

**实验与结果**：在重新构造的时间显式基准（Amazon Industrial/Office、Mercari，以2018年为全局截止时间严格划分训练/测试，杜绝未来信息泄露）上评估。最优配置（相对时间 + 并行量化 + 晚融合）在Industrial数据集上HR@3达12.60，相对MiniOneRec提升36.1%，Office上也提升40.1%。消融实验表明：仅增加codebook容量而不引入时间信息会导致性能下降，去除或零填充时间信号均造成显著退化，说明增益来自有意义的时间语义而非ID位数扩张；显式添加节假日等高级时间特征无额外收益，原始时间戳已足够让模型隐式学到这些模式。

**核心结论**：把时间显式注入语义ID，并采用相对时间编码与并行量化，是生成式推荐中获得鲁棒且高区分性item表示的关键。
