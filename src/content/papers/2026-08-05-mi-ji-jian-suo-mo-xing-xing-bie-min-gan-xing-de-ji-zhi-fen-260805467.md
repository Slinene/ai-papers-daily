---
title: A Mechanistic Analysis of Gender Sensitivity in Dense Retrieval Models
title_zh: 密集检索模型性别敏感性的机制分析
authors:
- Catherine Chen
- Maarten de Rijke
- Carsten Eickhoff
affiliations:
- Brown University
- University of Amsterdam
- University of Tübingen
arxiv_id: '2608.05467'
url: https://arxiv.org/abs/2608.05467
pdf_url: https://arxiv.org/pdf/2608.05467
published: '2026-08-05'
collected: '2026-08-08'
category: RecSys
direction: 密集检索偏见机制的因果分析
tags:
- gender bias
- mechanistic interpretability
- dense retrieval
- bi-encoder
- attention steering
- debiasing
one_liner: 揭示双编码器性别偏见源于输入嵌入并经少量后期注意力头传播，不同层级干预效果迥异
practical_value: '- **组件级拔除偏见方法**：借鉴论文的因果中介分析流程，对召回双塔模型的特定注意力头进行输出干预（加偏置向量），可定向抑制性别偏好而不伤及术语匹配信号，比全局嵌入调整更精细。

  - **生产环境公平性监控**：定期对双编码器组件的性别敏感度进行机制探测（如路径修补），识别偏见集中的注意力头，作为模型上线前的公平性检查点。

  - **解耦表征设计启示**：论文揭示性别与相关性信号在晚期层共享注意力头，提示在搜索推荐系统中，可尝试增加辅助任务头拉出性别无关分支，或在该层加入正交化损失，减少信号纠缠。

  - **干预层次选择**：嵌入层干预虽可中和分数差异，但非特异性地影响所有输出；注意力级干预能实现方向性偏移，类似少量样本针对性调整，更适合需要对特定查询类型（如无性别倾向的通用查询）去偏的场景。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：密集检索模型普遍存在性别偏见——对带有男性表述的文档打分更高，但偏见在模型内部的产生与传播机制尚不清晰，现有去偏方法缺乏组件级理解。

**方法关键点**：
- 以双编码器为对象，使用因果中介分析定位性别敏感性。
- 发现偏见信号起源于输入嵌入层，随后传入少数后期层的注意力头，这些头同时编码性别信息和术语匹配信号。
- 在识别的两个关键点进行干预实验：① 对输入嵌入施加性别方向修正；② 对特定注意力头的输出添加偏置向量。

**关键结果**：
- 嵌入级干预可非特异性地消除男女文档得分差异，但会同时影响无关内容。
- 注意力头级干预能按需产生定向偏移（如提升女性文档分数或降低男性文档分数），且对不包含性别信息的查询影响很小。
- 证明了性别信号与相关性信号在模型组件中高度纠缠，为去偏带来挑战。
