---
title: 'Δτ-Bench: Pushing Agents Toward a Moving Capability'
title_zh: Δτ-Bench：在持续演化的工具生态中评测 Agent 适应能力
authors:
- Shuofei Qiao
- Xuanguang Pan
- Yijun Chen
- Wendi Feng
- Bin Wu
- Runnan Fang
- Yuqi Zhu
- Shumin Deng
- Emine Yilmaz
affiliations:
- Zhejiang University
- University College London
arxiv_id: '2610.34238'
url: https://arxiv.org/abs/2610.34238
pdf_url: https://arxiv.org/pdf/2610.34238
published: '2026-10-24'
collected: '2026-10-27'
category: Agent
direction: Agent 工具生态演化评测与技能管理
tags:
- Agent Benchmark
- Tool Ecosystem
- Skill Management
- Capability Evolution
- MCP
one_liner: 构建可执行演化工具生态基准，并提出 STEWARD 联合维护工具与技能以跟上能力前沿
practical_value: '- 把内部工具/API 生态当作“会演化的能力前沿”：记录 skill-tool 依赖，工具下线只标记 inactive、不删除；接口恢复时可快速
  reactivate，适合推荐 Agent 频繁调用商品、促销、广告接口的场景。

  - 增量技能维护优于全量重建或冻结：从成功轨迹只做局部编辑，维护 token 省 30-40%，且 SR 更高；业务里不要每次接口变更都全量重蒸馏 SOP。

  - 执行时动态 provision tools+skills，而不是一开始灌全量工具列表：先按初步计划给一个小工具集，出现能力缺口再检索和检查 schema，能提高
  tool precision/F1，降低长上下文分心。

  - 监控 Agent 不能只看任务成功，要看相对当前版本最优路径的路径效率 SPE/IDR/DAR：只看成功会掩盖“旧流程仍能跑通但错过更优路径”的退化。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
LLM Agent 作为统一服务入口时，背后往往是一个持续演化的工具生态：部门独立更新、淘汰或替换工具，功能重叠、文档噪声普遍。已有基准通常把工具检索、多轮状态执行、适应变化分开评测，无法回答：Agent 能否在“能力前沿”移动时，主动发现更高效的工具路径，并及时修正积累的程序性知识。

**方法关键点**
- 构建 Δτ-Bench：42 个领域、1,588 个经过执行验证的多轮有状态任务，覆盖 6 个连续生态版本，通过保能力变换（一对一改接口、一对多拆分、多对一合并）生成演化。
- 用动态规划在构造出的实现空间内搜索 step-minimal 和 cost-minimal 参考路径，作为“当前生态最优解”。
- 指标同时考虑结果和效率：SR、工具检索 P/R/F1、Success-weighted Path Efficiency，以及改进发现率 IDR、退化适应率 DAR。
- 提出 STEWARD：三层技能库（planning / atomic / tool skills），基于已验证轨迹做增量维护；按工具可用性标记 active/inactive，保留可复用的旧技能；执行时先给任务视图，遇到能力缺口再动态补 tools/skills。

**关键实验**
- 最强模型或 harness 的 SR 仅 42.27%/41.65%，SPE 不到 30%；工具 recall 可达 90.36%，但 precision 只有 19.90%，说明模型难以排除无关候选工具。
- EvoSkill、AutoSkill、Trace2Skill、SkillOpt 等技能方法在 v1 有初始收益，但生态演化后增益不持续；AutoSkill 在 v3/v5 SR 低于 No Skill，SkillOpt 维护 token 约为其他方法 2-3 倍。
- STEWARD 在所有版本 SR 最高，平均 39.04% vs SkillOpt 36.36%；从 v2 起维护成本最低，baseline 需 1.2-5.5× token；平均 Step/Cost IDR 提升 4.04/3.69 pp，Step/Cost DAR 提升 5.28/4.76 pp。
- 消融显示增量维护优于全量重建和冻结库；动态 skill search 单独作用有限，tool search 能提升 SR 但路径效率弱，两者联合才全面受益。

**最值得记住的一句话**
工具与程序性知识必须作为耦合资源联合维护，只积累 skills 而不绑定工具可用性，无法跟上持续演化的能力前沿。
