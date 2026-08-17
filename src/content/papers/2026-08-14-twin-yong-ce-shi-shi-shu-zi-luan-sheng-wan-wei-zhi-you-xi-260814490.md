---
title: 'Twin: Playing an Unknown Game with a Test-Time Digital Twin'
title_zh: Twin：用测试时数字孪生玩未知游戏
authors:
- Alexy Skoutnev
- Kirill Acharya
- Gaston Longhitano
- Madeleine Udell
- Kevin Ellis
- Iddo Drori
affiliations:
- Stanford University
- Cornell University
- University of Southern California
- Yeshiva University
arxiv_id: '2608.14490'
url: https://arxiv.org/abs/2608.14490
pdf_url: https://arxiv.org/pdf/2608.14490
published: '2026-08-14'
collected: '2026-08-17'
category: Agent
direction: 测试时世界模型推断与规划
tags:
- World Model
- LLM Agent
- Test-time Compute
- Program Synthesis
- Model-Based Planning
- ARC-AGI-3
one_liner: 构建可执行世界模型，强制回放验证和规划后执行，以 93.3 分通关 ARC-AGI-3 23/25 个游戏
practical_value: '- 对高成本真实动作（广告投放、push 打扰、人工客服介入）的探索策略，可借鉴 Twin 的 `replay validation
  + halt-on-mismatch`：用可执行代码模拟用户/市场动态，每次真实动作前强制模型回放历史交互，不一致就修复；执行中逐步校验，一旦预测失配立即停止并收集
  counterexample，避免错误累积放大。

  - 把 `dynamics` 与 `goal/reward` 显式分离，先验证转移模型，再通过假设-测试循环推断目标。在推荐/搜索中，用户意图常不可见，可先假设当前
  session 目标（比价、闲逛、决策），用最小代价提问/推荐验证，而不是等点击或转化 reward 才优化。

  - 让 LLM 生成可执行代码作为世界模型，而非黑盒神经网络，获得可解释、可验证、可 BFS 规划的优势；电商 Agent 可让 LLM 写业务规则或用户模拟器，通过离线日志回放验证，再用于策略推演和路径规划。

  - 计算成本换真实动作数量：平均每个真实动作 224k tokens，但动作数减少约一半。对高价值动作划算，对高并发低风险推荐不划算；可按动作成本与风险决定是否启用
  test-time compute。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

**动机**  
ARC-AGI-3 是交互式网格游戏基准，规则和获胜条件完全未知，直接玩前沿模型仅得 7.8 分。核心挑战不是感知或知识，而是如何从零开始确认“世界如何变化”和“什么算赢”。人类能快速归纳动力学并规划，agent 需要同样的能力。

**方法关键点**  
- Twin 让 coding agent 把游戏写成 Python 可执行 twin：`step(grid, action)->grid` 与 `goal_reached(grid)->bool`。
- 三个 harness 例程：`Validate` 强制 twin 回放整个交互日志，无一失配才允许真实动作；`Explore` 在 dynamics 失败时生成排序的 bug 报告，在 goal 缺失时基于进度信号提出候选目标；`Plan` 在验证后的 twin 内 BFS 找最短路径。
- `ExecuteChecked` 逐个提交动作，实时对比预测与真实下一帧，遇到 mismatch 立即写入日志并冻结真实动作，直到模型修复。
- 目标发现先于 reward：在没有完成信号时，对候选状态构造 goal 谓词，并通过最便宜路径测试；只有关卡完成或精确到达非目标才能确认/排除。

**关键实验**  
在 25 个 ARC-AGI-3 游戏（183 关）上，Twin 得 93.3/100，通关 23 个游戏、179 关；同一 base model 直接玩仅 7.8，off-the-shelf harness 61.1，对比系统 OPINE-World 78.4、Prime Agent 78.3、EWM 63.8。在全部通关的 13 个游戏中，Twin 使用 3,357 动作，低于 OPINE-World 5,367、EWM 5,381、人类参考 7,485。世界模型对已记录 transition 回放 99.4%，对未见 state-action 对精确预测 70.1%，87.2% 的完成关卡第一个目标假设就正确。

**最值得记住的一句话**  
把未知交互环境写成一个可执行程序，强制每次动作前回放验证、执行中遇错即停并用 mismatch 修复模型，是达到人类级动作效率的关键；动力学建模比目标推断更容易。
