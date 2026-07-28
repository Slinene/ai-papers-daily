---
title: 'StateAct: Program State, before Pixels, for Long-Horizon Computer-Use Agents'
title_zh: StateAct：程序状态优于像素的长周期计算机操作智能体
authors:
- Yan Yang
- Xiangru Jian
- Ziyang Luo
- Zirui Zhao
- Yutong Dai
- Ziji Shi
- Hanshu Yan
- Jun Hao Liew
- Silvio Savarese
- Junnan Li
affiliations:
- Salesforce AI Research
arxiv_id: '2607.22798'
url: https://arxiv.org/abs/2607.22798
pdf_url: https://arxiv.org/pdf/2607.22798
published: '2026-07-23'
collected: '2026-07-28'
category: MultiAgent
direction: 程序状态接地的多智能体协作
tags:
- StateAct
- code-first agent
- multi-agent system
- computer-use
- state-grounding
- long-horizon tasks
one_liner: 提出以代码优先、程序状态为接口的多智能体架构，显著提升长周期任务成功率并降低成本
practical_value: '- **智能体接口设计**：在推荐对话智能体中，将底层数据（用户画像、商品库、特征存储）作为主智能体的直接工具，而非仅依赖 UI
  模拟，可以提升执行准确率和效率。

  - **多智能体上下文管理**：主智能体负责流程编排，将复杂子任务（如商品检索、理由生成）交给全新子智能体，避免上下文窗口被历史交互污染，保持核心决策的清晰度。

  - **程序状态验证**：在生成推荐结果后，设立独立的“完成门”智能体，基于数据库状态检查输出格式、必要字段和存储路径，快速发现结构性错误，减少低效的人工审核。

  - **长周期任务分解**：对多轮个性化配置、组合推荐等流程，让子智能体从干净状态开始执行子目标，阻断错误传播，提升整体鲁棒性。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：计算机操作智能体通常依赖屏幕截图感知，但截图是底层程序状态的损失表示，不同状态可产生相同像素，而代码可直接检查修改状态。长周期任务中，感知瓶颈之外还存在操作连贯性和结果验证问题。

**方法**：StateAct 提出代码优先、多智能体架构，将程序状态（文件、后端、DOM）作为主接口。主智能体通过编写执行代码直接操作状态，仅在必要时（28/108 任务，1.1% 步骤）调用 GUI 子智能体进行截图点击交互。独立的“完成门”基于状态验证输出是否正确保存、路径无误。主智能体将子目标交给全新子智能体，保持自身上下文聚焦，避免长步骤累积干扰。

**结果**：在 OSWorld 2.0 上，StateAct 将 Claude Opus binary success 从 20.6% 提升至 26.9%，partial success 从 54.8% 升至 61.6%，且成本降低约 9 倍。纯代码变体（无 GUI 子智能体）仅达 45.9% partial，低于截图基线的 54.8%，表明状态接地将瓶颈从感知转向推理。
