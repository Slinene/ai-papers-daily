---
title: Visual prompt engineering for video models
title_zh: 视频模型的视觉提示工程
authors:
- Robert Geirhos
- Yuxuan Li
- Thaddäus Wiedemer
- Neha Kalibhat
- Zi Wang
- Mani Malek
- Oyvind Tafjord
- Kevin Swersky
- Been Kim
- Priyank Jaini
affiliations:
- Google DeepMind
arxiv_id: '2607.25537'
url: https://arxiv.org/abs/2607.25537
pdf_url: https://arxiv.org/pdf/2607.25537
published: '2026-07-27'
collected: '2026-07-30'
category: Multimodal
direction: 视觉提示工程提升视频模型推理
tags:
- visual prompt engineering
- video reasoning
- foundation models
- multimodal
- test-time adaptation
one_liner: 自动修改任务图像（视觉提示）可显著提升视频模型推理性能，超过文本提示和测试时扩展
practical_value: '- **商品图像预处理增强理解**：借鉴 VIPE，对电商商品主图进行自动风格化（如光影优化、背景真实化），可提升多模态模型在属性抽取、类目识别上的准确率，无需重训模型。

  - **测试时输入优化**：在不改变模型权重的前提下，仅通过调用图像编辑API在推理前重绘输入，即可低成本提升下游效果，适合广告创意优选、直播封面自适应等场景。

  - **视觉 Agent 的输入增强**：在多模态 Agent 中，对采集到的画面做轻量预处理（去模糊、风格迁移）可提高后续推理决策的可靠性，作为 Agent
  感知流水线的一个即插即用组件。

  - **计算高效性**：相比文本提示工程或多次采样，VIPE 仅增加一次图像编辑开销，是计算资源友好的提效手段，适合线上实时服务。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：语言模型的提示工程已证明有效，视频大模型正成为视觉推理的基础模型。论文探究能否通过自动修改任务图像（视觉提示工程，VIPE）来提升视频模型的推理性能，而不需训练模型。

**方法**：将视觉提示定义为利用外部图像编辑模型把原始任务图像变换为更有利于模型推理的版本（如抽象草图→真实感图像）。在多个视频推理任务（物理模拟、逻辑谜题等）上，比较原始基线、用户手写文本提示、自动文本提示优化和测试时扩展等策略。

**关键结果**：VIPE 一致地提升视频模型准确率，且效果明显优于文本提示工程和测试时扩展。例如，在球体落点预测任务中，将简单草图转为照片级图像后，模型正确率大增。该收益对不同的视频基础模型保持稳健，意味着视觉输入空间的优化是易得且通用的性能杠杆。
