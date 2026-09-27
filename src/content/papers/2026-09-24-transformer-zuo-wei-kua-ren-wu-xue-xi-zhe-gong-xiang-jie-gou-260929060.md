---
title: 'Transformers as Cross-Task Learners: Shared Structure Drives Sample Efficiency
  in In-Context Learning'
title_zh: Transformer 作为跨任务学习者：共享结构驱动上下文学习样本效率
authors:
- Zhongjie Shi
- Rongjie Lai
- Alexander Cloninger
- Wenjing Liao
arxiv_id: '2609.29060'
url: https://arxiv.org/abs/2609.29060
pdf_url: https://arxiv.org/pdf/2609.29060
published: '2026-09-24'
collected: '2026-09-27'
category: Training
direction: ICL 理论 · 跨任务泛化
tags:
- In-Context Learning
- Transformers
- Sample Complexity
- Cross-Task Generalization
- Covering Numbers
- Softmax Attention
one_liner: 首次用覆盖数量化跨任务低维结构并构造 Softmax Transformer 实现 ICL 近似与泛化
practical_value: '- 多任务预训练/指令微调时，优先构造共享底层结构的任务族（如同品类推荐、同类型 query 改写），低维任务流形可让模型在小
  prompt 下完成新任务；不必盲目堆长上下文示例。

  - 覆盖数/锚函数思路可迁移为“任务原型检索”：对电商 Agent 或推荐场景，先对历史任务评估函数做聚类得到代表性锚点，再对新请求做软匹配与加权聚合，缩小检索与推理空间。

  - 误差界表明：当预训练任务数量足够覆盖任务空间时，prompt 长度依赖显著下降。这支持工程上优先扩充任务多样性、而非仅增加单任务样本数量。

  - 主要仍是学术贡献，直接可落地的算法较少，但可为多任务模型的任务划分、数据配比与上下文长度选择提供理论直觉。'
score: 6
source: arxiv-stat.ML
depth: abstract
---

**动机**：Transformer 预训练后仅用少量 in-context 示例即可适配新任务，但跨任务结构如何降低 ICL 样本复杂度缺乏刻画。本文用覆盖数量化任务空间复杂度，不依赖显式参数化。

**方法与关键点**：
- 在给定度量下用 covering number 定义任务空间复杂度，得到一组锚函数 cover。
- 设计 task-identification-and-evaluation 流程：上下文观测将新任务定位到邻近锚函数，对新 query 用这些锚函数的输出加权聚合预测。
- 显式构造带 Softmax attention 的 Transformer 近似该流程。
- 泛化误差界分离了预训练任务数量与 prompt 长度的影响：任务数量项由任务空间和输入域的内在维度决定；任务数量足够后，prompt 长度依赖变为 dimension-free。

**关键结果**：首次对一般非线性任务族量化跨任务复杂度并构造可实现的 Transformer；相关任务联合预训练通过低维共享结构提升 in-context 泛化。
