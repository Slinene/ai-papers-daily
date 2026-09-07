---
title: 'Beyond Co-purchase Relation: Evolution of Complementary Recommendations at
  Allegro'
title_zh: Allegro 互补推荐：从共购噪声到语义兼容
authors:
- Aleksandra Osowska-Kurczab
- Klaudia Nazarko
- Eliška Kosturová
- Lidia Wojciechowska
- Michał Bień
affiliations:
- Allegro.com
- NVIDIA
arxiv_id: '2609.05063'
url: https://arxiv.org/abs/2609.05063
pdf_url: https://arxiv.org/pdf/2609.05063
published: '2026-09-04'
collected: '2026-09-07'
category: RecSys
direction: 互补商品推荐 · 双塔+类别映射
tags:
- Complementary Recommendation
- Two Tower
- E-commerce
- Category Adapter
- Co-purchase
- Production RecSys
one_liner: 生产级互补推荐框架 AlleCompanion：用 Category Adapter 和 ComCat 类别映射抑制共购噪声，在 Allegro
  实现购物车 GMV 提升 15-21%
practical_value: '- **用类别映射解耦业务规则与模型**：将专家规则、LLM 推理、人工标注与共现统计融合成一个 Complementary Category
  Mapping（类似 ComCat），线上作为目标类别条件输入模型，业务规则更新无需重训。对电商互补/搭配推荐尤其适用，可维护性远高于改训练数据。

  - **双塔中加入 Category Adapter + 重建损失**：把目标互补类别 embedding 拼接到 query 塔，并加 auxiliary classification/reconstruction
  loss，能在 latent space 内直接约束检索类别，避免后处理 hard filter 导致候选不足（论文中 hard filter 即使采样 15
  倍也只剩 7 个有效候选）。

  - **数据清洗要克制，专家知识放映射层而非训练集**：用最小 pair count 和同 department 不同 category 启发式重平衡训练数据能提升互补占比，但过度用专家规则过滤/合成训练集会大幅降低
  Recall（纯专家规则 Recall@20 仅 0.0818）。建议保留大部分真实交易分布，把领域知识注入映射层。

  - **不同场景/位置调混合策略**：结算前 in-cart 场景用 same-category（互补+替代混合）带来 GMV +15-21%，而产品页 sponsored
  纯互补也有广告收入提升；说明电商推荐需要按 placement 分别配置互补/替代比例，而非全局统一模型。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
电商互补推荐（如相机配镜头）常被共购日志噪声干扰：同单购买多口味狗粮是替代，猫狗粮同购是独立需求，并非兼容。标准双塔易退化为相似度检索。Allegro 月活超 2000 万，需要可扩展、可维护的生产级互补检索。

**方法关键点**
- **AlleCompanion 架构**：共享参数双塔，输入 title/price/category/attributes/seller 等内容特征，训练目标为 sampled softmax + mixed negative sampling，支持冷启动。
- **Category Adapter**：将目标互补类别 embedding 与 query 产品 embedding 拼接后经 FC 生成 query 表示；辅助 Category Reconstruction Loss 让 query 回归目标类别 embedding，从而在 latent space 内引导检索到指定互补类别，避免线上 hard filter 的候选不足。
- **ComCat 映射**：融合自动化共现统计（Jaccard + taxonomy 距离、价格比过滤）、人工标注（含 LLM 辅助）、专家规则，按优先级合并；支持 same-category 规则，解耦业务规则与模型，可动态更新无需重训。
- **数据构造**：90 天交易 session 内有序对；过滤 heavy buyer；最小 pair count 增加精度；同 department 不同 category 启发式将训练集互补占比从 36% 提升至 61%，替代占比降至 4%。

**关键结果数字**
- 离线对比 Test 集：Vanilla-TT Recall@20 0.0447 → AlleCompanion 0.4567，MRR@20 0.0103 → 0.2000。
- Hard filtering（Seller-TT+HF）候选采样 15 倍，中位数有效候选仅 7，不可扩展。
- 数据消融：纯专家规则合成数据 Recall@20 仅 0.0818；预训练专家规则 + 交易微调保持 Recall@20 0.4458 并略升 Attribute Consistency。
- 在线 A/B：产品页 Organic 加 same-category 后 App GMV +9.35%*，Web +8.05%*；In-cart 场景 GMV App +15.73%*，Web +21.25%*；Sponsored 广告收入约 +50%。

**最值得记住的一句话**
把互补类别知识外置到可动态更新的 ComCat 映射，并通过 Category Adapter 在双塔内做约束，比后处理过滤更可扩展；真实购物车场景中互补+替代混合推荐带来最大 GMV。
