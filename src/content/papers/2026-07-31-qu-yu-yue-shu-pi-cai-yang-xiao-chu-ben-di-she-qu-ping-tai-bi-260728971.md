---
title: 'Don''t Contrast the Impossible: Region-Constrained Batching for Contrastive
  User Modeling on a Local Community Platform'
title_zh: 区域约束批采样：消除本地社区平台对比用户建模中的不可能负样本
authors:
- Seungho Han
- Byeongchang Kim
- Jin Yu
affiliations:
- Danggeun Market Inc. (Karrot)
arxiv_id: '2607.28971'
url: https://arxiv.org/abs/2607.28971
pdf_url: https://arxiv.org/pdf/2607.28971
published: '2026-07-31'
collected: '2026-08-03'
category: RecSys
direction: 对比学习 · 区域约束负采样
tags:
- contrastive learning
- user modeling
- negative sampling
- regional constraint
- two-tower
- batch sampling
one_liner: 提出区域约束批采样(RCBS)，通过构造区域同质mini-batch将地理不可能负样本替换为可行负样本，提升用户表征质量与下游推荐效果
practical_value: '- **地域受限业务的负采样策略**：外卖、本地生活、社区电商等有曝光半径的场景可直接借鉴，按配送区域或商圈组织batch，减少因配送范围外导致的无效负样本，让模型专注真实可曝光物品的对比。

  - **零模型改动的经验性trick**：仅改变数据加载时的shuffle逻辑，不改模型结构与loss，工程落地成本极低；可按粗/细粒度区域分组逐步降低不可能负样本比例（如从0.98→0.30），观察到Recall稳定提升。

  - **负样本难度信号的隐性引入**：RCBS使batch内天然充满“可行但未交互”的负样本，这种harder negative能提供更强训练信号，尤其适合两塔模型直接迁移。

  - **与倾向性加权的互补**：若存在进一步曝光偏差，可在区域batch内叠加IPS等倾向性修正，先行用RCBS去掉曝光概率为0的样本，再对剩余样本做概率加权，实用且易扩展。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
对比学习被广泛用于推荐系统用户建模，但普遍假设“任何物品都可能曝光给任何用户”。在本地社区平台（如韩国Karrot），86%以上的交易发生在5km半径内，曝光受到严格地理约束，导致batch内大量“不可能负样本”——物品因区域边界根本无法被该用户看到。这些负样本不携带任何偏好信息，反而稀释对比信号，损害用户表征的区分度。针对这一实际问题，论文定义了曝光可行性，并指出随机batch中不可能负样本占比高达98%。

**方法关键点**  
- **曝光可行性定义**：将地理空间离散为区域单元，用户仅能看见自身及相邻区域内的物品，记为 feas(u,i)=1[dist(r(u),r(i))≤δ]。  
- **区域约束批采样（RCBS）**：按用户所属区域构造同质mini-batch，使batch内所有用户来自同一区域，从而大幅降低不可能负样本比例；可调节区域粒度（粗/细）控制约束强度。  
- **不改模型结构**：沿用标准两塔Transformer+MLP架构，InfoNCE损失不变，仅改变batch的组建方式，实现即插即用。  
- **可行性保证**：粗粒度RCBS将不可能负样本比例从0.98降至0.79，细粒度进一步降至0.30；减少的不可能负样本会被可行负样本替代，后者天然难度更高，信号更纯。

**关键结果**  
- **用户建模Recall**：细粒度RCBS在随机评估下R@10达0.149（随机batching仅0.100），提升49%；若用同区域评估（更严格），R@10为0.139（随机仅0.082）。  
- **下游任务提升**：用户表征加入排序模型后，家庭feed排序NDCG@10相对提升+1.18%，检索R@10提升+7.56%，展示广告AUC提升+0.53%，均显著优于随机batching。  
- **在线A/B**：将RCBS学得的用户向量注入生产系统，家庭feed点击+10.0%，日活观看者DAV+1.91%，广告eCPM+6.01%，CTR+7.46%，确认了可行负样本信号的线上价值并已全面部署。

**最值得记住的一句话**：去除掉用户根本不可能看到的负样本，让对比学习只在真实曝光可行集上运行，就能显著提升用户表征质量并拉动下游点击与收入。
