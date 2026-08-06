---
title: 'Multi-Objective Ranking for Live-Streaming: Balancing Fresh and Delayed Signals
  with Segment-Aware Targeting'
title_zh: 直播多目标排序：平衡新鲜与延迟信号的分段定向优化
authors:
- Xiaoyi Gu
- Julia Tavares
- Eder Santana
- Carlos Mendoza-Cardenas
- Nikita Mishra
- Saad Ali
affiliations:
- Twitch Interactive
- Amazon Prime Video
arxiv_id: '2608.04455'
url: https://arxiv.org/abs/2608.04455
pdf_url: https://arxiv.org/pdf/2608.04455
published: '2026-08-05'
collected: '2026-08-06'
category: RecSys
direction: 直播推荐 · 延迟信号与MMoE
tags:
- live-streaming
- delayed signals
- MMoE
- user segmentation
- multi-objective ranking
one_liner: 通过延迟窗口、双模混合新鲜/延迟信号与MMoE，实现直播推荐多目标平衡及用户分群定向，DAV+0.09%
practical_value: '- **延迟窗口建模转化**：电商中购买、加购等行为常有延迟，可借鉴延迟窗口，用历史曝光样本延迟的正负标签更新模型，与实时信号模型融合，平衡即时兴趣与长期转化。

  - **用户分段独立优化**：将用户按生命周期或活跃度划分（如新客户、沉睡客户、高价值客户），为不同段单独训练或微调模型分支/偏差项，或调整不同目标的融合权重，实现定向提升（如促活、提频、提客单）。

  - **MMoE 多目标共享参数**：当需要同时优化点击、转化、收藏等多个目标时，采用 MMoE 共享底层专家，减少模型数量和维护成本，通过门控做任务特化，尤其适合多个有相关性的目标。

  - **移动端 feed 场景验证**：方法在移动端信息流推荐中也有效（互动提升 1.12%），说明跨场景可迁移，电商首页、猜你喜欢等 feed 类场景可尝试类似多模型、分段定向方案。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：直播推荐中用户行为稀疏、延迟，且不同用户分群存在偏差。观看、聊天、关注、付费等行为反馈延迟各异，传统即时反馈窗口无法捕捉延迟转化，且不同生命周期阶段用户需求不同。

**方法**：
1. **延迟窗口**：将反馈收集窗口从即时扩展至更长时段（如数小时/天），捕捉延迟正反馈。
2. **多模型混合架构**：两路模型分别基于新鲜信号（近期行为）和延迟信号（历史窗口聚合），通过融合层结合，平衡实时性与延迟奖励。
3. **分段感知定向**：按用户生命周期（新用户、低活跃、高活跃）划分，对每类用户独立优化排序分数（如对新用户侧重探索、对高活用户侧重变现），实现精准干预。
4. **MMoE 多目标建模**：用 Multi-gate Mixture-of-Experts 联合预测多个相关目标（如观看时长、关注、付费），共享底层专家并保留任务特化门控，模型参数减少 41.9%。

**关键结果**：线上 A/B 测试，整体日活用户 (DAV) +0.09%，对应每年数百万活用户天数；高活跃用户 ARPU +0.56%；分段定向为新用户/低活跃用户额外带来 +0.15% DAV；MMoE 进一步贡献 +0.08% DAV 和 +0.27% 新关注；移动端 Feed 互动率 +1.12%。
