---
title: 'HySparse2: Hybrid Sparse Attention with Two-Level KV Sharing'
title_zh: HySparse2：两级 KV 共享的混合稀疏注意力
authors:
- Jianyu Wei
- Yizhao Gao
- Qihao Zhang
- Shimao Chen
- Zhengju Tang
- Yu Cheng
- Shengjie Zhou
- Zihan Jiang
- Yifan Song
- Hailin Zhang
affiliations:
- Xiaomi LLM-Core
arxiv_id: '2609.26368'
url: https://arxiv.org/abs/2609.26368
pdf_url: https://arxiv.org/pdf/2609.26368
published: '2026-09-22'
collected: '2026-09-23'
category: LLM
direction: 长上下文高效稀疏注意力与 KV 共享
tags:
- sparse attention
- KV cache
- prefill optimization
- long context
- MoE
- agentic inference
one_liner: 通过两级 KV 共享使 prefill 只跑一半模型，同时提升长上下文检索并降低 KV 缓存
practical_value: '- 在电商/搜索 Agent 场景，工具返回长文本、多轮会话累积导致 prefill 成为主要延迟；可借鉴 self-decoder/cross-decoder
  分离：prefill 只执行 self-decoder（约半模型），cross-decoder 的 full-attention KV 由 self-decoder
  hidden states 投影生成。在 prefill-decode disaggregation 下，prefill 节点只需部署一半权重，显存和算力直接减半。

  - 稀疏注意力选择粒度很关键：对多轮 Agent 轨迹、检索历史，token-level top-k 明显优于 block-level（RULER-v2 +6.57、2-needle
  MRCR-v2 +8.14、GraphWalks +5.55）。如果业务正在用 block sparse 做长上下文召回或会话压缩，且 token-level
  kernel 可用，应尽早切换；至少在检索关键层保留 token-level。

  - 强制最近窗口进入稀疏选择，可以替代单独的 SWA 分支：省掉额外投影参数、局部 KV cache 和级联依赖，使 early exit prefill 成为可能。对需要保留最近会话/商品浏览状态的推荐
  Agent，固定保留最近 128 token 是低成本且有效的局部建模。

  - KV Bridging 只在 full-attention 层间连接，保留独立投影但共享 source hidden，可以在几乎不损失质量的前提下压缩 KV
  cache（1M 时 2.69GB vs 6.72GB/12.09GB）。对超长上下文电商 Agent，可考虑用跨层 KV 共享替代或叠加量化压缩。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**
长周期多轮 Agent 推理中，工具返回的观察往往远长于动作，上下文不断累积，带来三重压力：prefill 计算大、KV cache 占用高、长上下文检索精度不足。HySparse 已通过 full + sparse attention 交错降低注意力成本，但 prefill 仍需执行全部层，且 block-level 稀疏在多轮轨迹上精度受损。

**方法关键点**
- 架构按 YOCO 风格分为 self-decoder 和 cross-decoder：self-decoder 混合 full attention 与 sliding-window attention；cross-decoder 混合 full attention 与 sparse attention。
- 外层 KV Bridging 只连接两个 decoder 的 full-attention 层：cross-decoder full-attention 的 K/V 由对应 self-decoder full-attention 输入 hidden states 经独立投影得到，Q 仍由本层 hidden 计算。
- 内层 KV Reuse 沿用 HySparse 的 KV 共享，但做两个改进：block-level 改为 token-level top-k 选择；删除单独 SWA 分支，改为强制最近 128 token 进入稀疏选择。所有 cross-decoder KV 因此都能从 self-decoder hidden states 构建，prefill 可在 self-decoder 后提前退出。
- 实验模型为 80B-A3B MoE，49 层，MQA，mHC，full attention 仅 5 层；训练约 500B tokens 预训练 + 100B tokens 后训练引入 agentic 数据并扩至 256k。

**关键实验**
预训练后通用能力与 HySparse、Hybrid SWA 基本可比，NoLiMa 49.76 vs 40.27/30.13，RULER 90.77 最高。后训练后 MRCR-v2 平均提升 11.30 点、RULER-v2 提升 19.81 点（vs HySparse）；256k 下 RULER-v2 为 58.45 vs 32.61/35.74。1M tokens 时 prefill FLOPs 比 HySparse 降低 2.92×、比 Hybrid SWA 降低 5.02×；KV cache 为 2.69GB vs 6.72GB/12.09GB。消融显示 token-level 相比 block-level 在 RULER-v2、2-needle MRCR-v2、GraphWalks 分别提升 +6.57、+8.14、+5.55；KV Bridging 在 290B-A8B 上与无桥接质量相当；Forced SWA 与 Gated SWA 多数指标可比。

**最值得记住**：token-level 稀疏选择 + 强制 recent window + full-attention KV Bridging 三者组合，让 prefill 只需跑半模型，同时还能显著提升长上下文检索。
