---
title: 'When Attention Goes Blind: Numerical Failure in ALiBi Positional Encodings'
title_zh: ALiBi 位置编码的浮点下溢失明问题与缓解策略
authors:
- Christopher Schröder
- Lukas Gienapp
- Ferdinand Schlatt
- Martin Potthast
- Gerhard Heyer
affiliations:
- Leipzig University (InfAI)
- ScaDS.AI Dresden/Leipzig
- Seltz
- University of Kassel
- hessian.AI
arxiv_id: '2608.03994'
url: https://arxiv.org/abs/2608.03994
pdf_url: https://arxiv.org/pdf/2608.03994
published: '2026-08-03'
collected: '2026-08-06'
category: Training
direction: ALiBi 位置编码数值缺陷分析与缓解
tags:
- ALiBi
- positional encoding
- floating-point underflow
- attention
- passkey retrieval
- LLM training
one_liner: 发现 ALiBi 的线性偏置在长距离下因浮点下溢导致注意力权重为零，提出 log 缩放距离等缓解方法
practical_value: '- 若在电商搜索推荐等场景使用基于 ALiBi 的 decoder-only LLM（如生成 query、长用户序列建模），需注意长距离
  token 的注意力权重可能因浮点下溢变为零，导致头部“失明”，影响长文本检索能力。可通过监控 attention underflow 比例来诊断。

  - 训练时可改用 log-scaled distances 作为位置偏置，该方法在 passkey retrieval 任务中表现最稳定，能显著缓解下溢；也可结合
  clamping 或混合偏置。

  - 评估长上下文模型时，不能仅看常规困惑度或标准基准，需加入 needle-in-a-haystack 类 token 检索任务，避免 ALiBi 的隐性缺陷影响线上长序列性能。

  - 若必须沿用默认 ALiBi 斜率，应意识到其作为强基线在 needle-in-a-haystack 任务上仍有竞争力，但需权衡训练稳定性与检索能力损失。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：ALiBi 通过线性偏置注入位置信息，支持训练长度外推，但其偏置随距离线性增长，在长上下文（如 10000 token 距离）时 bf16 精度下发生下溢，使注意力权重直接归零，导致受影响头“失明”。现有预训练模型（如基于 ALiBi 的 LLaMA 变体）已观察到该现象。

**方法**：分析下溢比例与头盲规律，提出四种训练期缓解策略：(1) log-scaled distances，(2) clamping bias，(3) 混合斜率，(4) 学习缩放因子。在 148M 参数 decoder 模型上预训练并评估标准困惑度、passkey retrieval 和 needle-in-a-haystack 任务。

**关键结果**：ALiBi 失效对标准语言建模基准影响较小，但严重损害 token 精准检索任务（passkey 准确率大幅下降）；log-scaled distances 在 passkey retrieval 上带来最一致的提升；默认 ALiBi 斜率在 needle-in-a-haystack 检索中仍是强基线；推荐根据实际任务选择缓解策略，并强调了长文本评估需包含检索类测试。
