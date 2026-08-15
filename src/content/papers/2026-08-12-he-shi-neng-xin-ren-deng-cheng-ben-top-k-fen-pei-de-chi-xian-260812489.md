---
title: When Can You Trust Offline Evaluation of Equal-Cost Top-k Allocation? A Controlled,
  Reproducible Benchmark and Practitioner's Guide
title_zh: 何时能信任等成本 Top-k 分配的离线评估？
authors:
- Binshuang Li
affiliations:
- Independent Researcher
arxiv_id: '2608.12489'
url: https://arxiv.org/abs/2608.12489
pdf_url: https://arxiv.org/pdf/2608.12489
published: '2026-08-12'
collected: '2026-08-15'
category: Eval
direction: 离线策略评估 · 确定性 Top-k 分配
tags:
- Off-Policy Evaluation
- Top-k Allocation
- Effective Sample Size
- Optimizer's Curse
- Propensity Estimation
- Benchmark
one_liner: Top-k 离线评估：logger-目标动作对齐决定重叠，DR 最稳，诚实策略级切分才能消除优化者诅咒
practical_value: '- 离线评估新排序/预算分配策略前，先算 logger 与目标策略的 **action alignment**，不要只看 logging
  policy 的温度或平滑度。可用 logged actions + propensities 计算 ESS 跨环境排序风险，但 cut point 需按自己的样本量重校准；同一份日志内
  ESS 对候选策略排序几乎无效（ρ≈-0.11）。

  - 倾向得分模型质量是第一优先级：文中 flexible πb 估计让 IPS 失败率从 6.3% 升至 37-63%，甚至把 ESS 诊断 AUC 从 0.85
  反转为 0.05。业务上用 OPE 评估预算分配务必先验证 propensity model，否则诊断会误导；DR 对倾向估计误差几乎免疫，适合作为默认估计器。

  - 评估用同数据训练的策略时，不要只做 outcome nuisance cross-fitting，必须做 **policy-level honest splitting**：每个
  fold 重新训练策略并在 held-out fold 评估，才能消除 optimizer''s curse；否则 cross-fitted DR 比 plain
  DR 更乐观（bias 增加 16-36%）。

  - 做策略选择时，如果每个候选都有自己的 aligned log，会比较 policy-logger pairs 而不是 policies；应使用共同的 logging
  dataset，并注意 regret 和 accuracy 可能不一致，competitive slate 会缩小估计器差距。'
score: 9
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
预算受限的 Top-k 分配（如对响应概率最高 20% 用户发放优惠）部署前需要离线评估策略价值。评估对象是确定性策略，重要性权重为 0 或 1/πb，弱重叠直接生效。现有工作缺乏集成的基准：何时可信、选哪个估计器、能否从日志检测风险。

### 方法关键点
- 构造等成本二分 Top-k 分配 OPE 基准，5 个数据集（Synthetic/IHDP/Jobs/Hillstrom/Lenta）+2 个 known-effect 硬化套件；6 个估计器：DM、IPS、SNIPS、DR、Switch-DR、mIPS，共享 LightGBM nuisance。
- 显式控制 logger-target 对齐：self-aligned / misaligned / independent 三种 logger，温度 τ∈{0.5,2,5}，预算 k∈{0.1..1}，propensity floor 0.02。
- 用 exact value（合成/IHDP）和 RCT 上的 Horvitz-Thompson 参考值分开评估，不混池。

### 关键实验与数字
- RQ1：在 exact-value 数据上 DM/DR 中位相对 RMSE 约 0.030，IPS 约 0.057；RCT 参考下排名被参考噪声压缩，几乎不可分（0.037 vs 0.040）。
- RQ2：self-aligned / misaligned / independent logger 下，IPS 失败率 8.3%→13.3%→31.7%，ESS 中位数 0.56→0.42→0.19；ESS 跨日志环境排序 ROC-AUC 0.85，held-out 0.83/0.91，但 cut point 不迁移；同一日志内对候选排序 ρ≈-0.11。
- 倾向得分估计错误是最大退化：IPS 失败率从 6.3% 升至 37-63%，ESS 诊断在 marginal 模型下 AUC 反转为 0.05；DR 几乎不受影响。
- RQ3：nuisance-only cross-fitting 反而更乐观，bias 增加 16-36%；诚实 policy-level splitting 降低 |bias| 58-92%。
- Twins 非模拟参考复现机制，cut point 不迁移。

### 最值得记住
Top-k 离线评估的信任首先取决于 logger 与目标策略的动作对齐，而不是 logging 的平滑度；在有可靠倾向得分的前提下，DR 是更稳默认，诚实策略级切分是消除复用偏差的必要条件。
