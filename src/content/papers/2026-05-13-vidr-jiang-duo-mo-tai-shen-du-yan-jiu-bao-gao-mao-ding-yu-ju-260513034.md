---
title: 'ViDR: Grounding Multimodal Deep Research Reports in Source Visual Evidence'
title_zh: ViDR：将多模态深度研究报告锚定于源视觉证据
authors:
- Zhuofan Shi
- Peilun Jia
- Baoqin Sun
- Haiyang Shen
- Sixiong Xie
- Yun Ma
- Xiang Jing
affiliations:
- Peking University
- National Key Laboratory of Data Space Technology and System
- Beijing Jiaotong University
- Hunan University
arxiv_id: '2605.13034'
url: https://arxiv.org/abs/2605.13034
pdf_url: https://arxiv.org/pdf/2605.13034
published: '2026-05-13'
collected: '2026-05-17'
category: Multimodal
direction: 多模态深度研究报告的视觉证据定位与验证
tags:
- multimodal deep research
- source visual evidence
- report generation
- VLM
- visual grounding
- evidence verification
one_liner: 提出将源图像作为可检索、可解释、可验证的证据对象，结合证据索引提纲和视觉验证，提升多模态深度研究报告的可靠性和可验证性
practical_value: '- **多模态证据的可信报告生成**：在电商商品评测或行业分析报告的自动生成中，可将商品图片、图表视为可验证的源证据，通过类似“证据索引提纲”的方式将每个结论关联到具体视觉证据，提升生成内容的说服力。

  - **噪声图像的精炼流水线**：论文提出的“上下文感知过滤 + 提纲感知重排序 + VLM 视觉分析”流程，可直接用于从混乱的网页抓取商品图片中提取高质量、相关的证据原子，避免无关或低质量图片干扰报告。

  - **视觉引用的显式验证**：在生成报告中验证引用图像的准确性和位置合理性，减少“幻觉”或错配，这一思路可移植到多模态 RAG 系统，增强答案的可信度。

  - **多模态报告质量的量化评估**：MMR Bench+ 将源图检索、放置、解释、可验证性等纳入评测维度，可为电商多模态内容生成系统提供更全面的离线评估方案，指导优化方向。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：现有深度研究系统主要依赖文本证据，生成长篇报告；多模态系统往往只弱检索图像或自行生成图表，未能充分利用原始源图像作为证据，导致视觉支撑薄弱、报告可验证性差。

**方法关键点**：
- **证据对象建模**：将源图像视为可检索、可解释、可路由、可验证的原子证据，而非装饰。
- **证据索引提纲**：构建将报告声明与文本及视觉证据链接的结构化提纲，指导分段写作。
- **噪声图像精炼**：通过上下文感知过滤剔除无关图像，提纲感知重排序挑选最匹配证据，再利用 VLM 进行视觉分析（解释图表、提取关键信息），形成证据原子。
- **分章节证据驱动生成**：每个章节使用该章节特定的证据集进行生成，确保图文紧密对应。
- **视觉引用验证**：自动检查报告中引用的图像是否真实存在、位置是否合理，减少幻觉。

**关键结果**：在 MMR Bench+ 基准上，ViDR 在总体报告质量、源图像集成度和可验证性上均显著优于商用和开源基线，证明源视觉证据能显著提升深度研究报告的证据支撑和可信度。
