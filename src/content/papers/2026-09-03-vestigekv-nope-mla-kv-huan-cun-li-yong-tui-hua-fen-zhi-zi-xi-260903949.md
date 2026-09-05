---
title: 'VestigeKV: The NoPE-MLA KV Cache Carries Its Own Eviction Signal in a Vestigial
  Branch'
title_zh: VestigeKV：NoPE-MLA KV 缓存利用退化分支自身携带淘汰信号
authors:
- WenJie Fan
affiliations:
- Yotta Labs
arxiv_id: '2609.03949'
url: https://arxiv.org/abs/2609.03949
pdf_url: https://arxiv.org/pdf/2609.03949
published: '2026-09-03'
collected: '2026-09-05'
category: LLM
direction: LLM 推理优化 · KV Cache 压缩
tags:
- KV cache
- MLA
- NoPE
- eviction
- long-context
one_liner: 利用 NoPE MLA 缓存中 64 维退化分支作为查询无关显著性信号，实现无训练 KV 缓存分层压缩
practical_value: '- 若线上 Agent/LLM 服务采用 NoPE MLA 架构（如 Kimi 系列），可直接在长上下文场景（用户长期行为序列、商品知识库、会话历史）部署
  VestigeKV：以 decoupled branch 的 64 维子空间做 top-m 分层，将非 top 行归档且 GPU 常驻，避免删除导致不可逆信息丢失；无需修改权重或
  kernel，工程上可作为 cache policy 无损接入。

  - 观察注意力淘汰（H2O/SnapKV）在 NoPE MLA 上失效（needle retrieval 0.00–0.33），提醒在生成式推荐/Agent 长上下文服务中若目标模型为
  NoPE，不要沿用 RoPE 时代的 KV 淘汰策略；先验证查询无关显著性信号是否存在。

  - 分层缓存 + 可触发归档的思路可迁移到推荐系统特征缓存：将高频/高显著性特征放快速层，其余 bit-exact 放低成本 GPU/CPU 层，需要时按查询
  key 精确取回，避免近似压缩带来的检索精度损失。

  - 对多轮 Agent 对话或用户行为序列建模，利用缓存中已有分支的统计分布（top-1 目标 token 占比）判断可压缩性，可在推理前离线冻结阈值，避免在线调参。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：长上下文场景中 KV cache 需要在查询到来前压缩，基于观察注意力的淘汰方法（H2O、SnapKV）在 NoPE MLA 模型上 needle retrieval 降至 0.00–0.33，因为 token 重要性尚未被观察到。

**方法关键点**：VestigeKV 利用 Kimi Linear 缓存中已有的 64 维 decoupled branch（RoPE 残留，NoPE 训练将其变为显著性通道）作为查询无关淘汰信号。读取每行 11% 维度，将 top-m 行放入 attended tier，其余行原样移入 GPU-resident archive，不删除、可触发精确检索。无训练、无量化、无权重/kernel 修改。

**关键结果数字**：8x 压缩检索保持 1.00，32x 为 0.92（8k–65k 上下文），与全行选择零差距；32x 时 attended tier 每 token 仅 0.25KB（原 8.1KB），archive bit-exact；128x recall tier 达到 1.00。NoPE 独有性：相同操作在 RoPE MLA 上降至 0.08，query-independent 显著性仅在无旋转下存在。
