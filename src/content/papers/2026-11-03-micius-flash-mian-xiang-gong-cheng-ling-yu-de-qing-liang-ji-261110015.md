---
title: 'Micius-Flash: Lightweight Agentic Intelligence for Engineering'
title_zh: Micius-Flash：面向工程领域的轻量级智能体模型
authors:
- Hongcheng Gao
- Weiheng Li
- Yipeng Wei
- Yu Lei
- Shuo Sun
- Yi Li
- Yajiao Wang
- Jie Luo
- Jianwei Wen
- Xinyi Zhou
affiliations:
- Micius Team
arxiv_id: '2611.10015'
url: https://arxiv.org/abs/2611.10015
pdf_url: https://arxiv.org/pdf/2611.10015
published: '2026-11-03'
collected: '2026-11-12'
category: Agent
direction: 工程智能体模型训练
tags:
- Agent
- Distillation
- Multimodal
- Hardware Coding
- Data Flywheel
one_liner: 27B多模态工程模型，以知识树数据飞轮与多教师在线策略蒸馏整合专家能力，硬件代码与半导体Agent基准显著超同尺寸基线
practical_value: '- **知识树驱动数据飞轮**：用知识树组织领域知识、扩展数据合成，可用于构建垂直行业的训练数据——例如把电商类目、商品属性、用户意图做成知识树，系统性生成推荐解释、搜索改写、Agent决策等训练样本。

  - **多教师在线策略蒸馏**：训练多个专家模型（如检索、排序、文案生成、工具调用），再在自生成序列上蒸馏融合。适合把臃肿的多模型推荐/Agent系统压缩为单一轻量模型，降低线上推理成本。

  - **工具执行反馈闭环**：Micius Harness连接EDA、KiCad等工具，通过多步规划、代码调试、迭代验证提升任务成功率。可直接借鉴到电商Agent：让模型调用商品查询、价格计算、库存接口，基于执行结果自我纠错，而非只靠静态prompt。

  - **硬例增强**：质量校验阶段加入hard-example augmentation，能缓解长尾问题。对搜索/推荐中的稀疏类目、冷门query、复杂会话，可用类似方法定向合成困难样本提升鲁棒性。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：通用大模型在工程领域（硬件代码、芯片设计）表现不足，大型模型推理成本高，缺乏能连接专业工具的多模态推理Agent。

**方法关键点**：
- 提出知识树驱动的数据飞轮，三阶段：知识树构建与扩展、数据合成、质量校验+硬例增强。
- 训练多个专家模型：半导体知识推理、硬件编码、多模态理解、Agent专家。
- 采用Multi-Teacher On-Policy Distillation（MOPD），在Micius自生成序列上监督训练，将专家能力融合到统一27B模型，原生多模态输入，256K上下文。
- 开发Micius Harness，连接EDA工具、KiCad及执行环境，支持工具反馈驱动的多步规划、调试和迭代验证。

**关键结果**：在20+数据集约15K记录上，硬件代码基准平均64.2%，比同尺寸基线高15.0点；半导体专用Agent基准62.4%，高17.2点；SuperGPQA子集、HMMT、NetlistBench等部分指标接近或超过GPT-5.6、DeepSeek V4 Pro等更大模型。开源发布。
