---
title: 'T^2MLR: Transformer with Temporal Middle-Layer Recurrence'
title_zh: T2MLR：带时序中层循环的 Transformer
authors:
- Ziyang Cai
- Xingyu Zhu
- Yihe Dong
- Yinghui He
- Sanjeev Arora
affiliations:
- Princeton University
- Princeton Language and Intelligence
arxiv_id: '2607.15178'
url: https://arxiv.org/abs/2607.15178
pdf_url: https://arxiv.org/pdf/2607.15178
published: '2026-07-16'
collected: '2026-07-18'
category: Reasoning
direction: 中层时序循环增强Transformer隐式推理
tags:
- Latent Reasoning
- Middle-Layer Recurrence
- Transformer Architecture
- Multi-hop Reasoning
- Inference Efficiency
one_liner: 在Transformer中层引入跨时间步的隐状态循环，缓解自回归信息瓶颈，提升推理性能
practical_value: '- 可将中层循环引入现有LLM，通过微调提升多步推理任务性能，无需重新预训练，适合在已有Agent系统中以低成本增强模型推理能力。

  - 局部循环设计（仅对20%的中间层做递归）既有效又轻量，可作为工程优化思路：在微调大模型时只改装关键的中间层块，减少额外计算开销。

  - 隐状态跨步传递的机制可借鉴到需要跨轮次保持中间运算状态的应用，如对话Agent的长期上下文理解、多轮谈判策略规划等。

  - 实验表明，改装1.7B模型并微调即可大幅提升数学推理，该方法也可尝试用于电商搜索中的复杂意图解析或多条件过滤推理。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：自回归解码将每步丰富的隐层表示压缩为离散token，造成信息瓶颈，使中间推理状态难以跨时间步持续。T2MLR旨在通过隐状态循环打破此限制。

**方法**：在Transformer中引入时序中层循环路径——将上一步某中间层的输出缓存，并直接注入当前步的某一较早层，实现抽象中间计算跨步传递。该循环可仅作用于局部中间层块（如20%的层），参数和计算开销极低。

**关键结果**：
- 在自然语言预训练与多跳推理微调上，数据量和参数量匹配时，T2MLR consistently优于Transformer基线。
- 仅对局部中层块应用循环（小至20%网络）常优于全层循环，表明“中层”是关键。
- 将循环通路改装进已有1.7B预训练Transformer并短暂微调，数学推理准确率大幅提升，无需从头预训练。
