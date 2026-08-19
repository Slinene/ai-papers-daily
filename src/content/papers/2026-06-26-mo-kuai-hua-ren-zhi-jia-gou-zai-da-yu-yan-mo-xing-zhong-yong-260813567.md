---
title: Modular Cognitive Architecture Emerges in Large Language Models
title_zh: 模块化认知架构在大语言模型中涌现
authors:
- Pengrui Han
- Jacob Andreas
- Evelina Fedorenko
- Andrea Gregor de Varda
affiliations:
- Massachusetts Institute of Technology
arxiv_id: '2608.13567'
url: https://arxiv.org/abs/2608.13567
pdf_url: https://arxiv.org/pdf/2608.13567
published: '2026-06-26'
collected: '2026-08-19'
category: LLM
direction: LLM 模块化架构与功能特化
tags:
- LLM
- modularity
- circuit analysis
- functional specialization
- cognitive domains
- interpretability
one_liner: 通过46个认知任务的电路分析，发现LLM形成与人类大脑相似的模块化架构，同域任务共享神经元
practical_value: '- 电商推荐多任务模型可借鉴模块化思想：将语言理解、数值推理、用户意图/社会偏好等不同认知域任务分组，设计稀疏激活或MoE结构，让不同专家模块处理不同域，提高参数效率和效果；LLM内部已有功能分工，显式模块化可降低任务间干扰。

  - Agent系统设计：针对商品属性逻辑推理、用户评论情感分析、价格比较等不同性质子任务，可以设计专门的子Agent或推理链，因为LLM内部已存在对应模块化表征，显式引导能更好地调用相关能力。

  - 模型诊断与调试：在实际业务中遇到bad case时，可采用电路分析定位是哪个功能模块失效（例如语言理解模块还是数值推理模块），从而针对性地添加训练数据或调整prompt，而不是全参数微调或笼统调参。

  - 多任务学习中的任务分组：通过计算神经元激活重叠度来判断任务间关系，指导哪些任务可以共享底层参数、哪些需要独立分支，减少负迁移，提高整体效果。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：人类大脑具有高度功能特化，不同网络分别支持语言、形式推理、社会推理和物理推理。这种模块化是智能系统的基本原理还是生物进化的偶然？本文检验在LLM中是否出现类似组织。

**方法关键点**：对N=46个任务跨四个认知域，采用电路分析（circuit analyses），比较任务在LLM中激活的神经元重叠程度与人类脑网络对应关系。

**关键结果**：发现LLM发展出与人类大脑相似的模块化架构——在人类中依赖相同网络的任务，在LLM中招募重叠神经元；依赖不同网络的任务，招募不同神经元。该收敛现象表明模块化可能是智能系统的基本属性，而非生物大脑特有。
