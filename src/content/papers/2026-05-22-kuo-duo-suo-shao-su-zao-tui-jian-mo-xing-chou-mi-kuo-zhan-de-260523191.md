---
title: 'Expand More, Shrink Less: Shaping Effective-Rank Dynamics for Dense Scaling
  in Recommendation'
title_zh: 扩多缩少：塑造推荐模型稠密扩展的有效秩动态
authors:
- Guoming Li
- Shangyu Zhang
- Junwei Pan
- Wentao Ning
- Jin Chen
- Gengsheng Xue
- Chao Zhou
- Shudong Huang
- Haijie Gu
- Menglin Yang
affiliations:
- The Hong Kong University of Science and Technology (Guangzhou)
- Tencent Inc.
arxiv_id: '2605.23191'
url: https://arxiv.org/abs/2605.23191
pdf_url: https://arxiv.org/pdf/2605.23191
published: '2026-05-22'
collected: '2026-05-25'
category: RecSys
direction: 深度推荐模型缩放 · 有效秩动态调控
tags:
- Embedding Collapse
- Effective Rank
- RankElastor
- Dense Scaling
- CTR Prediction
one_liner: 通过参数化全混合与GLU-PFFN缓解RankMixer嵌入坍塌，提升稠密扩展性能
practical_value: '- **替换 RankMixer 的 token mixing**：将固定的块转置换操作改为可学习的 `Parameterized
  Full Mixing`（对 flatten 后的 token 向量做稠密线性变换加残差），能显著提升有效秩与交互细粒度，在电商推荐中可直接迁移。

  - **GLU 风格 P-FFN 防坍缩**：用 `GLU`（门控线性单元）替代原 GELU 型 P-FFN，即 `(GELU(MW1) ⊙ (MW2))W3
  + M Wr`，统计上可抑制有效秩收缩，实现“收缩少”。

  - **两个模块协同使用**：实验表明两者互补，单独使用增益有限，同时替换才能获得最大性能提升，是工程改造的可靠方案。

  - **有效秩监控诊断**：跟踪各层有效秩分布，可快速发现嵌入坍塌风险，指导模型架构调整。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
深度推荐模型（如 RankMixer）通过 token 混合与逐 token FFN 交替堆叠实现参数扩展，但存在嵌入坍塌（embedding collapse）问题——表示矩阵有效秩随层数振荡衰减，限制了扩展收益。本文从有效秩角度诊断：RankMixer 的块转置混合仅带来有限秩增长，而 GELU 型 P-FFN 会快速压缩秩，二者导致“阻尼振荡”轨迹，无法根本防止坍塌。为此，提出 **“扩多缩少”** 原则，设计 RankElastor。

**方法关键点**  
- **Parameterized Full Mixing**：将固定置换的块转置替换为可学习的稠密矩阵 W（加残差），在展平后的 token 向量（TD 维）上做全坐标交互，突破了原 Kronecker 约束，理论上有更高的秩扩展下界。  
- **GLU-improved P-FFN**：采用门控线性单元结构，输出 = (GELU(MW₁) ⊙ (MW₂)) W₃ + M W_r，利用 Hadamard 乘积引入度‑2 交互，结合残差，统计上能恢复甚至提升有效秩，缓解传统 FFN 的坍缩效应。  
- 两个模块联合使用时，一方面扩大秩（mixing），一方面保持秩（FFN），形成谱鲁棒的表示演化。

**关键实验与数字**  
- **数据集**：Criteo、Avazu 工业级 CTR 基准。  
- **基线**：MLP、xDeepFM、DCNv2、AutoInt、RankMixer。  
- **性能**：RankElastor 在 Criteo 上 AUC 达 0.81482（较 RankMixer 提升 +0.001），Avazu 上 AUC 0.79323（+0.00053），LogLoss 同步降低。  
- **秩动态**：有效秩分布图显示，RankElastor 的 mixing 层带来更强扩张，FFN 层收缩明显更弱；在 Avazu 上 RankMixer 出现坍塌，而 RankElastor 保持稳定增长。  
- **消融**：去掉全混合或退化为 GELU-FFN 均导致性能下降，二者同时使用有协同增益。  
- **扩展性**：在宽度、深度及联合扩展下，RankElastor 的 AUC 提升持续领先 RankMixer，且无性能退化，证明更强的尺度定律。  
- **行为序列建模泛化**：在 KuaiVideo 和 TaobaoAd 数据集上依然最优。

**关键结论**  
RankElastor 通过“参数化全混合 + GLU 风格 P-FFN”实现了更优的谱动态，指导推荐模型在增大参数时避免表示坍塌，是面向工业推荐系统稠密扩展的有效范式。
