---
title: 'TokenPilot: Cache-Efficient Context Management for LLM Agents'
title_zh: TokenPilot：双粒度缓存高效的智能体上下文管理
authors:
- Buqiang Xu
- Zirui Xue
- Dianmou Chen
- Chenyang Fu
- Chiyu Wu
- Caiying Huang
- Chen Jiang
- Jizhan Fang
- Xinle Deng
- Yijun Chen
affiliations:
- Zhejiang University
- University of Electronic Science and Technology of China
- Xi'an University of Electronic Science and Technology
- HomologyAI
arxiv_id: '2606.17016'
url: https://arxiv.org/abs/2606.17016
pdf_url: https://arxiv.org/pdf/2606.17016
published: '2026-06-14'
collected: '2026-06-16'
category: Agent
direction: Agent的上下文缓存管理
tags:
- Context Management
- Prefix Caching
- LLM Agents
- Cost Efficiency
- Lifecycle-Aware
one_liner: 通过前缀稳定化和残值驱动的驱逐实现缓存感知的上下文管理，大幅降低长时程LLM代理推理成本
practical_value: '- **前缀稳定化**：将系统提示中的动态变量（如工作目录、时间戳）替换为静态占位符，并将工具定义移至提示尾部，最大化跨轮次KV缓存命中。可直接应用于多轮对话式推荐助手，降低每次推理的预填充成本。

  - **带安全网的观测压缩**：对工具返回的环境消息（HTML、终端输出等）进行规则化瘦身和去重，同时保留恢复工具，允许代理在需要时拉取完整内容。类似思路可运用于电商Agent的页面抓取和处理，减少冗余token但不丢失关键信息。

  - **残值驱动的生命周期管理**：不立即清除已完成子任务的上下文，而是通过轻量估计器评估其剩余价值，只有在不再被后续任务依赖时才批量驱逐。这种保守策略能维持缓存连续性，适用于长期运行的商品搜索或营销任务流。

  - **缓存感知的成本建模**：评估上下文管理时，应直接统计缓存命中与未命中的token数，而非仅看总输入token，以此指导系统优化，使成本降低体现在实际计费上。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：LLM代理在长会话中不断累积工具调用、推理轨迹和执行结果，上下文膨胀导致每次推理的输入token激增。现有方法通过文本压缩或动态内存驱逐来削减token量，但这些序列变动破坏了提示前缀的连续性，使得KV缓存频繁失效，预填充成本抵消甚至超过了文本压缩节省的花费。因此，如何在实现文本级稀疏的同时保持缓存连续性，成为降低代理运行成本的关键问题。

**方法关键点**：
- **Ingestion-Aware Compaction（全局摄入感知压缩）**：在上下文摄入边界进行布局优化。通过将系统提示中的易变字段（如代理ID、工作目录、时间戳）替换为静态占位符，并将工具定义后置，保证前缀从第一轮起字节一致；对环境反馈（如HTML、日志输出）实施规则化降噪和去重，配合内容哈希和恢复工具，实现安全的有损压缩。
- **Lifecycle-Aware Eviction（局部生命周期感知驱逐）**：以批处理方式（每B个轮次）调用轻量估计器（Qwen3.5-35B-A3B）监控上下文段的残值，让已完成段落经历active→completed→evictable的保守状态流转，仅在残值归零时批量清除，从而避免频繁的单个轮次驱逐打乱缓存布局。

**关键结果**：在PinchBench和Claw-Eval两个基准上，与LLMLingua-2、SelectiveContext、LCM、Pichay、MemoBrain、MemOS等十种基线对比。隔离模式下，TokenPilot的总推理成本分别降低61%和56%（PinchBench: \$3.22 vs Vanilla \$8.31, Claw-Eval: \$2.27 vs \$5.16），同时任务性能不降甚至更优（PinchBench Overall 81.0 vs Vanilla 80.5）。连续模式下，成本降幅更为显著（PinchBench: 61%, \$2.79 vs \$7.24; Claw-Eval: 87%, \$10.58 vs \$81.52），缓存未命中token大幅减少。消融实验显示，仅前缀稳定就减少60%以上的缓存未命中token，残值驱遣避免了过度清除，维持了高缓存命中率。
