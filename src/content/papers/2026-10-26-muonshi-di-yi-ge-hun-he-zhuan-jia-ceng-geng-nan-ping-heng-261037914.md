---
title: Muon Makes the First Mixture-of-Experts Layer Harder to Balance
title_zh: Muon使第一个混合专家层更难平衡
authors:
- Marcos Hernanz
affiliations:
- Escuela Politécnica Superior, Universidad Autónoma de Madrid
arxiv_id: '2610.37914'
url: https://arxiv.org/abs/2610.37914
pdf_url: https://arxiv.org/pdf/2610.37914
published: '2026-10-26'
collected: '2026-11-05'
category: Training
direction: MoE训练优化器与负载均衡
tags:
- MoE
- Muon
- Load Balancing
- Optimizer
- Router
one_liner: Muon优化器使首个MoE层负载均衡更难，输入共享方向导致bias span翻倍，减均值或降lr可缓解
practical_value: '- 业务中若用MoE（如多专家推荐模型、LLM推理加速），采用Muon训练时需监控各层路由bias span，尤其第一层；对router输入做batch
  mean subtraction可消除过载且几乎不损失精度。

  - 第一层专家过载时，优先降低Muon学习率而非更换router优化器；本研究中减半lr在小模型上略改善loss。

  - 可解耦router与backbone优化器分析，发现backbone优化器对负载均衡影响更大；实际调参时可为不同部件独立设置优化器超参。

  - 注意结论基于55M/108M小模型，迁移到大规模生产需验证；但共享方向导致负载不均的现象可类比到query routing等多专家场景。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：开源MoE语言模型普遍用Muon替代AdamW，但各recipe中对router是否也用Muon不一致。负载均衡依赖每步调整的routing score bias，优化器如何影响这些bias的span尚不清楚。

方法：在55M和108M活跃参数模型上训练，以bias span（层内最大减最小）衡量负载均衡难度；对比Muon与AdamW，解耦router与backbone优化器；分析第一层router输入的方向性。

关键结果：在短运行调好的学习率下，Muon使第一个MoE层的span在每种子上都增加，平均约翻倍，其他层变化小；该效应来自backbone用Muon，与router优化器无关。第一层router输入共享一个方向，warmup后不久最忙专家平均获得4-7倍公平份额。前3000步从输入减去batch mean可消除过载且损失几乎不变；小模型上Muon学习率减半可消除大部分现象并略改善loss；仅将router改为AdamW使warmup期间负载偏移更大且loss略升，因此该规模下建议router保持Muon。
