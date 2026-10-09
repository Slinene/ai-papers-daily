---
title: 'SuperNav: An Agentic Navigation System for Any Task in Any Scene'
title_zh: SuperNav：面向任意任务与场景的智能体导航系统
authors:
- Jinkai Zhang
- Jingyi Xu
- Yuanhong Yu
- Jiarui Guo
- Ruizhen Hu
- Hujun Bao
- Xiaowei Zhou
- Sida Peng
affiliations:
- Zhejiang University
- Shenzhen University
- Causa Robotics
arxiv_id: '2610.12126'
url: https://arxiv.org/abs/2610.12126
pdf_url: https://arxiv.org/pdf/2610.12126
published: '2026-10-07'
collected: '2026-10-09'
category: Agent
direction: Agent 具身导航系统
tags:
- Agent
- MLLM
- Navigation
- Tool Use
- Visual Pointing
- Zero-shot
one_liner: 提出无需导航微调、以工具解耦决策与执行的 MLLM 智能体导航系统，实现任务与场景泛化
practical_value: '- 架构上解耦决策大脑与执行工具：不针对导航任务微调 MLLM，而是通过 agent harness 调用工具，保留通用推理与场景理解能力。对应推荐系统可将
  LLM 作为 planner，将召回/排序作为工具，避免微调导致通用知识遗忘。

  - 用 visual-point interface 让模型直接在图像上指定目标坐标，而非生成文本描述位置。在多模态推荐或广告素材分析中，可让模型在商品图/场景图中
  point 出兴趣区域，作为 grounding 信号辅助推荐解释或素材优选。

  - 引入 Navigation Skills 和任务进度管理：显式维护任务状态与目标进度，并在执行反馈后允许模型 revise 决策。在电商 Agent 长链路任务（如导购、多轮商品比较）中，可设计
  checkpoint 状态和重规划机制，提升任务成功率。

  - 工具与技能抽象：将底层运动封装为可调用的技能，模型只需高层决策。在电商 Agent 中可将搜索、筛选、加购等操作封装为工具，降低模型输出复杂度，提高动作可靠性。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：通用服务机器人需在陌生环境处理多样的人类请求，需同时具备任务泛化与场景泛化。现有方法通过微调多模态大模型直接预测导航动作，行为受导航训练数据覆盖限制，对新请求与环境泛化不足。

**方法关键点**：核心思想是让 MLLM 专注请求解读、场景理解与决策，保留其通用能力，将运动执行委托给导航工具。SuperNav 在不进行导航特定微调的前提下，为预训练 MLLM 配备专用 agent harness。harness 包括：Navigation Skills（导航技能）、面向智能体的物理交互 Tools、任务进度与上下文管理。统一 visual-point 接口允许模型直接在图像中指定目的地，并根据执行反馈修订决策。

**关键结果**：SuperNav 在实例级、多目标和需求驱动任务上超过四个基线；在 HM3D 上完成类别级评估，并在真实四足机器人上部署，验证了跨环境适用性。
