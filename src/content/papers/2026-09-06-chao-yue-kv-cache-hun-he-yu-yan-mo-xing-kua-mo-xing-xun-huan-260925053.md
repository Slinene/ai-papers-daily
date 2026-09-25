---
title: 'LatentPort: Beyond KV Cache - Cross-Model Transfer of Recurrent Memory in
  Hybrid Language Models: A 4B-to-9B Hybrid-State Handoff Without Target Prefix Replay'
title_zh: 超越 KV Cache：混合语言模型跨模型循环记忆迁移（4B→9B 无前缀重放）
authors:
- Simon P. Villani
arxiv_id: '2609.25053'
url: https://arxiv.org/abs/2609.25053
pdf_url: https://arxiv.org/pdf/2609.25053
published: '2026-09-06'
collected: '2026-09-25'
category: LLM
direction: LLM 跨模型记忆状态迁移
tags:
- KV cache
- recurrent memory
- cross-model transfer
- hybrid LLM
- Gated DeltaNet
- inference efficiency
one_liner: 首次展示不同尺寸混合语言模型间直接迁移 Gated DeltaNet 持久循环状态，无需目标模型重新读取上下文，显著降低续写损失
practical_value: '- 在长上下文 LLM 推理服务中，可从 4B 草稿模型迁移注意力 KV 与循环状态到 9B 主模型，避免重算历史前缀，显著降低首
  token 延迟；电商 Agent 长会话切换模型时可借鉴「直连复用 recurrent/conv state + 轻量 rank-4 修正」作为状态交接基线，不一定需要训练复杂映射。

  - 对生成式推荐/Agent 的长会话记忆：混合模型（full-attention + GDN）的持久状态跨模型直接复用其坐标比学习映射更有效，提示模型家族内
  hidden state 有一定兼容性，升级模型版本时可先尝试直接复制状态，再用极少量参数微调纠正。

  - 若业务上需做模型蒸馏或小模型生成草稿、大模型验证，可复用该思想：把草稿模型的 KV 和 recurrent state 迁移给大模型，省去大模型重新编码 prompt；rank-4
  修正成本极低（约 43 万参数），适合线上快速适配。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：模型切换通常需要接收方重读历史前缀并重建推理状态。全注意力模型已有 KV 翻译，但混合模型还包含 Gated DeltaNet（GDN）层的循环矩阵和卷积历史等持久状态；仅迁移 KV 会丢失这类记忆。

**方法关键点**：在 Qwen3.5-4B-Base → 9B-Base 同架构兄弟模型上，把源模型的注意力 KV 翻译到目标模型，并直接复用 GDN 的 recurrent 与 convolution 状态；直接复用优于学习的 GDN 映射。组件选择保留 translated KV + 直连 recurrent/convolution state，再加一个 rank-4 修正模块（434,176 参数）在 64 个新网页文档上适配。

**关键结果**：加入 GDN 持久状态使 teacher-forced NLL 再降 0.747 nats/token（95% CI [0.6921, 0.8047]），PG19 上 64/64 文档提升。最终 corrected 9B 相对 native 9B 的 excess NLL 为 0.076，JS 散度 0.022，NCR 0.918；且 zero 历史前缀 token 时 corrected 9B 显著优于 continued 4B。
