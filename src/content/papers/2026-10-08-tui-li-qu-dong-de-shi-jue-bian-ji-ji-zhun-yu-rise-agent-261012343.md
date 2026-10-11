---
title: Reasoning-Informed Visual Editing
title_zh: 推理驱动的视觉编辑基准与 RISE-Agent
authors:
- Xue Yang
- Peiyuan Zhang
- Yilun Zhu
- Qihao Yang
- Mingxin Liu
- Xiangyu Zhao
- Ziqian Fan
- Zhaokai Wang
- Yan Li
- Yifan Yang
affiliations:
- Shanghai Jiao Tong University
- Southeast University
- South China University of Technology
- Microsoft Research Asia
- Fudan University
arxiv_id: '2610.12343'
url: https://arxiv.org/abs/2610.12343
pdf_url: https://arxiv.org/pdf/2610.12343
published: '2026-10-08'
collected: '2026-10-11'
category: Eval
direction: 视觉编辑推理基准与 Agent 评估
tags:
- Visual Editing
- Benchmark
- Reasoning
- LMM-as-a-judge
- Agent
- Multimodal
one_liner: 构建首个推理驱动视觉编辑基准 RISEBench++ 及训练无关 Agent，覆盖六类推理并评估58个模型
practical_value: '- 复杂指令的分层拆解：将用户编辑需求按时间、因果、空间、逻辑、反事实维度解析，可借鉴到电商商品图修改、广告素材编辑等场景，提升指令遵循精度。

  - LMM-as-a-judge 的校准评估：结合人工校准的大模型裁判，可用于生成式推荐结果、文案或图像修改的多维度离线评估，降低人工评测成本并提高一致性。

  - 训练无关 Agent 工作流：RISE-Agent 的规划-执行-验证闭环，适合直接嵌入商品图或营销素材生成的业务流，先做推理规划，再调用修图/生成工具，最后用验证器自查，无需额外训练。

  - 多图条件输入保持外观一致性：多参考图机制可迁移到电商场景中跨图保持品牌 VI、模特、商品外观一致，减少多步编辑中的风格漂移。'
score: 6
source: arxiv-cs.CV
depth: abstract
---

**动机**：LMM 在视觉理解与生成上进展迅速，但视觉编辑在复杂指令遵循、外观一致性保持、灵活输入格式上仍有明显差距，缺乏系统评估推理驱动编辑的基准。

**方法关键点**：构建 RISEBench++，将任务划分为时间、因果、空间、逻辑、反事实及混合六类推理维度，进一步细化为 12 个子类、65 种任务类型；支持多图条件输入，包含 1000 个人工标注测试样例，中英双语发布。评估维度覆盖指令推理、外观一致性、视觉合理性，采用人工评判与 LMM-as-a-judge 校准结合。同时提出训练无关的 RISE-Agent，集成推理驱动规划、工具增强执行和验证器引导细化。

**关键结果**：在 58 个视觉编辑方案（34 开源、19 闭源、5 agentic）上评估，最强模型 GPT-Image-2.5 Sunburst 准确率仅 56.6%，显示推理感知视觉编辑仍面临显著挑战。
