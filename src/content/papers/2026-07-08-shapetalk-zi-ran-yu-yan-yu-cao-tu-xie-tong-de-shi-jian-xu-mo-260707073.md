---
title: 'ShapeTalk: Combining Natural Language and Sketch for Time-Series Pattern Querying'
title_zh: ShapeTalk：自然语言与草图协同的时间序列模式查询
authors:
- Guoruizhe Sun
- Yueqiao Chen
- Emily Guo
- Yutong Yao
- Dongyu Liu
arxiv_id: '2607.07073'
url: https://arxiv.org/abs/2607.07073
pdf_url: https://arxiv.org/pdf/2607.07073
published: '2026-07-08'
collected: '2026-07-12'
category: Other
direction: 时序数据查询·多模态交互
tags:
- Time-Series Query
- Natural Language Interface
- Sketch-based Query
- LLM Parsing
- Visual Analytics
one_liner: 提出用自然语言和草图互补查询时序模式，LLM解析语言为可编辑的形状约束
practical_value: '- 可借鉴 LLM 解析自然语言为可编辑特征约束的流水线，在电商销量趋势查询或异常检测中，让运营人员用自然语言描述模式（如“先涨后跌”），系统自动转化为形状过滤器。

  - 多模态协同思路可映射到推荐系统的用户意图表达：自然语言描述偏好，再通过可视化交互（如拖拽权重）细化需求，提升可解释性和可控性。

  - 同步视图和迭代查询的交互设计适用于推荐策略调试工具，分析师可通过多轮文本+交互逐步精炼召回或排序规则。

  - 落后于业务可直接迁移：将论文中的形状解析改造成对指标曲线的语义查询，用于广告排期或活动效果归因的快速检索。'
score: 6
source: arxiv-cs.HC
depth: abstract
---

**动机**：在金融、气候、医疗等领域的时序数据分析中，用户常需查找符合特定形状模式的片段，但现有工具难以表达模糊、复合或带有语义的查询意图（如“快速上升后缓慢下降”），导致试错成本高。

**方法**：ShapeTalk 提出将自然语言与草图作为互补的查询模态，而非强制性融合。自然语言擅长描述语义和组成结构，草图则提供几何形状的直接精修。系统通过 LLM 语义解析流水线把自由文本转换为可解释、可编辑的形状特征约束（如趋势斜率、局部极值），并与草图查询共享特征表示和结果视图。用户可在文本与草图间灵活切换，迭代构造查询。

**结果**：通过两个实际场景案例、用户研究及失败案例分析，表明自然语言是易用的起点，而草图在文本描述不足时提供有效的细化和纠偏能力，整体提升了时序模式搜索的效率和成功率。
