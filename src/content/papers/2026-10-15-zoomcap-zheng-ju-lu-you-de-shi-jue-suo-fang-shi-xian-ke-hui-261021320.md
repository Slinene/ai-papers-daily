---
title: 'ZoomCap: Evidence-Routed Visual Zooming for Recoverable Visual Information
  Transfer'
title_zh: ZoomCap：证据路由的视觉缩放实现可恢复视觉信息传递
authors:
- Hao Shi
- Jiafeng Wang
- Yuzhuo Fu
- Tao Zhang
- Jian Bai
- Juelu Zhang
- Qing Cui
- Chao Huang
affiliations:
- Ant Group
- Zhejiang University
arxiv_id: '2610.21320'
url: https://arxiv.org/abs/2610.21320
pdf_url: https://arxiv.org/pdf/2610.21320
published: '2026-10-15'
collected: '2026-10-18'
category: Multimodal
direction: 视觉caption生成与事实评估
tags:
- Fine-grained captioning
- VLM training data
- Adaptive zooming
- FactCycle
- OCR
- Visual information transfer
one_liner: 用草稿路由、自适应缩放和 FactCycle 事实校验生成高密度图像描述，提升 VLM 训练效果
practical_value: '- 借鉴“草稿—缺口恢复—定向补充”策略：在商品图文描述或广告素材理解中，先快速生成初稿，再针对 OCR 密集区域（成分表、注意事项、小标签）和覆盖缺口进行局部放大与二次采集，提升细节覆盖率与可信度。

  - 借鉴 FactCycle 事实锚定评估：将生成文案/卖点拆成原子事实，用源商品图和生成图重建做盲评，分离幻觉（虚假宣称）与模型表达能力问题；可用于广告审核、商品描述合规与真实性检查。

  - 自适应缩放只对复杂区域分配高分辨率计算，适合处理商品图多尺度信息（瓶身文字、包装细节、模特配饰），控制推理成本；可结合检测器先定位复杂度，再分档裁剪。

  - 数据飞轮效果表明，高质量细粒度描述预训练能显著提升下游文档 OCR、感知和医疗 VQA 分数，建议为电商多模态模型构建类似“证据路由”生成的高密度描述数据集，用于持续预训练。'
score: 6
source: arxiv-cs.MM
depth: abstract
---

**动机**：详细图像描述（dense caption）是 VLM 训练的关键监督来源，但描述质量容易被长度掩盖；单次生成长描述仍会漏掉小物体、文字和空间关系，或把不确定观察写成确定描述。本文将细粒度 captioning 形式化为可恢复视觉信息传递：教师模型在有限观察预算下获取遗漏证据并转化为可重用监督。

**方法关键点**：ZoomCap 先由草稿描述（draft caption）路由，进行条件知识检索、OCR 敏感阅读、覆盖缺口恢复和自适应视觉缩放；只对最复杂且符合条件的区域进行更深裁剪，空间关系从有根据的几何推导，融合非重复证据。FactCycle 将描述分解为原子事实，在两个盲锚上评分——源图像（真实性）和重建图像（可实现性）——逐条区分虚构与生成器损失。

**关键结果数字**：与 Qwen3.5-397B-A17B 对比，ZoomCap 人类平局调整偏好 81.9%，教师模型小 10 倍以上；FactCycle 统计每张图传递 52.4 个事实，而 ScaleCap 为 31.5。持续预训练中 ZoomCap-450K 在 11 个基准平均提升 1.31–2.38 分，Ling-Tiny-VL-v3 在 60B tokens 生产文档/OCR 监控套件上提升 1.4 分（感知 1.5）；医疗预训练 2.64M 图像提升五个 VQA 基准 3.04 分（同图 Gemini-3.1-Pro 为 1.76）。
