---
title: 'Abstention and Noise Filtering: Two Missing Primitives of Softmax Attention'
title_zh: 弃权与噪声过滤：Softmax 注意力的两个缺失原语
authors:
- Richard Zhe Wang
affiliations:
- St. John Fisher University
arxiv_id: '2609.22005'
url: https://arxiv.org/abs/2609.22005
pdf_url: https://arxiv.org/pdf/2609.22005
published: '2026-09-18'
collected: '2026-09-21'
category: Training
direction: 注意力机制原语 · 模型训练改进
tags:
- attention
- gating
- abstention
- noise filtering
- pretraining
one_liner: 显式加入弃权(sink logit)与值门控噪声过滤，两者结合在10M-350M匹配模型中均优于softmax基线
practical_value: '- 若在电商搜索/推荐中自研或微调 Transformer 排序模型（如 LLM4Rec、行为序列建模），可直接在 attention
  中加入 per-head sink logit 实现 abstention，几乎零参数且兼容 KV cache，适合长序列中忽略无关历史行为。

  - 在用户行为序列包含大量噪声（点击噪声、误触、跨域行为）时，对 value 侧加可学习 gate 过滤 residual stream 中的叠加特征干扰；模型规模越大，该噪声过滤收益越明显，10M→350M
  趋势提示大规模 CTR/CVR 模型优先考虑 value gating。

  - 两种原语有互补盲区，建议同时加入而非只选一种；在 Agent 多步推理或 RAG 检索上下文拼接时，attention 可能被迫把注意力质量分配给无关 token，sink
  logit 可以让头显式弃权，减少错误信息聚合。

  - 若用 LoRA 微调已有 LLM 推荐/Agent 模型，这些改动不增加缓存开销，可作为结构正则化 trick 加在 attention 子层，注意 warmup
  和初始门控设置。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：标准 softmax 注意力有两个结构性缺失：注意力权重必须求和为 1，导致 head 无法“什么都不输出”，只能把质量堆到某个位置（通常首 token）；value pathway 端到端线性，无法抑制 residual stream 中叠加特征的干扰。已有工作用 value pathway gating 改善 LLM pretraining，但原因有争议。

**方法关键点**：作者显式提供两种原语：abstention 通过 softmax 中每个 head 学习一个 sink logit，允许注意力质量被丢弃；noise filtering 通过每个 value 上设置可学习 gate，抑制无关/干扰信号。在 10M 到 350M 参数匹配模型上对比。

**关键结果数字**：abstention 收益随规模下降，10M 时几乎占 gating 全部收益，350M 时 filtering 占主导；每个规模最佳模型都同时包含两种原语；注入受控干扰实验证明 gate 能移除干扰，且两种 gate 形式各有盲区；参数增加可忽略，兼容 KV cache。
