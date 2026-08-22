---
title: Inducing Task Models from Computer-Use Traces
title_zh: 从计算机使用轨迹中归纳任务模型
authors:
- Yucheng Jiang
- Zora Zhiruo Wang
- Ruishi Chen
- Diyi Yang
affiliations:
- Stanford University
- Carnegie Mellon University
arxiv_id: '2608.20319'
url: https://arxiv.org/abs/2608.20319
pdf_url: https://arxiv.org/pdf/2608.20319
published: '2026-08-20'
collected: '2026-08-22'
category: Agent
direction: Agent 技能归纳与任务建模
tags:
- Task Model Induction
- Computer-Use Agents
- Hierarchical Decomposition
- Process Mining
- Skill Learning
- Trajectory Clustering
one_liner: 提出 TMI，自动从交错的低层级操作轨迹中分离潜在任务并构建分层目标与控制流模型，显著提升智能体技能迁移
practical_value: '- 在电商客服/运营自动化等 computer-use agent 场景中，可借鉴 TMI 从员工真实操作日志（点击、输入、页面跳转）自动归纳标准作业流程（SOP）及其子目标层次，即使用户同时处理多个任务也能分离，用于构建可复用的
  agent 技能库。

  - 技能迁移路径值得复用：先归纳出结构化任务模型（目标分解+控制流），再将其转化为 agent 可调用的技能或 few-shot 示例；论文显示该方式在 held-out
  任务上相对最强基线提升 30.0%，说明结构先验对泛化有帮助。

  - 任务模型同时包含目标层次和执行流程，比端到端 policy 更可审计、可解释，适合风控/合规要求高的电商自动化流程（如营销活动配置、订单异常处理）。

  - 低层事件抽象成步骤、再聚类/归纳分层目标的做法，可作为用户行为序列建模中从点击流恢复用户意图/任务的参考，辅助电商场景下的多会话用户建模与 query 理解。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**
自然发生的计算机使用轨迹（被动记录的截图、鼠标/键盘事件）蕴含大量未文档化的工作知识，但现有方法假设任务已知或单一工作流，只能生成步骤摘要，无法处理真实工作中多线程、目标交错的低层级事件流。

**方法关键点**
TMI 分两阶段：
1. **潜在任务发现**：从无约束轨迹中自动识别并分离并发的潜在任务，解决多线程交错的挑战；
2. **任务模型构建**：对每个潜在任务，归纳一个配对的任务模型——包含递归目标分解的层级目标模型（objective model），以及组织执行顺序的过程模型（procedure model/控制流）。

该过程不依赖预设任务标签，能把低层键鼠操作抽象为结构化、可审计、可复用的任务表示。

**关键结果**
- 在受控的人类与 agent 轨迹上，TMI 恢复交错任务与 ground-truth 分组的一致性达到 **0.974**；
- 对观察到的执行步骤重建率为 **74.9%**，远超最强工作流归纳基线；
- 外部评估中，基于 TMI 任务模型提取的技能在 held-out 任务准确率上相对最强基线提升 **30.0%**。
