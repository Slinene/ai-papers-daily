---
title: A Dual-Path Architecture for Scaling Compute and Capacity in LLMs
title_zh: 一种解耦计算与容量的双通道Transformer架构
authors:
- Markus Frey
- Behzad Shomali
- Joachim Koehler
- Mehdi Ali
affiliations:
- Lamarr Institute
- Fraunhofer IAIS
- University of Bonn
arxiv_id: '2605.30202'
url: https://arxiv.org/abs/2605.30202
pdf_url: https://arxiv.org/pdf/2605.30202
published: '2026-05-28'
collected: '2026-05-29'
category: LLM
direction: LLM架构 · 解耦计算与容量
tags:
- transformer architecture
- looped transformer
- dual-path block
- per-token routing
- compute-capacity scaling
one_liner: 通过并行的深度循环子层与宽FFN子层加可学习门控，在同FLOPs下同时提升语言建模与推理能力
practical_value: '- **计算与容量分离的层内设计可迁移到推荐模型**：在排序或召回模型中，可将宽FFN路径视为“知识容量”，循环路径视为“推理深度”，通过可学习门控动态分配每个特征（token）的计算资源，用更少参数达到近似效果。

  - **可解释的路由信号能直接复用**：论文中提出的`deep share`（深路径贡献比例）可用于分析模型对不同输入特征类型的偏好，在电商搜索或推荐中，可类似分析文本、数值、ID等特征被分配的计算量，辅助特征工程和模型调试。

  - **混合路径的组合方式具有工程优势**：两条路径总是一起计算，不引入稀疏性，避免负载均衡问题；门控是稠密sigmoid，实现简单，可直接嵌入现有Transformer层。在Agent多智能体或生成式推荐中，可将“循环体”复用为多次迭代推理的共享模块，与宽记忆分支结合。

  - **在等FLOPs下参数更少的特性对线上推理有价值**：双路径配置（α=50, K=4）仅用67%的参数就超越了纯宽度模型，推荐/Agent系统可借此在延迟和memory
  budget下压缩模型规模，同时保持甚至提升效果。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：标准Transformer层将“计算”（序列操作深度）与“容量”（单步参数）捆绑，循环模型用参数共享换取深度但牺牲容量，宽度模型增加参数但缺乏迭代计算。为此，论文提出一种双路径（dual-path）块，将二者解耦，使每个token可按需分配计算与容量。

**方法**：
- 块内包含两条并行路径：**深路径**（deep）将标准子层循环使用K次（共享参数），并通过加权组合各中间状态得到输出；**宽路径**（wide）使用扩大的FFN，仅应用一次。
- 二者由两个独立sigmoid门控融合：g_d, g_w ∈ (0,1)，通过线性投影从输入得到，初始化为0.5。
- 总FLOPs固定，通过分配因子α（深路径FLOPs占比）和循环次数K控制参数量与计算投入。
- 因为两条路径均对每个token完整计算，门控值可直接作为路由分析信号。

**实验**：
- 在GPT-2风格16层、768维Transformer上，设置两种每层FFN FLOPs预算（80M和160M）。
- 对比纯宽度（PUREWIDE）、纯循环（PURELOOP K=2,3,4）以及双路径配置（α=25,50,75, K=2,3,4），所有模型等FLOPs训练38B tokens。
- 主要结果：在80M预算下，α=50, K=4（483M参数，仅为纯宽度67%）在语言建模、常识和数学综合BPB上全面优于纯宽度和纯循环；160M预算下，α=25, K=4最优。
- 分析发现：门控分配具有系统性——功能词和实义动词倾向宽路径，标点、符号和算术token倾向深路径；中间层偏好宽，最后两层偏好深；数学推理任务相对知识任务更偏好深路径。

**一句话精华**：通过在同一层内并行“循环深度”与“宽容量”两条路径并让模型自主分配，可以在不增加FLOPs的前提下，用更少参数同时提升知识容量和推理计算。
