---
title: 'From Raw IDs to Semantic Planning: How Recommender Systems Utilize Information
  at Scale'
title_zh: 从原始 ID 到语义规划：推荐系统信息利用的演进
authors:
- Changhong Jin
- Shiqiu Yang
- Roger Zhe Li
- Yingjie Niu
- Aghiles Salah
- Mete Sertkan
- Zheng Ju
- Xingsheng Guo
- Huifeng Guo
- Ruihai Dong
affiliations:
- University College Dublin
- Huawei Ireland Research Centre
arxiv_id: '2607.09540'
url: https://arxiv.org/abs/2607.09540
pdf_url: https://arxiv.org/pdf/2607.09540
published: '2026-07-10'
collected: '2026-07-13'
category: Other
direction: 推荐系统信息利用的范式演进
tags:
- Raw IDs
- Semantic IDs
- Semantic Planning
- Multi-stakeholder
- Recommender System Evolution
one_liner: 提出推荐系统正从原始 ID 经语义 ID 走向语义规划，将曝光目标显式化以协调多方利益
practical_value: '- **引入语义规划层**：在 item 检索之前先预测本轮曝光的语义目标（如安抚犹豫用户、降低感知风险），再实例化为具体商品/广告/文案。面向电商场景，可将排序解耦为「目标制定
  → 实例化」，更容易对多业务目标（转化、GMV、留存、新客获取）进行显式协调。

  - **语义 ID 作为中间控制变量**：电商大目录下，语义 ID 可封装类目、属性、场景标签等，使得跨域、跨模态的 item 共享同一结构化标识。可借鉴其离散
  token 序列的形式，让召回、排序、创意生成等异构模块直接消费同一 ID，降低跨空间对齐成本。

  - **识别未满足需求**：当语义目标无法被现有商品满足时，系统能沉淀出「需求缺口」信号，反向推动选品、招商或内容生产。这比单纯做 item 匹配更贴近平台经营逻辑。

  - **适配多利益方**：将广告、自然推荐、消息推送等统一到「曝光目标」语义层，使得同一目标可通过不同渠道实例化（商品、优惠券、直播预告），平台可基于目标层面分配流量和创意资源，而非各自独立优化。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：工业推荐系统长期依赖原始 ID 作为操作锚点，便于精确记忆和系统耦合，但难以利用语义结构进行跨域泛化与多任务统一。近年来语义 ID 的兴起将部分语义信息封装进标识符，但现有工作仍停留在“为用户匹配已有 item”的检索范式，未显式处理用户、平台、商家等多方目标的冲突。本文提出下一阶段应转向「语义规划」，先确定曝光要达成什么语义目标，再实例化为具体 item 或创意，将推荐从被动匹配引擎提升为主动决策系统。

**方法关键点**：
- **三阶段演进框架**：原始 ID → 语义信息围绕 ID → 语义 ID → 语义规划。语义 ID 使 item 身份结构化，便于跨域、多模态和搜索推荐任务的统一。
- **语义规划架构**：在上下文与最终 item 之间插入一个中间层，显式输出“语义目标”（如“城市中心灵活退订的安心住宿”），再通过实例化层检索现有商品、生成广告或推送文案，甚至标记需求缺口。
- **多利益方协调**：语义目标作为决策变量，同时考虑用户需求、平台战略和商家供给，使得一次曝光不再是单一 item 选择，而是一次多方目标的聚合表达。

**关键观点**：
- 语义检索仅回答“该显示哪个已有 item”，语义规划则先问“这次曝光要达到什么目的”。
- 语义规划使系统能识别库存无法满足的真实需求，并驱动更灵活的实例化（商品、消息、生成创意）。
- 评估需从命中率转向“规划共振度”，即决策序列是否引导用户走向满足的真实意图，需引入仿真评估 Agent。

**值得记住的一句话**：*推荐系统的演进不在于引入更多信号，而在于将信号封装进身份层，并最终将“下一刷该出什么”的问题显式化为“下一刷要达成什么”。*
