---
title: 'From Retrieved Context to Runtime Control: Adaptive Compression for Edge-based
  RAG'
title_zh: 从检索上下文到运行时控制：边缘RAG的自适应压缩
authors:
- Zlatan Feric
- Amir Taherin
- Yanzhi Wang
- David Kaeli
affiliations:
- Northeastern University
arxiv_id: '2608.19535'
url: https://arxiv.org/abs/2608.19535
pdf_url: https://arxiv.org/pdf/2608.19535
published: '2026-08-20'
collected: '2026-08-23'
category: RAG
direction: RAG上下文压缩与边缘推理优化
tags:
- Edge RAG
- Context Compression
- Energy Efficiency
- Inference Optimization
- Adaptive Systems
one_liner: 实测边缘RAG中固定压缩率不可靠，中间压缩率可降GPU能耗53.2%且质量损失可忽略，主张遥测驱动的自适应压缩
practical_value: '- 在电商/广告的RAG型助手、搜索摘要或智能客服中，检索到的商品/内容上下文越长，prefill与KV cache成本越高；可引入LLMLingua-2等轻量压缩器先剪枝，再进入大模型生成。

  - 不要用固定压缩率：按query长度、上下文冗余度、当前GPU/SoC能耗或尾延迟预算动态选择压缩率，中间档位往往比固定高压缩更划算。

  - 把压缩器自身的延迟与能耗计入总账；端侧或边缘部署时，只有当生成节省明显大于压缩开销才启用，7B-8B模型下生成约占90%延迟，值得压缩。

  - 可采集设备telemetry（GPU功耗、KV cache占用、QPS）作为运行时策略输入，在低负载时少压缩保质量，高负载或省电模式时提高压缩率。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：RAG通过外部文本grounding提升回答质量，但检索上下文会拉长prompt，增加prefill计算、KV cache占用、内存流量、延迟与能耗。上下文压缩能缓解该问题，但现有方法多采用固定压缩预算或离线选好压缩率，推理时静态执行，忽略工作负载波动和边缘设备实时状态；且边缘SoC上压缩器与生成共享算力，压缩自身开销可能抵消收益。

**方法关键点**：在NVIDIA Jetson AGX Thor上，用Llama与Qwen生成器、Natural Questions和HotpotQA数据集，结合LLMLingua-2压缩器，系统测量不同压缩率下的延迟、GPU/SoC能耗与回答质量，刻画压缩-收益权衡区间，并提出用设备telemetry和工作负载特征做运行时自适应压缩策略。

**关键结果**：7B-8B生成器中，生成阶段占单query约90%延迟、约91% GPU能耗；过轻压缩错失能耗优化机会，过重压缩损伤回答质量；中间压缩率可最高降低GPU能耗53.2%、SoC能耗48.2%，同时质量损失可忽略。因此固定离线压缩率不具鲁棒性，自适应策略更适合边缘RAG部署。
