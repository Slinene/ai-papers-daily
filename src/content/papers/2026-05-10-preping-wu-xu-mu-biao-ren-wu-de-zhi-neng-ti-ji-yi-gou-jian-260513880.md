---
title: 'PREPING: Building Agent Memory without Tasks'
title_zh: PREPING：无需目标任务的智能体记忆构建
authors:
- Yumin Choi
- Sangwoo Park
- Minki Kang
- Jinheon Baek
- Sung Ju Hwang
affiliations:
- KAIST
- DeepAuto.ai
arxiv_id: '2605.13880'
url: https://arxiv.org/abs/2605.13880
pdf_url: https://arxiv.org/pdf/2605.13880
published: '2026-05-10'
collected: '2026-05-15'
category: Agent
tags:
- Agent Memory
- Pre-Task
- Synthetic Practice
- Procedural Memory
- LLM Agents
- Tool Use
one_liner: 通过提议者引导的合成实践与验证过滤，在部署前无需任何目标环境任务即可构建可复用程序性记忆
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：LLM agent 在接入新工具环境时，常因缺少环境特定的程序性知识（如工具组合、前置条件、故障恢复策略）而表现不佳。现有记忆构建方法要么依赖离线人工标注任务，要么从部署后的用户交互中在线积累，两者在新环境都会遭遇“冷启动”问题。为此，该工作研究**预任务记忆构建**：在没有见过任何目标环境任务（如人类演示、部署交互）的情况下，仅利用环境文档和工具调用反馈，提前构建可复用的程序性记忆。

**方法关键点**：
- 提出 **PREPING**（Pre-Task REusable Playbook makING）框架，将构建过程解耦为 **提议者记忆（M_prop）** 与 **求解器记忆（M_sol）** 两部分。提议者记忆用于控制合成实践的分布，求解器记忆是最终提供给 agent 部署使用的程序性记忆。
- 迭代循环中，**Proposer** 依据 M_prop 和环境文档生成一批合成任务；**Solver** 执行任务并产生轨迹；**Validator** 对每个任务-轨迹对进行可行性和完成度评分，只有可行性判为“完全可行”（5分）的轨迹才被允许更新求解器记忆。
- M_prop 同时记录实践历史（工具使用频次、失败原因）与**接地环境信息**（从执行中提取的实体、约束），从而引导 Proposer 生成覆盖不足、避免冗余、且可行接地的新任务。求解器记忆更新采用 ACE 的 reflector-curator 蒸馏管道，将轨迹提炼为简明的策略与陷阱要点，避免直接存储原始交互日志。
- 通过联合控制“练习什么”与“存储什么”，PREPING 从自生成实践中过滤掉不可行、冗余的合成任务，仅保留对下游有指导价值的程序性知识。

**关键结果**：
- 在 **AppWorld**（有状态应用）、**BFCL v3**（函数调用）和 **MCP-Universe**（MCP 服务器）三个基准上，PREPING 显著超过所有无任务经验的记忆构建方法，相比无记忆基线平均得分提升 **17.1 / 19.3 / 5.4** 点，且性能与使用离线或在线任务数据的 **ACE-Offline/Online** 相当甚至更优。
- 消融实验表明，**验证器门控** 是防止记忆污染的关键；**实践历史** 扩大了工具覆盖率（AppWorld 唯一 API 数从 69.0 升至 81.7），**环境信息** 确保任务接地可行，三者组合达到最佳。
- 将 PREPING 作为在线记忆构建的初始化（PREPING+ACE），进一步将 AppWorld 平均分从 71.3 提至 76.3，并大幅缓解了冷启动早期的失败率。
- 部署成本角度，PREPING 通过冻结的预构建记忆避免了在线更新调用，比 **ACE-Online** 的部署成本降低 **2.99×**（AppWorld）和 **2.23×**（BFCL v3），且只需约 30~50 个合成任务即可逼近在线方法的性能。

**核心洞见**：智能体记忆可以从被动等待部署交互转向主动的、受控的环境实践，通过联合优化练习分布与记忆质量，在无任务经验的情况下显著缓解冷启动问题。
