---
title: 'J-CoT: Chain-of-Thought in J-Space'
title_zh: J-CoT：在模型J空间中进行链式推理
authors:
- Junde Wu
- Jiayuan Zhu
- Fengling Liu
- Minhao Hu
- Jiazhen Pan
affiliations:
- University of Oxford
- Imprint Lab
- Stanford University
arxiv_id: '2607.21981'
url: https://arxiv.org/abs/2607.21981
pdf_url: https://arxiv.org/pdf/2607.21981
published: '2026-07-24'
collected: '2026-07-27'
category: LLM
direction: 递归推理 · J-space 接口
tags:
- J-CoT
- latent reasoning
- chain-of-thought
- J-space
- recurrent reasoning
- vocabulary-indexed coordinates
one_liner: 在Transformer的词汇索引坐标系中传递系数状态作为递归边界，替代显式文本或全量隐藏状态
practical_value: '- Agent 多步推理中可引入 J-CoT 式隐状态接口，在不吐出完整文本的情况下传递中间信息，降低上下文长度与生成成本

  - 利用预训练模型已存在的 J-space（词汇对齐的残差方向）作为记忆载体，在任务内循环传递知识，无需额外训练记忆模块

  - 自适应终止策略（连续两轮 J-thought 变化 <2%）可用于 Agent 的停止条件，避免固定步数浪费计算，且易工程实现

  - 若业务场景需要模型进行隐式多跳推理（如订单诊断、营销策略生成），可借鉴 J-CoT 的跨层系数运输机制，在冻结模型前提下增强推理深度'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：现有链式推理（CoT）用自然语言传递中间状态，但语言为沟通而设计，强制将部分形成、不确定的内部计算序列化为完整句子，增加冗余并限制信息形式。潜在推理方法虽可传递密集隐藏状态，却缺乏对必要信息的选择与组织，传递全量向量。本文受人类推理中“语言无关但概念引导”的特性启发，寻找一种既不依赖完整语句，又能对下一推理步提供有效信息的递归接口。J-space 是模型中与词汇表对齐的坐标系统，因此被选作这一中间接口。

**方法关键点**：
- 构建层特异 J-space 字典：通过平均下游雅可比将词嵌入方向拉回每一层，得到各层与词汇共享索引的残差方向集。
- J-thought 状态：在多个非语言载波位置上，用非负弹性网提取当前隐藏表征在该字典下的系数，形成系数矩阵；该矩阵可在不同层通过各自字典重建残差。
- 读-计算-写递归：读层用字典将上一轮系数重建为残差并加至载波，经若干 Transformer 块计算后，在写层重新提取系数，形成下一轮 J-thought。
- J-CoT-Zero 直接使用预训练模型的上述组件，无需训练；J-CoT-Train 仅优化载波嵌入与读门，冻结 Transformer 与字典。
- 自适应停止：监测两轮 J-thought 的归一化变化，连续低于阈值即终止，最大循环数 8。

**关键实验**：
- 主干模型 Qwen3-8B-Base，在 GSM8K、MATH-500、AIME 2024、GPQA-Diamond、HumanEval+、MBPP+、LiveCodeBench、CRUXEval 共 8 个基准上评测。
- 对比基线：CoT、PS+、Coconut、CODI、SIM-Coconut。J-CoT-Train 平均得分 50.2，显著优于 SIM-Coconut 的 47.5；J-CoT-Zero 也达到 47.9，持平或超过所有其他潜在推理方法。
- 在 7B 至 405B 五档模型规模与 4/8/16 最大循环深度上，J-CoT 的性能与计算量均呈现正向缩放，大模型附加更多推理周期带来的收益更大。
- 界面谱实验表明，J-CoT（λ=0.5）在密集潜在、J-CoT、显式语言三种界面的连续插值中取得最高准确率。

**一句话**：J-CoT 证明，在模型的词汇索引坐标系中仅传递稀疏系数，就能在保持计算自由度的同时，使递归推理既优于全语言化 CoT，也优于全密集潜在方法。
