---
title: 'MemOps: Benchmarking Lifecycle Memory Operations in Long-Horizon Conversations'
title_zh: MemOps：长周期对话中记忆生命周期操作的基准诊断
authors:
- Xixuan Hao
- Zeyu Zhang
- Zehao Lin
- Yihang Sun
- Ziliang Guo
- Xichong Zhang
- Yuxuan Liang
- Feiyu Xiong
- Zhiyu Li
arxiv_id: '2607.12893'
url: https://arxiv.org/abs/2607.12893
pdf_url: https://arxiv.org/pdf/2607.12893
published: '2026-07-14'
collected: '2026-07-15'
category: Agent
direction: 对话记忆操作评估
tags:
- memory lifecycle
- benchmark
- long-horizon conversations
- LLM agents
- evaluation
- memory operations
one_liner: 将对话记忆评估从黑盒问答转为显式操作诊断，揭示记忆失败的结构化原因
practical_value: '- **在购物助手/推荐Agent中显式建模记忆操作**：不要只依赖隐式的长期记忆，设计 remember、forget、update、reflect
  等原语，并记录每次操作的范围、触发条件和状态变迁，便于追踪用户偏好演化。

  - **评估记忆系统时分离最终答案与内部状态**：当Agent回答“我上次推荐了什么”时，不仅检查答案正确性，还需验证内部存储的交互历史是否一致，避免错误答案被掩盖。

  - **会话级检索优于逐轮检索**：对于基于检索的记忆系统，维持整个会话的上下文窗口或会话级索引比逐轮检索更可靠，可将此原则用于构建商品浏览会话记忆。

  - **长上下文模型在记忆轨迹重建上弱**：若直接使用长上下文LLM作为记忆载体，需注意其对有序操作序列的遗忘问题，建议结合结构化记忆日志或定期压缩/反思机制。'
score: 8
source: arxiv-cs.CL
depth: abstract
---

**动机**：现有多数长期记忆基准通过下游问答的最终答案正确性来评估，这种黑盒方式混淆了记忆失败的异质原因（未记录事实、记忆绑定错误、更新后仍用旧值），甚至可能奖励依赖不一致记忆状态的正确答案。

**方法关键点**：
- 将对话记忆重新定义为一系列显式的**生命周期操作**：remember、forget、update、reflect 及其组合。
- 构建可控生成管线，将结构化的操作轨迹嵌入长程、任务导向的对话中，并产生黄金操作跟踪与六类探针（相邻证据和长上下文两设置）。
- 每条记忆事件记录触发条件、目标实体、作用域、状态变迁和支持证据，实现操作级诊断。

**关键结果**：
- 在长上下文、检索式、参数式和管理记忆系统上评估发现，会话级检索显著优于逐轮检索。
- 长上下文模型在重建有序记忆状态轨迹上表现明显薄弱。
- 操作级探针能分离纯问答得分无法揭示的失败模式，表明当前系统远未达到一致可靠。
