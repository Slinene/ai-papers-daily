---
title: 'From Waste to Discovery: Recycling High-Scored Unexposed Candidates in Taobao
  Feed Recommendation'
title_zh: 从废弃到发现：淘宝信息流推荐中高分未曝光候选的回收利用
authors:
- Ge Fan
- Kai Meng
- Huiping Chu
- Yuning Jiang
- Han Zhu
- Bo Zheng
affiliations:
- Taobao & Tmall Group of Alibaba, Hangzhou, China
- Taobao & Tmall Group of Alibaba, Beijing, China
arxiv_id: '2611.05997'
url: https://arxiv.org/abs/2611.05997
pdf_url: https://arxiv.org/pdf/2611.05997
published: '2026-11-04'
collected: '2026-11-05'
category: RecSys
direction: 召回阶段 · 探索与发现 · 未曝光样本复用
tags:
- exploration
- recall
- unexposed samples
- discovery
- calibration
- industrial recommendation
one_liner: 回收排序高分但未曝光的候选，以训练无关的召回通道显著提升发现性且不损互动
practical_value: '- 不要盲目做 exploration boosting：先离线审计 ranker 在冷启动/discovery 候选上的 PCOC
  和 RMSE。如果冷候选被系统性高估且排序误差更大，boost 会放大 maximization bias，线上往往没有显著发现收益且可能负向互动。

  - 复用每次请求已经产生的高分未曝光样本：工业排序每天产生大量 scored but unexposed items，用异步落盘 + 批量聚合构建用户侧候选池，再通过
  O(1) KV lookup 接入召回。无需重训模型、无需改 serving 架构，适合资源受限团队。

  - 探索型召回要按“供给累积”设计：单日高分未曝光探索候选稀缺，但 30 天窗口内会变丰富。可用 UV coverage 和 effective sequence
  length 作为离线供给指标筛选窗口和注入配额，而不是直接烧线上 A/B 预算扫超参。

  - 方法可迁移到 freshness、creator fairness、long-tail exposure 等场景，前提是选择 ranker 对 never-exposed
  items 分数可信的 segment；对 ranker 明显盲区，如冷启动用户和冷类目，应保留专门的冷启动通道。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
工业推荐系统过度优化短期互动，导致用户曝光集中在少量熟悉类目中。在淘宝短视频推荐中，discovery categories 仅占平台曝光的 6.2%。常见的探索 boosting 直接注入冷内容，但冷候选对模型缺乏用户侧信号，rank 预测回落至 population prior，产生两个耦合问题：预测被系统性高估、排序误差大。在线对照实验显示随机注入发现类候选不仅没有显著发现收益，还使总视频观看量小幅负向。问题不在“注入更多”，而在“选择更好”。

**方法关键点**
URED 是一个训练无关的召回增强模块，核心是回收排序高分但从未曝光的候选：
- 每次排序后保留每个 session top-200 高分未曝光样本，异步写入 HDFS；
- 每日批量按用户聚合 30 天滑动窗口内的未曝光样本，去重并按 recency 排序，每人保留 top-10,000；
- Discovery-oriented mining：保留 category 在过去 d=15 天未曝光过的候选；
- Online serving：以用户 ID 建立 Redis KV 索引，请求时做一次 O(1) 查询，将最多 k=1000 个候选合并进统一召回池，流经原有排序和重排，端到端延迟开销低于 1%。

核心 insight 是：高分未曝光候选同时具备 relevance 和 predictability——rank 高分说明模型有足够用户信号，预测可信；而冷候选高分更多是 prior 高估，不可作为排序依据。

**关键实验与结果**
系统在淘宝 feed 推荐中已服务超过 6 个月，覆盖数千万 DAU。线上 A/B（超过一周）显示：
- discovered categories +3.47%，richness +8.47%，completion VV +2.62% 显著提升；
- total VV +0.36% 但不显著；
- ablation：1-day 聚合窗口将发现收益从 +3.47% 降到 +0.55%（不显著）；随机发现注入无显著收益且 total VV -0.17%；
- channel-level：URED 有效观看率 1.03× 平台平均，发现浓度 85.9%，是平台平均的 13.9 倍、最强 nearline baseline MNR 的 6.3 倍；
- 超参敏感性：窗口 t=30 天为 knee point；配额 k=1000 已捕获大部分收益，继续增大供给接近耗尽。

**最值得记住的一句话**
探索与互动的 trade-off 并非固有，而是注入了模型无法理解的内容；回收模型自己高分但未曝光的候选，能以低成本、零训练实现发现性提升而不损害互动。
