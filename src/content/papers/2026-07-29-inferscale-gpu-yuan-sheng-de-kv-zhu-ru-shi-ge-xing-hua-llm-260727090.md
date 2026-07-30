---
title: 'InferScale: GPU-Native KV Injection for Personalized LLM Serving'
title_zh: InferScale：GPU 原生的 KV 注入式个性化 LLM 推理系统
authors:
- Peter Li
- Prashant Pandey
affiliations:
- Northeastern University
arxiv_id: '2607.27090'
url: https://arxiv.org/abs/2607.27090
pdf_url: https://arxiv.org/pdf/2607.27090
published: '2026-07-29'
collected: '2026-07-30'
category: LLM
direction: LLM 推理优化 · KV 缓存复用
tags:
- KV cache
- serving optimization
- memory system
- Chunked RoPE
- context-window encoding
- vLLM
one_liner: 通过 GPU 驻留的记忆 KV 缓存与 Chunked RoPE，使 TTFT 几乎不随检索上下文增长，吞吐提升 3.7–4.5×
practical_value: '- 对电商 / 搜索推荐场景中频繁复用的用户画像、历史行为摘要等静态上下文，可离线编码为 KV 缓存，在线直接注入，避免每次请求都重新预填充，大幅降低首
  token 延迟。

  - Chunked RoPE 方法允许记忆块以任意位置组装注入，支持动态检索拼装，适合排序或对话中按查询相关性动态选择用户记忆的场景。

  - 上下文窗口编码可在离线阶段保留记忆块之间的局部依赖，还原近乎联合预填充的准确性，同时保持在线零额外开销；在推荐理由生成或对话式推荐中可提升事实一致性。

  - 实现采用 vLLM 的 KV-connector 接口，无需修改推理引擎或模型微调，易于在现有 LLM 服务栈中集成，降低落地成本。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**：生产级 LLM 应用常需为每个用户维护持久记忆（如长期对话历史、用户画像），现有系统（Mem0、Zep、MemGPT）每次请求都检索并注入记忆文本，导致预填充代价随记忆量二次增长，TTFT 升高，即使记忆内容在多轮间几乎不变。预填充成本浪费在反复计算相同的 KV。

**方法**：核心思想是在注意力层直接注入记忆的 KV 缓存，而非在 token 层注入文本。InferScale 为此提出三个关键技术：
1. **GPU 原生检索与 KV 存储**：记忆事实的语义向量和预编码 KV（保存旋转前 key）同时驻留 GPU，检索和注入均在设备内完成，避免 PCIe 传输和重复预填充。
2. **Chunked RoPE**：存储未旋转的 key，注入时按请求位置重新施加旋转，保证键值能够以任意位置组装，且注意力计算与在原位置预填充完全等价（定理 6）。
3. **上下文窗口编码**：离线编码每个事实时，在其前面拼接若干轮对话上下文，但只缓存目标事实的 KV，使记忆块携带足够的跨句上下文信息，弥补独立编码丢失的交互，恢复接近联合预填充的准确度。
系统作为 vLLM 插件实现，无需改引擎、无需微调。

**关键结果**：在 LoCoMo 长对话问答基准上，使用 Llama-3.1-8B、Mistral-7B、Qwen2.5-7B 测试。随检索预算 k=5→50，InferScale 的 TTFT 几乎不变（Llama: 16.6→17.3 ms，仅 +4%），而 Mem0 增长 106%（33.2→68.3 ms），在 k=50 时 TTFT 降低 72–79%（3.6–4.8×）。端到端延迟同样显著降低。在并发场景下吞吐量可达 Mem0 的 3.7–4.5 倍。通过上下文窗口编码，准确率可恢复至接近 Mem0（Llama-3.1-8B 上 60.3% vs 63.3%），且在较小 k 时甚至反超。KV 存储可卸载至 CPU 只增加约 3 ms，吞吐不受影响。

**一句话**：将检索记忆的预填充换成 GPU 端 KV 注入，并解耦位置与上下文编码，可使个性化 LLM 推理的延迟与吞吐近乎独立于记忆量，且准确率损失可控。
