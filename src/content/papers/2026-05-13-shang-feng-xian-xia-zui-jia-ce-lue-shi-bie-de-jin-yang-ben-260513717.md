---
title: Tight Sample Complexity Bounds for Entropic Best Policy Identification
title_zh: 熵风险下最佳策略识别的紧样本复杂度界
authors:
- Amer Essakine
- Claire Vernade
affiliations:
- ENS Paris Saclay
- University of Technology Nuremberg
arxiv_id: '2605.13717'
url: https://arxiv.org/abs/2605.13717
pdf_url: https://arxiv.org/pdf/2605.13717
published: '2026-05-13'
collected: '2026-05-17'
category: Other
direction: 风险敏感强化学习理论
tags:
- Risk-Sensitive RL
- Entropic Risk
- Sample Complexity
- Best Policy Identification
- Concentration Bounds
one_liner: 通过平滑性导出更紧集中界并设计新停时规则，匹配了熵风险RL策略识别的下界
practical_value: '- 对于需要控制尾部风险的应用（如金融、供应链），指数效用（entropic risk）可建模风险偏好，本工作的紧样本界能指导更高效的采样预算分配

  - KL-based 探索奖励（exploration bonus）的设计可迁移到其他需要乐观探索的场景，如在线推荐中冷启动策略的探索

  - 停止规则的紧致性思想可以启发推荐系统线上实验的早停机制，当收益差异的置信区间足够紧时提前终止实验

  - 整体上，业务直接应用有限，主要贡献在理论层面，但风险敏感视角在电商定价或广告出价中可能用于规避极端亏损'
score: 6
source: arxiv-stat.ML
depth: abstract
---

**动机**：风险敏感强化学习中，使用熵风险度量（entropic risk measure）的最佳策略识别问题存在样本复杂度上界与下界之间的指数级鸿沟：已知下界为 $\Omega(e^{|\beta| H})$，而上界仍为 $O(e^{2|\beta| H})$，差距达一个指数因子。本文追踪发现这是由于对指数效用函数的集中控制过于宽松所致，目标在于闭合这一间隙。

**方法**：提出基于前向模型的算法，在值迭代中构建 KL 散度形式的探索奖励（exploration bonus）。核心创新有两点：第一，利用指数效用函数的平滑性（Lipschitz 性质），为指数缩放后的收益推导出更紧的亚高斯型集中不等式，避免了先前工作直接套用 Hoeffding 不等式导致的额外指数膨胀；第二，设计新的自适应停止规则，在每一轮检验策略值估计的置信区间，一旦置信半径小于预设精度即终止采样，从而避免不必要的过量采样。

**结果**：理论分析证明，改进后的算法总样本复杂度达到 $\tilde{O}(e^{|\beta| H})$，匹配信息论下界，消除了指数级间隙。实验上也在简单环境中验证了较基线方法的样本效率提升。
