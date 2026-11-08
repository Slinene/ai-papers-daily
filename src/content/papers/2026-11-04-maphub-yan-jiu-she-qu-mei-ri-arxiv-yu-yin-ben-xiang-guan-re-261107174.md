---
title: 'MapHub: Daily Relevance Heatmaps of New arXiv Preprints for a Research Community'
title_zh: MapHub：研究社区每日 arXiv 预印本相关性热力图
authors:
- Kaili Cao
- Camille Avestruz
- Feige Wang
affiliations:
- Michigan Institute for Data and AI in Society (MIDAS), University of Michigan
- Department of Physics, University of Michigan
- Leinweber Institute for Theoretical Physics, University of Michigan
- Department of Astronomy, University of Michigan
arxiv_id: '2611.07174'
url: https://arxiv.org/abs/2611.07174
pdf_url: https://arxiv.org/pdf/2611.07174
published: '2026-11-04'
collected: '2026-11-08'
category: RecSys
direction: LLM 个性化内容相关性评分
tags:
- LLM
- personalized recommendation
- relevance scoring
- arXiv
- portfolio
- evaluation
one_liner: 用 LLM 为社区每位研究者对每日 arXiv 新预印本打 0–100 相关性分，并发布热力图
practical_value: '- 用 LLM 直接基于用户「作品/行为 portfolio」对候选内容进行 0–100 相关性打分，可作为召回后精排或重排层，尤其适合论文、资讯、短视频等非结构化内容；portfolio
  可来自用户历史发布、点击、收藏等。

  - 热力图的「item × user」打分矩阵不仅是推荐结果，也可作为算法日常监控和 case 诊断，快速发现哪些内容被谁高相关命中，辅助运营/审核。

  - 评估方式借鉴：用盲评的 top-k 命中率（如 top10% 覆盖 top5% 比例）替代单纯 AUC/相似度对比，更贴近业务真实「重要内容不会漏」的目标；文本匹配基线仅约
  1/3 而 LLM 约 70% 说明 LLM 语义匹配收益显著。

  - 成本与工程实现：标准 Claude 订阅即可支持每日全量论文打分，说明在中小 item 池（每日数百/千条）用 LLM 做相关性标注可行；可以缓存用户 profile、批量调用、只对新增
  item 评分。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：arXiv 每日新增大量预印本，研究人员无法平等关注；现有工具如 myADS、个性化推荐、开源 LLM 排名多为单用户或内部讨论，缺乏「每篇论文 × 每位成员」的全局相关性视图。

**方法关键点**：MapHub 为每个参与者构建 portfolio（代表其研究兴趣与工作），用 LLM 读取当天新论文并对照 portfolio 打 0–100 相关性分；发布为热力图，行=论文、列=参与者，公开显示每篇论文触达谁的工作；运行在标准 Claude 订阅上。

**关键结果**：作者盲评中，MapHub 分数前 10% 论文覆盖了评分者自身 top 5% 论文的约 70%，而文本匹配基线仅约 1/3；每天 astro-ph 论文中约 6% 对每个参与者达到 30 分，每三天有一篇达到 60 分。
