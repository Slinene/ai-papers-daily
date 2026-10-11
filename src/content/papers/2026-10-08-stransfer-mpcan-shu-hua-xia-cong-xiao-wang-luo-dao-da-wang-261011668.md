---
title: '$σ$Transfer: Uncertainty Transfer from Small to Large Networks under $μ\mathrm{P}$'
title_zh: σTransfer：μP参数化下从小网络到大网络迁移不确定性
authors:
- Richard Bergna
- Fernando Ruiz Mazo
- Nicolò Felicioni
- José Miguel Hernández-Lobato
- Kamil Ciosek
affiliations:
- University of Cambridge
- Spotify
arxiv_id: '2610.11668'
url: https://arxiv.org/abs/2610.11668
pdf_url: https://arxiv.org/pdf/2610.11668
published: '2026-10-08'
collected: '2026-10-11'
category: Training
direction: μP参数化 · Laplace不确定性迁移
tags:
- Uncertainty Estimation
- Laplace Approximation
- MuP
- Posterior Transfer
- Scale Transfer
- Bayesian Deep Learning
one_liner: 利用μP推导先验协方差缩放，使Laplace近似中的精度选择可零样本从小模型迁移到大模型
practical_value: '- **大模型不确定性评估省钱**：在LLM/Transformer上做Laplace近似或贝叶斯推断时，先用μP参数化，在小模型上sweep先验精度，再零样本迁移到大模型，避免大模型上昂贵的posterior
  sweep。工程上可直接降低OOD检测、主动学习、拒答决策所需的计算成本。

  - **μP参数化是迁移的基础**：若模型采用μP，先验协方差需按宽度缩放（论文中推导的重缩放），否则精度选择不随宽度稳定。迁移到业务模型时，需要同时采用μP初始化与对应缩放，不能只调精度。

  - **后验决策可跨尺寸复用**：论文验证了采集函数、OOD得分、拒答决策在后验稳定性下也能直接迁移，无需构造大模型后验。这对线上推荐/搜索系统里的不确定性相关模块（如置信度过滤、探索策略）有参考价值：可以只在小模型上调策略，再部署到大模型。

  - **适合模型升级场景**：当业务从1B模型升级到7B模型时，可复用已调好的先验精度，避免重新调参，加速约2.3～330倍（取决于任务），且NLL损失极小。'
score: 7
source: arxiv-stat.ML
depth: abstract
---

**动机**：Laplace近似中先验精度的选择对预测不确定性质量至关重要，但对数十亿参数的网络进行posterior sweep代价极高。

**方法关键点**：在Maximal Update Parametrization (μP)下，推导出先验协方差的重缩放形式，使选择的先验精度在模型宽度增长时保持稳定。由此提出σTransfer：在小模型上sweep选择先验精度，然后零样本直接迁移到大模型，完全无需在大模型上搜索精度。论文证明了先验核、后验协方差、所选精度以及后验衍生决策在显式条件下的收敛性。

**关键结果**：
- MNIST上从宽度128迁移到4096，精度扫描加速约5000倍，目标NLL仅退化0.002；
- 从公开1B模型迁移到7B模型，十项任务的中位数搜索加速约2.3倍（最高约330倍），平均目标NLL增加低于1e-4；
- 同样的后验稳定性还支持采集函数、OOD检测和拒答决策的直接迁移，无需构造目标后验。
