---
title: Are Concept Bottleneck Models Effective as Decision-Support Systems?
title_zh: 概念瓶颈模型作为决策支持系统真的有效吗？
authors:
- Alessandro Bogani
- Nicola Debole
- Emanuele Marconato
- Andrea Pugnana
- Katya Tentori
- Andrea Passerini
affiliations:
- DISI, University of Trento, Italy
- CIMeC, University of Trento, Italy
arxiv_id: '2608.25581'
url: https://arxiv.org/abs/2608.25581
pdf_url: https://arxiv.org/pdf/2608.25581
published: '2026-08-26'
collected: '2026-08-30'
category: Other
direction: 可解释AI · 人机协同决策
tags:
- Concept Bottleneck Models
- Human-AI Collaboration
- Interpretability
- User Study
- Decision Support
one_liner: 大规模用户研究验证CBM交互式概念修正仅在困难任务、易识别概念且主动交互下提升人机协同准确率
practical_value: '- 把推荐/广告模型的中间表征改造成“可编辑概念层”：先预测一组业务可理解概念（如价格敏感、类目偏好、即时意图），再由下游策略/模型输出最终排序或文案；产品运营可纠正概念而无需懂特征，CBM
  的用户研究表明这种交互式修正比仅展示解释更能提升人机协同准确率。

  - 交互式概念修正不是万金油：论文发现增益只在任务被用户认为困难、概念容易识别且用户主动交互时出现。在电商场景，可优先用于高价值、高不确定性的推荐/投放决策（如大促选品、push
  文案筛选），而不是所有流量都开放人工干预。

  - 概念检测的准确性会直接影响信任：如果模型经常识别错概念，用户反而会不信任系统。部署前应评测概念层准确率、对齐业务术语，必要时展示置信度或“不确定”状态，避免误导运营。

  - 对 LLM/Agent 方案，可将“reasoning/解释”视作 concept bottleneck：让 Agent 先输出可校验的中间意图或证据标签，再生成推荐/Query；同时提供人工修正这些标签的入口，借鉴该研究的用户实验设计做
  A/B 验证。'
score: 6
source: arxiv-cs.HC
depth: abstract
---

动机：CBM 因可解释、可干预被广泛用于人机协作，但实际作为决策支持系统是否有效缺乏大规模用户证据。

方法：两项用户研究，共 705 人、6,959 次观测，覆盖两个二分类任务；比较“纯人类”“非可解释 AI 支持”“CBM 解释”“CBM 解释+交互修正”下的人机团队准确率，并考察任务难度、概念可识别性、交互程度等条件。

关键结果：
- CBM 尤其交互式概念修正，相较纯人类和非可解释 AI 支持能提升人机团队准确率；
- 收益有条件：任务被感知为困难、概念容易识别、用户主动交互时才会显著出现；
- 概念检测不准会损害用户信任，可能抵消解释带来的正向效果。
