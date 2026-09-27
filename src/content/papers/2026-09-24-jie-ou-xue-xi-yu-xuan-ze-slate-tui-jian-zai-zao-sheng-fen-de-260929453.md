---
title: Decoupled Learning and Selection in Slate Recommendation for Privacy and Stability
  Under Noisy Scores
title_zh: 解耦学习与选择：slate 推荐在噪声分数下的隐私与稳定性
authors:
- Sam Urmian
- Qinyi Liu
- Mohammad Khalil
affiliations:
- University of Bergen, Centre for the Science of Learning & Technology (SLATE)
- City University of Macau, School of Education
arxiv_id: '2609.29453'
url: https://arxiv.org/abs/2609.29453
pdf_url: https://arxiv.org/pdf/2609.29453
published: '2026-09-24'
collected: '2026-09-27'
category: RecSys
direction: Slate 推荐 · 差分隐私与稳定性
tags:
- slate recommendation
- differential privacy
- re-ranking
- stability
- auditability
- noisy scores
one_liner: 形式化随机分数学习器+确定性选择器的解耦框架，给出差分隐私作用域契约和可证明的分数到 slate 稳定性证书
practical_value: '- 将模型学习与确定性选择层解耦，对选择器输出做差分隐私后处理审计：当选择器输入来自私有模型输出时，必须单独进行隐私记账，不能假设后处理自动提供全局隐私；可据此在推荐架构中明确『隐私作用域契约』，避免合规盲区。

  - 用 logged margin certificate 监控线上 slate 替换稳定性：记录每个 slate 的最小贪心决策间隔，当分数更新导致的目标移动小于一半
  margin 时，顺序不变；该机制可用于安全部署模型更新、减少线上排序抖动和 A/B 测试中的 churn。

  - 针对在线学习、探索噪声等 noisy scores 场景，引入 anchor weight 降低 ranking churn；电商推荐中可对新品或冷启动 item
  的分数增加先验锚定权重，稳定列表展示。

  - 审计轨迹：选择器输出附带可审计的差分隐私 trace，有利于治理与事件回溯；可在推荐系统日志中记录特征、分数、选择规则，形成可验证的决策链路。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：推荐系统中的学习模型与确定性选择层（去重、多样性、规则过滤等）通常解耦，但差分隐私、regret、fairness 等保证往往只针对学习模型，未覆盖选择层；当模型分数含噪声或隐私保护噪声时，最终 slate 可能出现不稳定的排名变化，且隐私保证边界模糊。

**方法关键点**：将 slate 推荐形式化为随机分数学习器 + 确定性选择器。差分隐私保证通过后处理传递到选择器及审计轨迹，但端到端隐私仅在选择器输入为公开、独立、历史私有输出或单独隐私记账时成立；固定原始状态或候选信息只能得到条件保证。推导出 logged margin certificate：分数引起的目标移动小于最小贪心决策间隔的一半时，有序 slate 不变。

**关键结果**：控制固定 margin 测试显示近线性指数缩放，经验斜率 -0.220（95% CI [-0.231, -0.210]），对比独立噪声参考值 -1/4。在 OULAD、MovieLens-25M、Amazon Musical Instruments 上，更大 anchor weight 显著降低分数噪声引起的排名 churn；OULAD 与 EdNet 的证书检查验证了 logged inequality 实现，闭环模拟显示目标漂移有界且下游效用随设置变化。贡献定位为隐私作用域契约与可证明的 score-to-slate 稳定性机制，而非普适效用提升。
