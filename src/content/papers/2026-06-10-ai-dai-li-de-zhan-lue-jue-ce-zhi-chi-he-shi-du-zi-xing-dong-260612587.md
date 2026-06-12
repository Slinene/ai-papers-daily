---
title: Strategic Decision Support for AI Agents
title_zh: AI 代理的战略决策支持：何时独自行动，何时寻求帮助
authors:
- Shayan Kiyani
- Sima Noorani
- George Pappas
- Hamed Hassani
affiliations:
- University of Pennsylvania
arxiv_id: '2606.12587'
url: https://arxiv.org/abs/2606.12587
pdf_url: https://arxiv.org/pdf/2606.12587
published: '2026-06-10'
collected: '2026-06-12'
category: Agent
direction: AI Agent 决策支持与自适应支持调用
tags:
- Decision Support
- Online Learning
- Counterfactual Error Control
- Calibration
- Agentic AI
one_liner: 提出在线自适应算法 SOS，以最小化支持调用次数同时保证反事实漏支持误差可控
practical_value: '- **Agent 工具调用的成本控制**：在电商推荐、客服等 Agent 系统中，外部工具（数据库、知识库、人工审核）调用成本高，SOS
  算法能自适应学习何时真正需要工具，使支持调用率大幅低于 LLM 自主决定基线，同时维持相同或更低的漏支持错误率，可直接嵌入 Agent 推理循环。

  - **在线校准与反事实反馈**：当反馈只能选择性获得（即只有调用支持时才得知其是否必要），随机探索+重要性加权更新阈值的机制可用于推荐系统中延迟或部分可观测的指标优化，例如判断何时需要人工审核高风险的推荐结果。

  - **与现有 LLM 训练解耦的监督层**：该框架作为无模型修改的外层监督，适用于任何黑盒 Agent，无需重训或微调 LLM，即可在线上实现错误率可控的支持决策，适合快速叠加强化已有
  Agent 的可靠性。

  - **分数设计启示**：实验表明使用表示学习的参数化分数（线性探针、锚定分数）比纯置信度分数更稳定高效，尤其在初始信号不可靠时，可通过在线校准逐步改善分离度，为设计
  Agent 中的支持价值估计函数提供实用参考。'
score: 9
source: arxiv-cs.HC
depth: full_pdf
---

**动机**：现代 AI 代理（Agent）在复杂任务中经常需要工具、人工或额外信息支持，但错误的支持调用会带来成本，而不寻求必要的支持又会酿成严重错误。经典决策支持研究多关注人机协作中机器的辅助角色，角色反转后，需要重新思考 Agent 何时应当自主行动，何时必须寻求支持。

**方法关键点**：
1. 将问题建模为**战略决策支持优化问题（SDS-Opt）**：最小化支持调用频率，同时约束“反事实漏支持误差”——即当支持本来可以显著改善输出时 Agent 却未请求的概率。
2. 在群体层面证明最优策略是对“支持价值”做阈值判定。
3. 提出在线算法 **SOS（Strategic Oversight for Support-seeking）**：维护一个支持价值分数（s_θ）和决策阈值 λ_t，通过随机探索（概率 μ）获取部分反馈，利用重要性加权更新阈值和分数参数（校准-on-the-fly），实现分布无关的有限样本误差控制。
4. 三种分数设计：纯置信度、基于冻结嵌入的线性探针、以及以 LLM 自报置信度为锚点的组合分数。分数可通过在线梯度更新，逐步改善。

**实验与结果**：
- 在四个场景（医疗诊断信息收集、WikiSQL 工具使用、VirtualHome 人机规划、MATH 推理协作）上，使用 Qwen-2.5-7B、Gemini-2.5-Flash 和 GPT-4o-mini 三款前沿 Agent。
- 与 LLM 自主决定基线对比，SOS 在匹配相同漏支持误差的前提下，显著降低支持调用率：例如在信息收集任务中，调用率从基线的约 0.6 降至 0.3 以下；在工具使用和推理任务中亦有类似幅度下降。
- 校准-on-the-fly 使表示学习类分数即使从无信息起点也能快速收敛至高效策略；锚定分数在初始锚点准确时可更快降低支持调用率，反之灵活回退。

**核心洞见**：Agent 即便擅长使用支持，也常常不擅长判断何时该用；可借助在线自适应阈值和部分反馈学习，在不修改 Agent 的前提下大幅减少冗余支持调用，同时将关键遗漏风险控制在预定水平。
