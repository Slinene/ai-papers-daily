---
title: Variance-Optimal Counterfactual Policy Design for Sample-Efficient Online A/B
  Testing
title_zh: 方差最优反事实策略设计：提升在线 A/B 测试样本效率
authors:
- Shashank Gupta
- Subhadeep Maji
affiliations:
- Microsoft, India
- DeepL, UK
arxiv_id: '2611.24757'
url: https://arxiv.org/abs/2611.24757
pdf_url: https://arxiv.org/pdf/2611.24757
published: '2026-11-18'
collected: '2026-11-19'
category: Eval
direction: 策略评估 · 方差最优实验设计
tags:
- A-B testing
- off-policy evaluation
- control variates
- variance reduction
- contextual bandits
- experimental design
one_liner: 给出动作级方差最优采样策略与控制变量联合设计，大幅降低策略 A/B 测试所需流量
practical_value: '- 在推荐/广告策略的增量 A/B 测试中，若新旧策略高度重叠，不要只用固定流量 split，可改用独立 logging policy
  采 action，并用 pairwise IPS 估计 ATE；工程上只需记录 action 概率并计算 policy contrast d(x,a)=π_t(a|x)-π_p(a|x)。

  - 可以按 q*(a|x) ∝ |d(x,a)| √s_m(x,a) 分配动作级流量：优先采「两个策略分歧大且残差 reward 不确定性高」的动作；这比只优化
  policy mixture 更省流量，也类似把 Neyman allocation 推广到策略重叠场景。

  - 有历史 reward model 时，control variate 不要用普通预测 loss 拟合，而应直接最小化 ATE estimator 的估计方差目标；MRDR
  思路与本文一致，模型误差不会被加权到无关动作上。

  - 部署时建议采用两阶段设计：历史日志只用于拟合 reward model、control variate 和 logger，冻结后再采评估流量；再加 5% uniform
  safety backoff，避免某些动作 propensity 过小导致 IPS 方差爆炸。这样即使 reward model misspecified，估计仍是无偏的。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
在线 A/B 测试是推荐/排序策略上线的标准流程，但 treatment 与 production policy 常常大量重叠：两者给同一 action 的概率相近时，该 action 对 ATE 几乎不提供信息，却仍会产生 reward noise，导致测试需要大量流量和长时间。已有方差缩减方法大多在数据收集方案固定后改进 estimator；overlap-aware 方法只优化两个 policy 的全局 mix，无法为每个 context 独立设置 action 采样概率。

**方法关键点**
- 将策略 A/B 视作 pairwise OPE：用独立 logger q(a|x) 采样 action，用 Δ-IPS 风格 estimator 估计 ATE；引入 control variate m(x,a)，estimator 为 z = g_m(x) + d(x,a)/q(a|x) × (y - m(x,a))，其中 g_m(x)=Σ_a d(x,a)m(x,a)。该 estimator 在支持条件下无偏，即使 reward model 不准。
- 推导固定 control variate 下的方差最优 logger：q*_m(a|x) ∝ |d(x,a)| √s_m(x,a)，d(x,a)=π_t(a|x)-π_p(a|x)，s_m 是残差二阶矩。这会把流量集中在策略分歧大且 reward 不确定性高的动作上。
- 通过 partial minimization 将 logger 消掉，只优化 control variate；文中给出 scalar control variate 和 action-wise logistic model-based control variate。后者直接最小化估计的 profiled variance objective，而不是最小化普通预测误差。
- 实践上增加 5% uniform safety backoff，并在历史日志上拟合 reward model 与 logger 后冻结，再收集评估数据，保证 unbiased。

**关键实验**
在 synthetic contextual bandit 环境（softmax policies、Bernoulli rewards、K=25/50/75、n_hist=10k/30k、n_eval=1k–10k、ATE≈0.005、500 repeats）中，与 Standard A/B、Balanced A/B + pairwise IPS、overlap-aware mixture、reward-aware mixture 对比。结果：Model-CV 在所有设置下 MSE 最低；其达到 Balanced A/B 相同 MSE 只需 39%–51% 的评估流量；相对更强的 traffic-split baseline，MSE 降低 26%–41%；n_eval=10k 时统计功效是 Balanced A/B 的 1.5–2.1 倍；选错策略概率降低 42%–63%。Scalar joint 也显著优于所有 policy-mixture baseline。

**最值得记住的一句话**
固定 control variate 时，方差最优 logger 对每个动作的采样概率正比于「策略概率差的绝对值 × 残差 reward 标准差」，从而把数据集中到两个策略真正分歧的动作上。
