---
title: 'SpatialClaw: Rethinking Action Interface for Agentic Spatial Reasoning'
title_zh: SpatialClaw：以编程为行动界面的空间推理Agent
authors:
- Seokju Cho
- Ryo Hachiuma
- Abhishek Badki
- Hang Su
- Byung-Kwan Lee
- Chan Hee Song
- Sifei Liu
- Subhashree Radhakrishnan
- Seungryong Kim
- Yu-Chiang Frank Wang
affiliations:
- NVIDIA
- KAIST
arxiv_id: '2606.13673'
url: https://arxiv.org/abs/2606.13673
pdf_url: https://arxiv.org/pdf/2606.13673
published: '2026-06-10'
collected: '2026-06-12'
category: Agent
direction: Agent 设计 · 代码作为行动界面
tags:
- Agent
- Spatial Reasoning
- Code as Action
- VLM
- Tool Use
- Iterative Reasoning
one_liner: 提出以Python代码作为行动界面，在持久内核中迭代组合感知工具，显著提升开放式空间推理性能。
practical_value: '- **Code as Action 替代固定工具调用**：在 Agent 设计中，用 Python 代码生成代替 JSON/XML
  结构化工具调用，可动态组合基础 API（分割、重建、计算）完成任意复杂任务。电商场景的智能客服或商品属性提取 Agent 可借鉴，让模型根据问题实时编写数据处理代码，而非受限于预定义工具列表。

  - **持久化内核支持观察-修正循环**：将执行环境设为持久化 Python 内核，中间变量、可视化结果跨步骤保留。推荐系统的在线调参或分析环节可引入类似机制：每步执行后保留状态，Agent
  根据输出反馈修正后续步骤，避免一次性提交全部分析策略。

  - **通用计算库赋能动态组合**：工具设计为普通 Python 可调用对象，同时预加载 NumPy/SciPy/Matplotlib，使 Agent 无需专属工具即可用基础运算实现统计、空间索引等需求。生成式推荐中，可让
  Agent 在召回、排序阶段动态组合检索策略与重排逻辑，利用通用库实现临时的指标计算。

  - **无微调的泛化 Prompt 工程**：系统提示编码领域通用推理原则（如“用度量计算代替像素估计”、“多证据交叉验证”），而非任务特定示例，跨 20 个基准和多个模型家族均有效。构建电商多模态
  Agent 时，可提取通用规则提示，降低每个新任务的手动适配成本。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：空间推理（判断物体三维位置、关系、运动）仍是 VLM 的薄弱环节。现有工具增强 Agent 虽引入感知模块，但行动界面（action interface）严重制约其灵活组合与迭代修正能力——单次代码执行需在未知中间结果时提前规划全部策略，结构化工具调用（JSON/XML）难以表达测试时才确定的复杂操作组合。

**方法关键点**：
- **核心思想**：将代码视为行动界面 (Code as Action)，让 VLM 在持久化 Python 内核中分步编写可执行单元，每步根据文本输出、变量摘要和渲染图像反馈调整。
- **持久内核**：预加载输入帧、感知工具（SAM3 分割、Depth Anything 3 重建）和标准库，所有中间结果（mask、深度图、坐标数组）作为普通 Python 变量保留，后续步骤可随时检查、组合或修正。
- **五步循环**：规划（单独 LLM 会话生成分析大纲）→ 代码生成（结构化输出 reason/purpose/code）→ 安全执行（AST 沙箱检查）→ 反馈组装（stdout、变量摘要、`show()` 注册的图像）→ 答案提交（`ReturnAnswer()`）。
- **通用提示设计**：系统提示仅编码通用空间推理原则（如“优先使用度量计算”、“检查数值合理性”、“交叉验证证据”），无任何基准或模型专属调优。

**关键实验**：
- 在 20 个空间推理基准上评估，涵盖静态/动态 3D/4D 任务。SpatialClaw 平均准确率 59.9%，比近期空间 Agent SpaceTools 高 +11.2 个百分点；在 Qwen3.5、Gemma4 等 6 个不同量级骨干（27B-397B）上一致提升，无需适配。
- 消融实验：移除所有预定义工具包装器后性能几乎持平（56.4% vs 56.9%），仅保留科学库和感知原语即可；完全去除感知工具后仍比无工具基线高 +2.7%，证明接口本身带来增益。
- 分析显示 50% 以上的胜利归因于代码组合能力（链式调用、控制流），且 Agent 自发根据问题类型选择合适数学原语（距离类用 KDTree，方向类用点积）。

**核心启示**：行动界面的设计对 Agent 推理能力影响巨大，灵活的代码 + 持久环境可解锁“观察-修正”循环，性能提升远超单纯增加工具数量。
