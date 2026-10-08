---
title: 'Beyond Outcome Rewards: Constructing and Assigning Retrieval Credit for Search
  Agents'
title_zh: 超越结果奖励：搜索智能体的检索信用构造与分配
authors:
- Wenyu Huang
- Xinyu Hou
- Pavlos Vougiouklis
- Ruofei Lai
- Jeff Z. Pan
affiliations:
- University of Edinburgh
- Huawei Technologies Research & Development (UK) Limited
arxiv_id: '2610.10179'
url: https://arxiv.org/abs/2610.10179
pdf_url: https://arxiv.org/pdf/2610.10179
published: '2026-10-07'
collected: '2026-10-08'
category: Agent
direction: 搜索Agent强化学习 · 检索信用分配
tags:
- Retrieval Credit Assignment
- RLVR
- Search Agents
- GRPO
- Evidence Coverage
- Process Reward
one_liner: 系统研究检索中间信号在 GRPO 中与动作对齐的信用分配，局部 credit 显著优于 scalar reward shaping
practical_value: '- 在 RLVR 训练搜索/工具调用 Agent 时，不要只给最终答案 F1。把检索证据覆盖等中间信号作为 token-level
  local credit，加到产生该次检索的 query tokens 上，比直接把检索 bonus 加到 trajectory reward 更有效；工程上可在
  GRPO 中保留 outcome advantage，再在 executed query tokens 上叠加 group-relative signed residual。

  - 信号设计要和 credit assignment 联合选择：同一 Cov 信号在 local 下最强，而带依赖约束的 Cov-Dep 更适合 scalar、不适合
  local。业务里如果做子问题/依赖图，建议先验证「不要过度约束」的检索信号在 local 框架下是否更好。

  - 保持 event-action 对齐很重要：把检索增量打乱到同 step 其他 rollout 会掉点，multi-hop 任务掉点更明显（Cov aligned-permuted
  差 2.12，AM 差 3.12）。实现时一定要把 credit 附着到实际产生 evidence 的 tool call tokens。

  - 中间监督主要提升证据获取，而非证据利用；如果业务目标是最终成交/答案质量，除了覆盖奖励还应设计证据使用或推理质量信号，否则可能出现检索更多但答案未见提升。'
score: 9
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：搜索 Agent 需要多跳检索与推理交替，但 RLVR 只给最终答案奖励过于稀疏。两条轨迹可能都拿零答案奖励，即使其中一条检索到了部分证据；于是 evidence 获取差异无法进入训练。中间监督可以改善这个问题，但「给什么检索信号」和「把 credit 分给哪一步」会共同决定训练效果。

**方法关键点**：
- 构建 corpus-grounded 数据：基于 Wikidata relations 组合 chain/conjunction/fan-in 问题，保留 subquestions、supporting passages 和依赖关系；训练集 14k，开发集 1.2k。
- 定义三种检索信号：Cov 覆盖子问题证据；Cov-Dep 在前置节点已覆盖时才给信用；AM 匹配最终答案字串。信号被转化为 retrieval-progress events（新覆盖增量）。
- 对比两种 incorporation：scalar 把累计增量加到 terminal reward 后做 GRPO 标准化；local 保留 outcome advantage，对同 question 同 step 的 rollouts 做 group standardization，将 signed residual 加到 executed query tokens，λ=0.5。
- 进一步消融 credit alignment（permuted vs aligned）和 outcome-group 限制（flat-only / no-flat）。

**关键结果数字**：
在七个 QA benchmark 上，Qwen3-4B 平均 F1：outcome-only 为 51.25；所有中间监督均优于 OO；Cov-local 最高 54.34，Cov-scalar 52.64，Cov-Dep-local 52.96，AM-local 53.51。multi-hop 上 Cov-local 较 OO 提升 4.81。对齐 credit 优于打乱：Cov 差 2.12，AM 差 3.12，multi-hop 更明显。限制仅在 outcome tied groups 给 local credit 会降低收益，说明中间信用不只是解决 tie group 问题。开发集上 Cov-local 平均 coverage 从 27.51% 升到 31.97%，但 coverage-conditioned answer F1 曲线相似，说明主要提升证据获取而非证据利用。

**最值得记住**：检索信号和如何分配 credit 必须联合设计；给到产生证据的那个 action 的局部 token 信用，比泛泛加 reward 更有效，且不要过度约束依赖关系。
