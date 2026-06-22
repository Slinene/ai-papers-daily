---
title: Zero-Shot Active Feature Acquisition via LLM-Elicitation
title_zh: 基于LLM引导的零样本主动特征获取
authors:
- Binyamin Perets
- Natalie Mendelson
- Shiran Vainberg
- Yehuda Chowers
- Shai Shen-Orr
- Shie Mannor
affiliations:
- Technion
- CytoReason
- NVIDIA
arxiv_id: '2606.18933'
url: https://arxiv.org/abs/2606.18933
pdf_url: https://arxiv.org/pdf/2606.18933
published: '2026-06-17'
collected: '2026-06-22'
category: Other
direction: LLM-引导的零样本主动特征获取
tags:
- Active Feature Acquisition
- LLM
- Markov Random Field
- Maximum Entropy
- Zero-shot
- Decision Making
one_liner: 仅从LLM获取判别性统计量，用最大熵闭合构建MRF，实现零样本主动特征获取，性能超越LLM直接决策
practical_value: '- **交互式推荐冷启动**：利用LLM提取用户/物品特征之间的判别性共变关系构建MRF，指导对话式推荐中下一个最优问题的选择，零样本适配新领域。

  - **最大熵闭合技巧**：当LLM只返回类间区分信息而忽略类内分布时，可通过最大熵原则补全缺失统计量，使概率模型可用于规划，解决LLM输出偏差。

  - **规划与知识分离架构**：不让LLM直接做序列决策，而是仅提供特征依赖的统计量，再用MRF进行精确推理，规避LLM规划不可靠的问题，可复用于Agent主动信息获取任务。

  - **预算受限下的top-k识别**：在电商搜索或推荐中，需从大量候选中快速锁定少量目标时，可借鉴top-k主动特征获取策略，动态选择最具区分力的特征询问用户，降低交互成本。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：主动特征获取（AFA）依赖大量标注数据训练概率模型，难以零样本迁移。LLM拥有无监督领域知识，但直接用于序列规划表现不佳。如何将LLM的知识安全地注入AFA，避免其规划弱点？

**方法关键点**：提出受规约的启发框架：仅向LLM索取它能可靠返回的信息——特征的一元偏差和成对共变，即马尔可夫随机场（MRF）的充分统计量。实际中LLM倾向于返回判别性统计量（区分不同类别的差异），而非每个类别内的完整分布，导致经典AFA无法直接使用。作者通过**最大熵闭包**解决这一规范歧义：基于已获取的判别性信息，在满足约束的条件下构造熵最大的概率分布，补全类内缺失统计量，形成完整的MRF。用此MRF指导下一步的特征选择，实现了零样本AFA。框架同时支持二分类和top-k识别两种设定。

**关键结果**：在炎症性肠病（IBD）患者诊断数据集上，该方法在真实标签和LLM自身信念上均优于LLM直接决策；尤其在困难病例上，top-k获取策略显著超越所有对比方法，证明了分离知识提供与规划决策的有效性。
