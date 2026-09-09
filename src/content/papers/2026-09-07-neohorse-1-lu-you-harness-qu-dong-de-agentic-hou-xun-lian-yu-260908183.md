---
title: 'NeoHorse-1: Towards Recursive Self-Improvement via Agentic Post-Training with
  Routing Harness'
title_zh: NeoHorse-1：路由 Harness 驱动的 Agentic 后训练与递归自改进
authors:
- NeoHorse Team
- Guoliang Cao
- Guohao Dai
- Tianyu Guo
- Kai Han
- Hailin Hu
- Zihan Jiang
- Xiang Kuang
- Boxun Li
- Yulong Li
affiliations:
- TokenRhythm
arxiv_id: '2609.08183'
url: https://arxiv.org/abs/2609.08183
pdf_url: https://arxiv.org/pdf/2609.08183
published: '2026-09-07'
collected: '2026-09-09'
category: Training
direction: Agent 后训练 · 路由驱动的课程与蒸馏
tags:
- Agentic Post-Training
- Recursive Self-Improvement
- Routing Harness
- On-Policy Distillation
- Curriculum Learning
- LLM Agent
one_liner: 通过路由 harness 记录能力需求并构建三阶段课程与蒸馏，实现 4B/9B agent 模型的递归自改进后训练闭环
practical_value: '- 利用线上多模型路由日志自动构建训练集：记录每次请求的预测能力需求、选择的模型档位和交互轨迹，形成天然的难度标签；电商/广告场景中可在低成本小模型与大模型路由架构上持续积累数据，定向提升小模型能力。

  - 三阶段课程由路由信号组织，先易后难进行 SFT，再衔接 on-policy distillation；相比直接 SFT，让学生模型在自身生成分布上被教师纠正，可稳定提升
  agent 工具调用和推理一致性，适合推荐/搜索 agent 的复杂指令跟随。

  - 数据准入的多维评估（结构校验 + 六维语义评分 + 子场景标注）值得借鉴：在构建推荐/搜索 agent 的交互数据时，过滤低质量轨迹，避免污染训练集，尤其对工具调用格式和上下文依赖敏感的场景。

  - 建立 evaluation→mixture allocation 的闭环：用评测反馈动态调整下一轮训练数据的任务配比，适合多任务持续迭代的电商 Agent
  平台（如商品推荐、广告文案、客服工具混合）。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：递归自改进（RSI）需要具体机制，将系统对自身能力的观察转化为下一轮学习信号。部署中的路由 harness 天然包含这种机制——每次用户轮都记录能力需求预测、选择的服务层级和后续交互结果。

**方法**：NeoHorse-1 构建异构模型池 + 智能路由，把每轮交互转化为保留推理、工具调用和 harness 上下文的训练样例。数据经过结构验证、六维语义评估和子场景标注后准入。路由信号用于组织三阶段 SFT 课程，并扩展到路由引导的 on-policy 蒸馏：教师在同样的阶段进展下监督学生生成。最后，能力引导的分配将评测反馈转为下一轮训练混合，闭合 evaluation–selection–update 循环。

**结果**：在 11 个基准上，后训练将 4B 模型宏平均从 58.94 提升到 64.87，9B 模型从 65.60 提升到 69.04，显著缩小了后训练 4B 模型与 9B 基座模型的差距。
