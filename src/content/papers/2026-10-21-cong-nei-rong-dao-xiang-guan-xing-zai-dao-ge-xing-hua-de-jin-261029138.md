---
title: Progressive Learning from Content to Relevance to Personalization for CTR Prediction
title_zh: 从内容到相关性再到个性化的渐进式 CTR 预估
authors:
- Zhiguang Yang
- Yulin Yang
- Fuyu Lv
- Dan Ou
affiliations:
- Alibaba Group
arxiv_id: '2610.29138'
url: https://arxiv.org/abs/2610.29138
pdf_url: https://arxiv.org/pdf/2610.29138
published: '2026-10-21'
collected: '2026-10-22'
category: RecSys
direction: 多模态 CTR 预测 · Semantic ID
tags:
- Semantic ID
- Multimodal CTR
- Progressive Learning
- Query-Item Relevance
- Cold-start
- Creative Discrimination
one_liner: 用多尺度细粒度 Semantic ID 将多模态内容融入 ID 型 CTR 模型，先做 query-item 相关性预训练再做点击微调，显著提升冷启动与创意区分
practical_value: '- 把连续多模态 embedding 换成多尺度、字段保留的离散 SID：图片用 VAR 多尺度 code maps（1×1/2×2/3×3/4×4）得到
  30 个 spatial token，不要用单个 global embedding；下游 SID lookup 可随机初始化，卡片离线抽取、在线只做 lookup，避免生成延迟。适合电商主图、创意图片、标题/OCR
  等多模态特征接入现有 ID 排序模型。

  - 两段式训练可直接迁移到业务：先做 query-item relevance 等语义相关任务（可用 LLM 教师或人工标注）全参数预训练共享 backbone，再用点击/转化日志全量微调。注意保留
  dense 和 normalization 状态，只重置稀疏 optimizer accumulators；这比 embedding-only transfer
  收益更大，也避免联合训练分布冲突。

  - 架构上用 query 做 Q、title/OCR tokens 做 K/V 的 cross-attention，输出按字段身份拼接；图片 SID 按 scale/position
  固定顺序拼接，避免平均池化。此设计在搜索广告、推荐主图排序里可复用，尤其适合需要识别同 item 不同创意差异的场景。

  - 评估时除 AUC/GAUC，建议增加冷启动子集和同 item 内不同创意的 replay CTR（NSCTR），否则 ID 记忆会掩盖语义理解收益；在线业务指标中
  GMV 提升幅度值得重点关注。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
电商搜索 CTR 排序需要同时建模 item 内容、query 相关性和用户偏好。纯 ID 模型依赖稀疏记忆，冷启动差；连续多模态 embedding 与 ID 特征空间分布不一致，而 RQ-VAE 等全局 SID 压缩过狠，丢失空间和文本细节，无法判断同商品不同创意的细微差异。核心需求是一套离散且细粒度、能与 ID 特征等权交互的内容接口。

**方法关键点**
FineSID 将训练拆成三阶段：
- Stage I 细粒度内容 tokenization：用 VAR 多尺度视觉 tokenizer 生成 1×1/2×2/3×3/4×4 共 30 个 spatial SID（codebook size 4096），文本按字段用 BPE/n-gram 独立 token 化。所有内容转成下游可训练的 SID lookup，保留 scale、position、field identity，离线抽取。
- Stage II 相关性预训练：用 Qwen3.5 教师提供的 query-item 相关性软标签，对共享特征交互网络做 full-parameter 预训练。网络采用 ordered fusion + latent-slot attention（HiFormer）+ Shared MLP（768→256→64），文本字段用 query-conditioned cross-attention。
- Stage III 个性化 CTR 微调：丢弃 relevance head，接 CTR head，用点击日志和 BCE loss 全量微调；保留 Stage II 的 dense/normalization 状态，重置稀疏 Adagrad accumulators。

**关键结果**
在 Taobao 工业搜索数据（51.2B 曝光训练/453M eval）上，FineSID 相对 HiFormer + ID baseline 提升 AUC +0.25pt、GAUC +0.26pt；冷启动子集提升更大：AUC +0.38pt、GAUC +0.34pt；同 item 内创意判别指标 NSCTR 提升 0.75%，明显超过 RQ-VAE SID、COINS 等 baseline。消融显示去掉 Stage II 或 fine-grained SIDs 后收益大幅下降；MMCTR 公开集上 AUC +0.77pt；在线 A/B 中 GMV +0.85%、IPV +0.21%。

**最值得记住的一句话**
真正带来冷启动和创意区分提升的不是“用了 SID”，而是保留多尺度空间位置和字段身份的细粒度 token 化，并让 relevance 预训练全量迁移到 CTR。
