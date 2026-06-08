---
title: Gated Bidirectional Linear Attention for Generative Retrieval
title_zh: 用于生成式检索的门控双向线性注意力
authors:
- Artem Matveev
- Vladislav Tytskiy
- Sergei Makeev
- Sergei Liamaev
affiliations:
- Yandex
arxiv_id: '2606.07317'
url: https://arxiv.org/abs/2606.07317
pdf_url: https://arxiv.org/pdf/2606.07317
published: '2026-06-05'
collected: '2026-06-08'
category: GenRec
direction: 生成式推荐 · 线性注意力
tags:
- Generative Retrieval
- Linear Attention
- Bidirectional Attention
- Hybrid Encoder
- Long Sequence
- Efficiency
one_liner: 提出GBLA混合编码器，以1:2交错自注意力与线性注意力，在长序列生成式检索中匹配双向自注意力质量，推理加速最高8.2倍
practical_value: '- **混合编码器是工程落地的优选策略**：在生成式推荐编码器中，以[SA, LA, LA]模式（1个标准自注意力层 + 2个线性注意力层）替换全自注意力，能在几乎不损失召回率的同时大幅降低长序列下的延迟，适合历史行为序列极长的电商或流媒体场景。

  - **GBLA的三个轻量组件可以直接复用**：针对线性注意力添加上下文卷积（Conv1D）、Key门控（soft forgetting）和RMSNorm门控输出，每个组件带来约0.5-1个点的Recall提升，实现成本低，可在自研模型里快速实验。

  - **双向注意力对编码器至关重要**：实验表明编码器用双向掩码比因果掩码在Recall@10上绝对高出9个百分点以上，设计生成式推荐编码器时应坚决保留双向上下文。

  - **长序列推理加速的临界点**：在H100上，序列长度超过4096时线性注意力开始反超FlashAttention-v3，到32K时加速8.2倍；这提示在用户序列长度上万级别时，线性注意力是延迟瓶颈的有效解法。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：在生成式推荐中，编码器-解码器架构通常让编码器处理用户长交互历史，标准的双向自注意力复杂度随序列长度平方增长，成为线上推理的瓶颈。已有子二次注意力方法（如线性注意力）多聚焦于因果掩码，而实际中双向掩码对检索质量提升显著。因此亟需一种可扩展的双向线性注意力机制，既能维持检索质量又能降低长序列下的延迟。

**方法关键点**：
- **Gated Bidirectional Linear Attention (GBLA)**：在核化线性注意力的基础上加入三项轻量组件：(1) 对输入做一维卷积（Conv1D）以增强局部建模；(2) 学习逐token的Key门控（softmax标量门），实现软遗忘重要度加权；(3) 对注意力输出使用带可学习门控的RMSNorm。这些组件均保持线性复杂度。
- **混合编码器设计**：不全部替换自注意力，而是以1:2比例交错插入SA和GBLA层（[SA, LA, LA]），兼顾长距离交互与局部精确建模。
- 采用多哈希嵌入与语义ID生成，解码器仅有一层因果层（自注意力+交叉注意力），将大部分容量留给编码器。

**关键实验**：
- **工业数据集**：Yandex Music流媒体平台，训练集4亿样本，历史长度2048~8192。混合GBLA在Recall@1000上几乎无损（2048时0.8668 vs 自注意力0.8667），且随序列增长差异微小。
- **推理速度**：在H100上单层对比FlashAttention-v3，序列长度4096时加速1.5倍，32768时加速8.2倍。混合模型训练步时间在长序列下亦有1.3倍加速。
- **公开基准**：在Amazon Beauty、Sports、Toys数据集上，混合GBLA的Tiger模型与纯自注意力的检索指标相近，验证了方法的泛化性。

**核心结论**：混合编码器（SA + GBLA）是长序列生成式检索的高效实用方案，线性注意力的门控增强使质量逼近标准自注意力，同时训练与推理效率显著提升。
