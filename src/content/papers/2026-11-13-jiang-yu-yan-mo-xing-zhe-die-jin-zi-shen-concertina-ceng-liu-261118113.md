---
title: Folding Language Models into Themselves
title_zh: 将语言模型折叠进自身：Concertina 层共享蒸馏
authors:
- Ziyang Zhang
- Yubin Jing
- Yuyao Li
- Haofan Wang
- Yichen Gong
affiliations:
- Peking University
- Georgia Institute of Technology
- Tsinghua University
- Lovart AI
arxiv_id: '2611.18113'
url: https://arxiv.org/abs/2611.18113
pdf_url: https://arxiv.org/pdf/2611.18113
published: '2026-11-13'
collected: '2026-11-16'
category: Training
direction: 模型压缩 · 层共享蒸馏
tags:
- Knowledge Distillation
- Model Compression
- Layer Sharing
- LoRA
- Parameter Sharing
- LLM
one_liner: 把相邻 N 层教师折叠成一个共享块并重复执行 N 次，用低秩修正与逐 token 门控恢复原层行为，以小数据量蒸馏出高性能紧凑模型
practical_value: '- **线上部署 LLM 到推荐/搜索链路时**：可参考 Concertina 的层折叠方法，将大模型压缩为 2-3B 参数的小模型，同时保持约
  85% 的教师能力，大幅降低推理延迟和显存占用，适合实时召回或排序阶段。

  - **蒸馏数据配方值得复用**：论文平衡通用、数学、学术、多项选择数据以避免能力此消彼长。电商场景可类比构建平衡数据集（商品知识、用户行为序列、搜索 query
  理解、文案生成等）进行领域蒸馏，防止只优化单一任务导致其他能力退化。

  - **共享层 + per-token gate 机制**：每个 token 动态混合低秩修正，可以借鉴到多场景或多任务模型中，实现参数共享与场景自适应，类似于动态路由或
  MoE 的轻量替代。

  - **从教师权重初始化而非从头训练**：直接用教师层初始化学生，只需蒸馏 22B token 即恢复大部分能力，节省数百倍训练数据与计算成本，对需要频繁更新或定制小模型的团队很有吸引力。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：知识蒸馏通常从头训练小模型，即使教师权重已包含大部分知识，学生仍需海量数据重新学习。本文尝试直接从教师权重构造学生，减少训练数据需求。

**方法关键点**：提出 Concertina，将每 N 个相邻教师层折叠为一个共享块，该块循环执行 N 次。每个循环步骤带一个低秩修正（类似 LoRA），初始化自被替换的层；同时引入 per-token 门控混合多个低秩修正，使每个 token 能从单一块中恢复对应原始层的行为。还设计了平衡通用、数学、学术和定向多项选择数据的蒸馏配方，避免能力相互挤压。

**关键结果**：在 Qwen3-4B 上，得到的 2.27B Concertina 模型仅用 22B token 蒸馏，在常识与数学推理基准上保留约 90% 教师性能，八项基准平均保留 84%；超越同尺寸 dense 和 layer-sharing 基线，也超过训练数据量千倍以上的 Qwen3-1.7B。代码开源。
