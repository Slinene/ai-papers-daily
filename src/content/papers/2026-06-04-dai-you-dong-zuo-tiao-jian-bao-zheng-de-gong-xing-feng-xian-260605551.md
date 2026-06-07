---
title: Conformal Risk-Averse Decision Making with Action Conditional Guarantee
title_zh: 带有动作条件保证的共形风险规避决策
authors:
- Zihan Zhu
- Shayan Kiyani
- George Pappas. Hamed Hassani
arxiv_id: '2606.05551'
url: https://arxiv.org/abs/2606.05551
pdf_url: https://arxiv.org/pdf/2606.05551
published: '2026-06-04'
collected: '2026-06-07'
category: Other
direction: 共形预测与风险规避决策
tags:
- Conformal Prediction
- Risk-Averse Decision
- Action-Conditional Guarantee
- Uncertainty Quantification
- Distribution-Free
one_liner: 引入动作条件共形预测，为每项决策动作提供显式安全保证，提升风险规避决策可靠性
practical_value: '- 推荐系统中的 risk-averse 场景（如高价值用户触达、推送时机选择）可借鉴动作条件保底思想：对每个候选动作（推送/不推送）单独构建共形预测集，避免因边际保证导致某些动作下风险失控。

  - 多智体动作选择中，可为每个 agent 的动作输出附带安全区间，防止某个动作因不确定性极高而拖垮整体收益，尤其适合电商广告自动出价等需要逐动作风险控制的决策。

  - 工程实现上 pinball loss 最小化为共形预测提供了一种无需重训练的有限样本算法，可直接集成到现有 ML pipeline 的后处理中，降低落地成本。

  - 在生成式推荐的候选集过滤阶段，用动作条件的 coverage 保证替代全局 top-k 截断，能提升对长尾商品/新商品的探索安全性，平衡收益与风险。'
score: 7
source: arxiv-stat.ML
depth: abstract
---

**动机**：现有共形预测提供的是边际安全保证，即对所有动作平均后的覆盖概率达标，但无法确保每个具体动作下的风险在容忍范围内。这在医疗、金融等高风险决策中可能导致致命错误。

**方法关键点**：
- 提出动作条件共形预测，将保证从边际扩展到条件于每个动作，使决策者在选定的动作下获得显式安全区间。
- 将动作条件预测集作为风险规避决策的可行空间，连接条件 Value-at-Risk 优化目标，证明该集合恰好是风险规避策略的可行动作域。
- 基于 pinball loss 最小化设计有限样本算法，无需额外校准集划分，直接利用 Gibbs et al. (2025) 的框架实现动作条件保证，并给出理论覆盖率边界。

**关键结果**：在两个真实数据集上，动作条件方法相比传统共形 baseline 显著提升了各动作下的覆盖概率与决策效用，尤其在高风险动作上改善明显。
