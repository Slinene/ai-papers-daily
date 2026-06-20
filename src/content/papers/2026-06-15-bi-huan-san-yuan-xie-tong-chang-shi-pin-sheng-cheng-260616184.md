---
title: Closed-Loop Triplet Synergistic Generation for Long-Form Video
title_zh: 闭环三元协同长视频生成
authors:
- Xinlei Yin
- Xiulian Peng
- Xiao Li
- Zhiwei Xiong
- Yan Lu
affiliations:
- University of Science and Technology of China
- Microsoft Research Asia
arxiv_id: '2606.16184'
url: https://arxiv.org/abs/2606.16184
pdf_url: https://arxiv.org/pdf/2606.16184
published: '2026-06-15'
collected: '2026-06-20'
category: Multimodal
direction: 闭环视觉-文本-记忆协同的长视频生成
tags:
- Video Generation
- Agentic Framework
- Closed-Loop
- Memory
- Vision-Language Model
- Consistency
one_liner: 提出闭环视觉-文本-记忆协同框架，迭代纠正多镜头视频中的身份漂移和不一致问题。
practical_value: '- 闭环验证-修正机制可迁移至生成式推荐：在生成商品描述、个性化文案时，引入VLM或评判模型检测生成结果与用户意图/商品属性的一致性，自动触发重生成或prompt
  refine。

  - 实体中心记忆可用于用户/物品的长期建模：维护一个可更新的记忆状态，追踪实物属性变化和跨会话演进，提升多轮对话推荐或个性化agent的连贯性。

  - 代理框架分解复杂生成任务：将长流程切分为规划-执行-批评的agent回路，可用于搜索推荐流程自动化（如自动选品、策略组合、创意生成）。

  - 多镜头一致性优化思想可用于视频广告素材生成：确保多个片段中品牌/产品视觉元素保持一致，提升广告质量。'
score: 6
source: arxiv-cs.MM
depth: abstract
---

**动机**：多镜头长视频生成存在身份漂移和跨镜头不一致，现有故事板驱动流程多为前馈式，无法利用已生成视觉证据修正后续条件。

**方法**：提出CoTriSyGen，一个闭环三元协同框架，将多镜头生成建模为视觉-文本-记忆的迭代修正过程。包含三个核心组件：规划意图（分镜提示链）、持久记忆（以实体为中心的视觉状态，动态记录新增/演变的实体外观、多视角证据及组合）、已生成视觉。基于VLM的分析器对三元组进行推理，沿两条路径更新提示和记忆：1) 镜头内精炼：检测语义/组合违规时触发重生成，并优化图生视频prompt以增强运动连贯性；2) 镜头间精炼：基于已生成视觉证据，重写后续镜头提示，传播新出现的实体/属性，提升构图基础与电影流畅度。记忆实体由生成器和分析器持续更新，反映故事演进。

**结果**：在自建StoryBench上，相比现有方法，CoTriSyGen在跨镜头一致性、提示遵循度和电影连续性上取得显著提升。
