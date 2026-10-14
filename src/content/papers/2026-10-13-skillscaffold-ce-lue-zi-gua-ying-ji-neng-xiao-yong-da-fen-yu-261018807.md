---
title: 'SkillScaffold: Scaffolding Agentic Reinforcement Learning with Policy-Adaptive
  Skill Credit Assignment and Selective Injection'
title_zh: SkillScaffold：策略自适应技能效用打分与选择性注入的 Agentic RL 训练脚手架
authors:
- Wenlin Zhong
- Hao Wang
- Kun Yuan
- Fan Yang
- Jinluan Yang
- Dian Jin
- Xu Tan
- Yiquan Wu
- Kun Kuang
affiliations:
- 浙江大学
- 中国科学院大学
- 快手科技
- 浙江科技大学
arxiv_id: '2610.18807'
url: https://arxiv.org/abs/2610.18807
pdf_url: https://arxiv.org/pdf/2610.18807
published: '2026-10-13'
collected: '2026-10-14'
category: Agent
direction: Agentic RL · 技能训练脚手架
tags:
- Agentic RL
- Skill Credit Assignment
- GRPO
- Policy-Adaptive
- Skill Injection
- LLM Agents
one_liner: 用已有 outcome 轨迹似然差做策略相对技能效用，正门控选择性注入训练期技能，推理时完全免技能
practical_value: '- 在电商导购/搜索 Agent 训练中，可借鉴「训练时注入技能、推理时移除」的 scaffold 思路：线上不依赖技能库或额外检索，避免推理延迟和技能库维护成本；技能只是帮助训练期探索和内部化。

  - 技能效用评估不要用额外环境 rollout，而是复用已有 outcome 轨迹：对比当前策略在 skill 条件与 skill-free 条件下对同一轨迹的
  token 对数似然差。工程上只需缓存 skill-free scores，再对 M 个候选做 M×N 次打分，成本 O(MN)，无环境交互。

  - 采用 positive gate 决定是否注入技能：只有效用估计 >0 才注入，否则保持 skill-free。这比强制注入或只按排名选择更稳定，特别适合稀疏
  reward 的 multi-turn 任务；可将效用作为策略相对信号，与 query 难度、策略当前 competence 关联，实现自适应注入。

  - 技能内部化可复用：让 Generator 和 Executor 共享参数，用环境 reward 更新 Executor、技能效用 detached reward
  更新 Generator，通过联合训练把技能引导的策略吸收进模型参数。对低延迟线上 Agent 很实用，可在训练后丢弃技能生成通路。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：Agentic RL 在长程、稀疏奖励环境中难以发现成功行为；文本技能可将历史交互压缩为可复用指导，但现有 skill-based RL 要么默认技能有益，要么用额外环境 rollout 评估效用，成本高且小样本下不稳定。同时技能收益随 query 和当前策略的 skill-free 能力变化，因此需要低成本的、策略相对的技能信用分配与选择性注入。

**方法关键点**：
- 共享策略分为 Executor 和 Generator：Executor 采样 skill-free Scout 轨迹，Generator 从带 outcome 标签的 Scout 证据生成候选技能。
- 效用估计不额外 rollout：在固定 Scout 轨迹上，比较 Executor 在候选技能条件与 skill-free 条件下 token 的对数似然差 d(s,τ)。按 Scout 组结果聚合：all-success 看成功轨迹的正 d，all-failure 看失败轨迹的负 d，mixed 时成功支撑与失败抑制各占 1/2；anchor 变体仅用一个成功 Scout 的 d。
- 选择效用最高且 >0 的技能注入后续 Post-Scout rollouts；否则保持 skill-free。环境 reward 监督 Executor，技能效用作为 detached reward 监督 Generator，二者用 GRPO 联合优化共享参数。
- 推理时去掉技能通路，完全 skill-free。

**关键结果**：在 ALFWorld、WebShop、ScienceWorld、τ2-Bench 上，SkillScaffold 在 skill-free 推理下优于 GRPO、SkillRL、Evolving-RL 等。ALFWorld 94.8（GRPO 85.6，+9.2），ScienceWorld 77.1（GRPO 72.9，+4.2），τ2-Bench 平均 63.4（GRPO 60.0，+3.4），WebShop 45.1。消融显示去掉 Generator learning、随机选择、去掉正门控、去掉 Executor 注入都会明显掉点。技能注入率自适应：WebShop 12.1%、ScienceWorld 21.3%、τ2-Bench 39.3%，且集中在 all-wrong/mixed Scout 组。技能内部化实验显示后期 skill-free 成功率显著回升。

**最值得记住**：技能不应作为推理期依赖，而应作为训练期策略自适应的脚手架；用已有 outcome 轨迹的似然差做 policy-relative utility，并通过正门控选择性注入，最终通过共享参数把技能吸收进策略。
