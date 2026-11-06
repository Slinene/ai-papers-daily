---
title: 'Muir: Linear Attention with Sensitivity-Allocated Gating and Matched-Filter
  Readout'
title_zh: Muir：灵敏度分配门控与匹配滤波读出的线性注意力
authors:
- Tushaar Gangavarapu
- Gil Tabak
- Clemens JS Schaefer
affiliations:
- University of Texas at Austin
- Google
arxiv_id: '2611.08376'
url: https://arxiv.org/abs/2611.08376
pdf_url: https://arxiv.org/pdf/2611.08376
published: '2026-11-05'
collected: '2026-11-06'
category: LLM
direction: 线性注意力架构优化
tags:
- Linear Attention
- Gated DeltaNet
- Low-rank Gating
- Matched-Filter Readout
- Long Context
- Efficient Training
one_liner: Muir 用敏感性分配低秩门控与匹配滤波读出改进线性注意力，PPL 更低且百万 token 外推稳定
practical_value: '- 在长序列用户行为或会话建模中，可借鉴「慢衰减状态行范数更大，需 matched-filter readout 重新加权」：对压缩记忆按
  row norm 做加权/归一化读出，避免低频/慢特征主导，提升长程记忆稳定性。

  - 做 memory / KV cache 压缩或线性注意力时，可用敏感性分析指导秩分配：erase gate 对误差不敏感，可显著降秩；write gate
  保持全秩，把省下的参数投给 FFN 或其他关键模块。

  - 需要大 chunk 并行训练线性 attention / state-space 模型时，可参考 Muir 的 parallel update：解决标准 chunkwise
  算法在 chunk size 增大时的数值不稳定，兼顾宽矩阵单元利用率与稳定训练。

  - Agent 长任务日志、用户长期行为或 RAG 长上下文场景，若采用固定大小状态压缩，可参考其低秩 erase + 静态 readout 在 1M token
  passkey 检索仍近 100% 的架构结论，降低在线服务延迟。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：Transformer 自注意力的计算随序列长度二次增长；线性注意力将上下文压缩为固定尺寸 KV state，但 Gated DeltaNet-2 仍存在状态更新对擦除/写入敏感性不均、慢衰减行范数过大问题。
**方法关键点**：分析表明 key 能量集中在稀疏 channel，擦除门可低秩化；value write 缩放所有 channel，写入门需保持高秩。据此提出 Muir：把门控融合为 sensitivity-allocated 低秩投影；用 matched-filter readout 对状态行按范数重加权；将省下的参数用于更宽 FFN；并设计 parallel update 稳定大 chunk 并行训练。
**结果**：166M–1.34B 规模下，Muir 的 PPL 比 GDN-2 低 1.8–2.0%、比 Transformer 低 2.5–3.6%；常识准确率最高提升 1.9 个百分点；1.34B 模型从 4K 训练长度外推至 10M token 无 PPL 漂移（2560×），1M token passkey 检索近 100% 准确；训练吞吐与 GDN-2 相当，达到 100B token 验证损失快 1.2×，32K 长度训练比 Transformer 快 2.7×。
