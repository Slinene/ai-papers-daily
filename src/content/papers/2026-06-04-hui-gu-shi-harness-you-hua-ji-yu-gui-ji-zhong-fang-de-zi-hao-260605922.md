---
title: 'Retrospective Harness Optimization: Improving LLM Agents via Self-Preference
  over Trajectory Rollouts'
title_zh: 回顾式 Harness 优化：基于轨迹重放的自偏好提升 LLM Agent
authors:
- Wenbo Pan
- Shujie Liu
- Chin-Yew Lin
- Jingying Zeng
- Xianfeng Tang
- Xiangyang Zhou
- Yan Lu
- Xiaohua Jia
affiliations:
- City University of Hong Kong
- Microsoft Research Asia
arxiv_id: '2606.05922'
url: https://arxiv.org/abs/2606.05922
pdf_url: https://arxiv.org/pdf/2606.05922
published: '2026-06-04'
collected: '2026-06-10'
category: Agent
direction: Agent 自进化 · Harness 优化
tags:
- Agent
- Self-supervised
- Harness Optimization
- Trajectory
- Self-preference
- DPP
one_liner: 提出无需标注的回顾式 Harness 优化方法 RHO，通过自偏好对比轨迹选择最佳技能/工具更新，在软件工程、技术等多个领域显著提升 Agent
  表现。
practical_value: '- **无标注的 Agent 自优化管道**：RHO 仅利用过去运行轨迹，通过自比较和自偏好选出最优 harness 更新，完全省去人工构造验证集。电商对话
  Agent、多智体协作流水线可直接借鉴，从历史对话或操作痕迹中自动提炼更好的提示/工具/技能。

  - **DPP 挑选困难且多样样本**：用 Determinantal Point Process 结合难度评分和语义多样性选取核心集，避免只挑困难而忽视类型覆盖。在推荐场景可类比地用于从海量离线日志中选出最具代表性且难例的样本进行复盘优化。

  - **Group Rollout + 双重诊断信号**：对同一任务并行执行多次，通过“自验证”（单条轨迹中的错误步骤）和“自一致性”（多条轨迹间的冲突）提取结构化改进指令。这一技巧可用于推荐
  Agent 的多路召回或结果比较，诊断模型飘移或策略分歧。

  - **Best-of-N Harness 提案与自偏好过滤**：并行生成多个 harness 候选，并用自偏好评分选最优，避免单次编辑的不稳定。工程上相当于多个候选流水线并行评估，可用来做线上策略变更的安全上线。'
score: 9
source: huggingface-daily
depth: full_pdf
---

**动机**：LLM Agent 的 harness（技能、工具、系统指令）决定其解决复杂任务的能力，持续优化 harness 是自适应新任务的关键。现有方法依赖带标签验证集进行迭代搜索，但在真实部署中标注数据难以获取。本文探究仅用 Agent 的历史轨迹（无标签）能否自我优化 harness 以提高未来表现。

**方法关键点**：
- *核心流水线* RHO 分三阶段：① 用 DPP（行列式点过程）从历史任务中选取难度高且语义多样的核心集；② 对每个核心任务并行执行 G=3 次重放，通过**自验证**（轨迹内检查工具误用/早停）和**自一致性**（轨迹间比较发现分歧）提取结构化诊断信号；③ 基于诊断生成 N=3 个 harness 候选，再用 agent 自身对候选轨迹与基线轨迹的成对偏好排名选出最佳 harness。全程不使用外部标签。
- *Harness 表面*：直接编辑配置文件、可执行脚本（工具）和技能文本，比仅增补记忆的方法更灵活。

**关键实验**：在 SWE-Bench Pro（软件工程）、Terminal-Bench 2（技术操作）、GAIA-2（知识工作）上评估。单轮优化后，SWE-Bench Pro 的通过率从 59% 升至 78%（绝对提升 19%），Terminal-Bench 2 提升 5%，GAIA-2 提升 8%。与无需验证反馈的基线（Dynamic Cheatsheet、ReasoningBank、Sleep-time Compute）相比提升显著且一致。与需要验证标签的 Meta-Harness 单轮相比，RHO 用更少的计算量获得更高分数（0.78 vs 0.62），且不在任何阶段使用标签。行为分析表明优化后 agent 在长步骤任务上成功更多，动作模式向频繁验证或新工具使用偏移。诊断信号的消融证明自验证和自一致性缺一不可。
