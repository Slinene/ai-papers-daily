---
title: A foundation model of numerical intelligence with cross-disciplinary generalization
title_zh: 构建数值智能基础模型：跨学科泛化的统一上下文算子网络
authors:
- Chenghan Wu
- Zongmin Yu
- Liu Yang
affiliations:
- National University of Singapore
arxiv_id: '2607.28432'
url: https://arxiv.org/abs/2607.28432
pdf_url: https://arxiv.org/pdf/2607.28432
published: '2026-07-30'
collected: '2026-08-02'
category: Other
direction: 数值智能基础模型·图上下文学习
tags:
- UNICON
- in-context learning
- graph neural network
- cross-disciplinary generalization
- numerical intelligence
- foundation model
one_liner: 提出 UNICON，以图结构示例作为上下文学习数值系统预测关系，实现跨学科零样本泛化，结合 LLM Agent 可超越专家模型
practical_value: '- 时序图数据（如用户-商品交互图）上的预测任务，可借鉴 UNICON 将系统示例组织为图上下文进行少样本推理的模式，无需微调即可泛化至新场景。

  - LLM agent 与数值模型松耦合的架构：LLM 负责任务理解与分解，UNICON 作为数值预测后端，此模式可用于搭建混合智能推荐系统，让语言模型调用专用数值预测器。

  - 训练语料多样性直接提升跨域泛化能力的结论具有普适性，在构建跨品域 / 跨场景的推荐模型时，应主动增加训练数据的领域多样性。

  - 目前主要面向科学与社会系统数值预测，与电商 / 推荐业务的直接关联有限，核心价值在学术层面。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
在交通、水文、气象等科学与社会系统中，数值观测先于形式化描述而存在。人类能从这些数值上下文中获取并应用知识，但现有模型缺乏这种“数值智能”。本文旨在构建一个能跨学科、从图结构示例中学习预测关系的基础模型，而无需针对每个系统重新训练。

### 方法
提出 **UNICON**（UNified In-Context Operator Networks）。它以图编码器为基础，接收一个系统的**示例对（输入-输出图）作为上下文**，再结合查询输入，**推理出示例间共享的算子并直接预测输出**。训练时在多领域数据集上随机采样上下文示例与查询，强迫模型学会提取可迁移的运算关系。此外，将 UNICON 与**语言模型代理结合**，LLM 进行任务规划和参数配置，UNICON 负责数值预测，形成混合智能流水线。

### 关键结果
- 在 **未见学科** 上，UNICON 可达到接近专用专家模型的性能；
- 结合 LLM agent 后，在未训练学科上**超越 SOTA 专家模型**；
- 训练语料的**学科多样性越高**，模型对全新学科的泛化能力越强。

这些结果确立了 UNICON 作为数值智能基础模型的地位，并展示了其作为更广泛 AI 生态基石的潜力。
