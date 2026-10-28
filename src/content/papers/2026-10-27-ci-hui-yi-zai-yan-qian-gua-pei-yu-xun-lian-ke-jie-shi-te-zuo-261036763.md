---
title: 'The Vocabulary Is Already Here: Adapting Pretrained Interpretable Features
  for Generative Recommendation'
title_zh: 词汇已在眼前：适配预训练可解释特征做生成式推荐
authors:
- Ziluowen Luo
- Ruochen Liu
- Jun Yin
- Hao Yan
- Zhengxuan Hu
- Xinze Shi
- Chaozhuo Li
- Chengqi Zhang
- Senzhang Wang
affiliations:
- Central South University
- The Hong Kong University of Science and Technology (Guangzhou)
- Hong Kong Polytechnic University
- Queen Mary University of London
- Microsoft
arxiv_id: '2610.36763'
url: https://arxiv.org/abs/2610.36763
pdf_url: https://arxiv.org/pdf/2610.36763
published: '2026-10-27'
collected: '2026-10-28'
category: GenRec
direction: 生成式推荐 · 可解释词汇复用
tags:
- Generative Recommendation
- Semantic ID
- Sparse Autoencoder
- Interpretability
- Item Tokenization
- Explainable Retrieval
one_liner: 复用预训练稀疏自编码器特征索引作为语义 ID，无需额外词汇学习，实现高效且可解释的生成式推荐
practical_value: '- 如果业务中有商品文本描述，可尝试用现成 P-SAE（如 SAELens 的 GPT-2 SAE、Gemma Scope）提取特征索引作为商品的离散语义表示，替代
  RVQ 等需要训练的 tokenizer；跨域或新品类冷启动时无需重新拟合词汇表，显著降低 tokenization 成本。

  - PID 构建的优先级公式 $\pi_{ij}=\log(1+a_{ij})\log(1/\rho_j)$ 本质是“激活强度 × 逆文档频率”，可借鉴到商品属性标签抽取：高频通用属性降权，保留有区分度的长尾属性，同时保留相对强度向量，避免相似商品共享相同
  token 序列导致碰撞。

  - SPA 的监督设计值得迁移：除了预测 ID 序列，还预测归一化激活强度，并用 Hellinger 距离作为强度一致性惩罚；更重要的是 preference
  alignment loss 让目标 item 的分数高于其他候选，而不是仅优化似然。在生成式推荐中，对相似商品（共享主导特征）尤其关键，可以提升排序指标。

  - 检索解释方案：将候选分数差分解到每个特征 token 的贡献，并关联预训练语义标注，可用于线上推荐理由生成、badcase 归因和特征级 A/B 实验；通过编辑历史激活强度还能做可控曝光（steering），适合做可解释的策略干预。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
生成式推荐（GR）将物品编码为语义 ID（SID）并通过语言模型生成下一物品。现有 SID 词汇表通常需要针对推荐数据额外拟合（如 RVQ、RKMeans、UTGRec），带来训练成本且领域依赖，难以跨域复用；学到的 token 语义也不可读。观察到预训练稀疏自编码器（P-SAEs）已将 PLM 特征分解为可解释的字典，特征索引本身可作为现成的 SID 词汇表，无需额外训练。但直接复用面临两个挑战：紧凑 token 预算下物品区分度不足，以及缺乏检索决策层面的解释。

**方法关键点**  
- **PID 构建**：对物品文本提取 PLM-SAE 稀疏激活，聚合得到特征强度；用优先级 $\pi=\log(1+a)\log(1/\rho)$ 兼顾激活强度和逆文档频率，选择 K 个特征并保留相对强度向量 q，构成 PID =（特征索引序列, 强度向量, 语义标注）。理论保证可区分共享特征序列的物品数量有上界。
- **SPA**：历史物品用候选池特征-强度对编码，推荐 Transformer 预测下一物品的特征索引序列和归一化强度；损失包括序列似然负项、强度 Hellinger 距离惩罚，以及 preference alignment loss 使目标物品分数高于候选集。检索时用同一分数排序。
- **检索解释**：将候选分数差分解为各特征贡献 $\phi = \ell_{u,r}(i) + \beta\sqrt{\hat q_{u,r} q_{i,r}}$，关联预训练语义标注，解释为何某物品胜过另一物品。

**关键结果**  
在 Amazon Beauty/Sports/Toys 上，API 在 12 个数据集-指标组合中 9 个最佳；SPA 在 AR 和 PR 解码下普遍提升直接 PID；PID 在 K=4 时碰撞率从 Native SAE 的约 80% 降至 17%；preference alignment 使 Recall@10 相对提升 13.3%-45.9%；跨域词汇复用实验显示 API 无需重新拟合，累计 tokenization 时间仅为 RVQ 的约 1/108；案例分析验证特征语义可读，激活编辑可控制目标特征曝光。

最值得记住的一句话：预训练可解释词汇本身就是生成式推荐的免费午餐，关键在如何适配——保留相对激活强度并用 item-level 竞争监督，就能同时获得效率和可解释性。
