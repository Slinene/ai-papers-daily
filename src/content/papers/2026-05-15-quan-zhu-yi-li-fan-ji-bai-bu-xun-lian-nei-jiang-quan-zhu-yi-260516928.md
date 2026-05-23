---
title: 'Full Attention Strikes Back: Transferring Full Attention into Sparse within
  Hundred Training Steps'
title_zh: 全注意力反击：百步训练内将全注意力转化为稀疏注意力
authors:
- Yanke Zhou
- Yiduo Li
- Hanlin Tang
- Maohua Li
- Kan Liu
- Lan Tao
- Lin Qu
- Yuan Yao
- Xiaoxing Ma
affiliations:
- Nanjing University
- Alibaba Group
arxiv_id: '2605.16928'
url: https://arxiv.org/abs/2605.16928
pdf_url: https://arxiv.org/pdf/2605.16928
published: '2026-05-15'
collected: '2026-05-23'
category: Training
direction: 长上下文推理 · 注意力稀疏化
tags:
- Sparse Attention
- Long Context
- KV Cache
- Inference Speedup
- Retrieval Heads
one_liner: 发现全注意力LLM存在内在稀疏性，通过轻量索引和动态选择仅需数百步训练即可达到近乎无损的稀疏推理
practical_value: '- **动态 top-p 筛选**: 对电商搜索/推荐中的长序列用户行为编码，借鉴 query-dependent 的动态 token
  预算，代替固定 top-k，可保留关键信息同时降低计算开销。

  - **检索头识别与保留**: 在 Agent 长对话记忆或商品详细页理解中，仅保留少数注意力头进行全长度上下文检索，其余头使用稀疏模式，可大幅压缩 KV 缓存。

  - **低维索引器设计**: 用 16 维索引矩阵替代完整注意力分数计算，适合实时性要求高的生成式检索或召回阶段，可在预填充阶段大幅提速。

  - **少步迁移训练**: 利用已有的全注意力模型，仅需数百步微调即可迁移到稀疏推理，无需从头预训练稀疏模型，节省训练资源且保持精度，适合业务快速迭代。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**: 长上下文大模型推理受制于全注意力的二次复杂度，现有稀疏方法大多需要原生稀疏训练或启发式 token 驱逐，在效率、训练成本和精度之间难以兼顾。

**方法**: 提出 RTPurbo，基于三个发现：(1) 只有少数“检索头”真正需要全长度上下文；(2) 长程检索可由低维子空间主导，故用 16 维索引器高效检索相关 token；(3) 有效 token 预算与查询强相关，动态 top-p 选择优于固定 top-k。训练时仅在检索头保留完整 KV 缓存，其他头用稀疏模式，并引入轻量 token 索引器以恢复全注意力性能，只需几百步适配即完成稀疏化。

**结果**: 在长上下文基准和推理任务上，RTPurbo 保持近无损准确率，同时在 1M 上下文预填充加速达 9.36×，解码加速约 2.01×，大幅优于 MInference 和 FlexPrefill。
