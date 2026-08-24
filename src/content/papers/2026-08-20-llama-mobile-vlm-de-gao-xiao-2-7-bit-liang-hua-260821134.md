---
title: 'Llama-Mobile: Efficient 2.7-Bit Quantization of VLMs'
title_zh: Llama-Mobile：VLM 的高效 2.7-bit 量化
authors:
- Luka Ribar
- Jeevan Bhoot
- Douglas Orr
affiliations:
- Graphcore Research
- Arm
arxiv_id: '2608.21134'
url: https://arxiv.org/abs/2608.21134
pdf_url: https://arxiv.org/pdf/2608.21134
published: '2026-08-20'
collected: '2026-08-24'
category: Multimodal
direction: VLM 量化与移动端高效推理
tags:
- quantization
- VLM
- QAT
- mobile inference
- model compression
- S3D8
one_liner: 提出无需原始训练数据的 VLM 量化 pipeline 与 S3D8 2.7-bit 格式，将 Llama 3.2 11B 压缩至 3.7GB
  并保持 VQA 性能
practical_value: '- 业务里若需在端侧/边缘部署多模态模型（商品图理解、广告素材审核、图文客服），可借鉴“无原始训练数据 QAT”：用目标模型自生成校准数据，避免数据不可得和分布偏移。

  - S3D8 2.7-bit 格式将三个有符号权重打包进一个字节，解码到 INT8 后推理，对 Arm CPU 友好；有移动端导购/Agent 或端上推荐模型时可评估该格式降低内存。

  - 量化训练数据选择对性能很敏感：合成与部署分布匹配的数据比通用公开数据更稳，做模型压缩时值得投入数据构造。

  - 11B VLM 压缩到 3.7GB 说明移动端内存预算可承载多模态大模型，适合端侧“拍照搜商品/图片问答”等场景。'
score: 6
source: huggingface-daily
depth: abstract
---

动机：VLM 部署到移动端受限于内存和算力，低比特量化困难，且 QAT 通常依赖原始训练数据。

方法：提出 Llama-Mobile 量化框架，包含两个关键点：①用模型自身生成 QAT 训练数据，无需访问原始训练管线；②设计 S3D8 2.7-bit-per-parameter 格式，将三个有符号权重通过共享 centroid index 打包进一个字节，推理时解码为 INT8，支持 Arm CPU 高效执行。

结果：将 Llama 3.2 11B Vision Instruct 压缩到 3.7GB，配合 8-bit activations，在标准 VQA 任务上保持强性能。
