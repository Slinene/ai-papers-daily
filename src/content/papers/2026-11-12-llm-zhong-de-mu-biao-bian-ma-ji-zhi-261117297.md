---
title: Goal Encoding in LLMs
title_zh: LLM 中的目标编码机制
authors:
- Arnab Sen Sharma
- Eric Todd
- Sheridan Feucht
- Andy Arditi
- Rohit Gandikota
- Natalie Shapira
- Gabriele Sarti
- Constanza Fierro
- Lisa Schut
- David Bau
affiliations:
- Northeastern University
- Parallax
- University of Copenhagen
- University of Oxford
arxiv_id: '2611.17297'
url: https://arxiv.org/abs/2611.17297
pdf_url: https://arxiv.org/pdf/2611.17297
published: '2026-11-12'
collected: '2026-11-14'
category: Reasoning
direction: LLM 目标编码 · 内部表征定位
tags:
- goal encoding
- mechanistic interpretability
- attention heads
- causal intervention
- non-recurrent goal-seeking
one_liner: 在 LLM 内部定位到编码下一子目标的稀疏注意力头，并提出非循环目标寻求机制解释其持续性
practical_value: '- 在构建多步 LLM Agent（如选品策略、活动规划、自动生成推荐文案）时，可借鉴 NRGS 机制：在每步 prompt 中显式重述总体目标与当前剩余子任务，让模型对比已完成的进度，而不是依赖隐式记忆，可能提升长程任务完成率。

  - 可解释性监控：定位与子目标相关的注意力头后，可在 Agent 运行中实时监控这些头的激活模式，判断模型当前“意图”，用于异常检测或提前干预，且只需训练轻量探针，无需修改模型。

  - 跨场景迁移：目标编码具有可塑性，移植到不同环境可触发相应操作，提示在多垂直业务（如不同品类推荐策略）中可尝试共享目标编码子空间，通过少量适配实现策略迁移。

  - 注意该研究在受控编码任务中进行，迁移到开放域电商 Agent 需先验证；可借鉴其构造受控子任务来评估 Agent 的目标坚持能力以辅助迭代设计。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：LLM 是否真正在内部编码目标，而非仅模仿人类语言中的意图表达？该研究旨在区分行为层面的目标导向与内部显式表征，在可控编码任务中检验目标编码的存在与机制。

**方法关键点**：构造包含多个子任务的编码环境，评估目标寻求与子目标选择；通过在稀疏注意力头输出中定位下一子目标的线性编码，发现这些头可解码未来动作的自然语言描述（如“我正在检查是否为回文”）；验证该编码对下一动作具有因果作用，且具有可塑性：将其移植到另一编程语言环境会触发相同操作但使用不同 token 序列；进一步探讨编码的持续性——transformer 无循环结构无法跨层携带状态，因此提出非循环目标寻求（NRGS）机制：模型频繁从任务规范中重读目标，与上下文中可见的进度对比，追求剩余部分，并通过定向因果干预验证该预测。

**关键结果**：定位到一组稀疏注意力头编码下一子目标；因果干预这些头可改变后续动作选择；目标编码可跨环境移植；NRGS 解释得到因果实验支持，表明 LLM 通过反复读取目标与进度比较来维持目标状态，而非依赖循环状态。
