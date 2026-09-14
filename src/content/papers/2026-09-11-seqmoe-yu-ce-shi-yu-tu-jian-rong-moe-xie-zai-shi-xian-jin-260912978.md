---
title: 'SeqMoE: Toward Full-Load Performance via Predictive and Graph-Compatible MoE
  Offloading'
title_zh: SeqMoE：预测式与图兼容 MoE 卸载实现近满载性能
authors:
- Zihan Wang
- Yuqi Wang
- Lei Gong
- Cheng Tang
- Wenqi Lou
- Teng Wang
- Chao Wang
- Xuehai Zhou
affiliations:
- University of Science and Technology of China
- Suzhou Institute for Advanced Research, University of Science and Technology of
  China
arxiv_id: '2609.12978'
url: https://arxiv.org/abs/2609.12978
pdf_url: https://arxiv.org/pdf/2609.12978
published: '2026-09-11'
collected: '2026-09-14'
category: Other
direction: MoE 推理卸载 · 预测式专家预取
tags:
- MoE
- Offloading
- Inference
- Sequence Modeling
- Prefetch Scheduling
- Caching
one_liner: 通过序列建模预测专家激活，结合联合预取调度与图兼容运行时，实现 45% 常留下 96.97% 命中率和 80.22% 满载性能
practical_value: '- 若业务使用 MoE 架构 LLM（如 Mixtral、DeepSeek-MoE）做 query 改写、文案生成或 Agent
  工具编排，可参考 SeqMoE 的专家激活序列预测：只让约 45% 的 expert 常驻显存，仍能获得约 80% 的 full-load 性能，适合在显存受限
  GPU 上部署大规模 MoE 推理服务。

  - 将“下一步需要加载哪些 expert”建模为序列预测问题，类似推荐中的 next-item prediction，可以用轻量 decoder 输出多步、多层的
  expert ID 序列，比按层独立 LRU 更精准，能直接迁移到 LLM serving 的预取模块。

  - 联合预取调度可形式化为 Job Sequencing with Deadlines：把 PCIe/NVLink 带宽作为约束、各 token 的 expert
  需求作为 deadline，统一调度一批请求的 expert 加载，能显著提升带宽利用率；在 Continuous Batching 场景下可以复用这一思想。

  - 图兼容 runtime 的做法值得工程实现借鉴：将 expert 放置与计算解耦，避免预取引入依赖同步，从而能用 CUDA Graph 捕获端到端执行路径，减少
  kernel launch overhead；不过动态 MoE routing 会加大图捕获复杂度，需在 serving 框架里做静态化或部分捕获。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

动机：MoE 结构天然适合 offloading——每个 token 只激活少数 expert，若能在计算前及时加载到 GPU，理论上可接近 full-load 性能。但实际 offloading 受命中率低、带宽利用不足和执行瓶颈限制，难以达到理想效果。

方法关键点：SeqMoE 从预测与执行两个层面解决：
- 序列到序列预测：首次将专家激活预测建模为序列建模，输出多步、多层的 expert 激活序列，为预取提供长时可靠窗口；
- 联合预取调度：把预取调度形式化为 Job Sequencing with Deadlines，在带宽约束下最大化期望 expert 命中率；
- 预测驱动的缓存：利用序列建模的递归性质，设计概率 Belady 缓存策略，进行未来感知的逐出；
- 图兼容 offloading runtime：提出计算透明 expert 放置与无同步编排，支持端到端 CUDA Graph 捕获，消除执行瓶颈。

关键结果：在 45% expert 常驻条件下，SeqMoE 平均达到 96.97% 的 expert 命中率，并获得 80.22% 的 full-load 性能，在 MoE offloading 上达到 SOTA。
