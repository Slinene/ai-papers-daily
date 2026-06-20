---
title: 'MemGUI-Agent: An End-to-End Long-Horizon Mobile GUI Agent with Proactive Context
  Management'
title_zh: MemGUI-Agent：基于主动上下文管理的端到端长时域移动GUI智能体
authors:
- Guangyi Liu
- Gao Wu
- Congxiao Liu
- Pengxiang Zhao
- Liang Liu
- Mading Li
- Qi Zhang
- Mengyan Wang
- Liang Guo
- Yong Liu
affiliations:
- 浙江大学
- 快手科技
arxiv_id: '2606.19926'
url: https://arxiv.org/abs/2606.19926
pdf_url: https://arxiv.org/pdf/2606.19926
published: '2026-06-18'
collected: '2026-06-20'
category: Agent
direction: Agent 上下文管理优化
tags:
- GUI Agent
- Context Management
- Long-Horizon
- MLLM
- Proactive
- Mobile
one_liner: 提出 Context-as-Action，将上下文管理作为一级动作压缩历史，让 8B 模型在长时域移动任务上超越更大规模模型
practical_value: '- **长时域任务中引入“折叠历史”机制**：在电商客服、导购 Agent 等多轮交互场景，可将对话历史分为“动作摘要+状态摘要+近期细节”三字段，关键信息不丢失且上下文长度可控，避免
  ReAct 模式下的 token 爆炸与事实稀释。

  - **将上下文管理作为策略动作统一训练**：在推荐对话或任务型 Agent 中，把“忘记/压缩/总结”等上下文操作与业务动作（如查询商品、推券）纳入同一策略模块，端到端
  SFT 可让模型学会主动压缩冗余信息，提升长会话稳定性。

  - **构造结构化动作-上下文标注数据**：可借鉴 MemGUI-3K 构建思路，为 Agent 交互轨迹增补“折叠/保留”等上下文管理标注，用于微调小尺寸模型，使其在长任务中推理成本更低、窗口利用率更高。

  - **小模型通过上下文管理超越大模型零样本**：该工作证明 8B 模型通过主动上下文管理可超越 235B 模型的零样本性能，适合资源受限的电商场景（如端侧智能助手）低成本部署。'
score: 6
source: arxiv-cs.HC
depth: abstract
---

**动机**：现有 MLLM 移动 GUI 智能体在短任务上表现良好，但在需要跨 App、多步记忆的长时域任务中不可靠。根因在于 ReAct 风格提示被动积累每步记录，导致上下文爆炸并稀释跨 App 关键事实。

**方法**：提出 MemGUI-Agent，核心是 **Context-as-Action (ConAct)**，将上下文管理提升为策略输出的一级动作，而非被动追加历史。ConAct 维护三个结构化字段：**折叠动作历史**、**折叠 UI 状态**、**最近步骤记录**，在紧凑上下文中保留关键 UI 事实。同时构建 **MemGUI-3K** 数据集（2956 条轨迹，含完整 ConAct 标注）用于监督训练与分析。

**结果**：用 MemGUI-3K 微调 8B 模型得到 MemGUI-8B-SFT，在 MemGUI-Bench 上达到最佳开源 8B 性能，并泛化到分布外基准 MobileWorld。ConAct 在 150 步时比 ReAct 节省约 1.5K 输入 tokens，帮助小模型超越 235B 大模型的零样本表现。
