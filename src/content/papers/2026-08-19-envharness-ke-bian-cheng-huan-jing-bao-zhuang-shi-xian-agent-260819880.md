---
title: 'EnvHarness: Awakening Static Worlds for Agent Learning'
title_zh: EnvHarness：可编程环境包装实现 Agent 定向学习
authors:
- Chengsong Huang
- Zifeng Wang
- Rujun Han
- Jun Yan
- Yanfei Chen
- Zoey CuiZhu
- Ke Jiang
- Peng Xia
- Han Yu
- Yufan Zhuang
affiliations:
- Washington University in St. Louis
- Google Cloud AI Research
- Google Cloud
- University of North Carolina at Chapel Hill
arxiv_id: '2608.19880'
url: https://arxiv.org/abs/2608.19880
pdf_url: https://arxiv.org/pdf/2608.19880
published: '2026-08-19'
collected: '2026-08-21'
category: Agent
direction: Agent 环境定制与自动化训练
tags:
- EnvHarness
- Environment Design
- LLM Agents
- Skill Learning
- Reinforcement Learning
one_liner: 提出 EnvHarness 可编程层与 EnvRigger 自动诊断循环，将静态环境改造成针对性训练环境，不改底层代码且保留原生验证器
practical_value: '- 可借鉴 EnvHarness 的 Stage/Contract/Chain 包装思路：在不修改现有电商沙盒、对话仿真器等模拟器底层代码的前提下，通过接口层注入初始状态变化、动作约束和观察过滤，低成本生成大量定向训练环境。

  - EnvRigger 的黑盒诊断-生成-验证循环适合迁移到客服/导购 Agent 的弱点修复：记录失败轨迹，自动写出限制快捷操作或强制验证行为的 wrapper
  代码，并通过新鲜 rollout 接受/拒绝，实现策略与环境共演化。

  - 在强化学习训练推荐/搜索 Agent 时，可利用 Contract 屏蔽高奖励但无学习价值的捷径（如直接推荐热门商品），迫使模型探索长尾策略；用 Stage
  预设不同用户状态（新用户、低活跃、购物车状态），覆盖长尾场景。

  - 保留原始 verifier 的做法值得采纳：所有环境改造通过标准 reset/step 接口完成，评估仍使用可信的人工验证器，避免生成式环境带来的评估失真问题。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
LLM Agent 依赖交互环境获取学习信号，但人工构建的环境是静态的：对所有 Agent 一视同仁，无法针对特定策略弱点提供训练信号，且 Agent 提升后环境很快失去教学价值。现有自动生成环境的方法存在领域专用、验证器不可靠、仍为静态等局限。

## 方法关键点
- **EnvHarness 框架**：类比 Agent Harness，将静态环境包装为可定制环境，通过标准 `reset/step` 接口介入，不改动底层逻辑，保留原有人工验证器。
- **三种可组合组件**：
  - **Stage**：通过回放状态操纵动作序列改变初始状态（如藏起目标物体）。
  - **Contract**：重写动作空间、转移函数或观察空间（如屏蔽快捷动作、截断观察）。
  - **Chain**：组合多个基础环境形成长程任务（如连续完成两个子任务）。
- **EnvRigger 自动化**：将目标策略视为黑盒，执行 Observe → Diagnose → Write → Validate 循环。观察成功/失败轨迹，诊断系统性弱点，生成候选组件，用新 rollout 验证，接受/拒绝/修订直至通过。
- 领域无关的接口协议，仅需少量 domain-specific prompt 即可适配不同基准。

## 关键结果
在五个基准四个领域（ALFWorld、WebArena、SWE-bench Verified、OfficeQA、SpreadsheetBench）上评估。
- 技能学习范式下，EnvHarness 环境训练的 Agent 全面优于原始环境，ALFWorld OOD 提升 9.0 点，SWE-bench Verified 提升 2.7 点，同时平均执行步数减少 9.8%（从 53.6 降至 49.6）。
- 在 SWE-bench Verified 上，EnvHarness 超过专用生成器 SWE-smith 2.46 个点。
- 强化学习范式下，ALFWorld 成功率从 81.4 提升至 87.9，WebShop 得分从 75.6 提升至 79.2。
- 环境数量扩展实验表明，EnvHarness 持续上升至 54.79，而原始环境和生成环境趋于平缓。

**最值得记住的一句话**：把环境构建从“重新编写”变成“接口包装”，即可在不牺牲验证可靠性的前提下，让环境与策略弱点共演化。
