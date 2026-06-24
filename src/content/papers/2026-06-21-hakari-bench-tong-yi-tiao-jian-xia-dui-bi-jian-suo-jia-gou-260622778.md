---
title: 'HAKARI-Bench: A Lightweight Benchmark for Comparing Retrieval Architectures
  and Efficiency Settings under Unified Conditions'
title_zh: HAKARI-Bench：统一条件下对比检索架构与效率设置的轻量级基准
authors:
- Yuichi Tateno
arxiv_id: '2606.22778'
url: https://arxiv.org/abs/2606.22778
pdf_url: https://arxiv.org/pdf/2606.22778
published: '2026-06-21'
collected: '2026-06-24'
category: Eval
direction: 轻量级检索基准 · 效率与质量权衡
tags:
- Retrieval Benchmark
- Embedding Models
- RAG
- Efficiency
- Multilingual
one_liner: 构建轻量级检索基准，高保真复现大规模排名，支持快速模型选择与效率权衡分析
practical_value: '- 覆盖 BM25、稠密、稀疏、后期交互、重排序等多种检索家族及量化/降维等效率变体，可直接用于推荐系统检索模块的快速选型和配置对比，避免每次全量评估。

  - Nano-sets 轻量数据集重构方法（保留排名一致性且规模仅 20%~50%）可借鉴到电商搜索/推荐场景，构建离线快速实验评估集，加速模型迭代。

  - 统一格式与固定候选集实现模型无关评估，并绘制质量-效率帕累托前沿，可指导线上模型压缩与加速策略，平衡推理成本与效果。

  - 多语言检索任务（43 种语言）可测试跨语言搜索推荐场景，评估模型在多语言电商或内容推荐中的泛化能力。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**  
随着 RAG 和语义搜索普及，选择嵌入与检索配置愈发困难。大型基准全面但重跑代价高，且缺乏在同条件下对比降维、量化、重排序等生产设置的基础设施。  

**方法关键点**  
HAKARI-Bench 将现有检索基准重构成 Nano-sets（小数据集），覆盖 35 个基准、551 个任务、43 种语言，统一为「语料-查询-标签-固定候选集」格式，确保模型无关的同条件评估。支持 BM25、稠密、稀疏、后期交互、重排序 5 种检索家族，以及 Matryoshka 降维、int8/binary 量化、float rescoring 等效率变体。  

**关键结果数字**  
在 55 个模型上，HAKARI-Bench 的总体排名与 MTEB retrieval v2、MMTEB v2 retrieval、English BEIR (full) 的斯皮尔曼相关系数均 >0.97（0.983 / 0.975 / 0.973），可作为高保真排名代理，支持快速模型筛选、回归检测和质量-效率帕累托前沿分析。
