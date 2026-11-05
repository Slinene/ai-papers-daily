---
title: 'ConceptARC at Scale: Studying Conceptual Understanding in Reasoning Models'
title_zh: 规模化 ConceptARC：研究推理模型的概念理解
authors:
- Philipp Mondorf
- Adrien Deliège
- Solim LeGris
- Claas Beger
- Ryan Yi
- Barbara Plank
- Brenden M. Lake
- Todd M. Gureckis
affiliations:
- LMU Munich & MCML
- University of Liège
- New York University
- Santa Fe Institute
- Princeton University
arxiv_id: '2611.06732'
url: https://arxiv.org/abs/2611.06732
pdf_url: https://arxiv.org/pdf/2611.06732
published: '2026-11-04'
collected: '2026-11-05'
category: Eval
direction: 推理模型概念抽象评测
tags:
- ConceptARC
- ARC
- reasoning models
- benchmark
- conceptual abstraction
- representation analysis
one_liner: 构建 1600 任务 ConceptARC-100 评测 LRMs，发现任务表征按对象变换操作聚类
practical_value: '- 评测可按“概念/操作”分组，而不是只看整体分数：对搜索/推荐的 Agent 链路，可定义“过滤、重排、属性归一化、条件替换”等操作，批量生成样本，定位模型在哪些抽象操作上不稳定。

  - 数据生成器+人工抽检：用模板约束批量产生评测/训练数据，能低成本扩量；适合业务中可被规则化生成的任务，如商品标题生成、query 改写、prompt 筛选等。

  - 表征诊断：若下游任务表现差，可分析 LLM 的 task representation 是否按操作类型聚集；没有清晰聚集时，针对该操作补数据或加适配器/LoRA
  精调。

  - 空间/对象变换可借鉴 ARC 网格思路，用于商品图片布局、GUI Agent 的合成数据，提升模型对对象包含、位移、改色等概念的泛化。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

动机：LRMs 在强推理基准上表现好，但不确定它们是否在概念相关的推理任务间形成可泛化抽象。ARC 只测单任务规则抽象；ConceptARC 按概念分组，但每个概念人工任务太少。

方法：构建 ConceptARC at Scale 生成器，可针对特定概念批量生成 ARC 风格任务；由此构建 ConceptARC-100，覆盖 ConceptARC 16 个概念，每个概念 100 个任务，共 1,600 个，人工复核，规模为原基准 10 倍。评测多种近期 LRM 和从头训练的模型，并分析内部表征。

结果：不同模型在各概念上可靠解决与困难点存在差异；任务表征按对象操作（recoloring、removal、translation）聚类，即使规则和场景差异很大，表明模型形成了跨任务稳定的变换操作抽象。
