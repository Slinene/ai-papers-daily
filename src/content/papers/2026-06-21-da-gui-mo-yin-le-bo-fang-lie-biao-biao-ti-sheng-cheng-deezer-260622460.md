---
title: Music Playlist Captioning at Scale with Large Language Models
title_zh: 大规模音乐播放列表标题生成：Deezer 基于 LLM 的工业化实践
authors:
- Mathieu Delcluze
- Léa Briand
- Benjamin Chapus
- Deniz Mekik
- Guillaume Salha-Galvan
affiliations:
- Deezer Research
- SJTU Paris Elite Institute of Technology
arxiv_id: '2606.22460'
url: https://arxiv.org/abs/2606.22460
pdf_url: https://arxiv.org/pdf/2606.22460
published: '2026-06-21'
collected: '2026-06-23'
category: RecSys
direction: LLM 生成推荐解释文案
tags:
- LLM
- Playlist Captioning
- Recommender System
- A-B Testing
- Music Streaming
- Semantic Framing
one_liner: 用 LLM 为推荐播放列表自动生成描述性标题，在不改动推荐算法的情况下提升用户参与度 24.9%
practical_value: '- **为推荐模块自动生成解释文案**：不修改底层推荐算法，仅通过给推荐结果增加 LLM 生成的描述性标题，即可显著提升用户采纳、重连与满意度，适用于电商推荐理由、广告文案和搜索推荐摘要等场景。

  - **上游聚类 + 批量生成降低计算成本**：先生成约 5,000 个艺术家簇的描述，再映射到数以百万计的个性化播放列表，避免为每个推荐逐个调用 LLM，电商/广告中可对商品类目、兴趣簇等做类似离线批量生成，再动态拼装到推荐结果上。

  - **多源弱信号融合作为 LLM 输入**：将音乐标签（流派、情绪、年代等）与用户 playlist 标题中的创意词频统计融合，用权重排序后送入提示词，可为推荐系统构造富含语义的上下文输入，类似思路可用于融合商品属性、用户评论和搜索词。

  - **低成本 LLM + 并行调用就满足线上近实时要求**：使用 Gemini 2.0 Flash，全量 5000 个簇并行生成 5 个候选标题，总耗时 <
  15 分钟、花费 ≈ $1，再通过 LLM-as-Judge 过滤，表明轻量级 LLM 结合离屏 pipeline 完全可支撑大规模推荐场景的文案生成。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：Deezer 的 Daily Mix 每天向用户推荐 5 个个性化播放列表，但仅展示两张专辑封面和部分艺人名称，缺乏描述性标题，用户难以理解每个列表的内容，影响点击率和满意度。人工撰写标题无法规模化，自动播放列表标题生成（playlist captioning）在工业界仍然困难。本文探索用 LLM 解决这一大规模文案生成问题，并强调即使推荐算法不变，仅靠语义框架（semantic framing）就能改变用户感知。

**方法关键点**：
- 不对单个播放列表生成标题，而是在上游对约 5,000 个艺术家簇生成标题；每个用户获得的 Daily Mix 由这些簇派生，从而通过复用降低计算量。
- 为每个簇构建多源描述信号：Deezer 专用标签库（流派、情绪、国家、年代等，带置信度权重） + 用户创建播放列表的标题文本（清洗、词频聚合、加权）。将排名后的加权描述词与代表艺人列表共同输入 LLM。
- 提示词设计让 LLM 扮演创意策展人，先分析输入、交叉验证，再生成 ≤16 个字符的简短标题，同时生成英、法、德、葡、西五种语言版本，并内置内容安全约束。
- 使用 Gemini 2.0 Flash 作为生成模型，并行调用 API，在全量簇上生成 5 个候选标题，总耗时 < 15 分钟，成本约 $1。
- 上线前通过三阶段校验：提示词内置安全规则；专业编辑人评；再用同款 LLM 作为评委对每个 (标题, 标签) 对打分 (平均 7.7/10)，只上线高分语言。

**关键实验与结果**：
- 2025 年 9‑10 月在 Deezer 上进行大规模在线 A/B 测试，实验组在原推荐列表上显示 LLM 生成的标题，对照组保持原有界面，推荐算法完全相同。
- 三项指标均显著提升 (p<0.01)：采纳率（至少播放过一次） +24.9%，重连率（至少三周有播放） +16.9%，满意度（收藏、加入列表或长播放且低跳过） +11.5%。
- 用户实际接触到的标题大部分 LLM 评委打分 ≥9/10，LLM 不仅产出流派类标题，还能准确捕捉到游戏原声、综艺节目等非音乐类主题。

**关键结论**：语义框架对推荐系统的用户行为有巨大影响，即便推荐内容完全未变，仅增加清晰且富有吸引力的文字说明，就可带来两位数的参与度提升，而 LLM 是实现这一目标的有力工具。
