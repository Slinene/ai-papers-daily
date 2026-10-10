---
title: 'SparseEngine: Sparse-First Inference Engine'
title_zh: SparseEngine：稀疏优先的LLM推理引擎
authors:
- Jitai Hao
- Quansheng Gu
- Qiang Huang
- Jun Yu
affiliations:
- Harbin Institute of Technology
arxiv_id: '2609.39068'
url: https://arxiv.org/abs/2609.39068
pdf_url: https://arxiv.org/pdf/2609.39068
published: '2026-09-29'
collected: '2026-10-10'
category: Other
direction: 稀疏注意力 · KV cache推理引擎
tags:
- Sparse Attention
- KV Cache
- Inference Engine
- Long Context
- LLM Serving
- Agent Workloads
one_liner: 通过统一生命周期契约支持15种稀疏注意力方法，并提供Chain Cache与可控前缀缓存剪枝，实现长上下文agent推理10倍吞吐提升
practical_value: '- **生命周期 hook 抽象可借鉴到自研推理服务**：将稀疏方法集成点解耦为 SparseController（注册回调）、CacheManager（方法特定状态存储）和
  AttentionView（连接注意力后端），可以不改模型代码快速接入多种稀疏/压缩策略，适合电商 Agent 服务中灵活切换 KV 优化方案。

  - **Chain Cache 对多轮 Agent 场景非常实用**：跨请求保留被 eviction 方法裁剪过的 KV 及元数据（如 H2O 累积分数），能避免每轮重新
  prefill 完整历史，对电商客服、推荐 agent 等多轮交互可显著降低首字延迟和重复计算。

  - **可控 prefix-cache pruning 允许业务方按价值管理上下文**：应用可以指定历史区间（如低价值的工具输出）和保留比例，用稀疏策略（如 KVzip）选择保留位置，同时保持逻辑前缀匹配，适合在广告/推荐
  agent 中清理过期或冗余的会话内容而不破坏缓存复用。

  - **实验结论表明物理 KV 驱逐是吞吐提升的关键**：在相同 GPU 内存下，SnapKV 物理驱逐可支撑约10倍更大 batch，带来约10倍 aggregate
  decode throughput；动态稀疏注意力在匹配并发下可获1.5-2.6倍 decode 吞吐提升，且质量几乎无损（LongBench 平均差异仅 +0.17
  分），可作为电商长上下文 LLM 推理优化的直接依据。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
长上下文 LLM Agent 在多次工具调用和推理链中，交互历史迅速膨胀，造成 KV cache 容量和 attention 计算的双重 GPU 瓶颈。稀疏注意力方法虽然能降低成本，但不同方法的 KV 表示、更新时机和存储语义差异巨大（如动态选择需要维护查询相关索引，驱逐方法会释放物理空间，量化/压缩方法需要专门元数据）。现有推理引擎往往围绕特定布局或工作流设计，如 Vortex 的页中心操作、SPIN 的分区流水线、Tangram 的非均匀头保留，导致方法覆盖受限，难以集成异构稀疏策略。

## 方法关键点
SparseEngine 提出**共享生命周期契约**，将集成边界定在模型原生模块执行顺序上：
- **细粒度 hooks**：通过 SparseController 在 prefill/decoding 的 attention 前后、层结束、步结束等位置暴露回调，让方法注册自己的计算流程（如 SnapKV 的 chunk 后选择与驱逐、Quest 的 query 相关页选择），无需修改模型实现。
- **方法定制 CacheManager**：每个方法拥有自己的 KV 表示、物理布局、位置映射及元数据，执行物理驱逐或逻辑选择时由 CacheManager 更新内部状态，实现存储与计算的分离。
- **AttentionView**：将方法特定的 cache 状态和选择结果转换为兼容注意力后端的视图，支持显式 KV、MLA latent 状态、压缩或量化表示。
- **Chain Cache**：允许驱逐类方法（SnapKV、H2O 等）跨请求复用被保留的压缩 KV 和元数据，即使物理 KV 不完整，逻辑前缀仍可匹配，续接请求只需 prefill 新后缀。
- **可控 Prefix-Cache Pruning**：应用可指定历史区间 [L,R) 和保留比例，用稀疏策略（如 KVzip）选择保留位置，释放其余物理 KV，同时保持逻辑前缀不变。

## 关键结果
- **性能**：在 Qwen3-30B-A3B 和 GLM-4.7-Flash 上，SnapKV 物理驱逐带来约 **10倍** 于 vLLM vanilla 的 aggregate decode throughput；Quest/OmniKV 在匹配 batch size 下实现 **1.5-2.6倍** decode throughput。与专项系统相比，SparseEngine 在 Quest 上比 Vortex 快 1.24 倍、比 HiSparse 快 1.55 倍；SnapKV 比 Tangram 快 1.55 倍。
- **质量保持**：LongBench V1/V2 上 SparseEngine 与原始实现相比平均差异仅 **+0.17 分**（方差 0.32），忠实保持任务质量。
- **Agent 场景**：SWE-bench Lite 上 SnapKV + Chain Cache 在 GLM 达到 24.7% 解决率（vanilla 25.0%），在 Qwen3 上 8.3%（vanilla 5.3%）。端到端 Agent replay 中，SnapKV (Mid) + Chain Cache 获得 **2.24倍** 端到端加速，H2O 达到 1.99 倍。

**一句话总结**：将稀疏推理引擎的抽象边界放在“生命周期契约”而非具体布局或工作流上，是同时支持方法多样性与服务高效性的关键。
