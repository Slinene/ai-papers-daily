---
title: 'OSWorld2.0: Benchmarking Computer Use Agents on Long-Horizon Real-World Tasks'
title_zh: OSWorld 2.0：面向长周期真实任务的计算机使用智能体基准测试
authors:
- Mengqi Yuan
- Zilong Zhou
- Xinzhuang Xiong
- Weiming Wu
- Jiayang Sun
- Jiamin Song
- Kaiqian Cui
- Bowen Wang
- Haoyuan Wu
- Yitong Li
affiliations:
- XLANG Lab
arxiv_id: '2606.29537'
url: https://arxiv.org/abs/2606.29537
pdf_url: https://arxiv.org/pdf/2606.29537
published: '2026-06-27'
collected: '2026-06-30'
category: Agent
direction: 长周期多步骤Agent评测基准
tags:
- benchmark
- computer-use-agent
- long-horizon
- GUI-agent
- real-world-evaluation
one_liner: 提出108个长周期真实工作流基准，暴露前沿智能体在约束追踪、流式交互与隐含状态推理上的严重不足
practical_value: '- 长周期、多步骤的Agent评测设计：可借鉴其构建包含动态环境变化、用户中途改需求、跨源信息整合的评测用例，用于压力测试推荐或对话Agent在实际业务流程中的稳定性。

  - 强调隐含状态追踪与跨源推理：推荐Agent常需结合用户历史、实时上下文和外部知识，可专门设计评测环节检验Agent是否具备“从历史中恢复隐含约束”的能力，避免遗漏关键条件。

  - 安全审计视角：引入任务执行后的安全合规检查（如越权操作、隐私泄露），对面向用户的电商Agent有直接借鉴意义，可在上线前自动化审计高风险操作。

  - 工程启示：智能体在长流程中容易丢失约束、跳过验证，提示我们需要在工程实现中增加显式的状态摘要、中间检查点和响应性用户询问机制，而非仅依赖模型自身记忆。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有计算机使用基准缺乏对真实长周期工作流的覆盖，无法有效揭示前沿智能体的真实局限。

**方法**：构建OSWorld 2.0，包含108个跨日常与专业领域的长周期任务，每个任务模拟一个端到端真实工作流（中位人工耗时约1.6小时）。任务刻意引入先前基准中被忽视的挑战现象：流式交互、动态环境变化、跨源推理、隐含状态推断、视觉空间精确操作等。评测过程使用真实的输入工件和有状态的用户画像文件，并包含独立的安全审计报告。

**关键结果**：在500步条件下，Claude Opus 4.8（最大思考模式+批处理工具调用）仅完成20.6%的任务（部分得分54.8%），GPT-5.5虽更节省token但完成率仅13%。失败主要源于智能体丢失长期约束、忽略中途到达的新信息、猜测而不向用户确认、以及跳过验证步骤，而非基础GUI控制或代码能力不足。

这表明当前智能体距离专业级计算机使用仍有较大差距，尤其在必须从隐藏状态中恢复关键信息的任务上表现最差。
