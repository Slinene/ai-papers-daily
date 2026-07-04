---
title: 'ADAPT: Attention Dynamics Alignment with Preference Tuning for Faithful MLLMs'
title_zh: ADAPT：通过注意力动态对齐与偏好调优实现可信多模态大模型
authors:
- Zhiyuan Yao
- Zheren Fu
- Zhixiao Zheng
- Jiajun Li
- Yi Tu
- Zhendong Mao
affiliations:
- University of Science and Technology of China
- Huawei Technologies Ltd.
- State Key Laboratory of Communication Content Cognition, People's Daily Online
arxiv_id: '2606.31054'
url: https://arxiv.org/abs/2606.31054
pdf_url: https://arxiv.org/pdf/2606.31054
published: '2026-06-30'
collected: '2026-07-04'
category: Multimodal
direction: MLLM幻觉缓解 · 跨注意力动态干预
tags:
- MLLM
- Hallucination
- Cross-Attention
- Preference Tuning
- Visual Grounding
- Attention Supervision
one_liner: 从文本-图像跨注意力退化中检测并纠正幻觉，结合视觉锚点与偏好对齐，将主流模型幻觉率降低40%–60%
practical_value: '- **生成式推荐中的视觉锚定**：在商品文案、图文搭配生成时，可借鉴ADAPT的早期解码提取视觉锚点，约束后续生成对图像关键区域保持高注意力，减少描述与图像不符的幻觉。

  - **在线注意力漂移检测与修正**：在Agent多模态交互（如视觉问答、商品搜索）中，可监控跨注意力分布的熵或偏移量，实时触发重聚焦或重新解码，提升回复的视觉忠诚度。

  - **偏好数据构造新思路**：利用注意力质量作为对比信号，自动筛选视觉grounding好的响应作为正例，无需人工标注即可构造DPO偏好对，低成本提升模型对齐效果。

  - **模型架构无关的轻量插件**：该方法无需修改原模型结构，只改变推理时的注意力使用与少量微调，可快速集成到现有MLLM pipeline中，适合业务快速验证与迭代。'
score: 6
source: arxiv-cs.MM
depth: abstract
---

**动机**：MLLMs 常产生与图像不一致的描述，即幻觉。本文发现幻觉的内部信号是 **文本-图像跨注意力在生成过程中逐渐退化**，出现注意力失焦、偏差等失败模式，而现有缓解方法多为结果驱动，并未直接干预这一内部机制。

**方法**：提出 ADAPT，直接操控跨注意力动态，包括三个组件：1) **视觉锚点**：从早期解码步骤中提炼稳定的空间注意力图，作为后续生成的视觉基础；2) **注意力监督推理**：在线检测注意力漂移（如熵增、偏移），并通过重新注入锚点进行校正；3) **视觉注意力引导的DPO**：构建偏好数据，偏向注意力聚焦于正确视觉区域的响应，通过偏好调优对齐模型行为。

**关键结果**：在多个幻觉基准上，ADAPT 将主流模型（如LLaVA系列）的幻觉率降低 **40%–60%**，达到最新最优，同时保持通用多模态能力不降。消融实验验证了每个组件的贡献。
