---
title: 'VisionWeave: Weaving Elastic Visual Representations as a Native Capability
  of MLLMs'
title_zh: VisionWeave：为多模态大模型原生编织弹性视觉表征
authors:
- Yuan Feng
- Qize Yang
- Ruizhe Chen
- Sibo Song
- Haolin He
- Muzhi Zhu
- Zihan Liu
- Yunfei Chu
- Xize Cheng
- Yuxuan Wang
affiliations:
- University of Science and Technology of China
- Alibaba Token Hub, Alibaba Group
- The Chinese University of Hong Kong
- Zhejiang University
arxiv_id: '2610.07987'
url: https://arxiv.org/abs/2610.07987
pdf_url: https://arxiv.org/pdf/2610.07987
published: '2026-10-05'
collected: '2026-10-12'
category: Multimodal
direction: 多模态 LLM 视觉 token 弹性压缩
tags:
- Multimodal LLM
- Visual Token Compression
- Adaptive Granularity
- MRoPE
- SGLang Serving
- Self-Distillation
one_liner: 提出 VisionWeave，通过 gated spatial pooler 与 granularity router 实现内容自适应视觉 token
  压缩，节省 43% token 保持 98.9% 性能
practical_value: '- 多模态商品/广告素材理解中，图片与视频区域信息密度不均，可借鉴 VisionWeave 的内容自适应 token 分配：对背景/空白用
  coarse-grained 池化，关键商品区域保留 fine-grained，降低推理成本同时保持识别精度。

  - 采用 gated spatial pooler + granularity router 两阶段设计，让模型学习“哪里需要细看、哪里可以粗看”，共享 MRoPE
  坐标无需改动位置编码，方便集成到现有视觉 Backbone 和 Serving 框架。

  - 使用 self-distillation 训练弹性表示能力，不依赖人工标注 token 重要性，适合业务数据标签稀疏；虽然训练成本高（30K A100 GPU-hours），但推理端吞吐提升
  2.3x、TTFT/TPOT 大降，对在线多模态推荐/Agent 服务有直接价值。

  - 工程上可复用开源的 SGLang 集成，注意变长 token 输入对批处理与 KV cache 管理的影响，适配电商多图/视频场景可显著提升 GPU 利用率与响应速度。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：MLLM 将视觉输入编码为密集固定大小的 patch tokens，但视觉信息分布不均匀，固定粒度导致冗余或丢失细节。现有 downsampling 牺牲细节，token pruning 与自适应方法在内容自适应粒度、任务泛化、以及与现代 MLLM 和服务基础设施集成方面存在局限。

**方法关键点**：VisionWeave 提出 elastic visual representation weaving 作为 MLLM 原生能力。包含两个组件：gated spatial pooler 在原生 fine-grained representations 旁构建 coarse-grained representations，共享 MRoPE 坐标；granularity router 学习内容自适应分配。通过 self-distillation 在 Qwen3.5-4B 验证，扩展到 Qwen3.8-27B，训练超过 30K A100 GPU-hours。

**关键结果**：基于 Qwen3.8-27B，VisionWeave 平均节省 43.0% tokens，保持 98.9% 原生性能（八个 benchmark），而固定 50% 节省的 token pruning baseline 仅保持 88% 性能。在 SGLang 部署达到 2.30x end-to-end throughput，mean TTFT 降 54.4%，mean TPOT 降 60.6%，验证跨任务/分辨率/视频帧的鲁棒效率-质量权衡。
