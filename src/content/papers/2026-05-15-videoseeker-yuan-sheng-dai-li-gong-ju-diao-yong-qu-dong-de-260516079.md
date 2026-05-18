---
title: 'VideoSeeker: Incentivizing Instance-level Video Understanding via Native Agentic
  Tool Invocation'
title_zh: 'VideoSeeker: 原生代理工具调用驱动的实例级视频理解'
authors:
- Yiming Zhao
- Yu Zeng
- Wenxuan Huang
- Zhen Fang
- Qing Miao
- Qisheng Su
- Jiawei Zhao
- Jiayin Cai
- Lin Chen
- Zehui Chen
affiliations:
- University of Science and Technology of China
- Xiaohongshu Inc.
- East China Normal University
- Xi’an Jiaotong University
arxiv_id: '2605.16079'
url: https://arxiv.org/abs/2605.16079
pdf_url: https://arxiv.org/pdf/2605.16079
published: '2026-05-15'
collected: '2026-05-18'
category: Agent
direction: 视频理解 · 代理工具调用 · 强化学习
tags:
- Video Understanding
- Agentic Tool Invocation
- RL Training
- Data Synthesis
- Instance-level Localization
- LVLM
one_liner: 用视觉提示和原生工具调用实现实例级视频理解，平均提升13.7%，超越GPT-4o与Gemini-2.5-Pro。
practical_value: '- **数据合成管线借鉴**：四阶段自动化生成实例级视频数据的流程（空间/时间定位标注、工具调用轨迹），可用于构建商品视频细粒度识别、直播片段检索等场景的高质量训练数据。

  - **原生工具调用训练范式**：冷启动监督+GRPO强化学习内部化工具调用能力，可迁移至电商多模态Agent（如商品问答、视频导购），让模型自主决定何时调用时空定位工具。

  - **视觉提示交互设计**：以框、掩码等视觉提示替代纯文本描述，提升时空指代精度，适用于商品图像区域标注、视频高光剪辑等交互式应用。

  - **反思机制与奖励设计**：通过反思步骤和多维度奖励（定位精度、推理正确性）优化策略，可直接参考用于生成式推荐或对话Agent的RL微调，平衡探索与利用。'
score: 7
source: arxiv-cs.CV
depth: abstract
---

**动机**：现有大视觉语言模型（LVLM）在需要精细时空定位的实例级视频理解上表现不佳，纯文本提示难以精确描述空间区域和时间片段，且感知与推理过程割裂，模型缺乏主动检索视觉证据的能力。

**方法**：提出VideoSeeker，一种基于视觉提示的原生代理工具调用范式。模型不再是单纯的文本交互，而是能够根据视觉提示（如目标框、时间掩码）主动调用时空检索、目标跟踪等工具。为此构建了四阶段自动数据合成管线：1）收集原始视频与对应描述；2）利用现有多模态模型生成初步定位标注；3）通过工具交互生成调用轨迹；4）过滤低质量样本。训练分两阶段：冷启动用合成数据微调基本行为，再通过GRPO强化学习优化工具调用和推理策略，奖励信号包含定位精度、问答正确性和工具调用合理性，并引入反思步骤让模型自检。

**结果**：在实例级视频理解基准上，VideoSeeker平均提升13.7%，显著优于Qwen2.5-VL、InternVL2.5等基线，甚至超过GPT-4o和Gemini-2.5-Pro。在通用视频问答（如Video-MME）上也展现出强迁移性，表明该范式不仅能解决细粒度定位，还能泛化到常规理解任务。
