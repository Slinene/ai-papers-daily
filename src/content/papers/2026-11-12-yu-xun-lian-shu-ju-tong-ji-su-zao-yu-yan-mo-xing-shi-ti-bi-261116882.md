---
title: Pretraining Data Statistics Shape the Phases of Learning Entity Comparison
  in Language Models
title_zh: 预训练数据统计塑造语言模型实体比较学习三阶段
authors:
- Yik Siu Chan
- Jing Huang
- Yanai Elazar
- Atticus Geiger
affiliations:
- University of Maryland
- Pr(Ai)2R Group
- Stanford University
- Bar-Ilan University
- Goodfire
arxiv_id: '2611.16882'
url: https://arxiv.org/abs/2611.16882
pdf_url: https://arxiv.org/pdf/2611.16882
published: '2026-11-12'
collected: '2026-11-13'
category: Training
direction: LM 训练动态与数据统计归因
tags:
- pretraining dynamics
- entity comparison
- data statistics
- heuristics
- scaling prediction
- interpretability
one_liner: LM 学实体比较会经历频率启发式、位置启发式、正确作答三阶段，且由预训练数据统计决定
practical_value: '- LLM 做商品/实体比较问答时，训练数据中的实体频次长尾会让模型先依赖“高频实体”而非事实；可通过 uniform 化或过采样长尾实体、加大任务数据量来跳过或削弱频率启发式。

  - 任务数据不足时，模型会退化到选择 prompt 中第一/最后出现的实体。评估 LLM 比较类能力时应做答案位置置换和 prompt 对称化，避免位置偏差冒充正确率。

  - 小规模 163M 合成数据实验能复现大模型 OLMo-2 32B 的训练动态，可作为低成本探针：在业务里先跑小模型数据配比实验，预判大模型需要多少任务数据才能从启发式跳到正确推理。

  - 对生成式推荐中的属性比较、卖点排序等场景，应显式构造比较对正负样本并监控训练阶段曲线；若模型卡在频率/位置阶段，优先调整数据分布和样本量，而不是只加参数或指令。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

动机：预训练数据如何驱动 LM 行为变化？用实体比较任务作为案例，研究数据统计对学习阶段的影响。

方法：训练 163M 小模型，混合自然文本与合成任务数据，覆盖九类比较任务、五类实体；改变实体频率分布（Zipfian 与 uniform）和任务数据量；并在 OLMo-2 32B 上验证。

关键结果：学习过程出现三个阶段：早期按实体频率选择，中期按 prompt 位置选择（第一/最后），晚期才正确作答。任务数据少时只出现前两阶段，模型无法学会任务；数据量足够时从频率阶段直接跳到正确阶段。把实体频率从 Zipfian 改为 uniform 会削弱频率阶段并加速学会。三阶段动态在 OLMo-2 32B 中同样出现，说明小规模合成实验可预测大尺度训练动态。
