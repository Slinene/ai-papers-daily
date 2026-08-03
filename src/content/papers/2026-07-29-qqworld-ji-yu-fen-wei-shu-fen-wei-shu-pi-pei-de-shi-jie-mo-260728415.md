---
title: 'QQWorld: Quantile-Quantile Matching for World Model Regularization'
title_zh: QQWorld：基于分位数-分位数匹配的世界模型正则化
authors:
- Zhoushun Yu
- Xiaoyu Hu
- Xiangyu Xu
affiliations:
- Xi’an Jiaotong University
arxiv_id: '2607.28415'
url: https://arxiv.org/abs/2607.28415
pdf_url: https://arxiv.org/pdf/2607.28415
published: '2026-07-29'
collected: '2026-08-03'
category: Agent
direction: 世界模型潜在空间正则化 · QQ匹配
tags:
- World Model
- Latent Regularization
- Quantile-Quantile Matching
- Gaussianity
- Heavy-tail Control
- Planning
one_liner: 用分位数-分位数匹配替代Epps-Pulley检验，解决世界模型潜在表示重尾控制失效问题
practical_value: '- 若推荐模型（如VAE、扩散模型）需要隐空间服从高斯先验，可用QQ匹配替代KL散度，强制尾部对齐，可能增强生成多样性和分布外泛化。

  - 跨批次QQ的内存库机制与推荐系统中动量对比学习（如MoCo）或历史嵌入缓存类似，能以低开销扩大样本池改善分布估计，值得在用户表征训练中尝试。

  - 监控隐向量的QQ图（而非单一分布距离）可更早发现训练中的尾部问题，适用于大模型调优。

  - 在涉及多步序列决策的推荐场景（如交互模拟），该正则化可提升世界模型稳定性，减少误差累积。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：隐式世界模型通过紧凑表示空间预测未来状态，但性能依赖潜在分布质量。现有LeWorldModel使用Epps-Pulley (EP) 检验正则化潜在变量趋向各向同性高斯，但论文发现EP对孤立尾部样本的校正梯度迅速消失，导致重尾现象未被充分控制，进而损害多步规划。

**方法**：提出QQWorld，用分位数-分位数匹配（quantile-quantile matching）直接对齐投影潜在样本与排序匹配的高斯分位数，因此在尾部区域保持有效校正梯度。进一步提出跨批次QQ（cross-batch QQ），利用历史批次的分离样本扩大排序池，并分析了其偏差-方差权衡。

**结果**：在四个控制环境（包括导航和机器人操作）中，QQWorld将LeWM的平均规划成功率从基线约0.65提升至0.75以上，并一致地实现更薄尾部、更好的高斯对齐度量。
