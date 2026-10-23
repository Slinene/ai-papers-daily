---
title: Bezier-Guided Adaptive Flow for Cross-domain Sequential Recommendation
title_zh: 贝塞尔引导自适应流用于跨域序列推荐
authors:
- Ziang Lu
- Yu Zhang
- Xinzhe Jiang
- Lei Sang
- Yiwen Zhang
affiliations:
- Anhui University, China
arxiv_id: '2610.30825'
url: https://arxiv.org/abs/2610.30825
pdf_url: https://arxiv.org/pdf/2610.30825
published: '2026-10-22'
collected: '2026-10-23'
category: RecSys
direction: 跨域序列推荐 · 贝塞尔流
tags:
- Cross-domain Recommendation
- Sequential Recommendation
- LLM
- Bézier Flow
- Personalization
- Residual Flow
one_liner: 提出 BGAFlow，结合 LLM 共享语义空间与个性化 horizon，用条件贝塞尔曲线和残差流实现跨域兴趣状态自适应迁移
practical_value: '- 跨域迁移不要用全局对齐，可按用户兴趣重叠度估计个性化 horizon 控制迁移强度；电商跨场景（短视频→货架、直播→商城）可借鉴，避免向低重叠用户注入无关表征。

  - 用 LLM 推断用户画像来辅助双域共享语义空间预训练，适合冷启动和少行为用户；工程上可把 LLM 画像向量作为跨域 embedding 初始化的辅助特征。

  - 贝塞尔曲线 + 残差流提供了一种可学习的平滑轨迹约束，可尝试把用户多会话兴趣漂移建模为带控制点的状态演化路径，而不是离散的状态转移。

  - 轨迹正则化能抑制跨域学习中的噪声和突变，在多域推荐/多任务学习中可作为稳定的域间表示约束。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

动机：跨域序列推荐中，用户在不同域间的偏好一致性差异大，现有方法依赖全局对齐或粗粒度迁移，容易注入无关偏好，且难以按用户适配语义表征。

方法关键点：
- 先做统一双域预训练，并引入 LLM 推断的用户画像，建立共享语义空间；
- 基于用户潜在兴趣重叠估计个性化 horizon，控制每个用户的迁移范围；
- 用条件贝塞尔曲线作为几何参考，学习残差流在中间偏好状态上逐步修正轨迹，动态反馈调整迁移方向；
- 推荐监督 + 轨迹正则化联合优化，兼顾有效性与平滑性。

关键结果：在真实数据集上一致超越 SOTA，验证个性化迁移控制与状态自适应语义演化的收益。
