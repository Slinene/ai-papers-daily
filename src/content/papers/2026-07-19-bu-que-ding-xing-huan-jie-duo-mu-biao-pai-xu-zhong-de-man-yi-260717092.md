---
title: 'Uncertainty as Remedy: Mitigating Satisfaction Label Bias in Short Video Multi-Objective
  Ensemble Ranking'
title_zh: 不确定性缓解多目标排序中的满意度标签偏差
authors:
- Zonghe Shao
- Tiantian He
- Xiaoxiao Xu
- Jiaqi Yu
- Minzhi Xie
- Jinfang Gu
- Yongqi Liu
- Kaiqiao Zhan
- Kun Gai
affiliations:
- Kuaishou Technology
arxiv_id: '2607.17092'
url: https://arxiv.org/abs/2607.17092
pdf_url: https://arxiv.org/pdf/2607.17092
published: '2026-07-19'
collected: '2026-07-21'
category: RecSys
direction: 不确定性感知多目标排序框架
tags:
- Multi-Objective Ranking
- Uncertainty-Aware
- Satisfaction Label Bias
- Pairwise Learning
- Short Video Recommendation
- Industrial Deployment
one_liner: 用高斯分布建模预测，以方差捕获多目标冲突不确定性，设计不确定性感知的自适应加权，缓解短视频排序中行为信号带来的满意度标签偏差
practical_value: '- **多目标冲突即不确定性**：在电商/广告排序中，多个业务目标（点击、转化、时长）常有冲突，可借鉴文中用预测方差表征冲突的思路，无需人工定义冲突强度，自动识别高冲突样本并加权，让模型聚焦于更影响最终满意度排序的物品对。

  - **线上零额外成本部署**：框架输出均值 μ（排序分）和方差 σ²（不确定性），线上推理时仅使用 μ 生成排序，方差仅训练时使用，不增加线上延迟。适合追求低延迟的工业系统直接替换现有排序网络。

  - **概率化 Pairwise 损失**：将传统确定性 pairwise loss 改为基于高斯 CDF 的概率形，可联合优化均值和方差，并配合不确定性正则避免方差无限增大。此类损失可平滑处理冲突标签的梯度矛盾，提升收敛稳定性。

  - **辅助监督让不确定性更可靠**：文中引入了基于物品在多目标下排序位置标准差的辅助损失，强制方差与真实冲突水平对齐。实际业务中，可基于多目标分数方差构造类似信号，提升方差的可解释性和鲁棒性。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
短视频推荐的核心是建模用户不可见的真实满意度，但工业两级排序框架中依赖的 pxtr 信号（点击、时长、点赞等）只是碎片化的满意度代理，存在天然偏差与彼此冲突。现有端到端多目标集成排序（如 EMER、EASQ）将所有样本对等权重优化，却忽视了高冲突物品对优化的重要性，导致模型偏向一致性高的简单样本，与真实满意度脱节。  

**方法关键点**  
- **不确定性建模**：将排序网络的输出设计为高斯分布 `ŷ ~ N(μ, σ²)`，均值 μ 作为满意度预测分，方差 σ² 量化由多目标冲突驱动的预测不确定性。  
- **概率化 Pairwise 损失**：基于两个物品得分差 `ŷ_i - ŷ_j ~ N(μ_i - μ_j, σ_i² + σ_j²)`，用标准高斯 CDF 计算 `P(ŷ_i > ŷ_j)`，代替传统的 sigmoid 概率。这允许方差通过梯度调节：正确排序时缩小方差，错误排序时扩大方差，但配合正则项 `log(1 + σ_i² + σ_j²)` 防止方差无限增长。  
- **不确定性感知自适应加权**：对物品对 (i,j) 定义综合不确定性 `U_ij = σ_i² + σ_j²`，经 batch 内最大最小归一化后乘以缩放因子 γ 得到权重 ω_ij。理论分析表明权重与样本级满意度标签偏差正相关，通过加权损失使优化聚焦于高冲突、高偏差物品对。  
- **辅助约束损失**：用物品在多目标下排序位置的标准差作为冲突度量，构建 pairwise 损失强制 σ² 与此度量对齐，使不确定性更可靠。  

**关键结果**  
- 在快手亿级日活短视频场景，基于 EMER 和 EASQ 两个 SOTA 骨干，离线 GAUC 全面提升，最高相对提升 pwtr 5.8%、plvtr 14.2%。  
- 7 天在线 A/B：长期留存、时长、互动等指标全面正向显著，如 LongView +1.6%，Follow +1.3%。  
- 问卷满意度对齐：NDCG@5 提升 8.71%，HR@5 提升 10.63%。  
- 不确定性真实反映标签偏差：与问卷偏差的皮尔逊相关系数 0.65，斯皮尔曼 0.67。  

**一句话**：预测的不确定性本身就可以作为解决多目标标签冲突的钥匙，通过自适应加权让模型从冲突中学习到更贴合真实满意度的排序。
