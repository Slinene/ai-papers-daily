---
title: 'Everything in Moderation: Per-Domain Coverage Optima and Alignment-Resistant
  Domain Gaps in Multi-Domain Mid-Training'
title_zh: 多域中期训练中每域覆盖最优与对齐抗性域差距
authors:
- Yunpeng Xu
- Kun Zheng
arxiv_id: '2609.09081'
url: https://arxiv.org/abs/2609.09081
pdf_url: https://arxiv.org/pdf/2609.09081
published: '2026-09-08'
collected: '2026-09-09'
category: Training
direction: 训练数据配比与领域覆盖优化
tags:
- mid-training
- data mixing
- domain coverage
- alignment
- LLM
- controlled experiment
one_liner: 证明各域覆盖率存在内部最优区间，且中期训练的域差距难以被后续SFT修复
practical_value: '- **多域/多任务数据配比存在非单调最优**：业务中的多域推荐或LLM微调，不应简单按数据量加权或追求某域越多越好，10%–40%的覆盖率区间普遍较优，可用小规模单形扫描实验（simplex
  sweep）确定各域峰值位置。

  - **中期训练的数据构成难以靠后续SFT弥补**：如果业务系统分阶段训练基础模型和任务模型，早期数据配比造成的领域差距不会在对齐阶段自动消失，必须把数据混合策略前移到中期训练阶段。

  - **零覆盖的代价与通用漂移混淆**：完全放弃某域会导致该域能力崩溃，但需要设置通用数据控制组（如FineWeb-Edu-only）区分是域缺失还是通用分布漂移，避免误判。

  - **探索性θ*配比思路可复用到推荐模型训练**：在多个候选数据配比中做端到端全流程评估，选择全流程增益最大的配比，即使单域统计不显著，也可能带来整体提升。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：中期训练（mid-training）是预训练与对齐之间的关键阶段，但各域数据覆盖率通常由数据可得性决定，缺乏原则性设计。论文检验该决策是否重要，以及后续对齐阶段能否修复覆盖率带来的差距。

**方法关键点**：在受控逻辑推理环境下（Qwen3-8B-Base 主模型，4B 复现；5个语义规则不相交的 KOR-Bench 域），训练30种覆盖分配（24个扫描配置+6个留出，各5个种子），覆盖五域单形；随后加入固定预算的对齐（SFT）观察差距能否被补偿。

**关键结果**：①每个域都存在内部覆盖最优区间，10%–40%覆盖率对所有5个域效果最佳，拟合的中期训练曲线峰值在9.9%–35.1%之间（校准排列检验 P≈0.010）。②这些域差距在对齐后依然存在：补偿性SFT平均提升116/120个单元（+4.32pp），但在5pp阈值下未能桥接任何配对（0/240），10%比率下仅桥接30/240，远低于排列零假设预期（13.8±3.3 和 77.9±8.5，P<0.001），且等预算均匀控制表现几乎相同。③零覆盖率导致中期训练准确率崩溃，但该崩溃与通用分布漂移混杂；探索性θ*配比获得最大全流程增益（+4.36pp vs +0.80/+0.64pp），但Welch检验下边际显著。
