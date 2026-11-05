---
title: 'Length Is Cheap, Competition Is Not: Attention Predicts Context Rot in Retrieval'
title_zh: 长度廉价，竞争不廉价：注意力预测检索中的上下文退化
authors:
- Yinuo Liu
affiliations:
- University of California San Diego
arxiv_id: '2611.04169'
url: https://arxiv.org/abs/2611.04169
pdf_url: https://arxiv.org/pdf/2611.04169
published: '2026-11-02'
collected: '2026-11-05'
category: RAG
direction: 长上下文检索 · 注意力竞争
tags:
- context rot
- long-context LLM
- attention dilution
- distractors
- RAG
- knowledge conflicts
one_liner: 发现检索中长上下文失败主因是注意力竞争而非长度；证据上的注意力质量可预测失败
practical_value: '- 在 RAG 与搜索增强 prompt 中，重点控制与目标证据同格式、同实体但冲突的干扰项；对召回文档做冲突检测/去重，保留高相关且无
  rival value 的片段，可避免准确率骤降。

  - 将“证据注意力质量”作为线上 LLM 检索/重排的可观测指标：离线计算关键证据片段上的注意力占比或衰减，低于阈值时触发上下文裁剪、重写、重排，提前拦截上下文退化。

  - 不要为了省 KV cache 直接 mask/丢弃长上下文 token：可见中性填充对检索几乎无损，但 mask 会扭曲注意力分布，损失可达 46 个准确率点；稀疏注意力策略需在检索任务单独验证。

  - 为 Agent 工具返回或商品知识构造上下文时，长度不是主要成本，信息竞争才是；可对工具输出做摘要压缩、去冲突，并把关键证据放到注意力竞争弱的显著位置。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：长上下文模型检索失败通常被归因于序列长度，但长度增长常伴随内容竞争，两者未解耦。本文旨在回答：检索中的上下文退化（context rot）主因是长度本身还是注意力竞争。

**方法关键点**：在五个开源模型（0.5B–3B，四个家族）上设计对照实验：①中性填充（无信息 token）与同格式证据语句（与目标证据结构相似但可能无关）置于相同位置；②引入 rival value（给查询键一个竞争值）的单条干扰语句，并逐条增加 rival；③测量证据 token 上的注意力质量（attention mass）。同时对比 masked-filler 协议（隐藏添加 token 但保留位置）与可见控制的差异。

**关键结果数字**：中性填充在 32K token 下准确率仍高达 0.97–1.00；同格式证据语句使准确率骤降至 0.11–0.21；单个 rival value 使损失放大 9–110 倍，且随 rival 数量线性累加。注意力质量与损失强相关：126,473 次试验中解释方差最高 58%，而 log 长度最多解释 8%。masked-filler 协议在 MMLU 上重现长度损失（30K token 掉 11–18 分），但在检索可见控制失败：mask 填充损失 46 个准确率点，相同填充可见则无损。结论：检索中的上下文退化本质是注意力竞争，而非长度。
