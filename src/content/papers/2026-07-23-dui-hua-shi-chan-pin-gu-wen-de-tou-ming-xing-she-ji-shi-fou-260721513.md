---
title: Transparent by Design, Usable in Practice? A Formative Usability Study of a
  Conversational Product Advisor
title_zh: 对话式产品顾问的透明性设计是否真的可用？一项形成性可用性研究
authors:
- Kevin Schott
- Dagmar Kern
- Daniel Hienert
affiliations:
- GESIS – Leibniz Institute for the Social Sciences
arxiv_id: '2607.21513'
url: https://arxiv.org/abs/2607.21513
pdf_url: https://arxiv.org/pdf/2607.21513
published: '2026-07-23'
collected: '2026-07-25'
category: RecSys
direction: 对话式推荐系统可用性研究
tags:
- usability
- conversational recommender systems
- transparency
- ranking explanation
- think-aloud study
- LLM
one_liner: 在笔记本电脑推荐对话系统中，设计上透明的排名解释功能反而引发了最严重的可用性问题，且用户需要额外的直接操控控件。
practical_value: '- 对话推荐中，即使提供排名解释，用户也可能因认知负荷过高而困惑，需将解释简化为关键因子的可视化（如权重条、标签），而非长文本。

  - 用户期望混合交互：对话式引导辅以直接操控控件（如滑块筛选、多选），可兼顾易用性与控制感，尤其适合参数敏感型商品（3C、家电）。

  - 比较功能不应仅列属性表，应突出差异化并解释“为何A比B更适合你”，否则用户仍难以决策。

  - 产品搜索agent设计时，需通过早期可用性测试暴露解释逻辑的认知断裂，避免“设计上透明”变成“体验上干扰”。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

动机：LLM 驱动的对话推荐系统易产生活泼但黑箱的体验，用户难以理解排序依据和证据。为研究设计透明性是否切实可用，作者对一款内置受限自然语言生成、按需排名解释和商品比较功能的笔记本电脑搜索聊天机器人进行了形成性可用性测试。

方法：采用有主持的出声思维实验室实验，7 名被试完成 3 项搜索任务，事后测量可用性量表，并对录像进行严重度分级的问题编码。

关键结果：系统易用性和满意度评分较高，但两个核心发现是——(1) 预先设计的透明度未保证理解：多位被试从理论上认可排名解释，但它却引发了最严重的可用性问题（对解释文本的解读困难、忽略或误解）；(2) 被试认可系统节省努力，但一些人希望有额外的直接操控控件（如滑块、筛选器）来增强控制感。最终贡献为一份按严重度排序的可用性问题清单及面向人本对话推荐系统的设计启示。
