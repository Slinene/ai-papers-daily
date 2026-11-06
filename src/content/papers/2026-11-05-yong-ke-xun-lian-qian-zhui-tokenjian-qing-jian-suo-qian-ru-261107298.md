---
title: Reducing Representational Interference in Retrieval Embeddings with Trainable
  Prefix Tokens
title_zh: 用可训练前缀Token减轻检索嵌入中的表征干扰
authors:
- Seongtae Hong
- Youngjoon Jang
- Jungseob Lee
- Chanjun Park
- Heuiseok Lim
affiliations:
- Korea University
- Soongsil University
arxiv_id: '2611.07298'
url: https://arxiv.org/abs/2611.07298
pdf_url: https://arxiv.org/pdf/2611.07298
published: '2026-11-05'
collected: '2026-11-06'
category: Training
direction: 可训练[DUMP] token优化检索嵌入
tags:
- trainable prefix tokens
- retrieval embeddings
- attention sink
- contrastive learning
- dense retrieval
one_liner: 在输入前添加可训练[DUMP] token，以对比学习目标训练，降低低信息token干扰、提升检索嵌入质量
practical_value: '- 在训练双塔召回或向量检索模型时，可在输入序列前添加几个可学习的前缀 token（如 [DUMP]）作为“信息垃圾桶”，吸收无信息
  token 的干扰，无需改动模型架构、pooling 和 loss，即插即用。

  - 适用于长文本或含大量噪音 token 的场景（如商品描述、用户评论、会话历史），能降低低信息片段对最终 item/query 向量的影响，提升召回相关性。

  - 对于 decoder-only 的 LLM-based retriever，该技巧可缓解 attention sink 带来的表示污染，提升嵌入质量，适合直接套用在现有生成式检索或向量召回流程的微调阶段。

  - 实现成本极低：只增加少量可训练 embedding 参数，训练目标保持对比学习，可作为 baseline 的轻量增强手段，快速验证收益。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：嵌入模型将变长文本压缩为固定向量，但压缩过程可能混杂语义内容与残余的 token 级信息（如 attention sink 行为产生的伪影），导致检索表示受到低信息 token 的干扰。

**方法关键点**：在输入序列前添加可训练的 [DUMP] token，保持模型架构、pooling 策略和训练损失完全不变，仅通过标准对比检索目标优化这些新增 token。训练时 [DUMP] token 与普通 token 交互，从而吸收或抑制无信息 token 对最终表示的贡献。该方法适用于 encoder 和 decoder 两类嵌入模型，无需改变推理流程。

**关键结果**：在标准检索和长上下文基准上，该方法相比微调基线取得一致提升，跨多种模型架构均有效；进一步分析表明 [DUMP] token 改变了与低信息 token 相关的激活和注意力模式，验证了其降低表征干扰的机制。
