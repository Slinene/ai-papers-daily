---
title: Reconciling Process Supervision with Outcome-Based Credit in Agentic Policy
  Optimization
title_zh: 协调过程监督与结果奖励信用：智能体策略优化 TASPO 框架
authors:
- Jingxiao Yang
- Wangjie Gan
- Yingxuan Zhuang
- Wenqi Zhang
- Jintao Chen
- Xuhong Zhang
affiliations:
- Zhejiang University
arxiv_id: '2608.31077'
url: https://arxiv.org/abs/2608.31077
pdf_url: https://arxiv.org/pdf/2608.31077
published: '2026-08-31'
collected: '2026-09-01'
category: Agent
direction: Agent RL 信用分配优化
tags:
- Agent RL
- Credit Assignment
- Privileged Information
- GRPO
- Process Supervision
- On-Policy Distillation
one_liner: TASPO 用轨迹对齐的特权信息在动作粒度重新分配 GRPO 结果优势，使过程监督不改变结果奖励方向
practical_value: '- 在电商导购/搜索 Agent 的 RL 训练中，若只有订单、成交等稀疏最终奖励，不要直接把历史成功轨迹作为 teacher
  做 SFT/蒸馏目标；可以先离线提取「条件规则/证据」并只对当前会话路径匹配，保留适用的特权指导，否则回退 GRPO，这样能避免无关路径信息带来的梯度冲突。

  - 信用分配粒度应放在可执行动作（query、工具调用、商品筛选、消息推送等）而非 token 粒度；把 token 概率变化聚合成 action 级分数、再做
  trajectory 内去均值与 tanh 重加权，可显著降低训练方差、提升收敛稳定性，并减少成功轨迹所需交互步数。

  - 如果团队已有 GRPO 训练流程，TASPO 的改造很轻：只把 trajectory advantage A_i 换成 eA_i = A_i * w_i，保持
  w_i 为正、有界 [1-ε,1+ε]、均值 1。这样 outcome 决定方向与平均更新力度，过程信号只做分配，避免了新增蒸馏 loss 和目标冲突，无需额外环境交互。

  - 构造 PI 的外部 analyzer 可以是 frozen 大模型，且对模型选择不敏感（DeepSeek/GLM/Qwen 等差异小），工程上可以低成本复用；但前提是必须从
  verified successful sibling rollouts 提取证据，并对目标 trajectory 做显式匹配。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
在长 horizon Agent RL 中，GRPO 用 trajectory-level advantage 更新所有决策，无法区分哪些中间动作真正贡献成功。On-policy self-distillation 提供更细过程监督，但存在 supervision-credit gap：特权信息可能与当前状态不相关、token 粒度与可执行决策不对齐、且缺乏结果语义；直接合并 outcome credit 与过程监督会产生冲突梯度。

### 方法关键点
- 严格角色分离：verified outcome 决定更新方向和平均尺度，PI 只决定信用在动作之间如何重分配。
- 轨迹对齐 PI：从同 rollout group 中 verified successful sibling trajectories 提取 conditional guidance items（规则、条件、证据）。对目标轨迹仅用其 interaction history 匹配条件，只保留适用指导；无匹配则回退 GRPO。
- Action-level 打分：用 frozen rollout policy 在有/无 PI 下重估同一响应，得到 PI-induced likelihood shift Δ；过滤掉 |Δ|<κ 的 token 噪声，按可执行动作长度归一化，再减去 trajectory 均值得到相对支持分。
- 结果锚定重分配：按 trajectory advantage 符号定向 tanh 得到 q，再映射为 w=1+η(q-mean q)，权重正、有界 [1-ε,1+ε]、均值 1；最终 eA_i = A_i * w_i。

### 关键实验
在 ALFWorld、Search-QA、WebShop 三个环境、Qwen2.5-3B/7B 和 Qwen3-1.7B 上，TASPO 相对 GRPO 平均提升：ALFWorld +16.9%（三个模型 +12.1/+11.1/+27.4），Search-QA 和 WebShop 也一致提高。PI 消融：generic skill 76.9、random success 79.2、nearest success 81.1、TASPO aligned 86.3（GRPO 74.2）。Action-level 优于 token-level：ALF avg 86.3 vs 79.7，WebShop succ 78.1 vs 72.1，成功轨迹平均步数 9.2 vs 11.4。对比 OPSD、外部教师 OPD、GRPO+OPSD，TASPO 最高且无需额外教师模型；对 analyzer 模型不敏感。

### 最值得记住的一句话
特权过程监督应该 refine 而不是 replace verified outcome credit；在动作粒度聚合 PI 的似然变化并重分配到轨迹优势，可以稳定提升 Agent RL。
