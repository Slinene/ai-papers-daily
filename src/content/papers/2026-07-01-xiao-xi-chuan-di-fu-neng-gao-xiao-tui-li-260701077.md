---
title: Message Passing Enables Efficient Reasoning
title_zh: 消息传递赋能高效推理
authors:
- Xuecheng Liu
- Daman Arora
- Gokul Swamy
- Andrea Zanette
affiliations:
- Carnegie Mellon University
arxiv_id: '2607.01077'
url: https://arxiv.org/abs/2607.01077
pdf_url: https://arxiv.org/pdf/2607.01077
published: '2026-07-01'
collected: '2026-07-02'
category: Reasoning
direction: 消息传递并行推理与抢占
tags:
- message passing
- parallel reasoning
- preemption
- context efficiency
- Sudoku
- LLM
one_liner: 提出 MPLM 框架，通过持久线程间的点对点消息传递和抢占机制，实现远优于串行 / Fork-Join 的推理扩展效率
practical_value: '- 在多 Agent 协作中采用持久线程与点对点消息传递，避免 Fork-Join 式全局聚合带来的通信瓶颈，可应用于复杂推荐流程的并行子任务调度

  - 引入抢占机制：一旦某个子线程得出确定结论，立即终止其它并行分支，节省推理开销，适合搜索/规划类任务

  - 利用 respawn 压缩上下文，让线程自我总结关键状态后重启，既支持长程迭代又不爆上下文，可迁移到需要多轮协商的 Agent 对话系统

  - 让模型学习何时向谁 send/recv，而非硬编码通信拓扑，使通信模式随任务动态涌现，有助于实现自适应的分布式推理'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**：推理时扩展（inference-time scaling）依赖串行长链式思考（CoT），自回归生成成为计算瓶颈；而 Fork-Join 并行虽能并行化子任务，但所有信息必须通过中心节点聚合，上下文短暂且无法点对点通信，限制了可扩展性。需要一种更分布式的并行推理框架来降低上下文开销并支持灵活协作。

**方法关键点**：
- 引入 **消息传递语言模型（MPLM）**：模型在推理时动态创建持久线程，通过生成特殊指令 `<spawn>/<send>/<recv>/<stop>` 实现线程控制。
- **持久线程 + 点对点通信**：线程保持上下文，仅与必要的邻居通信，避免每次迭代重新构建完整上下文；理论上最大上下文需求从 Fork-Join 的 O(TNM) 降至 O(TkM)（k 为邻居数）。
- **抢占（preemption）**：子线程找到解后可直接通知父线程，父线程提前终止其它分支，减少无效计算。
- **respawning**：线程可自我总结压缩上下文后重启，实现无界推理而不爆窗口。
- 通过轻量级调度器在标准批推理引擎（如 vLLM）上实现并行解码，不需修改模型架构。

**关键结果**：
- **Sudoku**：训练后 MPLM 在 25x25 谜题上达 72% 准确率，而 GPT-5 Pro 仅 20%；串行和 Fork-Join 因上下文爆炸无法扩展至该尺寸。MPLM 的序列 token 和最大上下文缩放指数 α≈1.1-1.2，远低于串行/FJ 的 1.8，表现出质变的扩展行为。
- **3-SAT**：抢占机制使 MPLM 延迟显著低于 Fork-Join，最大加速比达 2.4-3.5 倍。
- **LongBench-v2** 无需训练仅通过提示，MPLM 在 Qwen3-30B-A3B 上比 Fork-Join 基线 RLM 准确率提升 8%（29.9→37.8%），延迟降低 1.7 倍；在更大模型上延迟降低 2.2 倍，准确率持平。

**核心信息**：通过将并行范式从中心化 Fork-Join 迁移到持久线程 + 点对点消息传递，MPLM 在结构化推理和长上下文 QA 上同时取得更高效率与更强扩展性。
