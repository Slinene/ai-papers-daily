---
title: 'Theory of Mind and Persuasion Beyond Conversation: Assessing the Capacity
  of LLMs to Induce Belief States via Planning and Action'
title_zh: 超越对话的心智理论：评估LLM通过规划行动诱导信念的能力
authors:
- Ben Slater
- Matteo G. Mecattaf
- Lucy G. Cheke
- John Burden
- Winnie Street
affiliations:
- University of Cambridge
- Prolific
- Google
arxiv_id: '2606.31916'
url: https://arxiv.org/abs/2606.31916
pdf_url: https://arxiv.org/pdf/2606.31916
published: '2026-06-30'
collected: '2026-07-01'
category: Agent
direction: Agent 心智理论评估与规划能力
tags:
- Theory of Mind
- Agentic Evaluation
- NCP-ToM
- Planning
- GPT-5
- Human Benchmark
one_liner: 提出非对话规划心智理论（NCP-ToM）评估框架，GPT-5在约80%任务中成功诱导信念，超越人类
practical_value: '- **Agent 规划能力评估**：在电商推荐Agent开发中，可借鉴NCP-ExploreToM框架设计多步骤规划测试，评估Agent是否具备通过环境交互（如调整推荐展示顺序、控制推送时机）来塑造用户偏好的能力。

  - **真假信念对齐信号**：模型在诱导真信念上成功率更高，暗示可据此设计安全约束——确保推荐Agent的目标是引导用户形成真实偏好而非虚假期望，降低误导风险。

  - **自主 Agent 需主动评估**：论文强调被动问答不适用于自主 agent，对搜索推荐系统同样适用：应构建 agentic 场景下的离线评测，而非仅依赖静态数据集指标，例如模拟用户动态信念更新的推荐环境。

  - **复杂推理与规划结合**：任务要求多步逻辑推理（如物体可见性、角色知识限制），对构建能处理多约束、多目标规划的商品组合推荐或广告投放策略 agent 有启发，可引入类似的符号关系推理微调方案。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：现有 LLM 心智理论（ToM）评估依赖被动问答，无法衡量自主 agent 通过行动（而非对话）主动诱导其他智能体信念的能力。这种非对话规划心智理论（NCP-ToM）对用户助手、劝导场景及安全对齐至关重要。

**方法**：提出 NCP-ExploreToM 框架，设计 600 个任务实例，要求模型在虚拟环境中移动物体或指引角色进入房间，以实现特定的信念状态目标（真/假信念）。评估了 GPT-5、Gemini 2.5 Pro、Claude 4 系列及人类对照组的完成率与鲁棒性。

**关键结果**：GPT-5 在 agentic 设置下成功率达约 80%，是唯一超越人类的模型，但场景鲁棒性仍弱于人类。所有模型（含人类）在诱导真信念任务上表现更好，表明 AI 较少有意欺骗，有利于安全对齐。研究突显 LLM 已涌现非对话的社会推理能力，并呼吁采用 agentic 评估以理解自主社会 agent 的能力与风险。
