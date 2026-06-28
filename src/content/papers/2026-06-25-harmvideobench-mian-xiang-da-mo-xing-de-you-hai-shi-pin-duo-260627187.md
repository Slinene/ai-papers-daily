---
title: 'HarmVideoBench: Benchmarking Harmful Video Understanding in Large Multimodal
  Models'
title_zh: HarmVideoBench：面向大模型的有害视频多层理解基准
authors:
- Jiajun Wu
- Haoyu Kang
- Yining Sun
- Jiacheng Hou
- Heng Zhang
- Danyang Zhang
- Zhenjun Zhao
- Haochi Zhang
- Leixin Sun
- Eric Hanchen Jiang
affiliations:
- Central South University
- Tsinghua University
- ByteDance Inc
- Tencent
- Nankai University
arxiv_id: '2606.27187'
url: https://arxiv.org/abs/2606.27187
pdf_url: https://arxiv.org/pdf/2606.27187
published: '2026-06-25'
collected: '2026-06-28'
category: Multimodal
direction: 多模态安全审核 · 动态检索增强
tags:
- multimodal-benchmark
- harmful-video
- content-moderation
- retrieval-augmented
- LLM
- safety
one_liner: 构建首个多层次有害视频诊断基准并配套边界感知检索方法，将LVLM理解能力提升至84.4%
practical_value: '- 在商品视频审核中，可借鉴“可观察证据→片段内含义→超出片段推理”三层框架设计评测集，避免只做二分类漏判隐性违规。

  - BCR 的推理边界预测机制可嵌入多模态 RAG 审核链路：模型先判断是否需要检索外部知识，降低高并发审核场景的推理延迟与成本。

  - 该基准暴露了现有模型依赖表面捷径的缺陷，建议在推荐系统的内容理解评测中加入对比测试，防止因浅层匹配误判而放过违规内容。

  - 动态按需检索的思路可迁移至 Agent 的视觉推理任务，例如商品短视频的自动解说生成，仅在需要外部产品知识时触发检索，提升生成效率。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：现有有害视频评测仅做二分类，忽略视频的多层危害特性且缺失解释性，导致模型可借表面捷径通关，黑盒评估无法诊断深层理解能力。

**方法关键点**：
- 构建 **HarmVideoBench** 基准，含 1,379 个视频与 4,137 道选择题，覆盖三个递进维度：可观察证据（表层视觉）、片段内含义（叙事语境）、超出片段推理（外部知识/社会常识）。
- 提出 **BCR**（Boundary-aware Context Retrieval），让模型先预测自身推理边界，仅当 clip 内信息不足时才触发动态检索外部上下文，避免无关知识噪音。

**关键结果**：19 个主流 LVLM 的评测暴露诸多模型深层推理短板；BCR 将基模型宏平均准确率从 61.7% 大幅提升至 84.4%，登上新 SOTA。
