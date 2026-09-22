---
title: 'Complex KDA: Understanding and Enhancing the Expressivity of Kimi Delta Attention'
title_zh: Complex KDA：理解并增强 Kimi Delta Attention 的表达能力
authors:
- Julien Siems
- Riccardo Grazzi
- Korbinian Pöppel
- Jaisidh Singh
- Arber Zela
- Timur Carstensen
- Jenia Jitsev
- Frank Hutter
- Volkan Cevher
- Antonio Orvieto
affiliations:
- University of Freiburg
- Microsoft Research
- University of Tübingen
- MPI-IS Tübingen
- EPFL
arxiv_id: '2609.24797'
url: https://arxiv.org/abs/2609.24797
pdf_url: https://arxiv.org/pdf/2609.24797
published: '2026-09-21'
collected: '2026-09-22'
category: LLM
direction: 线性 RNN 表达能力增强
tags:
- Linear RNN
- Delta Rule
- Kimi Delta Attention
- Expressivity
- State Tracking
- Language Modeling
one_liner: 通过扩展门控与 delta 系数范围，提出 CKDA，在不增加秩或成本下实现 2D 旋转并达到 DeltaProduct2 的表达能力
practical_value: '- 对需要轻量序列建模的电商/广告场景（如用户行为序列、点击流预测），CKDA 提供了一种保持状态非膨胀的对角加秩一线性 RNN，计算开销低，可作为长序列用户建模的候选架构。

  - 参数范围扩展（门控 [-1,1]，beta [0,2]）简单且不增加推理成本，可以尝试在已有 KDA 或 delta-rule 模块中直接调整范围，观察对长尾序列或周期行为（如促销周期）的建模提升。

  - 文中证明 CKDA 可跟踪 SO(3) 子群，表明其具备更强的状态跟踪能力，适合需要精确维护内部状态的 Agent 或对话系统，可能减少层数或状态维度需求。

  - 注意：论文核心是基础架构创新，业务直接迁移价值有限，主要在需要高效长上下文处理且对表达能力有要求的场景（如用户长期兴趣演化）可考虑替换 Transformer
  层或作为轻量 backbone。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：基于 delta rule 的线性 RNN 虽然序列建模高效，但单次更新只能做低秩修正，表达能力受限。已有工作表明组合两个 delta-rule 转移能建模 2D 旋转，但会增加秩和更新成本。Kimi Delta Attention (KDA) 通过将单个 delta-rule 变换与通道门控提供的反射相结合，理论上可以突破该限制，但需扩展参数范围。

**方法关键点**：将 KDA 的门控取值范围从 [0,1] 扩展到 [-1,1]，delta rule 系数 β 从 [0,1] 扩展到 [0,2]，得到 Complex KDA (CKDA)。该扩展使得单次循环更新可实现 2D 旋转，同时保持转移矩阵为对角加秩一且非膨胀（non-expansive），维持稳定性和效率。理论证明每个正交对角加秩一矩阵都是 CKDA 转移矩阵，单层 CKDA 可跟踪所有同构于 SO(3) 子群的有限群，相比其他对角加秩一线性 RNN 在多个状态跟踪任务中少用一层。

**关键结果**：在 S3、S4 分组状态跟踪和周期音频延续任务上，综合两种扩展的 CKDA 在长度外推上表现最强。在语言建模中，CKDA 超越 Transformer 和其他线性 RNN，与 KDA 基线性能相近，并展现出良好的 scaling 行为。代码与模型已开源。
