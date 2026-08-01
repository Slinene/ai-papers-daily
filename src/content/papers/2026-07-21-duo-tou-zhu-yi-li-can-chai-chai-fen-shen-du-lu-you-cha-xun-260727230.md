---
title: Multi-Head Attention Residuals
title_zh: 多头注意力残差：拆分深度路由查询突破单头瓶颈
authors:
- Cheng Luo
- Zefan Cai
- Junjie Hu
affiliations:
- Independent Researcher
- University of Wisconsin–Madison
arxiv_id: '2607.27230'
url: https://arxiv.org/abs/2607.27230
pdf_url: https://arxiv.org/pdf/2607.27230
published: '2026-07-21'
collected: '2026-08-01'
category: Training
direction: 多头深度路由 · 消除单头深度读瓶颈
tags:
- multi-head attention residuals
- depth routing
- transformer architecture
- forced compromise
- compute-equivalent gain
one_liner: 将注意力残差的单头路由查询改为多头，零参数提升模型跨度，单头在大模型退化成有害
practical_value: '- 推荐系统 Transformer 堆叠中，可借鉴 MHAR 替换标准残差连接：不同特征子空间（如用户长期兴趣 vs 短期行为）可从不同层检索信息，缓解单头深度读的妥协，预估中小尺寸实验见
  100M–1B 连续改善。

  - 单头深度路由在大模型上退化（1B 时比基线差 0.105），提示在大型 CTR/CVR 模型的多层聚合设计中应避免单一全局查询，分组路由更安全。

  - 恒等转换方法（delta attention residuals）支持在已预训练模型上无损嫁接 MHAR 进行中训练，可迁移到推荐模型增量训练，避免 loss
  spike。

  - 融合 Triton 路由内核将内存绑定操作的训练吞吐从 0.2–0.5× 提升至 0.55–0.88× 基线，类似的定制算子可优化推荐模型中层间特征重读的工程开销。'
score: 9
source: huggingface-daily
depth: full_pdf
---

**动机**  
Transformers 通过残差连接逐层传递信息，但无法重新直接访问早期层的输出。注意力残差（Attention Residuals）引入深度注意力，用一个可学习的查询向量对历史子层输出做软混合，然而单头查询强制所有特征维度共享一个深度分布，随模型宽度增加，不同子空间的分歧加剧，该“强制妥协”从小模型上的无害变为大模型上的有害。  

**方法关键点**  
- **多头注意力残差（MHAR）**：将单头查询 reshape 为 H 个头，每个头独立对深度历史做 softmax 路由，零参数、零 FLOPs 增加，H=1 时精确退化为原注意力残差。  
- **超参数无关默认值**：取 H 等于 KV 头数量（GQA 层级）接近最优，无需调参。  
- **融合 Triton 内核**：提供确定性前向/反向内核，将路由训练吞吐从 0.2–0.5× 基线提升至 0.55–0.88×，峰值显存接近基线。  
- **恒等转换**：用 delta 注意力残差将 MHAR 无损嫁接到预训练模型，零初始化门控，无训练冲击，支持中训练继续提升。  

**关键实验**  
- **规模实验**：在 FineWeb-Edu 上从头训练 100M / 350M / 1B 三个尺寸的 Transformer，MHAR 分别获得 −0.049 / −0.080 / −0.063 验证损失改善；单头路由则在 1B 时比基线差 +0.140。计算等效增益 1.27–1.49×。  
- **中训练 8B**：在公开 anneal 语料上进行 10B token 中训练，MHAR 较 schedule-matched 控制组提升 GSM8K +3.2（p=0.004）、GPQA +3.1（p=0.038），MMLU 等持平。  
- **消融与探针**：训练后的查询子空间分裂测量证实宽度增加导致子空间路由分歧增大，与单头退化同步；路由头数在欠训练时越多越好，完全收敛后 H=KV 为最佳。  

> 核心结论：注意力是multi-head的，深度读也应该是multi-head的；仅此一改，无需额外参数，便让模型从无害到持续获益。
