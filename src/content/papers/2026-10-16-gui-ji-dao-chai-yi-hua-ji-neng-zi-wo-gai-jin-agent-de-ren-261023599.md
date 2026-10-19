---
title: 'From Trajectories to Differentiated Skills: Cognitive Differentiation for
  Self-Improving Agents'
title_zh: 轨迹到差异化技能：自我改进 Agent 的认知分化
authors:
- Yewei Zhao
- Derong Xu
- Wei Chen
- Yin Xu
- Peilun Zhou
- Xiaohan Wang
- Guojun Yin
- Wei Lin
- Mingjun Xiao
affiliations:
- University of Science and Technology of China
- Meituan
- City University of Hong Kong
arxiv_id: '2610.23599'
url: https://arxiv.org/abs/2610.23599
pdf_url: https://arxiv.org/pdf/2610.23599
published: '2026-10-16'
collected: '2026-10-19'
category: Agent
direction: Agent 技能自进化 · 功能分化
tags:
- Agent Skills
- Self-Improvement
- Cognitive Differentiation
- Trajectory Learning
- Skill Evolution
- LLM Agents
one_liner: 提出 CDSE 将轨迹提炼为 Meta/Experience/Tool/Script 四类功能分化组件，统一维护与自适应调用，在 36 个评测设置中全面超越既有技能进化方法
practical_value: '- 在构建电商/广告领域的 Agent 技能库时，不要把所有经验写进一个大 prompt 或文档，而是按 Meta/Experience/Tool/Script
  拆分；例如商品运营 Agent 中，Meta 管任务规划和停止条件，Experience 管类目/活动上下文的启发规则，Tool 管具体 API 调用注意事项，Script
  管可复用的数据清洗/报表脚本。

  - 从成功和失败轨迹中提取“语义梯度”时，要求每条更新附带轨迹证据行，先做证据过滤和因果定位，再保留；可借鉴用于自动从客服对话、运营操作日志中挖掘可复用规则，减少无证据的泛泛总结。

  - 对可执行脚本类知识引入独立验证和自测，未通过验证不进库；这可以避免自动化流程中错误脚本污染后续任务。

  - 采用描述可见的自适应调用：在组件加载前提供简短 scope/触发条件/预期收益描述，让 LLM agent 自主选择何时加载哪个组件；实验表明零加载也能通过描述影响行为，适合在
  prompt 预算有限时做渐进式披露。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有轨迹驱动的 agent 技能进化方法通常以技能文档、记忆条目或技能库等 artifact 边界为单位组织知识，但忽略了单个技能内部的功能异质性：同一条执行轨迹可能同时产生任务级控制、上下文启发式、工具操作指导和可执行脚本等不同功能知识，需要的表示、更新和验证方式不同。作者对 500 个高排名技能包的分析显示 96.8% 包含至少两类功能内容，说明传统单一文档组织方式不匹配实际需求。

### 方法关键点
- CDSE 将统一技能状态拆为 Meta（任务级控制）、Experience（上下文启发式与恢复）、Tool（工具选择与操作指导）、Script（可执行程序及验证契约）四个组件。
- 通过 Outcome-Contrastive Semantic Gradient Discovery 从成功/失败轨迹中提取带证据支持的“语义梯度”；成功轨迹识别可保留行为和脆弱点，失败轨迹定位决定性错误和最小恢复。
- Cognition-Guided Gradient Consolidation 通过保留门控过滤无证据/实例特定/冗余梯度，并按功能角色分配主/次组件。
- 组件特定更新：Meta/Experience 维护原子规则，Tool 按工具类别维护，Script 需实现、自测并通过独立验证；再经跨组件协调解决冲突，并用描述重写实现自适应调用，让 agent 在加载前看到组件 scope/适用条件/预期贡献。

### 关键结果
在 OfficeQA、SpreadsheetBench2、SealQA、LiveMathBench、SWE-Pro、AutomationBench 六个基准上，用 GLM-5.2、DeepSeek-V4-Flash、MiniMax-M3 和 Claude Code/Codex，CDSE 在全部 36 个设置中取得最高分，平均超过 Base 7.6 pp，超过每项设置中最强基线 2.6 pp。消融表明功能分化贡献最大；Script 在 SpreadsheetBench2 调用率仅 6% 但移除导致 8 pp 下降；跨模型迁移 11/12、跨 harness 12/12 有效；多轮进化第一轮收益占比最大；token 效率每 pp 提升成本最低。

### 最值得记住的一句话
技能进化不应按文档边界组织知识，而应按功能角色（Meta/Experience/Tool/Script）分别维护、验证和调用，这样同一批轨迹经验可以沉淀到正确位置，获得更高效的 Agent 自我改进。
