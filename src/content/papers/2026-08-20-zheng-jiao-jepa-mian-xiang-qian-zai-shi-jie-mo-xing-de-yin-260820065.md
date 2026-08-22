---
title: 'Orthogonal JEPA: Factorized Predictive States for Latent World Models'
title_zh: 正交 JEPA：面向潜在世界模型的因子化预测状态
authors:
- Taoyong Cui
- Pheng Ann Heng
- Wanli Ouyang
affiliations:
- The Chinese University of Hong Kong (CUHK)
arxiv_id: '2608.20065'
url: https://arxiv.org/abs/2608.20065
pdf_url: https://arxiv.org/pdf/2608.20065
published: '2026-08-20'
collected: '2026-08-22'
category: Other
direction: 预测表征学习 · 世界模型
tags:
- JEPA
- World Models
- Predictive Factorization
- Orthogonality
- Representation Learning
one_liner: 提出正交预测因子化框架，将目标状态分解为多个正交组件分别预测，缓解主导信号对表征学习的干扰
practical_value: '- 多任务/多目标推荐中共享 backbone 常面临负迁移：可借鉴正交因子分解，将目标空间分解为多个正交组件，每个任务/目标使用独立预测头，显式鼓励任务表征方向不重叠，缓解主导任务（如
  CTR）对辅助任务（如收藏、GMV）的梯度压制。

  - 在用户序列建模或商品表征预训练中，JEPA 式自监督学习可用：对 next-item 预测或跨视图预测，把目标 embedding 用基矩阵分解为多个正交因子，分别预测后合成，避免单一预测头只拟合热门/高频特征，提升对长尾兴趣的覆盖。

  - 在线方差正则化可防止 embedding 坐标坍缩，适合推荐模型 embedding 层或序列编码器，避免有效维度减少；因子活动正则化思想可迁移到多兴趣表征，保持不同兴趣向量的多样性。

  - 该预测状态机制可支持 planning/rollout，对 Agent 在推荐环境中做用户模拟或策略评估时，可构建因子化世界模型，生成更稳定的用户状态转移。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

动机：标准 JEPA 将所有可预测内容压缩到单一目标嵌入和一条预测通路，复杂系统中主导信号会占用冗余容量，削弱非主导结构的梯度，造成表征偏差。

方法：Orthogonal JEPA 引入正交预测因子化。学习基矩阵把目标状态分解成多个组件；共享上下文表征分别经专用预测分支估计每个组件。四个核心机制：预测回归保存合成所需的因子幅值；正交目标去重方向；因子活动正则维持投影目标变化；在线方差正则防止坐标级编码器坍缩。预测组件可合成为完整潜在状态，供 readout、decoder、planner 或自回归 rollout 使用。该机制同样适用于时间未来、空间隐藏或其他部分观测目标。

结果：在受控视觉、单细胞转录组、纵向健康记录、连续控制、分子动力学五个领域评估，覆盖表征质量、预测、规划和长期稳定性。
