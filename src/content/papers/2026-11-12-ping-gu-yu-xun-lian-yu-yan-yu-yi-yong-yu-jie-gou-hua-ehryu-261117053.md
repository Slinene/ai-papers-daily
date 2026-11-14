---
title: Evaluating Pretrained Language Semantics for Structured EHR Prediction Tasks
title_zh: 评估预训练语言语义用于结构化EHR预测任务
authors:
- Ashvin Gupta
- Brendan Delaney
- Alessandra Russo
affiliations:
- Imperial College London
arxiv_id: '2611.17053'
url: https://arxiv.org/abs/2611.17053
pdf_url: https://arxiv.org/pdf/2611.17053
published: '2026-11-12'
collected: '2026-11-14'
category: LLM
direction: LLM 医疗时序预测
tags:
- EHR
- LLM
- LoRA
- Continual Pretraining
- Clinical NLP
- Longitudinal Modeling
one_liner: 用自然语言事件描述+EHR持续预训练+LoRA微调LLM，提升多时间窗结构化EHR预测性能
practical_value: '- 将用户历史行为写成自然语言事件流（如“购买了X，价格Y，间隔Z天”），可用LLM做用户编码，替代ID embedding；注意保留数值字段（价格、数量），文本中显式时间间隔收益不大。

  - 领域自适应两阶段：先在领域语料上做持续预训练（continued pretraining），再对下游任务LoRA微调；相比直接微调更稳，尤其跨分布预测（类比跨品类/新客冷启动）。

  - 事件描述质量至关重要：错位/不确定的描述会损害性能；做query/商品语义映射时尽量用准确、一致的文本描述。

  - 学到的用户表示可分析：聚类/结构能体现疾病风险与历史模式，电商中可用来做用户分层、人群洞察。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

动机：结构化EHR模型通常把每个临床概念当作数据集特定token，丢弃自然语言语义，概念关系只能从共现中学习。

方法要点：tEHR 将事件用自然语言描述表示，形成纵向文本流；先进行 EHR 自适应持续预训练（continued pretraining），再针对下游任务做判别式 LoRA 微调，把 LLM 当作患者序列编码器。输入包含临床描述与数值信息，并测试了显式 elapsed-time 描述。

关键结果：在 MIMIC-IV 四个预测任务和 CPRD 胰腺癌预测（1–12 月窗口）上，基于 Mistral-7B-v0.3 的 tEHR 总体最强。消融显示：去掉/错位临床描述、省略数值、去掉任一适应阶段都会造成性能下降；显式时间间隔描述无额外收益。患者表示呈现与疾病风险和病史相关的临床一致结构。
