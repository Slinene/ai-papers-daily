---
title: 'ParaVT: Taming the Tool Prior Paradox for Parallel Tool Use in Agentic Video
  Reinforcement Learning'
title_zh: ParaVT：驯服并行视频工具调用的工具先验悖论
authors:
- Zuhao Yang
- Kaichen Zhang
- Sudong Wang
- Keming Wu
- Zhongyu Yang
- Bo Li
- Xiaojuan Qi
- Shijian Lu
- Xingxuan Li
- Lidong Bing
affiliations:
- MiroMind
- Nanyang Technological University
- The University of Hong Kong
- Hong Kong University of Science and Technology (Guangzhou)
- Tsinghua University
arxiv_id: '2605.20342'
url: https://arxiv.org/abs/2605.20342
pdf_url: https://arxiv.org/pdf/2605.20342
published: '2026-05-18'
collected: '2026-05-26'
category: Agent
direction: Agent 多智体协作与工具调用优化
tags:
- Parallel Tool Calling
- Tool Prior Paradox
- GRPO
- Multi-Agent RL
- Video Understanding
one_liner: 首个并行视频工具调用多智能体RL框架，识别并解决工具先验悖论导致的格式崩溃与工具跳过问题。
practical_value: '- **工具先验悖论处理**：当使用预训练已有工具能力的模型做 RL 微调时，会出现格式崩溃（例如标签错误）和跳过工具的捷径。可借鉴
  PARA-GRPO 的探索锚定技术：对关键格式标记（如 `</think>`、`</answer>`）施加额外奖励，并用约束生成强制开头标记，稳定结构化输出。在电商
  Agent 中，若模型需要生成 API 调用格式，可以类似地对调用标签进行强化。

  - **并行工具调度设计**：从串行工具调用转为并行调度，能避免错误传播、降低上下文膨胀、实现固定延迟。在推荐系统多路召回或 Agent 多工具并行执行场景中，可以设计主代理一次调度多个子系统并行工作，并聚合结果，提高效率和容错。

  - **nFrames Gating 创造工具必要性**：通过随机控制输入的信息量（如减少概览帧），强制模型在部分样本上必须使用工具，避免奖励黑客行为。此法可迁移到检索增强场景：在训练
  Agent 判断是否需要检索时，可随机删除部分文档，确保不使用检索的答案得分低，从而强化检索动机。

  - **串行轨迹转并行数据构造**：将串行工具调用轨迹合并为单轮并行调用，并用文本总结替代原始输出，既对齐训练格式又控制上下文长度。对于电商操作数据（如搜索、点击、加购），可将顺序操作按独立性合并成并行动作轨迹，用于训练多任务
  Agent。'
score: 9
source: huggingface-daily
depth: full_pdf
---

**动机**：在长视频理解中，现有工具增强方法采用串行调用（一次一个裁剪），错误会逐步传播，多轮上下文累积污染，且推理耗时随调用次数线性增长。并行工具调用可缓解这些问题，但直接应用 RL 训练会遇到 **工具先验悖论**：预训练模型自带的工具调用能力（先验）在温度采样下会导致结构化格式崩溃（如标签错误），同时许多问题无需工具就可回答，RL 策略会收敛到跳过工具的捷径，使工具学习失败。

**方法关键点**：
- **ParaVT 框架**：主智能体单轮发出 K 个并行 `crop_video` 调用，派发给 K 个权重复用的子智能体，各自返回文本摘要，主智能体聚合证据后作答。并行调度提供对等纠错、控制上下文增长、限制推理延迟。
- **工具先验悖论诊断**：通过 Qwen3-VL（强先验，格式崩溃但工具调用）与 Qwen2.5-VL（弱先验，格式完美但零工具调用）的跨模型对比，确认预训练工具先验是格式崩溃与工具探索的共同驱动力。
- **PARA-GRPO 算法**：包含两个组件。**探索锚定**：在 `</think>` 等关闭标签位置施加选择性奖励（α, β, γ），并用受限生成固定开头 `<think>
`，稳定格式而不限制内容；**nFrames Gating**：每样本随机选择概览帧数 n∈{4,8,16,32,64}，低 n 时概述不足以直接回答，创造工具调用奖励差距，解决必要性缺口。
- **数据配制**：97K 多任务 SFT 数据（30% 含工具调用），通过合并独立串行调用并替换帧响应为文本摘要，构建单轮并行轨迹；4.4K RL 数据覆盖开放式 QA、选择题、时域接地点。

**关键结果**：在六个长视频基准上，ParaVT-8B 相对 Qwen3-VL-8B 平均提升 **+7.9%**，LongVideoBench +15.7%，LVBench +20.2%。训练时格式奖励从 0.13 升至 **0.64**，工具调用率维持在 0.21，避免了两极分化。并行调度相比串行在全部基准上提升。

**记住**：工具先验悖论是提升模型工具使用能力的核心矛盾，PARA-GRPO 通过锚定格式和门控工具必要性，为工具增强的 Agent RL 提供了可泛化的训练方案。
