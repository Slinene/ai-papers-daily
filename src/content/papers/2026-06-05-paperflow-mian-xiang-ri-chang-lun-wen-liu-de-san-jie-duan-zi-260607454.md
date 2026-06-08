---
title: 'PaperFlow: Profiling, Recommending, and Adapting Across Daily Paper Streams'
title_zh: PaperFlow：面向日常论文流的三阶段画像-推荐-自适应框架
authors:
- Fuqiang Wang
- Song Tan
- Zheng Guo
- Jiaohao Fu
- Xinglong Xu
- Bihui Yu
- Jie Dong
- Zheng Sun
- Siyuan Li
- Jingxuan Wei
affiliations:
- Key Laboratory of Computing Power Network and Information Security, Ministry of
  Education, Shandong Computer Science Center (National Supercomputer Center in Jinan),
  Qilu University of Technology (Shandong Academy of Sciences)
- University of Chinese Academy of Science
- Shanghai Artificial Intelligence Laboratory
arxiv_id: '2606.07454'
url: https://arxiv.org/abs/2606.07454
pdf_url: https://arxiv.org/pdf/2606.07454
published: '2026-06-05'
collected: '2026-06-08'
category: RecSys
direction: 科研论文流推荐 · 画像漂移自适应
tags:
- Paper Recommendation
- User Profiling
- Interest Drift
- Multi-signal Ranking
- Longitudinal Benchmark
one_liner: 提出面向日常论文流的三阶段框架，通过动态画像、多信号排序和兴趣漂移自适应提升纵向推荐效果
practical_value: '- 日常流式推荐场景可借鉴三阶段架构：Profiling阶段将冷启动证据转化为结构化兴趣画像，电商中可从用户行为序列、搜索词等构建动态画像，避免静态特征失效。

  - Recommending阶段的多信号聚合排序在固定曝光预算下平衡相关性与多样性，类似电商信息流或消息推送，可以将CTR预估、多样性指标、时效性等信号加权融合，并引入曝光预算控制。

  - Adapting阶段利用语义不同的反馈信号（点击、忽略、收藏等）增量更新用户状态，建模兴趣漂移，适合电商中基于用户实时行为的在线学习系统，可与类似EWC或记忆回放的方法结合防止遗忘。

  - 提出的纵向用户-日基准设计思路可直接复用：固定时间窗口、用户、候选池，模拟每日决策与累积反馈，评估系统在连续交互下的长期表现，比单次离线评估更贴近线上效果。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：学术论文推荐通常被简化为静态候选集上的单次排序，但真实场景中研究者每天面对新论文流，阅读时间有限，兴趣随时间漂移，需要系统能够动态适应用户状态变化。现有方法缺乏对纵向、日常交互的建模。

**方法**：提出PaperFlow框架，将推荐过程解耦为三个循环阶段：Profiling从冷启动时的异质证据（如已发表论文、关键词）构建结构化、可解释的学术画像；Recommending在每个日期对特定论文流进行多信号聚合排序，在固定展示预算下平衡相关性、多样性和时效性；Adapting利用语义不同的反馈信号（如点击、忽略）增量更新用户状态，显式建模兴趣漂移，避免信息覆盖。同时构建了一个纵向用户-日基准，包含24个模拟研究者、50天论文流、1200个用户-日episode，并设计人工盲评协议验证指标对齐。

**结果**：与五个学术推荐基线相比，PaperFlow在基于oracle的排序指标、模拟阅读选择的行为对齐度以及人工盲评得分上均达到最优，证明了长周期、自适应框架在流式论文推荐中的有效性。
