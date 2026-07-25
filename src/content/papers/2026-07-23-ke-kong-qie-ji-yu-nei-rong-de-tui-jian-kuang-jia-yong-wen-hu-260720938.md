---
title: Controllable and Content-Based Recommendations
title_zh: 可控且基于内容的推荐框架：用文本瓶颈实现用户干预
authors:
- Fırat Öncel
- Jihoon Jeong
- Emiliano Penaloza
- Mirco Ravanelli
- Laurent Charlin
- Cem Subakan
affiliations:
- Concordia University
- Université de Montréal
- Laval University
- HEC Montréal
- Mila – Quebec AI Institute
arxiv_id: '2607.20938'
url: https://arxiv.org/abs/2607.20938
pdf_url: https://arxiv.org/pdf/2607.20938
published: '2026-07-23'
collected: '2026-07-25'
category: RecSys
direction: 可控推荐 · 文本瓶颈介入
tags:
- controllable recommendations
- text bottleneck
- content-based
- multimodal
- collaborative filtering
one_liner: 通过在协同过滤中嵌入文本瓶颈，让用户通过文本直接控制推荐方向，且文本概要从物品内容（图像/音频/视频）自动生成。
practical_value: '- **文本瓶颈实现细粒度用户控制**：电商场景可直接复现——用户输入短文本（如“更多休闲风、亮色”）即可调整推荐方向，无需重新训练。可将此模块嵌入已有协同过滤模型，作为实时干预层。

  - **从商品多模态内容自动生成可控概要**：利用商品图片、音频或视频自动抽取文本描述作为控制柄，避免人工标注。对图像电商、短视频带货等场景，可低成本构建可控推荐系统。

  - **与现有模型即插即用**：CCBR 作为协同过滤的插件，不影响原有模型推理效率，且维持竞争性推荐性能。工程上可先训练基础模型，后接入文本瓶颈，降低落地风险。

  - **支持文本与多模态混合干预**：允许用户同时用文本和示例图片调整偏好，适配导购、搜索重排序等场景，提供更灵活的用户体验。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：传统推荐模型依赖隐向量，难以解释和干预。当用户临时意图与历史行为不一致时，缺乏直接控制手段。现有可控推荐方法大多需要人工设定属性，且不从物品内容自动推断控制信息。

**方法关键点**：
- 在协同过滤模型（如 Mult-VAE）中插入**文本瓶颈**：从物品原始内容（图像、音频或视频）通过预训练模型自动生成文本概要，用作文本瓶颈的初始化；
- 训练时，物品内容到文本概要的映射与推荐损失联合优化，保证概要既保留物品区别性又可由用户编辑；
- **控制干预**：用户编辑文本概要（或提供示例图像），模型据此更新推荐，实现可解释、可控制。

**关键结果**：
- 在图像、音频、视频三个数据集上，CCBR 的推荐性能（Recall/NDCG）与纯隐向量基线持平甚至更优；
- 超越近期可控推荐基线 TEARS；
- 通过系统性干预实验（如修改颜色、风格关键词），验证用户操控能有效引导推荐输出。
