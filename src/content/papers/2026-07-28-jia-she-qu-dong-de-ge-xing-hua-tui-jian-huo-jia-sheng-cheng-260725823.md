---
title: Hypothesis-Driven Shelf Generation for Personalised Recommendation
title_zh: 假设驱动的个性化推荐货架生成
authors:
- Aleksandr V. Petrov
- Tarun Chillara
- Matthew D. Moellman
- Lucas de Haas
- Yabai Song
- Alina Susoykina
- Melissa Crawford
- Gabriel Negash
- Erik Franco
- Tasnim Rahman
affiliations:
- Spotify
arxiv_id: '2607.25823'
url: https://arxiv.org/abs/2607.25823
pdf_url: https://arxiv.org/pdf/2607.25823
published: '2026-07-28'
collected: '2026-07-29'
category: GenRec
direction: 生成式推荐 · Semantic ID 货架生成
tags:
- Shelf Generation
- Generative Retrieval
- Semantic ID
- LLM-as-a-Judge
- Personalization
- Offline Serving
one_liner: 将推荐界面货架抽象为自然语言假设，解耦生成规划与目录检索，离线批量产出高质量个性化推荐行
practical_value: '- **将推荐行（如“猜你喜欢”）抽象为“假设-填充”架构**：先基于用户画像生成自然语言意图（如“北欧氛围后摇”），再用检索填充具体物品，解耦了意图规划与物品召回，便于独立优化与扩展，可迁移到电商首页多排推荐或搜索推荐横幅。

  - **使用 Semantic ID 生成式检索 + 约束解码**：在特定内容类型索引上做受限生成，相比 BM25/稠密检索显著提升了检索结果的假设覆盖率与多样性，适合处理大规模异构目录的精准匹配，可直接复用到商品多模态索引或广告创意检索。

  - **LLM-as-a-Judge 评估货架级质量**：设计用户→假设、假设→货架两张评鉴表，从匹配度、特异性、连贯性等维度打分，突破传统逐物品 recall
  指标的局限，可用于生成式推荐离线快速迭代。

  - **离线批量生成避免线上 LLM 推理延迟**：全流程预计算，货架作为附加候选参与排名，无需实时调用大模型；结合均匀随机曝光实验公平评估线上效果，适合高流量场景快速试错。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
现代推荐界面普遍采用货架（shelf）组织内容，如“为你精选”“新碟推荐”。传统生产系统依赖手工设计的固定模板并绑定专属召回逻辑，难以覆盖长尾个人兴趣。本文提出将货架生成建模为假设驱动的规划问题：用自然语言描述个性化货架概念，随后由检索系统填充目录实体，从而突破模板数量的瓶颈。

**方法关键点**
- **四阶段流水线**：假设生成（基于用户画像生成货架标题与意图描述）→ 目录填充（基于假设通过生成式检索产出 Semantic ID，再解析为具体实体）→ 货架对齐（LLM 联合优化最终选品与标题/副标题，确保文案与物品一致）→ 离线交付（预计算货架作为 Home 排名候选，无额外延迟）。
- **生成式检索填充**：使用扩展了 Semantic ID 词表的小模型，在特定类型（专辑/播客/艺术家）的 Trie 约束下解码，支持熟悉/发现/新发布等多种策略索引，实现内容和约束的精准落地。
- **LLM-as-a-Judge 评估**：设计用户→假设（5 维度）与假设→货架（7 维度）两套评鉴表，0-2 分制评断假设特异性、条目标相符性、行列连贯性等，替代传统点式相关性指标。

**关键结果数字**
- 生成式检索在假设→货架评鉴上整体得分 0.71，显著优于 BM25（0.56）、稠密检索（0.39）和混合（0.49），在覆盖率、多样性维度尤其突出。
- 货架对齐后整体法官得分从 0.71 提升至 1.27（+78%），标题吻合度翻倍（+99%），行列连贯性提升 56%。
- 线上随机均匀曝光实验：专辑类货架的 30 秒流式收听率 +36%，艺术家/播客略弱，播客节目 －41%，表明生成式货架在多数类型中可竞争最强手动物架，并大幅扩展个性化供给。
