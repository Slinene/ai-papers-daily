---
title: 'Experience Funnel: A State-Policy Alternating Loop for Self-Evolving Agents'
title_zh: Experience Funnel：自进化智能体的状态-策略交替循环
authors:
- Wenbo Gao
- Zhaomou Song
- Zhiyuan Ji
- Renxi Liu
- Xing Li
- Xianzhi Yu
- Xiaoguang Li
- James Chung-wai Cheung
- Weizhe Lin
- Yaoyuan Wang
affiliations:
- The Hong Kong Polytechnic University
- Huawei
- Renmin University of China
arxiv_id: '2609.08919'
url: https://arxiv.org/abs/2609.08919
pdf_url: https://arxiv.org/pdf/2609.08919
published: '2026-09-08'
collected: '2026-09-09'
category: Agent
direction: 自进化 Agent 状态-策略交替蒸馏
tags:
- Self-Evolving Agents
- State-Policy Distillation
- Skill Distillation
- On-Policy
- Agent RL
- Experience Internalization
one_liner: 用状态-策略交替循环把显式经验渐进蒸馏进参数策略，同时保留快速可编辑状态
practical_value: '- 把线上 Agent 的 prompt/skill 显式状态与模型参数策略拆成两层：先用 held-out 验证门控快速更新
  skill，再离线周期把反复有用的 skill 蒸馏进小模型，降低线上 context 长度和推理成本。

  - 用三态对比（state-free / previous-state / updated-state）挑选要固化的样本，只保留 newly useful 和
  persistently useful 轨迹，避免把噪声或模型已会的行为蒸馏进参数；电商导购/客服 Agent 可用点击、转化等 reward 做类似增量过滤。

  - 做 token-level 归因蒸馏：用有状态/无状态两路概率的 JSD 定位真正被 skill 改变的 token，只给这些位置更高权重，比整条轨迹均匀蒸馏更数据高效，适合把大模型教师或
  prompt 增益迁移到在线小模型。

  - 固化后的策略仍需保留少量 residual state 才能拿到最大值，说明显式信息不能一次性全部内化；实践中应保留轻量 state/skill，待下一轮验证后再决定淘汰或更新。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

动机：Agent 反复交互会积累大量经验。显式 textual state 快、可读、可编辑，但无限增长会带来检索和上下文成本；参数化 policy 紧凑、可复用，但更新慢。关键不是积累更多经验，而是逐步把经验转化为模型能力，同时保留快速适应机制。

方法关键点：
- State-Policy Alternating Loop：交互轨迹先跨轨迹反思，归纳成候选 state edits；用 held-out validation 做门控，只有提升环境级结果才接受。
- Transition-Aware Skill Distillation：对每个样本分别跑 state-free、previous-state、updated-state 三种 rollout，得到 r0、r-、r+；根据 b-, b+ 把样本分为 newly useful、persistently useful、regressive、inactive，只固化前两类。
- Token-level attribution：对选中轨迹，用同一冻结策略在有/无 updated state 下逐 token 计算 JSD 并归一化，作为蒸馏权重，集中学习真正被 skill 改变的位置。
- 训练目标：加权 KL 蒸馏到 state-free student，再叠加 state-free RL reward；候选策略在验证集达标后才提交。

关键实验：在 SearchQA、ALFWorld、WebShop 上，用 Qwen3.5-4B 作为演化策略，Qwen3.5-27B 作为教师。相比 SkillOpt、OPID、SkillRL 等，平均分数达到 57.6%，其中 SearchQA 62.4%、ALFWorld 67.9%、WebShop 42.4%。动态耦合分析显示，co-evolved pair 到最终阶段比同 state 配初始 policy 高 2.2 点；state-free 策略随固化从 58.1% 升到 61.3%。经验选择上，01+11 组合达到 63.0%，未过滤只有 58.9%。

最值得记住的一句话：有效自进化不是积累更多经验，而是持续决定什么应保留为显式状态、什么应固化进参数策略。
