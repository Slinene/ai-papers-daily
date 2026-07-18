---
title: 'Multimodal Unlearning Across Vision, Language, Video, and Audio: Survey of
  Methods, Datasets, and Benchmarks'
title_zh: 多模态遗忘：视觉、语言、视频与音频的综述
authors:
- Nobin Sarwar
- Shubhashis Roy Dipta
- Zheyuan Liu
- Vaidehi Patil
affiliations:
- University of Maryland, Baltimore County
- University of Notre Dame
- UNC Chapel Hill
arxiv_id: '2607.07907'
url: https://arxiv.org/abs/2607.07907
pdf_url: https://arxiv.org/pdf/2607.07907
published: '2026-07-08'
collected: '2026-07-18'
category: Other
direction: 多模态遗忘 · 选择性去学习
tags:
- multimodal
- unlearning
- survey
- vision-language
- diffusion
- safety
one_liner: 系统梳理多模态遗忘的干预点、方法、数据集与基准，建立跨架构的统一分类体系
practical_value: '- **电商/推荐系统中数据删除与模型矫正**：若用多模态模型生成商品描述或推荐，当用户要求删除个人数据或平台需移除版权物料时，可借鉴参数高效遗忘方法（如
  LoRA 适配器、梯度编辑），在不重训模型的前提下定向遗忘。

  - **消除跨模态不良关联**：在搜索推荐中，用联合图文表征可能产生性别、种族等偏见关联（如“医生→男”），可采用架构约束遗忘或解码时干预，切断特定跨模态联系，同时保留通用能力。

  - **在线服务安全迭代**：面对舆情或法规变化，需紧急屏蔽某类商品或内容，可利用训练时的“遗忘正则项”或数据侧屏蔽，快速使模型停止生成相关推荐，避免全量回退。

  - **评估体系参考**：综述整理了多模态遗忘的度量维度（遗忘强度、保留度、效率、可逆性、鲁棒性），从业者可据此设计离线验证指标，确保遗忘操作不影响推荐核心指标。'
score: 6
source: arxiv-cs.MM
depth: abstract
---

多模态基础模型（VLM、DM、LLM、AFM）易从训练数据中编码敏感、侵权或有害的跨模态关联。数据删除或策略更新后重新训练成本高昂，且知识分布在共享表示中难以定向遗忘。多模态遗忘（multimodal unlearning）为此提供解决方案。

本综述按干预点将方法分为四类：数据侧屏蔽、训练时（含正则化、微调）、架构约束编辑、解码时后处理。统一比较了遗忘强度、知识保留、计算效率、可逆性和对抗鲁棒性之间的权衡。同时整理了面向多模态（视觉、语言、视频、音频）的遗忘数据集与基准，并讨论评估协议与开放问题。

主要发现：现有方法多侧重单一模态或简单跨模态关联，对复杂交织表示的遗忘仍困难；评估缺乏统一标准，遗忘-保留权衡、可解释性与效率难以兼顾。综述配套开源资源库，旨在推动多模态遗忘的研究与落地。
