---
title: Extreme Compression of Per-Layer Embeddings via Cross-Layer Latent Vector Quantization
title_zh: 通过跨层潜向量量化实现逐层嵌入的极致压缩
authors:
- Jiacheng Liu
- Yaxin Luo
- Xiaohan Zhao
- Peng Sun
- Xinyi Shang
- Jiacheng Cui
- Yonina C. Eldar
- Zhiqiang Shen
affiliations:
- Mohamed bin Zayed University of Artificial Intelligence
- Westlake University
- Zhejiang University
- University College London
- Weizmann Institute of Science
arxiv_id: '2610.31309'
url: https://arxiv.org/abs/2610.31309
pdf_url: https://arxiv.org/pdf/2610.31309
published: '2026-10-21'
collected: '2026-10-27'
category: LLM
direction: LLM 嵌入压缩 · 向量量化
tags:
- Per-Layer Embeddings
- Vector Quantization
- Model Compression
- Gemma 4
- Cross-Layer Latent
- OPTIC
one_liner: 提出 OPTIC，每 token 只存一个共享量化码，各层用仿射解码器还原层嵌入，实现约 100 倍 PLE 压缩并保留 97.8% 性能
practical_value: '- 对超大 embedding 表（如 item/user ID embedding、多粒度语义 ID、序列模型 token embedding）做压缩时，可以借鉴「每
  token/item 只存一个共享 code tuple + 各层/各任务用轻量仿射解码器」的结构，避免为每个层或每个上下文单独存储完整向量，显著降低参数量和存储成本。

  - 压缩时不要只做向量重建，要直接拟合输出路径或下游任务损失。业务中可改为用蒸馏 loss 或 CTR/CVR 损失联合训练 codebook 和 decoder，比单纯最小化
  embedding MSE 更能保留排序/推荐质量。

  - 在生成式推荐或 LLM4Rec 场景，如果使用多层 Decoder 的 per-layer item/token embedding，OPTIC 的 shared
  token code 可等价为仅存一份 item 语义码，逐层 affine 解码出适合不同层表征需求的 embedding，适合推理端内存敏感的服务部署。

  - 工程上可借鉴其 29.7% GPU 内存下降、几乎不增加延迟的结果：对 embedding 表做高倍压缩能直接释放显存，支撑更大 batch 或更长序列，但要避免
  decode 过程引入高额计算，建议用简单仿射变换而不是复杂网络。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：Gemma 4 的 Per-Layer Embeddings (PLE) 为每个词汇在每一层 decoder 都保留可学习向量，占 E4B 参数的 35.2%。在模型 embedding 与 Transformer 计算同步扩容的趋势下，极端压缩 PLE 能直接降低存储与显存开销，但常规量化方法在 100 倍以上压缩时性能损失严重。

**方法关键点**：OPTIC 不逐 token-layer 独立存储 code，而是每个 token 只存一个量化 code tuple，在每一层用 layer-specific 的仿射解码器将其映射为层嵌入。code 与 decoder 的训练目标不是重建原始 PLE 向量，而是拟合 PLE 输出路径，使压缩后的模型行为更接近未压缩模型。相比 product quantization 等六种 baseline，OPTIC 在高压缩率下保持性能的关键是共享 code + 逐层 affine 变换。

**关键结果数字**：BF16 E4B 在约 100 倍 PLE 压缩下，OPTIC 在 7 个 benchmark 上保留 97.8% 聚合性能，而最强的 PQ baseline 仅 66.3%；594 倍和 1002 倍压缩下分别保留 90.5% 和 84.1%。官方 W4A16 E4B 在约 100 倍压缩下保留 96.9%。推理端约 100 倍压缩时 GPU 内存减少 29.7%，耗时最多增加 0.40%。
