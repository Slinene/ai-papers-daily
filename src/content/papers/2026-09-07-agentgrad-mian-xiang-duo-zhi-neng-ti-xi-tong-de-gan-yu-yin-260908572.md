---
title: 'AgentGrad: Intervention-guided Prompt Optimization for Multi Agent Systems'
title_zh: AgentGrad：面向多智能体系统的干预引导提示优化
authors:
- Jaewon Chu
- Jinwoo Seo
- Jaewon Cho
- Jeehye Na
- Yunyang Xiong
- Youngdae Kim
- Hyunwoo J. Kim
affiliations:
- Korea University
- KAIST
- Meta AI
- UNIST
arxiv_id: '2609.08572'
url: https://arxiv.org/abs/2609.08572
pdf_url: https://arxiv.org/pdf/2609.08572
published: '2026-09-07'
collected: '2026-09-11'
category: MultiAgent
direction: 多智能体提示优化 · 文本梯度
tags:
- Prompt Optimization
- Multi-Agent Systems
- Textual Gradient
- LLM
- Semantic Clustering
one_liner: 通过逐代理干预定位问题提示，并用语义聚类生成通用文本梯度，提升多智能体提示优化效果与效率
practical_value: '- 在多智能体电商/搜索/广告 pipeline 中，出现最终失败时，不要直接凭感觉改 prompt：借鉴 sequential
  intervention，逐一替换单个 agent 的输出或行为，判断修改哪个 agent 才能消除失败，再针对性优化其 prompt。

  - 用「干预后的正确输出」作为 agent-level supervision，让 LLM 基于具体输出差异生成文本梯度，而不是只给最终正确/错误标签；这能让
  prompt 更新更细粒度、更可落地。

  - 批量优化时，先对失败 case 对应的梯度做语义聚类，再按簇抽象成通用修正规则，避免把无关 failure mode 混在一起导致 prompt 过拟合或泛化差。

  - 若要在生产环境自动提示迭代，AgentGrad 的干预定位+聚类聚合可减少 LLM 调用次数，实测优化墙钟时间比次快 baseline 平均少 2.5 倍，适合成本敏感场景。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：现有多智能体系统的文本梯度提示优化存在两个问题——梯度提取时未验证修改目标 prompt 是否真能解决失败，也缺少 agent 级中间输出监督；梯度聚合时随机拼接，混合无关失败模式，导致泛化差。

方法关键点：
- Sequential intervention：对每个失败 case，逐个干预单个 agent 的行为，定位修改哪个 agent 能消除失败；将该 agent 被干预后的输出作为 agent-level supervision。
- 基于该 supervision 提取细粒度文本梯度，描述从错误输出到修正输出的模式。
- Semantic textual gradient abstraction：对多个梯度做语义聚类，防止混合无关失败模式；每个簇抽象成一条通用梯度，捕获共享的修正模式。

关键结果：在五个 MAS benchmark 上达到 SOTA，并且优化墙钟时间比次快 baseline 平均降低 2.5 倍。
