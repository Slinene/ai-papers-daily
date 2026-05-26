---
title: 'VGenST-Bench: A Benchmark for Spatio-Temporal Reasoning via Active Video Synthesis'
title_zh: 主动合成视频的时空推理评测基准
authors:
- Jinho Park
- Youbin Kim
- Hogun Park
- Eunbyung Park
affiliations:
- Sungkyunkwan University
- Yonsei University
arxiv_id: '2605.22570'
url: https://arxiv.org/abs/2605.22570
pdf_url: https://arxiv.org/pdf/2605.22570
published: '2026-05-20'
collected: '2026-05-26'
category: Eval
direction: 多模态大模型时空推理评测
tags:
- spatio-temporal reasoning
- video benchmark
- MLLM evaluation
- active synthesis
- multi-agent pipeline
- visual reasoning
one_liner: 通过生成式模型主动合成可控视频，构建精细诊断多模态大模型时空推理能力的基准。
practical_value: '- 若业务涉及视频理解或多模态 Agent，可借鉴通过主动合成可控场景构建评测集的方法，避免真实视频的变量不可控和偏差。

  - 多智能体流水线配合人工质控的流程可迁移用于构建领域专有评测集，例如商品展示视频中的交互理解评测。

  - 将任务解耦为低级视觉感知和高级时空推理的层级设计，可用于开发细粒度模型诊断工具，定位推理薄弱环节。

  - 视频分类法（空间尺度、视角、场景动态）提供了构建更全面视频评测集的结构化思路。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**
现有时空推理评测依赖静态图像或被动选取的真实视频，难以控制变量，无法精细诊断多模态大模型（MLLM）的细粒度时空理解能力。

**方法**
提出 VGenST-Bench，利用生成式模型主动合成高度可控、多样化的视频场景。构建过程中采用多智能体流水线，并加入人工质量控制环节，确保视频和问答对的质量。定义了一个 3×2×2 视频分类法（空间尺度、视角、场景动态），覆盖丰富场景。设计层级任务套件，将低级视觉感知（对象计数、身份追踪）与高级时空推理（空间关系、时间排序）解耦，实现对模型能力的细粒度诊断。

**结果**
在多个 SOTA MLLM 上评测显示，模型在空间关系、时间排序等高级推理任务上性能明显不足，证明基准能有效暴露短板，推动模型改进。该基准范式从被动策展转向主动合成，为视频理解评测提供了新方向。
