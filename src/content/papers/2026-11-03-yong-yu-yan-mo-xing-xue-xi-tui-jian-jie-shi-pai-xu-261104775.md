---
title: Learning to Rank Explanations for Recommendation with Language Models
title_zh: 用语言模型学习推荐解释排序
authors:
- Ben Kabongo
- Vincent Guigue
affiliations:
- Sorbonne University, CNRS, ISIR
- AgroParisTech, UMR MIA Paris-Saclay
arxiv_id: '2611.04775'
url: https://arxiv.org/abs/2611.04775
pdf_url: https://arxiv.org/pdf/2611.04775
published: '2026-11-03'
collected: '2026-11-05'
category: RecSys
direction: 推荐解释 · 稠密检索
tags:
- Explanation Ranking
- Dense Retrieval
- Contrastive Learning
- Personalization
- LLM
- Recommender Systems
one_liner: LMStaR 将个性化解释排序建模为稠密检索，多正例对比学习联合适配双塔，NDCG@1 三个域均最优
practical_value: '- 将电商推荐理由/评价标签选择建模为稠密检索：query 编码用户交互历史+目标商品元数据，statement 编码候选评论语句，用多正例对比学习训练双塔，可直接复用到商品详情页推荐理由、评论区精选、push
  文案候选排序。

  - 用真实用户评论作为候选解释，而非让 LLM 直接生成，能规避幻觉和事实性评估难题；在需要可解释推荐又重视内容安全性的场景尤其值得借鉴。

  - 任务特定适配后无需目标域微调即可跨域迁移，说明小品类/新业务冷启动时，可以用已有标注数据训练通用双塔，减少重复标注成本。

  - 反事实分析表明用户特定历史对个性化解释排序很重要，工程实现中不能只用 target item 特征，需要显式编码用户行为序列，例如将用户最近交互的商品标题/评论压缩进
  query embedding。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：推荐系统需要可解释性，LLM 生成自然语言解释虽流行，但事实性和个性化相关性难以评估；statement-level ranking 通过选择评论派生语句，能用成熟 ranking 指标做细粒度可复现评估。现有语句排序方法多依赖协同表示，语义增强常无法超过简单的用户历史流行度基线，直接适配语言模型做个性化语句排序尚未被探索。

**方法**：提出 LMStaR，完全基于文本，将个性化解释排序建模为 dense retrieval。query encoder 编码用户交互历史和目标物品元数据，statement encoder 编码候选解释语句，两者映射到共享嵌入空间；通过多正例对比学习联合适配两个编码器，学习个性化相关性。

**结果**：在 Amazon Beauty、Amazon Toys、Yelp 三个数据集上，LMStaR 均取得最高 NDCG@1，比 CLER 提升 1.06–8.25 点（+11.8–65.9%）；在两个 Amazon 数据集上 top-5 排序也领先，Yelp 上 CLER 更强。任务特定适配提升全部 5 个 backbone，且无需目标域微调即可跨域迁移。反事实分析显示用户特定历史对排序性能贡献显著。
