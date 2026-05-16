---
title: 'APWA: A Distributed Architecture for Parallelizable Agentic Workflows'
title_zh: APWA：面向可并行化 Agent 工作流的分布式多智能体架构
authors:
- Evan Rose
- Tushin Mallick
- Matthew D. Laws
- Cristina Nita-Rotaru
- Alina Oprea
affiliations:
- Northeastern University
arxiv_id: '2605.15132'
url: https://arxiv.org/abs/2605.15132
pdf_url: https://arxiv.org/pdf/2605.15132
published: '2026-05-14'
collected: '2026-05-16'
category: Agent
tags:
- Multi-Agent
- Parallelization
- Distributed System
- LLM
- Agentic Workflow
one_liner: 提出 APWA，一种将任务自动分解为无干扰子任务并大规模并行执行的分布式多智能体架构，在现有系统失败的场景下实现线性扩展
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

**动机**  
当前基于大模型的多智能体系统（如 AutoGen、Magentic-One）在解决复杂任务时面临推理、协调和计算扩展瓶颈，尤其当任务涉及海量数据或不重叠的子问题时，集中式协调导致串行执行、上下文爆炸或编排失败，无法利用底层并行计算资源。亟需一种能够自动分解任务、支持大规模并行执行且对数据和任务模式无特化假设的分布式架构。

**方法关键点**  
- **核心抽象**：引入 Manager（全局任务分解与编排）、Worker（自治解决子任务）和 Executor（分布式资源调度与容错）三层解耦，Manager 仅维护紧凑的元数据，Worker 拥有完全本地状态，消除中心推理瓶颈。  
- **并行化机制**：通过 *subtask templates* 和占位符机制实现批量子任务定义，Manager 无需逐一构造每个子任务实例，数据规模与任务逻辑解耦。  
- **数据抽象**：*Data Tables* 为 LLM 提供只读、 schema 化的超大规模数据集表示，搭配分析/操作工具，使 Manager 能在不枚举全部数据的前提下推理和重构数据。  
- **动态能力发现**：*Capability Registry* 允许 Worker 在运行时加载领域专用工具或 Agent（如 WebSurfer），Manager 通过预设自动匹配能力，实现任务无关性。  
- **实现**：基于 Ray 框架实现执行器，支持数千个 Worker 并发、自动重试和轻量路由（对简单子任务直接调用 LLM 而非完整 Agent 环境）。

**关键实验**  
在三个并行化基准上评估：PII-300k（结构化 PII 遮蔽，27 类）、SchemaBench（异构文档结构化提取）和 SummaryBench（层次化摘要，三文本规模 166KB–10.5MB）。对比直接 LLM、Magentic-One 和 MegaAgent：**直接 LLM** 在小输入可工作但在 4096 条记录或 10.5MB 文本时 100% 失败；**Magentic-One** 在所有 SummaryBench 实验中全部失败（编排失误或上下文爆炸）；**MegaAgent** 失败率 60–80%，输出质量近乎为 0。APWA 在所有规模下均完成任务，SummaryBench 失败率 0%，PII-300k 扩展至 4096 条时结构/语义分数分别为 0.9/0.544（直接 LLM 0.75/0.162 但仅 512 条），墙钟时间仅从 19s 增至 221s（近 200× 数据量仅增加约 10× 时间）。在 Web 浏览报告合成实验中，APWA 以 100 个 topic 完成时间 595s，质量>0.975，证明其对异构子 Agent 的编排能力。

**最值得记住的一句话**  
APWA 通过 Manager-Worker 的双层规划与大规模并行子任务执行，首次让多智能体系统在数据量远超出单模型上下文窗口时仍能保持高成功率与线性可扩展性，其关键在于**让 LLM 只推理全局元数据，而无需直接处理全量数据**。
