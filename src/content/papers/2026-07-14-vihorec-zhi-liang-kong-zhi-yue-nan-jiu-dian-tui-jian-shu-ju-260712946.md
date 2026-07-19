---
title: 'ViHoRec: A Quality-Controlled Vietnamese Hotel Recommendation Dataset and
  Cold-Start Benchmark'
title_zh: ViHoRec：质量控制越南酒店推荐数据集与冷启动基准
authors:
- Minh Hoang Nguyen
affiliations:
- Faculty of Information Technology, University of Science, Ho Chi Minh City
- Vietnam National University, Ho Chi Minh City
arxiv_id: '2607.12946'
url: https://arxiv.org/abs/2607.12946
pdf_url: https://arxiv.org/pdf/2607.12946
published: '2026-07-14'
collected: '2026-07-19'
category: RecSys
direction: 低资源推荐数据集构建 · 冷启动评估
tags:
- Vietnamese
- Hotel Recommendation
- Quality Control
- Cold-start
- Entity Resolution
- Privacy
one_liner: 贡献面向低资源越南语的酒店推荐数据集，通过跨平台对齐、质量控制和冷启动基准揭示稀疏数据下的难题
practical_value: '- **跨平台实体对齐**：电商/酒店业务涉及多数据源时，可借鉴论文的实体解析（Entity Resolution）方法，利用文本相似度与启发式规则统一不同来源的商品ID，构建统一交互。

  - **冷启动策略选择**：实验表明在极度稀疏、用户历史短的情况下，UserKNN优于BPR-MF等模型，提醒我们在新客/长尾场景下，基于邻域的协同过滤可能更稳定，可作为召回或兜底策略。

  - **可复现的数据质量控制**：论文采用可量化指标（如覆盖率、重复率、稀疏度）审计数据，而非人工清理，迁移到工业数据集构建时可设计类似的质量看板，确保数据迭代可追溯。

  - **隐私合规发布**：使用HMAC伪名化用户ID，既保护隐私又能维持可benchmark性，对于希望公开内部数据做学术合作的团队，提供了轻量级脱敏参考。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：越南语推荐系统缺乏公开的酒店交互数据，构建数据集面临跨平台名称对齐、可控质量审核、隐私保护下可基准化三大挑战。

**方法关键点**：
- 从Booking.com、Traveloka、Ivivu爬取交互，经跨平台实体解析统一酒店名，并结合定量指标（如覆盖率、重复率）进行质量控制。
- 采用HMAC伪名化处理用户ID，在保证隐私前提下生成可复现的公开数据集（18,267交互，6,832用户，560酒店）。
- 设计时间序列留一法冷启动基准，提供无外部依赖的基线（BPR-MF、UserKNN等），并通过数据消融分析稀疏性影响。

**关键结果**：
- 学习型模型在用户历史较短时性能骤降（BPR-MF Recall@10从0.120跌至0.065），而UserKNN整体最优。
- 数据集稀疏且冷启动主导，成为低资源场景的典型测试床，揭示冷启动下简单近邻方法更稳健。
