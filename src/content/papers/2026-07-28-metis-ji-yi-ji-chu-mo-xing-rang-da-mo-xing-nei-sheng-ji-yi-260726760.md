---
title: 'Metis: Memory Foundation Model'
title_zh: Metis：记忆基础模型，让大模型内生记忆能力
authors:
- Zeyu Zhang
- Ziliang Guo
- Yihang Sun
- Xichong Zhang
- Xixuan Hao
- Zehao Lin
- Yang Zhang
- Xiaoyan Zhao
- Tong Shen
- Bo Tang
affiliations:
- MemTensor (Shanghai) Technology Co., Ltd.
- Renmin University of China
- National University of Singapore
- Shanghai Jiao Tong University
- Tongji University
arxiv_id: '2607.26760'
url: https://arxiv.org/abs/2607.26760
pdf_url: https://arxiv.org/pdf/2607.26760
published: '2026-07-28'
collected: '2026-07-31'
category: Agent
direction: 记忆基础模型·原生记忆状态与过程
tags:
- Memory Foundation Model
- Native Memory
- Agent Memory
- Mid-training
- Fast Weight Programmers
- Dense Memory Network
one_liner: 首个记忆基础模型原型，将记忆内化为原生参数化状态和计算过程，用中间训练获得自主记忆能力
practical_value: '- 可用轻量级固定尺寸记忆矩阵（M_t, S_t）隐式存储多轮对话历史，替代显式文本拼接或外部检索，上线仅需前向传播，无需梯度更新，适合在线推荐
  Agent 部署

  - 记忆更新（Gated Delta Network 风格）与当前推理完全解耦，可与原始注意力并行计算，推理延迟主要取三者最大而非相加，对实时性要求高的电商对话系统有参考价值

  - 中间训练数据构造方法可复用：将公开事实型数据集改造成含记忆操作（记住/更新/遗忘/反射）的多步交互序列，显式标注记忆一致性，用于训练推荐对话 Agent 的上下文理解与状态管理

  - “原生记忆过程”思想可扩展到推荐模型：将用户行为序列压缩为模型内部动态参数，用特殊设计的记忆重建与操作损失联合优化，实现端到端的个性化状态保持'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
现有 AI Agent 的记忆几乎都依赖外部模块（如 RAG、检索库），与模型主干解耦，导致梯度无法贯通、推理时额外延迟高、难以端到端优化。论文提出记忆基础模型的概念，将记忆能力原生整合进大模型的计算流中，使模型具备有状态的参数化记忆和自主的存储 / 利用过程。

**方法关键点**
- **原生记忆状态**：在 Transformer 中插入 Metis 块（由局部记忆块和超记忆块组成），局部记忆块维护一个稠密记忆矩阵 \(M_t\) 和归一化向量 \(S_t\)，作为固定大小的动态参数，跨多步持久更新。
- **原生记忆存储过程**：超记忆块从当前隐藏状态中自适应选出重要 token，投影为记忆 key/value，并用门控增量网络（GDU）以指数衰减方式更新 \(M_{t+1}\) 和 \(S_{t+1}\)，整个过程无梯度、仅一次前向。
- **原生记忆利用过程**：用学习到的记忆查询投影 \(\tilde{W}_Q\) 从记忆状态中读出信息，通过记忆注意力融合到主干注意力输出，平衡原始注意力和记忆注意力的权重。
- **大规模训练数据构造**：从 27 个公开基准合成 357k 条多步交互样本（约 406M tokens），覆盖 remember、forget、update、reflect 四种记忆操作，结合显式 / 隐式指令和噪声干扰；另构造 609k 条辅助数据应对多实体绑定、选择性遗忘和对话混合等复杂场景。
- **中间训练目标**：联合记忆重建、记忆操作和正则化三个损失，用任务权重采样器实现从存储能力到复杂通路的课程学习，只优化 Metis 块参数，冻结主干。

**关键结果**
论文展示 Metis 在多种记忆任务上展现了原生记忆能力，同时对长程任务存在性能衰减、信息混淆等局限，并分析了误差来源。实验表明原生记忆在架构效率、端到端可优化性及并行推理方面优于外部记忆方案，但未给出与 RAG 等 baselines 的直接定量对比数字。
