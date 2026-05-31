---
title: 'Why Far Looks Up: Probing Spatial Representation in Vision-Language Models'
title_zh: 为何远处向上看：探究视觉-语言模型的空间表征
authors:
- Cheolhong Min
- Jaeyun Jung
- Daeun Lee
- Hyeonseong Jeon
- Yu Su
- Jonathan Tremblay
- Chan Hee Song
- Jaesik Park
affiliations:
- Seoul National University
- The Ohio State University
- NVIDIA
arxiv_id: '2605.30161'
url: https://arxiv.org/abs/2605.30161
pdf_url: https://arxiv.org/pdf/2605.30161
published: '2026-05-27'
collected: '2026-05-31'
category: Multimodal
direction: 视觉-语言模型 · 空间表征分析
tags:
- VLM
- Spatial Reasoning
- Representation Analysis
- Shortcut Bias
- Synthetic Benchmark
one_liner: 发现VLMs将垂直图片位置与距离混淆，提出SpatialTunnel基准暴露空间捷径偏见，并表明解耦空间轴可提升鲁棒性
practical_value: '- 多模态推荐（如基于产品图像的空间关系推荐）需警惕模型依赖垂直位置作为距离的捷径，建议用对比对探测内部表征是否解缠。

  - 构建具身Agent的视觉模块时，应使用合成基准（如SpatialTunnel）评估空间推理鲁棒性，确保在反直觉视角下仍准确。

  - 电商视觉搜索中涉及空间关系查询（如“沙发左侧的台灯”）时，可借鉴表征分析方法验证模型是否真正理解3D空间。

  - 模型选型时，相似基准得分可能掩盖内部偏见差异；可补充表征探针，优先选择空间轴分离度高的VLM。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：视觉-语言模型（VLMs）在空间推理基准上表现强劲，但尚不清楚这是由于结构化3D理解还是利用自然图像统计捷径。日常照片中“远处物体在图片上方”的透视规律可能被模型滥用，导致缺乏真实空间认知。

**方法**：提出表征层分析框架，通过构建最小对比对，测量VLM嵌入中空间坐标轴（水平、垂直、距离）的组织与解缠程度；并引入合成基准SpatialTunnel，剔除自然图像中的透视相关性，专门暴露捷径偏见。

**结果**：多个模型族均存在**垂直-距离纠缠**：模型将图片垂直位置与真实距离混淆，在透视一致与反直觉样例间产生显著准确率差距；数据扩大会加剧这种偏见，即便整体准确率提升。具有良好分离空间轴的模型在多个基准上表现出更高鲁棒性，SpatialTunnel实验证实纠缠是模型内在的。工作提示，仅看基准分数不足以衡量空间推理能力，内部表征结构是关键。
