---
title: 'Beyond Sequence Order: Syntax-Informed Positional Embeddings for Transformers'
title_zh: 语法信息位置嵌入：超越序列顺序的Transformer增强
authors:
- Haris Riaz
- Hyungji Kim
- Mihai Surdeanu
affiliations:
- University of Arizona
arxiv_id: '2608.06111'
url: https://arxiv.org/abs/2608.06111
pdf_url: https://arxiv.org/pdf/2608.06111
published: '2026-08-06'
collected: '2026-08-09'
category: Other
direction: 语法增强的位置编码
tags:
- Syntax
- Positional Embeddings
- Transformers
- Dependency Parsing
- GLUE
- Architecture-Aware
one_liner: 将依赖解析语法先验按架构特性注入位置编码，大幅提升句法及语义理解，且推理成本极低
practical_value: '- 序列推荐中若使用**相对位置编码**（如Transformer-XL），可将用户行为依赖关系（浏览→加购→购买）作为语法先验，与相对位置注意力分数**相乘**，强化行为结构信号。

  - 对使用**绝对/旋转位置编码**的编码器，可把预计算的行为依赖嵌入**直接加在输入嵌入**上，简单组合原生位置机制，不改动模型主体。

  - **推理时仅需单一依赖图**（离线预先解析），无额外计算开销，适合线上实时推荐/Agent系统，避免多解析树集束搜索或边际化。

  - 对话Agent的状态追踪可借鉴：将对话动作序列解析为依存树，生成语法感知的位置嵌入，增强长程对话理解，并可分别按encoder/decoder调整注入策略。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：Transformer位置嵌入仅编码序列距离和顺序，完全忽略句法结构，限制了语言模型对长程依赖和结构化模式的学习。

**方法**：提出SiPE（Syntax-informed Positional Embeddings），在预训练时从依赖解析树提取轻量语法先验，并将其注入三大类位置编码（绝对、相对、旋转）。关键在于“架构感知”的注入策略：
- 对于使用**相对PE的自回归decoder**，将语法先验**乘性耦合**到注意力分数的相对位置项中，效果最优；
- 对于**encoder**，直接将语法嵌入**加至输入嵌入层**，与自身的位置机制组合；
- 保持自注意力及整体架构不变，推理时仅使用单个解析树，无边际化开销。

**结果**：预训练模型在SyntaxGym句法泛化基准上提升最高**10.3%**，同时GLUE语言理解得分提升最高**8.2%**，困惑度降低**9.0%**——而多数现有句法注入方法反而损害困惑度。SiPE还建立了新的Pareto前沿：以最少的推理成本（单棵解析树）取得最强句法监督增益。
