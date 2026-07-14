---
title: Evidence-Backed Video Question Answering
title_zh: 证据驱动的视频问答：从文本答案到时空分割掩码的联合输出
authors:
- Shijie Wang
- Honglu Zhou
- Ziyang Wang
- Ran Xu
- Caiming Xiong
- Silvio Savarese
- Chen Sun
- Juan Carlos Niebles
affiliations:
- Salesforce
- Brown University
arxiv_id: '2607.11862'
url: https://arxiv.org/abs/2607.11862
pdf_url: https://arxiv.org/pdf/2607.11862
published: '2026-07-13'
collected: '2026-07-14'
category: Multimodal
direction: 视频理解与可解释性 · 时空证据接地
tags:
- Video QA
- Spatio-Temporal Grounding
- Explainability
- Evidence-Backed
- Video LLM
- Fine-tuning
one_liner: 提出 E-VQA 任务，要求模型同时输出语义答案与精确时空证据（时间段+稠密分割掩码），并构建基准与数据集以弥合推理与细粒度接地的鸿沟
practical_value: '- **可解释推荐中的证据输出范式**：将推荐结果与细粒度证据（如关键帧、区域掩码）绑定，可迁移到商品视频理解、直播切片解释等场景，增强推荐理由的可信度。

  - **自动标注流水线放大稀缺数据**：借鉴论文的 scalable 生成 pipeline（概念识别→掩码获取→跟踪→QA 对生成），可在电商领域自动构造大量带有空间
  grounding 的商品描述与对比问答，降低人工标注成本。

  - **统一视觉接地与文本生成的模型架构**：微调 Video LLM 使其输出时空掩码 token，为电商多模态 Agent 提供“定位并解释”的能力，例如在用户问“这款口红在哪一秒涂抹了”时，精准返回片段与分割区域。

  - **解耦 QA 准确性与真视觉感知的发现**：警惕仅靠缩放模型不能解决可解释性问题，需显式训练接地能力；在构建电商问答/搜索系统时，应设计专门的接地评估集，避免模型依赖语言偏见生成答案。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

**动机**：现有 Video LLM 在视频 QA 中仅输出文本答案，缺乏可验证的视觉证据，在黑盒决策场景（如自动驾驶、医疗）中信任度低。文本解释或稀少边界框不足以捕获遮挡、非刚性形变等复杂时空动态。

**方法关键点**：
- 定义 **Evidence-Backed Video QA (E-VQA)** 任务：模型需联合输出语义答案和精确时空证据——包含时间片段和稠密、跟踪的对象分割掩码（masklet）。
- 构建人工验证基准 **ST-Evidence**，覆盖判别式和生成式像素级接地的评估。
- 开发自动化生成流水线，创建 **ST-Evidence-Instruct**（160k 样本），将高层推理与细粒度接地配对，用于微调 Video LLM。
- 模型扩展输入为视频帧与问题，输出文本答案和时空掩码 token，经掩码解码器生成分割结果。

**关键结果**：在 ST-Evidence 上，缩放模型只提升 QA 准确率但视觉感知仍差（解耦现象）；微调 7B 模型后在 t-mean 上提升 **+27.2**，J&F 上提升 **+13.8**，显著超越同尺寸 UniPixel 基线，建立了可解释视频理解的强基线。
