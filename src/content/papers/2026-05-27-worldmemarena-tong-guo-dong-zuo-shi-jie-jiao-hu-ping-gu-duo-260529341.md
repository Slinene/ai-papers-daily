---
title: 'WorldMemArena: Evaluating Multimodal Agent Memory Through Action-World Interaction'
title_zh: WorldMemArena：通过动作-世界交互评估多模态Agent记忆
authors:
- Chengzhi Liu
- Yuzhe Yang
- Sophia Xiao Pu
- Yepeng Liu
- Lin Long
- Yichen Guo
- Nuo Chen
- Zhaotian Weng
- Elena Kochkina
- Simerjot Kaur
affiliations:
- University of California, Santa Barbara
- J.P. Morgan Chase
- ETH Zurich
- Stanford University
- Johns Hopkins University
arxiv_id: '2605.29341'
url: https://arxiv.org/abs/2605.29341
pdf_url: https://arxiv.org/pdf/2605.29341
published: '2026-05-27'
collected: '2026-05-29'
category: Agent
direction: 多模态 Agent 记忆评估
tags:
- Multimodal Agent
- Memory Evaluation
- Action-World Interaction
- Memory Lifecycle
- Benchmark
one_liner: 提出将多模态Agent记忆建模为动作-世界交互循环，构建覆盖写入、更新、检索、使用四阶段诊断的基准
practical_value: '- 记忆评估应分解为写入、更新、检索、使用四个阶段，避免仅看最终问答分数，帮助在电商对话Agent中精确定位失败点（如偏好更新延迟、证据检索错误）。

  - 多模态记忆（商品图、界面截图）不可简单压缩为文本，需保留视觉细节，否则关键信息丢失会直接影响推荐与问答质量。

  - 记忆维护需支持修订和遗忘，而非单纯追加；电商中用户兴趣变化、商品状态更新等需及时覆盖，防止过时知识干扰决策。

  - 自管理记忆（harness）更灵活但成本高，可结合场景采用混合策略：核心任务用结构化记忆，长尾交互尝试自主管理，平衡效果与开销。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机** 现有Agent记忆评估以静态对话为主，只看最终问答准确率，无法诊断记忆在写入、更新、检索、使用各环节的失效，且忽视多模态输入和动态交互对记忆的压力。随着Agent开始自建记忆，缺乏统一的四阶段诊断基准。

**方法关键点**
- 将多模态Agent记忆形式化为**动作-世界交互循环**，并定义可观察的四阶段生命周期：观察-写入、更新-整合、检索决策、使用-行动。
- 构建 **WorldMemArena** 基准：400个多会话任务，覆盖**终身演化**（个人/项目状态变化）和**Agent执行**（真实轨迹中的观察-动作-反馈），平均每任务18.4个会话、9.1K tokens，包含24,258个QA对和15,595张图片。
- 每个会话标注gold memory points、状态更新点、干扰点及证据链，支持按阶段诊断。
- 统一对比三类记忆范式：长上下文模型、人工设计的记忆系统（RAG、MemGPT等）、基于harness的记忆Agent（OpenClaw、Codex）。

**关键实验**
- 高**记忆存储召回**不一定带来高QA正确率：Qwen3-VL-Embedding存储召回86.2%但QA正确率仅51.86%；MemGPT存储召回85.2%却达到57.81% QA正确率。
- **多模态记忆仍是瓶颈**：系统在视觉搜索、跨模态推理上性能显著下降（平均QA正确率约0.33-0.55）。
- **更新与干扰拒绝普遍较弱**：多数系统更新时间处理正确率约57-59%，干扰拒绝率仅22-32%，倾向追加而非修订。
- **Agent执行比终身演化更难**：系统在Agentic Execution任务上QA正确率比Lifelong Evolution低约0.15-0.25。
- Harness记忆Agent（OpenClaw+GPT）QA正确率48.31%，低于部分手动系统但更灵活，不过token消耗和推理成本显著更高。

**值得记住的一句话** 强记忆存储不等于可靠决策；记忆应被当作通过交互不断演化的能力，而非可独立优化的静态模块。
