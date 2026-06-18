---
title: 'Visual-Seeker: Towards Visual-Native Multimodal Agentic Search via Active
  Visual Reasoning'
title_zh: Visual-Seeker：通过主动视觉推理实现视觉原生多模态智能搜索
authors:
- Zhengbo Zhang
- Changtao Miao
- Jinbo Su
- Zhaowen Zhou
- Chunxia Zhang
- Xukai Wang
- Ruiqi Liu
- Kaiyuan Zheng
- Jiansheng Cai
- Bo Zhang
affiliations:
- UCAS
- Institute of Automation, CAS
- Ant Group
- RUC
- BIT
arxiv_id: '2606.15231'
url: https://arxiv.org/abs/2606.15231
pdf_url: https://arxiv.org/pdf/2606.15231
published: '2026-06-12'
collected: '2026-06-18'
category: Agent
direction: 多模态搜索代理 · 主动视觉推理
tags:
- multimodal agent
- deep search
- visual reasoning
- active visual reasoning
- tool use
- VQA
one_liner: 提出视觉原生多模态搜索代理，主动关注细粒度视觉细节并动态收集视觉证据，在多模态搜索基准上达到SOTA
practical_value: '- 电商搜索场景中可借鉴主动视觉推理，让 Agent 动态分析商品图片的局部细节（如品牌、款式），提升多模态查询的匹配精度。

  - 构建视觉原生搜索代理的数据流水线，合成多模态搜索轨迹，用于训练面向电商场景的视觉推理模型。

  - 在推荐对话 Agent 中引入动态视觉证据收集机制，对用户上传的图片进行多跳细粒度推理，增强可解释性和准确率。

  - 工程上可将主动视觉推理模块集成到现有多模态 LLM 搜索管道中，处理复杂的视觉问询，如“找类似这件衣服但领口不同的商品”。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：多模态大模型（MLLM）在开放世界视觉问答中缺乏事实准确性，现有搜索代理仅依赖简单图片和纯文本证据链，无法进行多跳、跨模态的细粒度推理。

**方法**：提出 **Visual-Seeker**，一种视觉原生的多模态深度搜索代理。它不再将视觉视为静态输入，而是通过**主动视觉推理**动态关注图片中的细粒度视觉细节，并在搜索过程中持续收集视觉证据。为释放其视觉原生潜力，设计了主动视觉推理数据流水线，合成了 **5K 高质量多模态搜索轨迹**用于模型训练。代理在每一步能自主决定需要关注的图像区域，并结合网页搜索、工具调用完成多跳推理。

**结果**：在 **5 个具有挑战性的多模态搜索基准**（包含真实网页环境）上取得 **SOTA 性能**，甚至超越多个闭源商用模型，验证了其在真实网络环境中鲁棒的视觉原生推理与搜索能力。
