---
title: '"I don''t know anything about laptops!" - User Perception of Digital Product
  Advisors Adapting to Their Knowledge Levels'
title_zh: 新手用户的笔记本电脑搜索助手：领域知识水平自适应的信息呈现效果研究
authors:
- Kevin Schott
- Andrea Papenmeier
- Daniel Hienert
- Dagmar Kern
affiliations:
- GESIS – Leibniz Institute for the Social Sciences
- University of Twente
arxiv_id: '2608.06091'
url: https://arxiv.org/abs/2608.06091
pdf_url: https://arxiv.org/pdf/2608.06091
published: '2026-08-06'
collected: '2026-08-08'
category: RecSys
direction: 对话推荐 · 用户知识水平自适应
tags:
- conversational commerce
- product recommendation
- domain knowledge
- explanation
- user study
- personalization
one_liner: 在聊天机器人产品推荐中，兼顾技术信息、性能分类与属性解释的 TCE 设计最能提升新手体验且不妨碍专家
practical_value: '- **默认采用 TCE 信息呈现模式**：在电商对话助手中，对技术类商品（如电脑、相机）统一提供“技术参数 + 性能等级标签
  + 通俗解释”，既帮助新手理解，又不损害专家效率，避免需要显式检测用户知识水平。

  - **避免孤立使用性能分类标签**：仅有“高性能”“入门级”等分类而无解释，新手会感到困惑且认为信息量不足；建议始终搭配类别含义说明与参数解读。

  - **单一自适应界面优于多版本分流**：不必为新老用户设计不同界面，一套包含解释和类别的混合呈现即可覆盖所有群体，降低工程维护成本。

  - **增加用户控制与个性化入口**：尽管 TCE 适合多数场景，仍可让用户主动调整信息详尽度或标注自身知识水平，用于进一步精排解释粒度，满足极端偏好。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：对话式电商中，数字助手如何向不同领域知识的用户呈现复杂商品信息是一大难题。单纯的技术参数对于新手难以理解，而过多的解释可能干扰专家效率。需要设计一种能同时服务两类用户的自适应信息呈现策略。

**方法**：构建一个笔记本选购聊天机器人场景，采用 2×2 被试间实验（n=251），探究四种信息呈现方式对新手和专家的影响：仅提供技术规格（T，基线）；技术规格 + 性能类别标签（TC，如“高性能处理器”）；技术规格 + 属性解释（TE，如“处理器影响多任务速度”）；三者组合（TCE）。评价指标包括感知有用性、信息量适当性、感知学习等。

**关键结果**：对新手而言，包含解释的呈现（TE、TCE）显著提高了感知帮助性和学习效果；TCE 在信息量适当性上优于 T 和 TC；仅在 TC 条件下新手会感到困惑和不足。专家在各条件下无显著差异，表明对新手有益的额外信息并未带来负面影响。最终提炼出四条设计指南：默认使用 TCE；保持单一包容性界面；避免孤立使用性能类别；支持用户自主性和场景个性化。
