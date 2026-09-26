---
title: The Alignment Illusion in Multimodal Large Language Models
title_zh: 多模态大语言模型中的对齐幻觉
authors:
- Hong-Han Wang
- Yuntao Wang
- Hu Ding
affiliations:
- University of Science and Technology of China
arxiv_id: '2609.30210'
url: https://arxiv.org/abs/2609.30210
pdf_url: https://arxiv.org/pdf/2609.30210
published: '2026-09-24'
collected: '2026-09-26'
category: Multimodal
direction: 多模态 LLM 表征几何诊断
tags:
- MLLM
- Alignment Illusion
- Representational Similarity
- Principal Angle Gap
- CKA
- Multimodal Interpretability
one_liner: 揭示 MLLM 标量视觉-文本对齐指标无法区分噪声与真实视觉流，提出主角度间隙 PA gap 作为几何诊断
practical_value: '- 在多模态推荐或广告中，使用 CKA/SVCCA 等标量相似度评估视觉-文本融合质量时，务必结合下游任务指标（如点击率、相关性、A/B
  结果）校准；单独看相似度曲线容易产生“对齐幻觉”，误导模型选型或层数截断。

  - 可借鉴 PA gap 作为轻量几何诊断，监控多模态模型在微调、量化、蒸馏或视觉编码器替换后视觉 token 结构是否退化，及时发现信息丢失。

  - 论文揭示共享 MLP 下投影会制造权重诱导对齐，若业务中将图像/文本投影到统一 LLM 空间做检索或生成，需警惕共享通路导致的虚假相似性；可考虑对投影层增加正则或采用多维几何指标评估。

  - 在 Agent 或多模态 RAG 中，若用视觉输入辅助决策，应定期用受控任务测试（如噪声图像或无关图像）校准内部表征诊断，避免仅凭几何指标判断模型理解能力。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

动机：MLLM 中逐层视觉-文本相似度上升常被解读为视觉内容逐步融入共享表征空间，但该解读依赖标量对齐分数能反映内容级跨模态交互的假设。方法：对视觉流施加受控干预——将 projector 输出的视觉 token 替换为高斯噪声，然后在 13 个 MLLM（5 个家族、0.5B-72B 参数）上检验四个标量指标（CKA、SVCCA、MIR、leading principal-angle cosine）能否区分损坏流与原始流；进一步将失效追溯至共享语言模型通路中的各向异性 MLP 下投影，它把视觉和文本 token 拉向共同输出方向，形成权重诱导对齐；据此提出主角度间隙（PA gap），即前两个主角度余弦之差，以分离权重诱导相似性与多方向视觉结构。结果：噪声替换显著降低任务精度，但四个标量指标无法一致区分；在分级视觉损坏下，PA gap 比这些标量分数更一致地跟踪任务精度；在结构化但无关图像下，PA gap 进一步暴露内部几何与任务精度背离的情形。结论：内部视觉-文本对齐更适合作为视觉流在语言模型内部的几何诊断，而非内容级跨模态交互的直接代理，并且应当由受控任务证据校准。
