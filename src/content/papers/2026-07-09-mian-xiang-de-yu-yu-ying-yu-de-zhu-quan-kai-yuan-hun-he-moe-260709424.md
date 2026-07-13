---
title: A Sovereign, Open-Source Foundation Model for German and English
title_zh: 面向德语与英语的主权开源混合MoE Mamba Transformer基础模型
authors:
- The Soofi-Team
- Benedikt Droste
- David Fitzek
- Ruben Härle
- Lukas Helff
- Maximilian Idahl
- Alex Jude
- Abbas Goher Khan
- Maurice Kraus
- Timm Ruland
affiliations:
- Fraunhofer IAIS
- Technische Universität Darmstadt
- DFKI
- L3S Research Center
- KI Bundesverband
arxiv_id: '2607.09424'
url: https://arxiv.org/abs/2607.09424
pdf_url: https://arxiv.org/pdf/2607.09424
published: '2026-07-09'
collected: '2026-07-13'
category: Other
direction: MoE 混合架构 · 多语言主权开源
tags:
- MoE
- Mamba
- Sovereign AI
- German NLP
- Open-Source
- Foundation Model
one_liner: 混合MoE与Mamba架构激活3B参数即匹配14-27B稠密模型，长上下文吞吐大幅领先
practical_value: '- MoE与Mamba混合的恒定缓存设计，适合高并发长序列推理，可直接迁移至推荐系统用户长期行为建模，减少线上推理成本。

  - 通过故意上调目标语言（德语）的数据采样权重，显著提升下游性能，对于多语言电商推荐场景，可借鉴该策略强化小语种或特定领域效果。

  - 完全开放训练数据配比、超参与评估代码，为构建自有可控的业务基础模型提供了可复现的工程范式，适合对数据主权有要求的企业。

  - 模型在代码相关任务上突出，若业务需处理搜索词解析、规则匹配等代码生成，可作为微调基座。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有开源模型德语能力不足，且稠密模型在高并发长上下文场景下推理效率低。团队旨在构建一个主权自控、高性能的德英双语基础模型，完全在德国本土AI云上训练，并以最大开放性发布。

**方法关键点**：
- **架构**：MoE混合Mamba-Transformer，总参数量30B，每token仅激活3B，KV缓存接近恒定，长文本推理吞吐显著优于同规模稠密模型。
- **训练**：在约27万亿token上预训练，包含大量精心筛选的德语、英语及代码数据，故意上调德语采样权重以强化德语性能。
- **开放**：除权重外，发布中间检查点、全量数据来源说明、超参及训练评估代码。

**关键结果**：
- 在德英综合评测上与14-27B稠密模型持平，代码评测在17个开源模型中最佳。
- 超越所有参数量更大的欧洲主权基线（如Olmo 3 32B、Apertus 70B）。
- 完全开源模型中，德英两项评测得分最高。
