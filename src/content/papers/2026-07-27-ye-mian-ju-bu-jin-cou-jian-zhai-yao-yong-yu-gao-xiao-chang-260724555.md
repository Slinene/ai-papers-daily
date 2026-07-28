---
title: 'LOCKS: Page-Local Compact Key Summaries for Efficient Long-Context Decoding'
title_zh: 页面局部紧凑键摘要用于高效长上下文解码
authors:
- Junsung Hwang
arxiv_id: '2607.24555'
url: https://arxiv.org/abs/2607.24555
pdf_url: https://arxiv.org/pdf/2607.24555
published: '2026-07-27'
collected: '2026-07-28'
category: LLM
direction: KV cache 压缩 · 稀疏注意力
tags:
- KV cache compression
- sparse attention
- long-context decoding
- page-level summarization
- vLLM plugin
one_liner: 通过页面局部光谱摘要和稀疏选择，大幅减少长上下文解码中 KV cache 读取量，保持质量
practical_value: '- 电商推荐中常需用 LLM 建模长用户行为序列，LOCKS 的页面级压缩可将序列分块，每块保留紧凑谱摘要，在生成时仅注意 top
  块，降低长序列推理延迟

  - 该选择机制只基于摘要估计注意力质量，不读取原始键值，适合在推荐 query 生成等需要可控延迟的场景中部署

  - 可作为 vLLM 插件直接集成到现有推理服务，无需修改模型，对已部署推荐系统的 LLM 组件改造成本极低

  - 长形式推理（如 Agent 多步规划）收益最大，若推荐 Agent 需要长上下文推理，此方法可明显提升响应速度'
score: 7
source: arxiv-cs.AI
depth: abstract
---

长上下文 LLM 解码时每个步骤都需读取整个 KV cache，内存带宽成瓶颈。注意力键在页面内局部低秩，共享全局基会损失页面特有方向信息。LOCKS 为每个页面构建紧凑的谱摘要（约为 cache 的 1/10），基于该摘要重建页面内 logits，用 log-sum-exp 估计各页面注意力质量，仅对 top 页面计算注意力，且选择过程无需读任何原始键值。在 LongBench-v1 长文档问答上，仅靠摘要选择就能在 FullKV 的 1 个百分点内；在 retrieval-dense 的 RULER 上匹配全读 key oracle；在长形式推理（AIME26、MATH-500）上优势最大，基线选择器崩溃。以 2048 token 预算，在 100K+ 上下文下匹配 FullKV 质量，仅关注约 2% token，解码延迟减半（1M token 时 2.0× 加速）。已作为插件集成到 vLLM，支持批量解码和完整 CUDA graph。
