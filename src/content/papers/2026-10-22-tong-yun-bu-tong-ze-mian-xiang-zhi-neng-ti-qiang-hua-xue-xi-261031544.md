---
title: 'Same Luck, Different Choice: Twin-World Credit Assignment for Agentic Reinforcement
  Learning'
title_zh: 同运不同择：面向智能体强化学习的孪生世界信用分配
authors:
- Zeropy Surio
- Tobias Engel
- Mei-Lin Chou
- Anika Raman
- Samuel Okafor
affiliations:
- University of Sheffield
- Carnegie Mellon University
- University of Michigan
arxiv_id: '2610.31544'
url: https://arxiv.org/abs/2610.31544
pdf_url: https://arxiv.org/pdf/2610.31544
published: '2026-10-22'
collected: '2026-10-23'
category: Training
direction: Agent RL 训练 · 反事实信用分配
tags:
- credit assignment
- counterfactual
- Gumbel noise
- RL
- agentic search
- variance reduction
one_liner: 共享 Gumbel 噪声的孪生世界实现 turn 级反事实信用分配，方差降为 1−ρ 倍，7 个 QA 基准平均提升 5.3/4.5 点 EM
practical_value: '- 在 LLM Agent 或多轮交互推荐中，固定检索/工具/打分等确定性组件，引入 keyed Gumbel noise 做
  counterfactual rollout，评估某个 query 改写、工具调用或推荐 action 的增量收益；twin 共享下游噪声可把方差降为 (1−ρ)
  倍，以更少样本判定方向。

  - 预算分配采用「predicted discordance / cost」平方根规则：对分歧大且便宜的决策多分 twin，对必成功/必失败的 prompt/trajectory
  少分；实际可用 logistic 模型预测分歧概率，配合 Horvitz-Thompson 加权保持无偏。

  - 信用回传可组合：token-level advantage = trajectory-level GRPO advantage + 标准化 twin credit（A_t
  = A_traj + ω Â_t/σ̂），简单有效；在电商搜索 Agent 中可将最终成交/点击奖励回传给关键 query、是否继续搜索、最终回答等 action，减少好决策被失败
  episode 误罚。

  - 工程上 keyed noise 作为 logits processor 开销约 2%；self-twin 和 same-evidence shortcut
  能省大量 auxiliary tokens；注意 live web/stateful API 需缓存或替换为确定性版本，否则耦合减弱但无偏性仍保留。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**
Agentic RL 只给 episode 级奖励，GRPO 将标量广播到每个 token，PPO 需要训练 critic，二者都无法准确回答“如果当时换一个 query/action，这次 episode 会不会成功”。独立反事实分支虽然直接比较不同决策的 outcome，但分支的后续采样噪声与事实轨迹独立，导致 outcome 差异混杂了决策效应和运气差异；事实轨迹自身的运气无法平均消除，信用估计存在方差下限，判定大小为 Δ 的 advantage 需要 Θ(Δ⁻²) 次 rollout。作者观察到 agentic search 中 retriever、corpus、grader 均确定，episode 是策略决策与采样噪声的确定性函数，因此可通过共享噪声构建 twin world。

**方法关键点**
- 用 Gumbel-max 采样，将噪声按 (episode, turn, line, position) 键控，使 twin 与事实轨迹共享下游噪声且每条轨迹仍是 π 的精确采样；keyed noise 作为 logits processor 仅增加约 2% 生成时间。
- 对事实决策 (s_t, y_t) 抽取 alternative y′，用事实后续 keys 继续 rollout 得到 twin utility U′，差异 D_t=U−U′ 为 turn-level advantage 的无偏估计；通过 self-twin 和 same-evidence shortcut 节省生成。
- 按概率 q_t ∝ sqrt(predicted discordance / cost) 分支，用 Horvitz-Thompson 加权保持无偏，实现方差最优的 rollout 预算分配。
- Token-level advantage 为 GRPO trajectory advantage 与标准化 twin credit 的加权和，仅 actor 部署。

**关键结果数字**
在 7 个 QA 基准（NQ, TriviaQA, PopQA, HotpotQA, 2Wiki, MuSiQue, Bamboogle）上，Qwen2.5-3B/7B 平均 EM 分别达 42.7/46.5，比 GRPO 高 5.3/4.5 点，比最强基线 AT2PO 高 1.7/1.7 点；token 成本为 GRPO 的 1.70×，比 VinePPO 少 68% auxiliary tokens。信用审计中 wrong-sign 从 CRR 的 21.7% 降至 6.9%，与 oracle advantage 的相关性从 0.46 升至 0.72。消融显示 coupling 贡献最大（去掉后 −1.5 点、反转率 ×3），预算规则再 +0.8。

**最值得记住的一句话**
把采样噪声当作可重放的随机数，用 twin world 共享下游运气，信用分配从估计均值变成检测差异。
