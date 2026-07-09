---
title: 'MentalThink: Shaping Thoughts in Mental SVG World'
title_zh: MentalThink：在心理SVG世界中塑造思维
authors:
- Kangheng Lin
- Jisheng Yin
- Dingming Li
- En Yu
- Yana Wei
- Han Zhou
- Liang Zhao
- Hongyu Zhou
- Hongbo Peng
- Jianjian Sun
affiliations:
- Beijing University of Posts and Telecommunications
- University of Chinese Academy of Sciences
- StepFun
arxiv_id: '2607.03530'
url: https://arxiv.org/abs/2607.03530
pdf_url: https://arxiv.org/pdf/2607.03530
published: '2026-07-02'
collected: '2026-07-09'
category: Multimodal
direction: 多模态视觉推理 · SVG中间表示
tags:
- MLLM
- SVG
- Visual Reasoning
- Spatial Understanding
- RL Fine-tuning
one_liner: 让多模态大模型生成并执行SVG代码作为中间视觉表示，实现可验证的空间推理。
practical_value: '- 商品空间关系理解：用 SVG 生成商品轮廓与布局，辅助多模态模型理解复杂场景（如家具搭配、服装层次），提升搜索与推荐的准确性。

  - Agent 多步规划：借鉴“心理图像”机制，在 Agent 执行动作前生成场景 SVG 草图，用于自我反思和步骤优化，提高任务成功率。

  - 广告创意迭代：利用 SVG 的可编辑性，快速生成和调整广告图片的空间构图，结合 RL 迭代精炼，降低人工设计成本。

  - 训练范式复用：SFT 对齐结构化语法 + 多轮 RL 迭代修正是可迁移的通用训练策略，适合需要精确控制输出格式（如图形代码）的生成式推荐场景。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**  
人类推理常依赖心理图像进行空间操作，而当前多模态大模型缺乏可执行的可视化中间态。MentalThink 引入“用 SVG 思考”范式，让模型生成、渲染并解释可缩放矢量图形，将抽象空间假设外化为可验证的视觉工作区。

**方法**  
核心是 think-with-SVG 流水线：模型生成 SVG 代码，通过确定性渲染获得视觉反馈，在多轮交互中迭代检查、修改、精炼中间假设。训练分两阶段：先用监督微调（SFT）对齐 SVG 语法，再用多轮强化学习（RL）鼓励模型自主发现几何约束、修正错误、优化构图，无需外部编译器反馈。

**结果**  
MentalThink 在空间推理基准 VSIBench 上达 55.1%，MindCube 上达 76.0%，显著优于现有 MLLM，证明可执行矢量图形能有效支持动态视角切换、视觉反思和组合场景构建。
