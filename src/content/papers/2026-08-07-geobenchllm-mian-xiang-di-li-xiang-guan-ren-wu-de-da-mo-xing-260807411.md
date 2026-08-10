---
title: 'GeoBenchLLM: A Comprehensive Benchmark for Evaluating LLMs on Geo-Related
  Tasks'
title_zh: GeoBenchLLM：面向地理相关任务的大模型综合评测基准
authors:
- Rodrigo Ferreira Rodrigues
- Karim Radouane
- Jose G Moreno
- Lynda Tamine
affiliations:
- University of Toulouse
arxiv_id: '2608.07411'
url: https://arxiv.org/abs/2608.07411
pdf_url: https://arxiv.org/pdf/2608.07411
published: '2026-08-07'
collected: '2026-08-10'
category: Eval
direction: 地理空间推理 · 评测基准
tags:
- Benchmark
- LLMs
- Geo-spatial
- Temporal Reasoning
- Evaluation
- Generalization
one_liner: 构建覆盖12类地理时空任务的多维度LLM评测基准，揭示推理与模型规模对地理理解的关键影响
practical_value: '- 地理位置相关搜索/推荐系统可借鉴该基准中的空间关系推理、路径规划等任务，评测模型对用户时空意图理解的能力

  - 评测框架中多任务、多数据集的构造方式可用于构建电商场景下的位置感知 Agent 或推荐模型评测集，避免单一任务过拟合

  - 发现推理能力对地理任务性能的提升显著，提示在搭建位置敏感型 LLM 应用时，应优先选用具备强推理能力的模型（如思维链增强）而非单纯增大参数规模

  - 数据集覆盖事实问答、路径规划等实用任务，可直接用于微调模型以提升对地址、POI、区域范围等实体的语义与空间关系建模，改善本地生活服务推荐质量'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**
现有地理领域 LLM 评测基准存在规模小、任务覆盖不全或局限于特定场景的问题，难以全面衡量模型的地理时空理解与泛化能力。为弥补这一空缺，研究者构建了综合基准 GeoBenchLLM。

**方法关键点**
从公开渠道精选 12 个地理相关数据集，涵盖空间关系推理（如城市方位判断）、路径规划、事实型地理问答、时间理解等多样任务与领域。在统一框架下评估不同规模、不同推理能力的 LLM（包括 GPT 系列、开源模型等），重点分析模型规模与推理策略对性能的影响。

**关键结果**
- 推理能力与模型规模对整体性能有显著影响，配备思维链等推理增强的 LLM 表现大幅领先。
- 在复杂空间关系推理与路径规划任务上，纯规模增长收益递减，而显式推理设计带来更稳定增益。
- 各模型在不同任务间表现差异明显，凸显单一任务评测的局限性，综合多任务基准更能反映真实地理理解水平。
基准完全开源，提供统一测试接口，支持快速复现与扩展。
