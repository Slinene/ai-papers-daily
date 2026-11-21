---
title: Can LLMs Resolve Entity Conflicts in Domain Specific NLU Pipelines?
title_zh: LLM 能否解决领域特定 NLU 管道中的实体冲突？
authors:
- Akansha Bhardwaj
- Mingbo Cui
- Victor Guimaraes
- Dominik Kohler
- Diana Nicoleta Popa
- Meghana M. Reddy
- Paolo Rosso
affiliations:
- Telepathy Labs GmbH, Zürich, Switzerland
arxiv_id: '2611.25733'
url: https://arxiv.org/abs/2611.25733
pdf_url: https://arxiv.org/pdf/2611.25733
published: '2026-11-19'
collected: '2026-11-21'
category: LLM
direction: LLM 用于 NLU 实体冲突解决
tags:
- LLM
- Entity Conflict Resolution
- NLU
- LoRA
- Few-shot Prompting
- NER
one_liner: 对比规则、多 shot 提示与 LoRA 微调 LLM 解决多 NER 实体冲突，微调擅长模糊案例、提示更灵活，最佳为两者结合
practical_value: '- 在电商搜索 Query 解析或商品属性抽取中，若采用多个 NER 服务（品牌、型号、规格）且存在冲突，可在 pipeline
  末端增加 LLM 仲裁器，替代硬编码规则优先级；仅对冲突 span 调用 LLM 以控制延迟和成本。

  - 先用多 shot 提示快速测试新实体类型和冲突模式，积累错误案例；对模糊/高价值冲突再用 LoRA 微调内部小模型，同步获得可定制性和准确率。

  - 评估时要同时看“匹配原有规则输出”和“人工标注准确率”两个指标，否则可能把 LLM 训练成复现旧规则错误，失去改进意义。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

## 动机
领域特定 NLU 管道常采用多个 NER 提取器以利用各自专长，但不同提取器可能对重叠文本给出冲突实体类型。传统规则式冲突解决方法缺乏灵活性和可扩展性，因此探索 LLM 的通用知识能否承担仲裁角色。

## 方法关键点
以汽车领域数据为例，对比三种实体冲突解决策略：
- 传统规则方法；
- 多 shot prompting 使用 Llama3.1-8B-Instruct；
- LoRA 微调 Llama3.1-8B-Instruct。

评估设置包括两种场景：一是广泛评估 LLM 匹配现有 NLU 管道输出的能力，二是在人工标注数据上评估准确率，以更严格地衡量真实冲突解决能力。

## 关键结果
多 shot 提示在适应性和快速行为调整方面具有优势，适合快速迭代；LoRA 微调模型在复杂、模糊的冲突案例上表现更优，准确率更高。最佳实践是结合两种策略：利用多 shot 提示的灵活性快速响应变化，同时依赖 LoRA 微调带来的广泛准确率提升。
