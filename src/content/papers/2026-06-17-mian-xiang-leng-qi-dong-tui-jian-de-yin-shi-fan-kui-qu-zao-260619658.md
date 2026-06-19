---
title: Denoising Implicit Feedback for Cold-start Recommendation
title_zh: 面向冷启动推荐的隐式反馈去噪方法 DIF
authors:
- Gaode Chen
- Shicheng Wang
- Shikun Li
- Rui Huang
- Xinghua Zhang
- Yunze Luo
- Shipeng Li
- Shiming Ge
- Ruina Sun
- Yinjie Jiang
affiliations:
- Kuaishou Technology
- Hong Kong Baptist University
- Peking University
- Nanjing University
- Chinese Academy of Sciences
arxiv_id: '2606.19658'
url: https://arxiv.org/abs/2606.19658
pdf_url: https://arxiv.org/pdf/2606.19658
published: '2026-06-17'
collected: '2026-06-19'
category: RecSys
direction: 去噪隐式反馈 · 冷启动推荐 · 伪标签生成
tags:
- denoising
- cold-start
- pseudo-labeling
- implicit feedback
- multi-modal
- industrial deployment
one_liner: 利用内容相似暖物品为冷物品生成置信度加权的伪标签，并通过不确定性估计自适应修正标签噪声
practical_value: '- **冷启动物品的伪标签生成套路**：利用已经训练充分的暖物品协同表示和用户塔输出，通过内容相似度检索top-k暖物品，用内积生成伪标签。电商冷启动物品（新品、新店铺）可复用这一思路，用图像/文本多模态相似度找到同类历史商品，借用其学习好的交互信号。

  - **置信度加权聚合**：对top-k伪标签按内容相似度做softmax加权，提升伪标签精度，避免简单平均带来的噪声。温度系数τ可调节相似度区分度，实践中相似度通常很高（>0.9），需要τ来拉开差异。

  - **样本级不确定性自适应修正**：结合相对熵（模型预测与标签的差异）和物品冷启动状态（曝光次数指数衰减）估计标签噪声，再按该不确定性对原始标签与伪标签做 convex
  组合。这一机制可灵活插入任何双塔或CTR模型训练，且对暖物品影响极小。

  - **工业在线部署架构**：详细给出了内容相似暖物品实时检索与表示更新的pipeline设计——多模态推理服务→消息队列→item-to-item ANN服务→协同表示
  Embedding 服务，完全适配流式训练场景，可供搭建推荐系统实时特征工程的团队直接参考。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：推荐系统中的冷启动物品（新内容）由于曝光机会少、点击诱饵和位置偏差等因素，其隐式反馈（点击/观看）所含噪声远高于暖物品。例如快手数据表明，冷启动物品在点击诱饵指标前10%的比例比后10%高37.7%，且出现在尾部位置的几率比顶部高28.3%。然而，现有去噪方法多依赖 loss 值、预测分数等启发式信号，这些信号对冷物品本就偏高，因此完全失效。作者旨在专门为冷启动物品设计隐式反馈去噪方案，避免噪声误导模型，提升冷启动物品的推荐效果。

**方法**：提出模型无关的去噪框架 DIF，核心思路是用内容相似的暖物品间接为冷物品生成可靠的伪标签，并自适应修正原始标签。流程如下：
- 伪标签生成：对每个冷物品，通过多模态内容相似度 ANN 检索 top-k 暖物品，取用户塔输出与这些暖物品协同表示的内积作为伪标签。
- 置信度建模：基于内容相似度分数做 softmax 归一化，得到每条伪标签的置信度，加权求和得到聚合伪标签，提升准确性。
- 不确定性估计：计算当前样本标签的相对熵（预测与标签的交叉熵），并结合物品的冷启动状态（用曝光次数的负指数建模，新物品接近1，暖物品趋近0），乘积得到该样本标签的不确定性。
- 标签修正：按不确定性比例 w = t/(t+1) 混合伪标签和原始标签得到修正标签，训练时仍用交叉熵损失，实现自适应去噪。
提供了工业级在线部署方案，包括多模态推理服务、实时更新暖物品候选库的 Runner 服务、存储协同表示的 Embedding 服务，完整打通从内容表示到训练样本增强的流式链路。理论分析证明，随着暖物品数量增加和邻居数 k 选择，伪标签的误差可控，且加权机制能最小化均方误差。

**实验**：在 Amazon-Sports、Amazon-Baby、TikTok 三个多模态数据集上，基于 NeuMF、LightGCN、SimGCL 三种 backbone 进行离线评估。DIF 在所有冷启动物品指标上大幅超越 DECL、RINCE、MWUF 等去噪/冷启动方法。例如在 Amazon-Sports 上，NeuMF 冷物品 Recall@20 从 0.00244 提升至 0.00461，LightGCN 从 0.00191 提升至 0.00325；且对暖物品和整体性能有稳定提升。噪声鲁棒性实验表明，在 20%-80% 人工噪声下 DIF 始终最优。在线 A/B 测试在快手亿级用户上线，冷启动物品的有效观看 +2.327%、观看时长 +2.921%、互动（点赞/评论/关注/分享）也均有显著提高。
