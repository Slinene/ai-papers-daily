---
title: 'ProQuant: Progressive Quantization-aware Training for Edge MLLMs'
title_zh: ProQuant：边缘多模态大模型的渐进式量化感知训练
authors:
- Yufei Xue
- Yushi Huang
- Jiawei Shao
- Pingcheng Dong
- Yonghao Tan
- Shiyao Li
- Kwang-Ting Cheng
- Jun Zhang
affiliations:
- The Hong Kong University of Science and Technology
- Northwestern Polytechnical University
- Institute of Artificial Intelligence (TeleAI), China Telecom
- Tsinghua University
arxiv_id: '2611.08216'
url: https://arxiv.org/abs/2611.08216
pdf_url: https://arxiv.org/pdf/2611.08216
published: '2026-11-05'
collected: '2026-11-08'
category: Training
direction: MLLM低比特量化感知训练
tags:
- Quantization-aware training
- MLLM
- Low-bit
- Progressive block activation
- Self-relabeling
- Edge deployment
one_liner: 提出渐进式量化感知训练框架ProQuant，通过自重标记与分块激活将W4A8小模型性能损失降至约1%
practical_value: '- 若业务需要在端侧/边缘部署多模态Agent（如商品图像识别、视频理解模块），可借鉴渐进式分块激活策略：先重训视觉编码器和多模态投影层恢复视觉理解，再微调语言建模部分，并用视觉敏感因子τ识别关键层，对它们分配更高量化精度或更多训练轮数，能有效降低W4A8下商品属性提取等任务的精度损失。

  - self-relabeling技巧可直接用于多模态微调数据构建：用预训练MLLM重新生成开源数据集的响应，使微调数据分布对齐原始预训练分布，提升低比特训练的稳定性；电商领域可对商品图文对重写问题或答案，有助于量化后模型保留指令跟随能力。

  - 该工作证明2B小模型经W4A8量化后可接近全精度性能（仅约1%下降），为在边缘侧部署轻量多模态模型提供了工程路径；不必局限于PTQ，可先SRL后PBA进行轻量再训练，无需全量数据。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

动机：边缘设备部署MLLM受计算与内存限制，低比特量化（如W4A8）下性能损失严重，小模型尤甚。

方法关键点：ProQuant引入两个机制。一是self-relabeling (SRL)，用预训练模型重新生成开源多模态数据集的响应，使有限微调数据分布对齐原始预训练分布。二是解耦多模态理解与语言建模能力，提出渐进式分块激活 (PBA)，在训练中优先恢复多模态理解模块；同时引入视觉敏感因子τ，自动识别对多模态性能关键的transformer层，让这些层获得更充分的低比特恢复训练。

关键结果：在2B-8B参数模型、多个benchmark上显著超越现有方法。例如W4A8 Qwen3-VL-2B-Instruct平均精度提升6.6%，与全精度模型相比性能下降仅约1%。
