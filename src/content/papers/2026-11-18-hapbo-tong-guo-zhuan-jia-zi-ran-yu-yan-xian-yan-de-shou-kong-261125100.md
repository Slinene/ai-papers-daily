---
title: 'HapBO: Harnessed $α$-$π$ Bayesian Optimization via Expert Natural Language
  Priors'
title_zh: HapBO：通过专家自然语言先验的受控 α-π 贝叶斯优化
authors:
- Jean-Sébastien Giroux
- Rose Guay Hottin
- Marco Bonizzato
affiliations:
- Polytechnique Montréal
- MILA – Quebec AI Institute
- Université de Montréal
arxiv_id: '2611.25100'
url: https://arxiv.org/abs/2611.25100
pdf_url: https://arxiv.org/pdf/2611.25100
published: '2026-11-18'
collected: '2026-11-22'
category: LLM
direction: LLM 先验注入贝叶斯优化
tags:
- Bayesian Optimization
- LLM Priors
- Expected Improvement
- Sample Efficiency
- AutoML
one_liner: 一次性将专家/LLM自然语言信念编译为可复用信念函数，以有界乘子注入采集函数，零循环token成本且对误导先验鲁棒
practical_value: '- 将业务专家经验/运营文档一次性编译成 belief function（区间指示、单调倾向、分箱权重等），再用有界乘子乘到 EI/UCB
  等 acquisition 上；不要直接当硬约束，避免过早锁死搜索区域。

  - 适合推荐/广告场景少量在线实验调参：预算 12–20 次时先验注入能显著改善；可离线一次调用 LLM 提取先验，线上循环零 token 成本，降低延迟和费用。

  - 工程上给先验乘子设上限（0 < multiplier ≤ M），即使专家先验有误，后悔只受有界因子影响，适合需要稳健性的 AutoML、出价策略搜索。

  - 先验表示不必强制高斯：分段常数/单调/分箱等非参数形式更贴合业务直觉。'
score: 6
source: arxiv-stat.ML
depth: abstract
---

**动机**：BO 在昂贵黑盒优化中样本效率高，但专家先验常以自然语言存在，难以转为显式概率先验；现有 prior-guided BO 多假设高斯分布，LLM 方法在循环中反复调用 token 成本高。

**方法关键点**：
- 一次性从人类专家/LLM/两者获取信念，确定性编译为结构化规范，生成可复用 belief function π: X→[0,1]，非高斯、表达能力更强；
- 在 α-πBO 基础上，将 π 通过有界正乘子作用到任意非负 acquisition（如 EI），保持 acquisition 正值支撑，不硬性排除搜索空间；
- 优化过程中零 LLM 调用；理论证明在 EI 下即使面对对抗性信念，仍保留标准 simple-regret 速率，仅受有界因子影响。

**结果**：
- 40 个 HPOBench 任务上取得最低聚合 regret；
- 6–15 维合成套件与两个真实应用（皮层神经刺激、约束太阳能设计）表现强；
- 真实任务中在 12–20 次查询预算下仍改善优化结果，墙钟与 token 成本仅为其他 LLM 方法的很小一部分。
