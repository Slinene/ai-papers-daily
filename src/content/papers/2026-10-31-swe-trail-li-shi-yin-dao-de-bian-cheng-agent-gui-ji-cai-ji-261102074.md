---
title: 'SWE-Trail: History-Guided Trajectory Collection for Coding Agent Training'
title_zh: SWE-Trail：历史引导的编程 Agent 轨迹采集
authors:
- Ziming Li
- Lu Yu
- Jiatan Huang
- Qing Cui
- Jun Zhou
- Chuxu Zhang
affiliations:
- University of Connecticut
- Ant Group
arxiv_id: '2611.02074'
url: https://arxiv.org/abs/2611.02074
pdf_url: https://arxiv.org/pdf/2611.02074
published: '2026-10-31'
collected: '2026-11-04'
category: Training
direction: Agent 轨迹采集 · 历史引导分配
tags:
- trajectory collection
- coding agent
- post-training
- SWE-bench
- history-guided
- train-test mismatch
one_liner: 用历史轨迹引导采集资源分配但不进入 agent 上下文，训练收益提升 2.33/1.60 pp
practical_value: '- **可直接迁移到电商/导购/搜索 Agent 的轨迹采集**：为每个 task 维护 prior trajectories
  bank，但不要把这些历史塞进 agent context；用历史作为 collector 侧信号，让 agent 从普通上下文生成动作，避免模型在测试时依赖不存在的外部
  advice。

  - **做分支对比采样**：在历史检测到的关键状态，从同一 checkpoint 并行短执行两个候选动作，用环境反馈/奖励/测试信号选择路线；保留 agent
  原始 reasoning/actions，删除未选分支和 collector 私有事件，保证训练轨迹为连续且无外部信息的单条 rollout。

  - **优先在 mixed histories 上投入采集**：成功/失败都有的任务最值得多做分支比较，stable-solved 和 never-solved
  收益有限；历史规模 5 条 prior attempts 已接近饱和，继续加到 10 条 token 成本增加 66% 但收益很小。

  - **评估数据采集方案时，值得做 H0 和随机化消融**：H0 控制采集管线本身，random detection/random retention 分别检验“在哪里比较”和“保留哪条路线”，能避免把
  resolved 轨迹数量误当成下游训练价值。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
Coding agent 的交互轨迹越来越多被用作 post-training 数据，但同一 issue 独立采样多条轨迹会迅速冗余：后续 rollout 常重复探索相同修复目标。若把历史作为 advice 放入 agent 上下文，训练轨迹会依赖测试时没有的信息，造成 train-test mismatch。

**方法关键点**
- 两阶段设计：离线 compiler 读取某 issue 的历史 Hi 和只读仓库检查，生成冻结的 detector Di、本地比较目标 ui(d)、采样温度 λi；在线 rollout 中 detector 基于动作/观测识别需要额外采集的状态。
- 到达关键状态后，agent 仅从普通上下文采样候选 next actions（不带历史）；SWE-Trail 从同一 checkpoint 并行短暂执行两个候选后缀。
- 用 identity-blind selector 根据 ui(d) 选择更优路线；保留 agent 原始 reasoning/actions，删除未选后缀和私有 collector 信息，训练记录仍是单条连续 trajectory。
- 对 stable-solved / mixed / never-solved 历史定义不同比较规则：mixed 关注成功失败分叉，never-solved 关注重复失败模式。

**实验结果**
在同一 300 个 SWE-rebench V2 issues、每 issue 5 条 trajectories 的设置下，用 GLM-5.1 采集，训练 124B Ling-3.0-flash-base。H5 相对 SeedBank 独立采样在 SWE-bench Multilingual 提升 2.33 pp，SWE-Pro 提升 1.60 pp；无历史的 H0 仅 +0.11 pp；Qwen3-14B-Base 学生模型同样提升 3.11/2.42 pp。随机化比较位置或保留路线均降低收益，Top-5-of-10 后选也不能弥补差异。H10 仅多 +0.22/0.14 pp，但采集 token 增加 66%。

**最值得记住的一句话**
历史的价值不是给模型当 advice，而是告诉采集器在哪些状态下多做比较；动作由 agent 自己生成，训练数据里只留下它自己的决策。
