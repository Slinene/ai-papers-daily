---
title: Mind the Couch! Eliciting MLLM Reasoning in Interior Design via Weak-to-Strong
  Task Vector Injection
title_zh: 小心沙发！弱到强任务向量注入激发多模态大模型室内设计推理
authors:
- Yuxuan Yang
- Jingyao Wang
- Luntian Mou
affiliations:
- Nanjing Forestry University
- Institute of Software Chinese Academy of Sciences
- University of the Chinese Academy of Sciences
- Beijing University of Technology
arxiv_id: '2608.23242'
url: https://arxiv.org/abs/2608.23242
pdf_url: https://arxiv.org/pdf/2608.23242
published: '2026-08-24'
collected: '2026-08-30'
category: Reasoning
direction: 多模态大模型推理增强 · 任务向量注入
tags:
- MLLM
- Task Vector
- Weak-to-Strong
- Multimodal Reasoning
- Latent Intervention
one_liner: 提出 DART-I，用弱专家提取空间/颜色先验生成任务向量，残差注入冻结 MLLM 以改善室内设计推理
practical_value: '- 可将业务中的确定性规则（价格带、商品属性兼容性、布局安全距离等）封装为轻量 weak expert，输出连续数值特征，再投影为
  task vector 注入冻结 LLM/MLLM 的 latent space，实现零微调的领域约束注入，避免灾难性遗忘和高昂训练成本。

  - 在电商多模态场景（商品图 + 描述）中，可借鉴 DART-I 的残差注入方式：先用弱模型提取商品间空间关系、颜色搭配等先验，引导 MLLM 生成更合理的搭配或布局建议，减少幻觉，优于仅靠
  prompt 中的文字约束。

  - 弱到强范式适合标注稀缺的业务：用弱模型/人工规则先产生结构化信号，再驱动强模型，可复用到推荐系统，例如将用户行为序列的统计先验（点击间隔、序列长度分布）注入生成式推荐模型，提升生成质量。

  - 任务向量注入作为一种参数高效适配手段，比 LoRA 等微调方法更轻量，适合快速在多业务线之间切换和迭代。'
score: 6
source: arxiv-cs.MM
depth: abstract
---

**动机**：多模态大模型（MLLM）在室内设计等密集约束空间推理中常出现模态错位，视觉编码丢失高频局部拓扑细节和细粒度美学信息，导致幻觉、物理空间碰撞和视觉不和谐。传统文本提示难以精确传达硬性空间与美学约束。

**方法关键点**：提出 DART-I（Dual-prior Activation Residual Task-vectors Injection），从有损文本提示转向直接潜在干预。分三步：
1. 使用极轻量弱专家从图像显式提取连续空间距离和颜色排版特征；
2. 通过线性投影网络将确定性先验转换为方向性任务向量；
3. 将这些向量作为残差动态注入冻结 MLLM 的潜在空间，引导模型进行精确推理，无需微调 MLLM。

**关键结果**：在多个 benchmark 上验证了 DART-I 的有效性与优势；方法完全绕过微调，避免了昂贵计算成本和灾难性遗忘。
