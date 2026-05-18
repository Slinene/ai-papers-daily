---
title: A Mutual Information Lower Bound for Multimodal Regression Active Learning
title_zh: 多模态回归主动学习的互信息下界采集函数
authors:
- Leonardo Ferreira Guilhoto
- Akshat Kaushal
- Paris Perdikaris
affiliations:
- University of Pennsylvania
arxiv_id: '2605.14917'
url: https://arxiv.org/abs/2605.14917
pdf_url: https://arxiv.org/pdf/2605.14917
published: '2026-05-14'
collected: '2026-05-18'
category: Other
direction: 主动学习采集函数 · 不确定性分解
tags:
- mutual information
- active learning
- regression
- epistemic uncertainty
- mixture density network
- lower bound
one_liner: 提出 MI-LB，分离认知与偶然不确定性，为多模态回归主动学习提供闭式互信息下界
practical_value: '- 电商推荐中用户行为常呈多模态（如“浏览/购买/忽视”），采用**混合密度网络(MDN)**建模预测分布，代替单高斯输出，可更真实地捕捉不确定性。

  - 主动选择标注样本时，用**MI-LB作为采集函数**，能可靠区分模型可减少的认知不确定性，优于方差或熵，特别适用于冷启动或在线学习场景。

  - MI-LB对MDN集成提供**闭式下界近似**，工程实现直接，无需采样或数值积分，适合大规模推荐系统实时决策。

  - 框架中的Two-Index分解思路可迁移至多臂老虎机或强化学习的探索：将认知指数作为抽象动作，驱动更高效的探索策略。'
score: 6
source: arxiv-stat.ML
depth: abstract
---

**动机**：连续回归的主动学习在面对多模态预测分布时，现有采集函数（如方差、BALD）无能为力——方差无法捕捉模态间分歧，BALD仅适用于离散输出。实际系统中（如物理模型、用户行为预测）多模态普遍存在，急需能分离认知不确定性的原则性目标。

**方法**：提出Two-Index框架，引入两个随机指标：一个选择模型假设（认知源），另一个控制假设内随机性（偶然源）。基于此分解，证明输出与认知指标之间的互信息正是可被数据消减的认知不确定性，并随数据量增加而趋于零。对连续输出，该互信息难以直接计算，作者针对混合密度网络（MDN）集成，推导出**互信息下界（MI-LB）**，得到一个闭式表达式，仅依赖MDN的输出参数，计算轻量。

**结果**：在多模态回归基准上，MI-LB匹配或优于所有基线（包括基于几何、Fisher信息的方法），且是唯一在所有条件下表现一致的方法。传统基线仅在输入空间已编码多模态信息时才有效，否则完全失效，验证了MI-LB的鲁棒性和理论基础。
