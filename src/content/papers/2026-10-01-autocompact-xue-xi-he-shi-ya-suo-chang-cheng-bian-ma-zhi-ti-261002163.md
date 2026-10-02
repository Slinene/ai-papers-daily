---
title: 'AutoCompact: Learning When to Compact Context in Long-Horizon Coding Agents'
title_zh: AutoCompact：学习何时压缩长程编码智能体上下文
authors:
- Xuan Zhang
- Longtao Zheng
- Cunxiao Du
- Bo An
- Xin Dong
affiliations:
- Singapore Management University
- Nanyang Technological University
- Harvard University
arxiv_id: '2610.02163'
url: https://arxiv.org/abs/2610.02163
pdf_url: https://arxiv.org/pdf/2610.02163
published: '2026-10-01'
collected: '2026-10-02'
category: Agent
direction: 长程 Agent 上下文主动压缩
tags:
- Context Management
- Coding Agents
- Proactive Compaction
- Reinforcement Learning
- SWE-bench
one_liner: 训练编码智能体主动决定何时压缩上下文、保留什么工作状态以及如何继续，显著提升长程任务成功率
practical_value: '- **主动压缩而非长度触发**：在长程多轮Agent（如电商导购、搜索Agent）中，可引入类似`compact()`的工具，让模型在任务阶段转换时主动总结上下文，而非等到窗口将满；证明即使上下文未溢出，主动压缩也能提升效果。

  - **Judge-guided在线纠错数据收集**：用更强模型作为judge在线审查agent的每个动作（压缩时机、摘要内容、后续行动），并执行纠正后的动作继续轨迹，能高效收集示范数据，尤其当目标行为在基座模型中很少出现时。

  - **RL联合优化压缩与任务执行**：使用最终任务成功作为唯一奖励，同时优化压解决策、摘要生成和压缩后行动，无需额外的压缩专用奖励；实现上将轨迹按上下文重写点分段，各段共享advantage，简单有效。

  - **摘要自一致性检查**：除信息覆盖外，还要求摘要记录的状态与提出的下一步行动一致；在业务中可借鉴此标准评估Agent生成的中转状态质量。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

## 动机
长程编码智能体在解决仓库级软件工程任务时，轨迹累积大量代码、工具输出和中间发现，其中很多信息随任务推进变得过时。保留全部历史会填充上下文，但下一阶段只需要紧凑的工作状态。现有上下文管理方法要么基于长度触发（等到窗口快满才压缩），要么只教何时压缩却忽视压缩后如何继续行动。AutoCompact训练智能体将压缩作为策略的一部分，同时学习何时压缩、保留什么、如何从压缩状态继续。

## 方法关键点
- **模型可调用的`compact()`动作**：在工具集中加入主动压缩动作，模型可在任意步骤调用，替换历史为带`# Auto Context Summary`的工作状态摘要。
- **Judge-guided在线纠错数据收集**：基座模型很少主动压缩，因此用GPT-5.5-Codex作为judge在线审查每一步提案，对三类错误进行纠正：触发时机、摘要内容、压缩后行动；纠正后的输出被实际执行，使轨迹继续，得到1,052条高质量轨迹。
- **两阶段训练**：先用纠错轨迹做SFT，学习基本压缩行为；再用GRPO进行结果奖励RL，以最终任务通过与否为唯一奖励，联合优化编码与压缩，无需额外奖励塑形。
- **RL中的轨迹分段**：由于`compact()`会重写上下文前缀，将轨迹按重写点拆成多个段，所有段共享同一advantage，token级损失在整个批次上平均。

## 关键实验
在SWE-bench Verified和SWE-PolyBench Verified上，AutoCompact分别比Base模型提升9.2%和5.0%的pass rate；主动压缩方法在256K上下文中（无溢出）普遍优于全历史基座；在预算受限（$0.10-$4.00）下，AutoCompact在所有预算点均优于Base和SFT版本，且在低预算下优势更大；忽略压缩动作（仅训练但不执行压缩）会导致性能下降，证明执行压缩本身贡献了部分收益；RL后摘要缺失关键状态和下一步行动的比例从3.1%和8.2%降至0.2%和2.2%。

## 最值得记住的一句话
压缩不是上下文管理问题，而是Agent策略的一部分：必须同时学习何时压缩、压缩出什么工作状态、以及如何从该状态可靠地继续行动。
