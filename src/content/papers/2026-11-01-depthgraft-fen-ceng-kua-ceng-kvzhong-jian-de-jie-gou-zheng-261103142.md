---
title: 'DepthGraft: Structural Regularization through Hierarchical Cross-Layer KV
  Reconstruction'
title_zh: DepthGraft：分层跨层KV重建的结构正则化
authors:
- Xiaohan Qin
- Xiangdong Zhang
- Yu Wang
- Huaijin Wu
- Zhuo Xia
- Yebin Yang
- Junchi Yan
affiliations:
- School of AI, Shanghai Jiao Tong University
- Shanghai Innovation Institute
- Dots Studio, Xiaohongshu Inc.
arxiv_id: '2611.03142'
url: https://arxiv.org/abs/2611.03142
pdf_url: https://arxiv.org/pdf/2611.03142
published: '2026-11-01'
collected: '2026-11-11'
category: LLM
direction: LLM 深度扩展 · 跨层 KV 共享
tags:
- LLM architecture
- KV cache
- cross-layer sharing
- structural regularization
- MoE
one_liner: 提出DepthGraft分层跨层KV共享架构，用浅中层配对重建深层KV，通过梯度路径正则化提升性能并减少1/3 KV cache
practical_value: '- 若自研或微调 LLM 作为推荐/搜索/Agent 底座，可在 transformer 层间采用 DepthGraft 式 stride-aligned
  浅中层配对重建深层 KV，保持效果的同时减少约 1/3 KV cache，直接降低在线推理显存与 TTFT。

  - 跨层 KV reuse 可视为对源 KV 投影的隐式正则化；当训练出现深层信息稀释或下游任务指标停滞时，可引入类似非局部梯度通路，而不必增加额外参数或内存访问。

  - 该设计保留 prefill early completion，对线上低延迟场景友好；尤其适合 GQA/MLA 及 MoE 架构，在文章 0.5B–16B 模型上收益稳定，可作为大模型推理优化的验证方向。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：Pre-LN 架构随深度增加出现深度方向信息稀释，深层表征利用不充分。现有跨层连接虽有效，但常引入额外计算或内存访问。重新审视跨层 KV 共享，发现除缓存压缩外，每条 KV 复用边会建立从深层到源 KV 投影的直接梯度路径，从而隐式正则化 KV 表示几何。

**方法关键点**：提出 DepthGraft，一种分层 KV 共享架构，采用 stride-aligned 的浅层-中层源配对来重建深层 KV。这种拓扑将非局部梯度流分布到多个源层，同时保留 prefill 早完成特性，并将 KV cache 减少约三分之一。论文系统分析表明，合适的共享拓扑能锐化 key 的检索方向并丰富 value 的内容子空间，而现有相邻层或全局锚点设计未充分挖掘该效应。

**关键结果**：在 0.5B 至 16B 的 dense 与 MoE 模型、GQA 与 MLA 下均取得一致下游提升。16B MoE 模型上，MMLU-Pro 绝对提升 7.0%，CMMLU 提升 6.6%，C3 提升 6.4%；同时 TTFT 和 KV cache 显著下降。
