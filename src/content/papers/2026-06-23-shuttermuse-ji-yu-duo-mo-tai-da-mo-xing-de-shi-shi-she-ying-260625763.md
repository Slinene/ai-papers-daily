---
title: 'ShutterMuse: Capture-Time Photography Guidance with MLLMs'
title_zh: ShutterMuse：基于多模态大模型的实时摄影指导
authors:
- Jiayu Li
- Yixiao Fang
- Tianyu Hu
- Wei Cheng
- Ping Huang
- Zheheng Fan
- Gang Yu
- Xingjun Ma
affiliations:
- Fudan University
- StepFun
arxiv_id: '2606.25763'
url: https://arxiv.org/abs/2606.25763
pdf_url: https://arxiv.org/pdf/2606.25763
published: '2026-06-23'
collected: '2026-06-28'
category: Multimodal
direction: 多模态大模型 · 拍摄指导
tags:
- Multimodal LLM
- Photography Guidance
- Capture-Time
- Composition
- Pose Recommendation
- Benchmark
one_liner: 构建拍摄时机摄影指导基准与统一多模态模型，联合优化构图决策与姿态推荐
practical_value: '- **多模态决策+细化联合建模**：将构图决策（是否调整）与细化（精确裁剪区域）统一到一个模型，可借鉴到电商场景中，例如商品展示图的自动评估与局部优化，或广告创意的整体布局判断与元素微调。

  - **场景条件生成式推荐**：通过场景图片生成主体姿态建议，本质上是一种条件生成式推荐。在虚拟试穿、搭配推荐中，可以根据用户输入的场景（如背景、环境）直接推荐合适的姿态、穿搭或商品，提升交互体验。

  - **统一多任务减少推理成本**：用一个 MLLM 同时处理摄影师侧和主体侧任务，避免多模型流水线。推荐系统中可将召回、排序、解释生成等合并，降低工程复杂度与延迟。

  - **结构化视觉标注增强可解释性**：训练中加入关键点等结构化数据，使模型输出可执行的视觉指导。可将类似思路用于商品关键属性（如领型、袖长）的结构化标注，提升模型对细粒度属性的控制力。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**  
现有美学裁剪基准仅评估事后裁剪，忽略拍摄时的实时构图指导和主体姿态建议，多模态大模型在拍摄指导的能力未被探索。  
**方法**  
构建 CaptureGuide-Bench 基准，包含两个互补任务：摄影师侧的构图决策与细化（评估当前构图是否需调整，并给出精确裁剪区域），以及主体侧基于场景条件的姿态推荐。评估发现通用 MLLM 能做构图决策但缺乏精确定位，专用裁剪模型擅长细化但局限于裁剪范畴。进一步构建 CaptureGuide-Dataset（130K 样本，含文本理由与结构化视觉标注），并训练统一多模态模型 ShutterMuse，采用监督微调与强化微调相结合的方式。  
**关键结果**  
在 CaptureGuide-Bench 上，ShutterMuse 在摄影师侧性能整体最优，主体侧姿态推荐具有竞争力，且推理成本大幅低于基线模型，展示了 MLLM 作为实时交互摄影助手的潜力。
