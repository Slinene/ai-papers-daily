---
title: 'ACC: Compiling Agent Trajectories for Long-Context Training'
title_zh: ACC：面向长上下文训练的Agent轨迹编译
authors:
- Qisheng Su
- Zhen Fang
- Shiting Huang
- Yu Zeng
- Yiming Zhao
- Kou Shi
- Ziao Zhang
- Lin Chen
- Zehui Chen
- Lijun Wu
affiliations:
- University of Science and Technology of China
- Shanghai Innovation Institute
- Shanghai AI Laboratory
arxiv_id: '2605.21850'
url: https://arxiv.org/abs/2605.21850
pdf_url: https://arxiv.org/pdf/2605.21850
published: '2026-05-20'
collected: '2026-05-22'
category: Training
direction: 长上下文训练 · Agent轨迹编译
tags:
- Long-Context
- Agent Trajectories
- SFT
- MRCR
- GraphWalks
- MoE
one_liner: 将多轮agent轨迹编译为长上下文QA对，无需额外标注，在长程依赖建模上媲美8倍参数模型
practical_value: '- 直接复用业务中已有的agent交互日志（如电商智能客服多轮对话、数据库查询、代码调试等），将其组装为长上下文训练数据，无需额外标注，低成本提升模型多跳推理和信息整合能力。

  - 在生成式推荐或搜索中，可将用户与推荐系统的多轮交互（查询、候选列表、点击/购买行为等）编译为长上下文，让模型直接基于长历史序列生成最终推荐，替代逐步候选筛选流程。

  - 训练时加入不相关的干扰项（如未点击的商品、未使用的搜索结果）并随机打乱顺序，能增强模型在长上下文中定位关键信息的能力，可迁移至电商场景下处理杂乱的浏览历史。

  - 完全基于标准SFT，无需复杂强化学习，工程实现简单，适合快速实验和部署。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：当前大模型的长上下文推理能力主要依赖昂贵的长文档标注或启发式合成数据。Agent在解决任务时产生的多轮轨迹中，答案所需的证据分散在不同回合的工具响应里，但标准的agent SFT掩码了这些响应，仅监督局部工具选择，导致分散的证据信号未被利用，形成“监督盲点”。Agent Context Compilation (ACC) 正是为了解决这一问题，将agent轨迹直接编译成长上下文QA对，使监督信号直达每一条证据。

**方法关键点**：
- 从搜索、软件工程（SWE）、SQL三类agent的正确答案验证轨迹中，提取工具响应和环境观测，将包含答案证据的片段（网页全文、代码文件、数据库表）与原始问题拼接为长上下文，同时混入未使用的搜索结果或文件作为干扰项，并随机打乱顺序，迫使模型学习语义关联而非依赖位置。
- 使用DeepSeek-V3.2-Thinking为编译后的上下文生成推理链，仅保留能得出正确答案的推理过程。训练时直接对模型在（问题+编译上下文）上生成的推理和答案进行监督，消除中间工具选择步骤，使最终答案的梯度直接传播到每一个证据token。
- 该方法无需额外标注，可与任意长上下文扩展或训练方法结合，仅使用标准SFT。

**关键结果**：在长程依赖建模基准MRCR和GraphWalks上，训练后的Qwen3-30B-A3B分别比基线提升18.1和7.6分，达到与8倍活跃参数量的Qwen3-235B-A22B相当的水平，同时通用能力（GPQA、MMLU-Pro、AIME、IFEval）未出现负迁移，部分指标略有提升。消融表明，加入干扰项和多种agent类型混合训练均有益。机制分析显示，模型在训练后表现出任务自适应的注意力重组和专家专化，而非固定模式。

**最值得记住的一句话**：将agent轨迹中的工具响应与原问题直接编译成长上下文进行训练，可有效将间接监督转化为长上下文推理的直接监督，大幅提升模型的长程依赖建模能力。
