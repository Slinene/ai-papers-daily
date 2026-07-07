---
title: 'MultAttnAttrib: Training-Free Multimodal Attribution in Long Document Question
  Answering'
title_zh: 基于注意力头的训练无关多模态文档问答归因方法
authors:
- Dang Quang Thien Tran
- Quang V. Dang
- Vinamra Tyagi
- Sai Soorya Rao Veeravalli
- Trang Nguyen
- Ryan A. Rossi
- Franck Dernoncourt
- Nedim Lipka
- Koustava Goswami
- Samyadeep Basu
affiliations:
- University of Massachusetts, Amherst
- Adobe Research, San Jose
arxiv_id: '2607.01420'
url: https://arxiv.org/abs/2607.01420
pdf_url: https://arxiv.org/pdf/2607.01420
published: '2026-06-30'
collected: '2026-07-07'
category: Other
direction: 多模态归因 · 注意力头定位
tags:
- Multimodal
- Attribution
- Attention Head
- Training-Free
- Long Document QA
- Citation
one_liner: 利用预填充注意力头与校准阈值实现训练无关的多模态问答证据定位，速度提至七分之一。
practical_value: '- 在推荐系统、对话 Agent 生成解释时，可借助注意力头快速定位关键证据（如用户历史行为、物品描述片段），无需额外训练，降低工程复杂度。

  - 利用特定层的注意力头选择与校准阈值，可做实时归因，适合高延迟敏感的电商推荐解释场景。

  - 思路可迁移至多模态商品问答：结合商品图片和描述，用类似方法自动高亮答案对应的图片区域或文本 span，提升购物体验。

  - 训练无关的特性适合冷启动或频繁变更的情景，避免为归因重新训练模型，降低迭代成本。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：多模态长文档问答系统需求日益增长，但答案的细粒度证据归因（定位到具体文本或图像区域）研究薄弱，缺乏数据集与方法。现有方法多依赖强 prompt 或微调，推理慢且扩展性差。

**方法**：提出 MULTATTNATTRIB，一种训练无关的归因生成方法。核心思路：在模型预填充阶段，计算特定层注意力头对答案 token 的累积注意力权重，通过多模态对齐将其映射回源文档的文本块或图像区域，再结合校准阈值筛选高置信度证据。同时构建 MULTATTREVAL 评测集，包含人工标注的多模态细粒度归因标签。

**关键结果**：在文本与图像归因任务上，MULTATTNATTRIB 全面超过强 prompt 基线，准确率与最新前沿模型（如 GPT-5.4）持平；推理延迟仅为同模型上 prompt 方法的 1/7，大幅降低代价。
