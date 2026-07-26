---
title: 'Beyond Sufficiency: Time Series Explanation with Counterfactual Necessity'
title_zh: 超越充分性：基于反事实必要性的时间序列解释框架
authors:
- Hongnan Ma
- Yiwei Shi
- Mengyue Yang
- Weiru Liu
affiliations:
- University of Bristol
arxiv_id: '2607.21573'
url: https://arxiv.org/abs/2607.21573
pdf_url: https://arxiv.org/pdf/2607.21573
published: '2026-07-23'
collected: '2026-07-26'
category: Other
direction: 时间序列解释 · 反事实必要性
tags:
- Time Series
- Explanation
- Counterfactual
- Necessity
- Causal
- Interpretability
one_liner: 提出 TimePNS，利用反事实干预量化时间序列解释的必要性，过滤虚假子序列，提升解释保真度
practical_value: '- 针对用户行为序列推荐模型的可解释性，可借鉴两步设计：先学习充分性掩码，再利用反事实干预剔除噪音行为，识别真正驱动推荐的关键交互。

  - 在广告点击序列归因中，用必要性信号替代纯充分性打分，有助于排除偶然关联的曝光，提升关键触点的定位精度。

  - 整体框架与推荐场景差异较大，直接迁移成本高，更适合作为序列解释的理论参考。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：现有时间序列解释方法主要追求充分性——找出能独立保持分类器预测的子序列，但这类方法容易将虚假相关但非因果必要的片段赋予高重要性。为此，论文引入 Pearl 的反事实必要性概念，定义真正必要的时序因子为：若对其干预，原预测会被破坏。

**方法**：提出 **TimePNS** 两阶段框架。Stage I 基于可识别的因果生成过程学习一个充分性导向的解释掩码，同时建模时序变量的潜在因果因子。Stage II 对潜在因子实施反事实干预，通过比较干预前后预测的变化生成必要性信号，进而训练一个时序门控，抑制非必要成分、放大反事实必要的子序列，得到精炼解释。

**结果**：在合成数据和多个真实世界时间序列基准上，TimePNS 相比强基线（如 Dynamask、Extrmask）更准确地识别决策关键子序列，在充分性-必要性权衡指标上取得一致提升，验证了必要性信号对过滤虚假解释的有效性。
