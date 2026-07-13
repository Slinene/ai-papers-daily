---
title: 'Failure as a Process: An Anatomy of CLI Coding Agent Trajectories'
title_zh: CLI编程代理的失败轨迹：一项过程导向的实证解剖
authors:
- Xiangxin Zhao
- Han Li
- Shuaiting Li
- Tianyi Zhao
- Earl T. Barr
- Federica Sarro
- He Ye
affiliations:
- University College London
- Nanjing University
arxiv_id: '2607.09510'
url: https://arxiv.org/abs/2607.09510
pdf_url: https://arxiv.org/pdf/2607.09510
published: '2026-07-10'
collected: '2026-07-13'
category: Agent
direction: Agent 故障过程分析
tags:
- Agent Trajectory
- Failure Analysis
- LLM Coding Agents
- Process-Oriented
- Empirical Study
one_liner: 首次大规模实证分析LLM CLI编程代理的失败轨迹，发现失败主要由认知错误驱动且早期隐蔽。
practical_value: '- **代理监控引入过程性指标**：不应仅以最终成败评估代理，可借鉴失败轨迹三阶段（onset, evolution, recovery），在推荐/搜索代理的交互过程中实时监测错误征兆，尤其是认知类错误（如错误理解环境状态），在早期步骤插入校验。

  - **早期干预策略设计**：论文指出多数失败在前几步就已埋下伏笔，且修复机会随时间衰减。在电商Agent工作流（如自动选品、广告出价）中，可对前几个动作设置更严格的沙箱验证或人工确认，阻断错误传播。

  - **分阶段日志分析与故障归因**：对线上代理的失败案例进行复盘时，可按执行步骤切片并标注错误类型（epistemic vs. aleatoric），定位“不可恢复点”，用于优化提示或工具描述。

  - **多框架与模型一致性发现**：研究覆盖7个模型、3个coding脚手架，其失败模式具有跨系统一致性，说明某些薄弱点（如对环境状态的误判）是LLM本质缺陷，对多Agent协作系统（如竞品分析、商品信息检索）的可靠性设计有普适参考价值。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

**动机**：LLM编程代理在终端任务中日益普及，现有研究将失败视为最终结果，缺乏对失败如何产生、演变和变得不可恢复的过程性理解。

**方法**：构建首个大规模代理失败轨迹数据集，收集7个前沿模型在3种脚手架（OpenHands, MiniSWE, Terminus2）上的3843条执行轨迹，筛选出1794条完整轨迹，手动标注超6.3万步，提出失败的发生（onset）、演化（evolution）和恢复（recovery）三阶段框架。

**关键结果**：
- 认知错误（epistemic errors，如系统状态误判）是主导性失败根源，远多于偶然错误。
- 失败通常在前几步就已开始，但往往在执行后期才暴露，修复窗口早于问题显现。
- 不同模型与脚手架间失败模式高度一致，表明某些缺陷源于LLM本质局限。
- 建议在早期步骤引入验证与干预机制，而非仅依赖最终结果评估。
