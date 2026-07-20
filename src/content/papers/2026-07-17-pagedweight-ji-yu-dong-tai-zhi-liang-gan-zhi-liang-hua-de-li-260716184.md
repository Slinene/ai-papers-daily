---
title: 'PagedWeight: Efficient MoE LLM Serving with Dynamic Quality-Aware Weight Quantization'
title_zh: PagedWeight：基于动态质量感知量化的高效 MoE LLM 推理
authors:
- Yuchen Yang
- Yifan Zhao
- Anisha Dasgupta
- Sasa Misailovic
affiliations:
- University of Illinois Urbana-Champaign
arxiv_id: '2607.16184'
url: https://arxiv.org/abs/2607.16184
pdf_url: https://arxiv.org/pdf/2607.16184
published: '2026-07-17'
collected: '2026-07-20'
category: LLM
direction: MoE 推理优化 · 动态量化
tags:
- MoE
- Quantization
- KV cache
- Serving
- Memory management
one_liner: 通过运行时动态量化 MoE 专家权重，在 KV 缓存压力下平衡精度与内存，最高节省 72% 显存并提升 1.94 倍吞吐
practical_value: '- 在电商大模型（如多专家推荐、多任务模型）的推理部署中，可借鉴 PagedWeight 的动态量化策略：依据请求负载和剩余 KV
  缓存空间，实时调整专家权重的量化精度，避免 OOM 同时保留推荐质量。

  - 系统设计上，可引入“精度-内存-延迟”三维感知的调度器，类似 PagedWeight 的质量感知策略，在延迟约束下动态为不同专家分配不同位宽，相比静态均匀量化可大幅提高内存利用率。

  - 当推荐模型规模膨胀到需要多 GPU 或 KV 缓存成为瓶颈时，权重的页式管理（paged offloading/quantization）思路可直接复用，通过将非活跃专家权重以低精度或卸载方式管理，降低常驻显存。

  - 实验中表明，在同等显存预算下，PagedWeight 比强 baseline（如 GPTQ、AWQ）质量提升最高 39.3%，证明动态精度分配比固定量化有显著收益，业务中可优先考虑实现“按需精度”而非全局统一量化。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：MoE 模型在长上下文推理时，KV 缓存与庞大的专家权重竞争 GPU 显存，现有量化方法通常是静态、全局的，无法根据实时内存压力灵活调整，导致要么精度损失过大，要么 OOM 风险。

**方法关键点**：
- **动态质量感知量化**：将每个专家权重切分为页（page），在推理过程中根据当前 KV 缓存占用和请求延迟要求，实时决定每页的量化位宽（如 FP16/INT8/INT4）。
- **三维权衡建模**：显式建模精度、内存、吞吐/延迟三者关系，通过在线求解整数规划，在满足延迟 SLO 前提下最大化内存节省。
- **系统实现**：基于 vLLM 框架，将量化决策与 PagedAttention 的 KV 缓存管理联动，实现权重页的按需加载与释放。

**关键结果**：
- 在多个 MoE 模型（Mixtral 8x7B 等）和长文本任务上，可达 FP16 同等精度，同时节省最多 72.0% GPU 显存，吞吐提升最高 1.94 倍。
- 在相同显存预算下，相比 GPTQ、AWQ 等静态量化方法，任务质量最高提升 39.3%，且仅增加最多 4.1% 的吞吐损失。
