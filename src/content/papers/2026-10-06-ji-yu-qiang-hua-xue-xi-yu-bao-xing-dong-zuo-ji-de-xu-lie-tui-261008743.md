---
title: 'Reinforcement Learning with Conformal Action Sets: An Application to Sequential
  Recommendation'
title_zh: 基于强化学习与保形动作集的序列推荐
authors:
- Wenwen Si
- Honghao Wei
affiliations:
- University of Pennsylvania
- Washington State University
arxiv_id: '2610.08743'
url: https://arxiv.org/abs/2610.08743
pdf_url: https://arxiv.org/pdf/2610.08743
published: '2026-10-06'
collected: '2026-10-07'
category: RecSys
direction: RL + Online Conformal 动态候选集
tags:
- Conformal Prediction
- Reinforcement Learning
- Sequential Recommendation
- Action Set Pruning
- Online Calibration
- Diversity
one_liner: 用 critic gap 打分和在线保形阈值动态裁剪候选集，在不增大 set size 下提升 catalog diversity，并给出有限会话价值界
practical_value: '- 把固定 top-M slate 换成 critic gap 打分 + 在线阈值裁剪：在粗排/召回到精排链路中，用\( g_\theta(s,a)=\max_b
  \hat Q_\theta(s,b)-\hat Q_\theta(s,a) \) 和阈值 \(\tau_t\) 动态决定候选集，同样 size cap 下能显著提升
  catalog diversity 和 ILD，适合新品/长尾曝光和多样性约束场景。

  - 阈值更新只需要 binary miss 信号：\( e_t=1\{C_t\cap \tilde A_{\varepsilon,t}=\emptyset\}
  \)，然后 \(\tau_{t+1}=\tau_t+\eta_t(e_t-\alpha)\)。实现简单、不需要真实 \(Q^*\)，可做成精排后的动态截断层，阈值快更新、critic
  慢更新。

  - 把“候选集是否包含好 item”和“下游 selector 是否选中好 item”解耦，对应 filtering loss 与 selection loss。业务中不要只看召回命中率；若重排/用户选择会选差，retention
  保证没有意义，应分别优化覆盖与选择策略。

  - 注意 item-level MDP 条件：如果 reward、退场或 position bias 依赖整个 slate/collection，则必须把 collection
  当 action；click/like reward 也不直接等价 session depth。此方法收益主要是曝光多样性提升，不是点击/LTV 全面大幅提升。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**：序列推荐通常每步展示固定数量 slate，但会话内“值得保留的候选项”数量会变化；固定 top-M 无法同时兼顾候选集紧凑性和不误删高价值动作。过滤还会改变后续访问状态，并且保留好 item 不等于后续 selector 会选中它，因此需要把候选集构建和长期价值绑定。

**方法关键点**：
- RLCP 用 critic 估计价值差作为 score：\( g_\theta(s,a)=\max_b \hat Q_\theta(s,b)-\hat Q_\theta(s,a) \)，以阈值 \(\tau\) 保留 \( \{a:g_\theta\le\tau\} \)，非空 fallback，可加 top-K cap。
- 阈值在线校准：\( e_t=1\{raw\ set\ \text{未命中}\ proxy\ target\} \)，\( \tau_{t+1}=\tau_t+\eta_t(e_t-\alpha) \)；即使 critic/policy/state 持续变化，也能给出路径平均 miss rate 的 \(O(1/T)\) 确定性界。
- 评估使用双层目标：在由保留集诱导的下游策略 occupancy 上最小化期望 set size，并满足 retention \(\ge 1-\alpha\)。
- 核心价值分解：\( V^*-V^\pi=E_{d^\pi}[\Delta_D+\zeta_{\pi,D}]/(1-\gamma) \)，把过滤损失与选择损失分开；结合 proxy fidelity、critic error、selection error 得到有限会话回报界。

**实验**：在 KuaiSim 全会话协议下，用 KuaiRand-Pure 和 MovieLens 1M，对比 A2C/DDPG/TD3/HAC，共 19 个配置。每个配置下至少一个 RLCP 变体获得最高 catalog diversity，达到最强 baseline 的 1.11×–5.21×；KuaiRand-Pure 上 RLCP-Single 最高 diversity 1.48×–4.56×，平均 retained set 在 9/10 配置中小于固定 slate，最大减少 25.5%，session depth 与最强 baseline 差距 0.4 以内；MovieLens 上 full RLCP 在 7 个配置达到/并列最高 session depth，ILD 始终 1.00。收益主要是同等 size cap 下更大曝光多样性，而非全面 reward 提升。

**最值得记住**：把 critic 打分和 threshold 校准解耦，并用 binary miss 在线调节阈值，能稳定扩大候选多样性，同时把过滤损失和选择损失分开归因。
