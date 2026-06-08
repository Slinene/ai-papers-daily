---
title: 'SSRLive: Live Streaming Recommendation with Dynamic Semantic ID'
title_zh: 直播推荐中的动态语义ID方法
authors:
- Teng Shi
- Zhaoheng Li
- Yuanhang Qu
- Yi Liu
- Lixiang Lai
- Yuning Jiang
affiliations:
- Taobao & Tmall Group of Alibaba
arxiv_id: '2606.06970'
url: https://arxiv.org/abs/2606.06970
pdf_url: https://arxiv.org/pdf/2606.06970
published: '2026-06-05'
collected: '2026-06-08'
category: GenRec
direction: 生成式推荐 · 动态语义ID
tags:
- Live Streaming Recommendation
- Dynamic Semantic ID
- Generative-Discriminative Architecture
- Pre-Ranking
- Multi-Task Learning
- Real-Time
one_liner: 提出动态语义ID捕捉直播实时内容，混合生成-判别架构融合交互特征，在工业直播场景带来显著提升
practical_value: '- **动态Semantic ID设计**：将直播物品的ID分为静态部分（主播多模态历史特征）和动态部分（实时内容特征），动态码本用EMA持续更新，可复用到其他流式或实时性强的推荐场景（如短视频、新闻）。

  - **混合生成-判别架构**：生成模块只负责产出SID作为辅助特征，判别模块融合显式交互特征（点赞、下单）做多任务预测，避免了纯生成式对交互信号建模的不足，适合电商直播等强交互场景。

  - **Codebook更新策略**：动态SID的码本随实时向量变化通过EMA更新，保持紧凑性，减少重训代价，可迁移到需要在线学习或概念漂移的推荐系统。

  - **工程化部署技巧**：通过Partial Run将生成模块提前计算，使额外延迟仅增加1.33%，为高复杂度模型在线服务提供了可行范式，尤其适合预排序环节。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：直播推荐中传统DLRM计算资源利用低（FLOPs低），生成式推荐虽在短视频等场景成功，但直接迁移面临两个挑战：静态语义ID无法刻画直播内容的实时变化，且生成式pipeline通常不显式建模用户与主播的互动信号（如点赞、下单）。为此，提出动态语义ID和混合生成-判别架构。

**方法关键点**：
- **静态与动态SID**：静态SID从主播历史多模态片段编码并融入协同信号后量化得到，代表长期稳定特征；动态SID从实时直播特征编码后量化，码本通过EMA持续更新以适应内容变化。
- **混合生成-判别架构**：用户编码器处理用户画像与序列，解码器交错自回归生成静/动态SID，同时并行执行多个任务查询，从SID和用户特征中提取任务相关表征；判别端通过交叉注意力融合用户和直播表征，并拼接显式交互特征，进行多任务预测（观看时长、下单等）。
- **训练目标**：联合优化下一token预测损失（SID生成）与多任务学习损失。

**关键结果**：
- **离线实验**：在10亿交互记录的工业数据集上，SSRLive较在线基线和多种代表性模型全面领先（Watch30 AUC +0.0082, Order AUC +0.0046等）。
- **在线A/B测试**：核心指标显著提升：观看时长+3.38%，GMV+0.72%；互动指标：粉丝增长+3.12%，互动数+2.92%；在线Hit Rate也明显改善。
- **效率**：模型参数0.04B，FLOPs 15T，通过Partial Run提前计算生成模块，端到端延迟仅增加1.33%。

**值得记住的一句话**：动态语义ID结合混合生成-判别设计，有效解决了直播推荐中实时内容建模与多信号融合的难题，并在大规模工业场景取得显著业务收益。
