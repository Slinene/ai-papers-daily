---
title: 'PEA-DPO: Perception-Enhanced Alignment Direct Preference Optimization for
  MLLMs Alignment'
title_zh: PEA-DPO：感知增强直接偏好优化用于多模态大模型对齐
authors:
- Jiawei Feng
- Jiancan Wu
- Xingyu Zhu
- Junkang Wu
- Xiang Wang
- Xiangnan He
affiliations:
- University of Science and Technology of China
- National University of Singapore
arxiv_id: '2608.19598'
url: https://arxiv.org/abs/2608.19598
pdf_url: https://arxiv.org/pdf/2608.19598
published: '2026-08-20'
collected: '2026-08-21'
category: Multimodal
direction: 多模态 LLM 对齐与视觉偏好优化
tags:
- PEA-DPO
- Multimodal Alignment
- Visual Insensitivity
- DPO
- Hallucination
- MLLM
one_liner: 提出 PEA-DPO 显式利用视觉偏好信号，解决多模态 DPO 中的视觉不敏感问题并显著减少幻觉
practical_value: '- 在电商图文推荐或商品文案生成中，仅靠文本偏好对齐容易让模型忽略图像关键信息；可借鉴 PEA-DPO 思路，构造显式视觉对比样本（例如移除商品属性区域前后）作为偏好对，强制模型感知视觉差异。

  - 多模态场景下 DPO 失效往往表现为「视觉不敏感」，建议在偏好数据中显式注入视觉信号，而不是简单复用文本偏好对；这能降低商品描述与图片不一致的幻觉。

  - PEA-DPO 在增强视觉敏感性的同时保持语言建模能力，说明多模态对齐可以解耦：对视觉模块加感知约束，对语言模块保持原有优化目标，适合需要兼顾文案流畅性和图片一致性的业务。

  - 论文验证了不同规模 MLLM 上均有效，说明该方法可作为轻量级偏好优化插件，接入现有多模态推荐或搜索问答系统，无需改变主架构。'
score: 7
source: arxiv-cs.MM
depth: abstract
---

**动机**：DPO 已广泛用于 LLM 对齐，但在多模态场景下直接迁移存在局限。作者通过表征分析发现，多模态模型往往无法分辨原始图像与关键视觉上下文被移除的图像，称之为「视觉不敏感」，并进一步理论定位为跨图像不敏感与图像内不敏感。

**方法关键点**：提出 PEA-DPO，显式引入视觉偏好信号来增强感知对齐。该框架在偏好优化中加入视觉对比信息，使模型在保持语言建模能力的同时，被迫关注图像中的关键视觉差异。理论分析证明 PEA-DPO 能同时缓解两类视觉不敏感问题。

**关键结果数字**：在三个幻觉基准上，使用不同规模的 MLLM 进行评估，PEA-DPO 显著增强视觉上下文敏感性，大幅减少幻觉，同时保留基础模型的语言能力。
