---
title: 'Triadic Linear Attention: Three-Dimensional Recurrent States for Long-Context
  Sequence Modeling'
title_zh: 三阶线性注意力：三维循环状态用于长上下文序列建模
authors:
- Oliver Sieberling
- Bharat Runwal
- David Jin
- Ryan Chin
- Rameswar Panda
- Yoon Kim
affiliations:
- Massachusetts Institute of Technology
- MIT-IBM Computing Research Lab
arxiv_id: '2609.36529'
url: https://arxiv.org/abs/2609.36529
pdf_url: https://arxiv.org/pdf/2609.36529
published: '2026-09-28'
collected: '2026-10-05'
category: LLM
direction: 线性注意力 · 长上下文状态扩容
tags:
- Linear Attention
- Long Context
- Recurrent State
- Gated DeltaNet
- Tensor Product
- Recall
one_liner: 将线性注意力的矩阵状态扩展为三阶张量，用第二个 key 维度以极少参数成倍扩大状态容量，显著提升长上下文语言建模与 recall
practical_value: '- 电商/推荐用户长期行为序列建模：用户行为序列长且稀疏，Transformer KV cache 显存贵；可把 user encoder
  或长期兴趣提取器替换为 Triadic GDN/sGLA，用 E=4~8 扩大状态，参数只增加约 1%，线上保持 O(1) 状态，对历史兴趣 recall 提升明显。second
  key/query 建议用 softplus/sigmoid 非负激活，避免切片间抵消。

  - Agent 长期记忆/长上下文工具结果：如果 Agent 用线性注意力做记忆，可在长上下文扩展阶段把 E=1 upcycle 到 E=8，不必从头训练；论文显示
  upcycling 可恢复约 50%-75% 从 scratch 的收益，适合已有模型低成本升级。

  - 混合架构取舍：搜推广 rerank 或 Agent 模型若采用 linear+softmax 混合，优先扩大 linear state 而不是 softmax
  GQA 的 KV cache；论文在 3:1 混合中，triadic E=4 比 GQA-4 在长上下文 PG19 和 NIAH 更好，且 64k 显存少约一半。

  - 工程实现：chunkwise-parallel 实现中，把三阶 state 沿 value 轴切成 32 列块放到 registers，避免 SM 持有完整
  state；joint key 内积分利用 Kronecker 结构降维，E 维只增加少量 C^2E 计算，长上下文效率优于 Transformer。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
线性注意力/RNN 用固定大小状态换取 O(1) 推理，但状态大小直接决定能 recall 多少上下文；现有增大状态的方法（加 heads、加 value 维度、grouped values）要么大幅增加参数，要么挤压 MLP 宽度。  

**方法关键点**  
- 将 dyadic outer product (key⊗value) 推广为 triadic outer product (key⊗second_key⊗value)，状态从 d×d 矩阵变成 d×E×d 三阶张量；读取时用两个 query 沿两个 key 轴收缩。  
- E 维 second key/query 只需两个线性投影，E=8 增加约 1.2% 参数，但状态容量扩大 8 倍；E=1 退化为普通线性注意力。  
- 兼容 modern 线性注意力组件：给每个 second-key slice 独立 forget gate；delta rule 在联合 key 上 erase；chunkwise-parallel 训练利用 Kronecker 结构把 joint key 内积分成两个普通内积，并把 state 沿 value 轴分块到寄存器。  

**关键实验与结果**  
- MQAR 合成任务：E=16 时容量约为普通线性注意力的 16 倍，非嵌入参数仅增加 1.08 倍。  
- 400M/1.3B 语言模型，Fineweb-Edu 预训练 50 tokens/param，长上下文扩展到 64k；对比 Transformer、更大 head/value、grouped values、更多 heads。  
- Triadic GDN E=8 在 PG19 各区段优于 Transformer；400M E=4 时 Wiki 10.93 vs Transformer 11.11，recall 31.1 vs GDN base 26.2；1.3B E=8 Wiki 7.87 vs GDN 8.08，recall 44.4 vs 36.1。  
- 3:1 GDN/GQA-8 混合模型中，triadic E=4 比扩大 KV cache 的 GQA-4 在 PG19 和 NIAH 更好，且 64k 显存 220MB vs 407MB。  
- E=8 训练开销比 GDN 高 28-30%，但在 64k 推理/训练比 Transformer 快 5.1 倍。  

**最值得记住的一句话**：状态大小是线性 RNN 长上下文能力的关键瓶颈，三阶张量外积用几乎可忽略的参数开销成倍扩大状态容量，是比加 head/加 value 维度更有效的扩容路径。
