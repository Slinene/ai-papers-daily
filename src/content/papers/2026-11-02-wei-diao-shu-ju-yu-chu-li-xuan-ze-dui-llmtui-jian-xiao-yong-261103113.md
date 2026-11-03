---
title: 'Preprocessing Choices in Fine-Tuning Data Matter: Utility and Demographic
  Sensitivity in LLM-Based Recommendation'
title_zh: 微调数据预处理选择对LLM推荐效用与人口统计敏感性的影响
authors:
- Furkan Yasir Goksu
- Yaren Yilmaz
- Sule Gunduz Oguducu
affiliations:
- Istanbul Technical University
arxiv_id: '2611.03113'
url: https://arxiv.org/abs/2611.03113
pdf_url: https://arxiv.org/pdf/2611.03113
published: '2026-11-02'
collected: '2026-11-03'
category: GenRec
direction: 生成式推荐 · 数据预处理与公平性
tags:
- LLM4Rec
- Fine-tuning
- Constrained Decoding
- Fairness
- Data Preprocessing
- Prompt Augmentation
one_liner: 系统评估微调预处理对LLM生成式推荐效用与公平性的影响，并验证目录约束解码与提示增强的有效性
practical_value: '- 采用 catalog-constrained decoding（基于合法商品/标题集合约束解码）可从根本上避免 LLM 生成不存在的商品或标题，并保证固定长度输出；对电商推荐落地非常关键。

  - 微调数据中 item-title 表示显著影响效用：优先保留原始商品标题而非清洗/简化文本。该研究显示原始标题使 HR@10 从 10.67% 提升到 12.47%，Coverage@10
  从 41.36% 提升到 47.88%。

  - prompt augmentation（补充用户/商品上下文模板）可提升 prompt 一致性与推荐效用，适合作为低成本数据增强/正则化手段。

  - 人口统计平衡具有属性依赖性：年龄平衡和知识增强可在不损失效用下缩小部分群体差异，但性别平衡可能损害效用且不改善性别指标；业务中不要盲目平衡所有敏感属性，应分属性评估。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

动机：LLM 生成式推荐虽然能直接生成商品列表，但面临输出合法性、prompt 一致性、以及对人口统计描述敏感等问题，微调数据预处理对效用与公平性的影响尚不明确。

方法关键点：构建受控推荐 pipeline，包含 supervised fine-tuning、catalog-constrained decoding 和 prompt augmentation；系统研究三种预处理选择——item-title 表示、人口统计平衡、辅助商品知识增强。实验基于 MovieLens-1M。

关键结果：catalog-constrained pipeline 消除了 out-of-catalog 商品并保证完整十项输出；prompt augmentation 提升 prompt 一致性和推荐效用；使用原始 MovieLens 标题使 HR@10 从 10.67% 提升至 12.47%，Coverage@10 从 41.36% 提升至 47.88%。公平性效果与属性相关：年龄平衡和知识增强在基本保持效用的情况下缩小了部分群体效用差距，而性别平衡降低效用且未改善评估的性别相关指标。整体结论是微调数据预处理需要联合评估效用、输出行为和人口统计敏感性。
