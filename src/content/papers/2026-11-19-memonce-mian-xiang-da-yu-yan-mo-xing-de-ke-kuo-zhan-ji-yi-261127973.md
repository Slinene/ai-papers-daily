---
title: 'MemOnce: A Scalable Memory Architecture for Large Language Models'
title_zh: MemOnce：面向大语言模型的可扩展记忆架构
authors:
- Chang Nie
- Chaoyou Fu
- Songlin Liu
- Yiqing Hu
- Caifeng Shan
affiliations:
- Nanjing University
- University of Science and Technology of China
arxiv_id: '2611.27973'
url: https://arxiv.org/abs/2611.27973
pdf_url: https://arxiv.org/pdf/2611.27973
published: '2026-11-19'
collected: '2026-11-23'
category: LLM
direction: LLM 长程记忆架构 · KV cache 压缩
tags:
- Memory Architecture
- KV Cache Compression
- Long-Context
- Sparse Attention
- Linear-Time Inference
- LLM
one_liner: 通过末层状态子集缓存与单次稀疏检索动态解码为各层KV，实现线性推理和恒定活跃记忆，1M上下文缓存降低1313倍并超越full-context
  baseline
practical_value: '- 在电商/推荐的长用户行为序列建模中，可借鉴 MemOnce 的做法：只保留末层隐藏状态的尾部 1/8 token 作为紧凑记忆，而非逐层存
  KV；通过轻量 MLP 按层解码还原 KV cache，几乎不损失效果下将显存降低一个数量级，适合在现有 LLM 推荐模型上加装长期记忆。

  - 检索索引只计算一次并跨所有层复用，避免每层重复路由和 CPU-GPU 通信；论文中单次检索比 M+ 快 12 倍、比 RAG 管线快 17 倍，对 Agent
  记忆或 RAG 选段有直接借鉴价值——可一次性选出 top-K 相关记忆，统一注入各层。

  - 将持久记忆分为 local short-term 窗口和 sparse long-term pool，活跃子集常驻 GPU（约 25MB），其余 offload
  到 CPU/SSD；对于需要处理 1M token 级用户序列的在线推荐系统，可用类似架构实现近恒定显存、线性 prefill 和稳定吞吐。

  - 后训练适配时冻结 backbone，仅训练轻量投影和 LoRA（只在编码记忆时激活），避免灾难性遗忘；在向已有电商/广告 LLM 添加用户长期记忆或外部知识时，可采用这种低风险适配方式。'
score: 8
source: huggingface-daily
depth: full_pdf
---

动机：
在长程交互和持续推理场景下，标准 Transformer 需要逐层保存 token 级 KV cache，GPU 显存随上下文线性增长、注意力计算二次增长；线性架构虽然压缩到固定大小但丢失细节，无法准确回忆细粒度信息。如何同时实现准确回忆、线性推理和有限 GPU 缓存是一个核心问题。

方法关键点：
- Memory encoder-decoder：只缓存 final-layer hidden states 中每个 segment 的尾部 1/r（例如 r=8）token 作为紧凑记忆表示，通过轻量 MLP 按层解码为 KV cache，实现跨深度和时间维度 Lr× 压缩。
- Memory sparse attention：每次新增输入只执行一次 top-K 检索，选出相关长期记忆；检索索引跨所有注意力层和解码步共享；活跃记忆由 K 个长期表示 + 短期窗口组成，大小保持常量，其余持久记忆可卸载到 CPU/SSD。
- 混合骨干默认使用 GDN 线性块与 Memory Sparse Attention 交错；预训练时端到端联合优化，后训练时冻结 backbone，只训练轻量投影和 LoRA（仅在记忆编码时激活）。

关键实验：
- 从 150M 到 1B 预训练，MemOnce r=8 在 WikiText 和 LAMBADA 上 perplexity 接近或优于 Transformer，下游零样本平均准确率 52.35/52.63，超过 GDN、YOCO、SWA 等。
- 在 Qwen3.5-4B 上适配后，5 个记忆 benchmark（MemBench、LoCoMo、LongMemEval、PersonaMem-128/1M）平均得分 60.07%，超过 full-context baseline 的 54.30%（+5.77%），并大幅领先 M+（41.39%）、Metis（27.80%）。
- 1M 上下文下 memory state cache 降低 1313 倍，prefill latency 降低 6.9 倍，吞吐提升 3.5 倍；在 32K memory load 下通用推理平均 65.98，与基座相比无灾难性遗忘。
- 零样本表示能力：在 8 个检索 benchmark 上 Recall@10 69.21，超过 BGE-M3 65.60；作为 reranker 可将 A-MEM 代理记忆系统提升 +17.2 点。

最值得记住的一句话：
缓存末层尾部 1/8 状态作为全局记忆，每次查询只检索一次并按层解码成 KV，同时共享稀疏索引，是兼顾长程记忆和推理效率的可规模化架构范式。
