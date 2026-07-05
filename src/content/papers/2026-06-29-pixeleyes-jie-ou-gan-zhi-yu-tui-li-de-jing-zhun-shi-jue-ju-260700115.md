---
title: 'PixelEyes: Decoupling Perception and Reasoning for Pinpoint Visual Evidence
  Seeking'
title_zh: PixelEyes：解耦感知与推理的精准视觉证据搜索
authors:
- Dengxian Gong
- Yuanzheng Wu
- Haobo Yuan
- Zhengdong Hu
- Tao Zhang
- Yikang Zhou
- Shihao Chen
- Quanzhu Niu
- Kai Wang
- Jason Li
affiliations:
- Wuhan University
- UC Merced
- UTS
- NUS
- NTU
arxiv_id: '2607.00115'
url: https://arxiv.org/abs/2607.00115
pdf_url: https://arxiv.org/pdf/2607.00115
published: '2026-06-29'
collected: '2026-07-05'
category: Agent
direction: 解耦感知与推理的视觉Agent
tags:
- Visual Search
- Multimodal Agent
- Decoupling
- Semantic BFS
- Mask-guided Search
- Localization
one_liner: 提出解耦式视觉Agent：推理器决定找什么，专用分割工具给出掩码级定位，配合语义区域BFS消灭冗余路径。
practical_value: '- **解耦架构可直接迁移到电商Agent**：用LLM做高层推理决策（如“找 logo 在衣服的哪个部位”），调用专精的视觉基础模型（如商品分割模型）给出像素级定位，避免LLM直接输出
  bbox 不准导致的多轮无效追问。

  - **语义区域 BFS 策略用于多轮商品对比**：对商品详情图进行语义分割（如领口、袖口、印花区域），按区域广度优先提问，可系统性地收集细粒度属性，替代当前对话式推荐中随机或深度优先的循环。

  - **合成专家轨迹数据集的方法**：将高效搜索策略（如 BFS + 掩码引导）内化到模型训练中，可借鉴用于训练对话式推荐或客服 Agent，让模型学会用最短轮次完成信息收集。

  - **Pinpoint-Bench 的细粒度失败分析框架**：分离定位错误与推理错误，有助于诊断业务中多模态 Agent 的“注意盲视”（看到区域但识别错），可用于离线评估和迭代优化。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：多轮视觉推理中，现有 MLLM 常因推理与感知耦合在一起，定位不准引发反复裁剪错误子图，导致轨迹冗长甚至撞到轮次上限。核心问题在于让一个模型同时决定“找什么”和“在哪”会放大错误。

**方法**：提出 PixelEyes Agent，显式解耦推理与感知：
- **掩码引导视觉搜索**：推理器生成“找什么”的描述，调用引用分割模型输出实例掩码，精确裁剪目标区域，消除背景干扰，避免粗糙 bbox 引入的无关内容。
- **语义区域广度优先搜索**：对图像先做语义分割，按区域同级探索，而非陷入某一区域的深度裁剪循环，从机制上防止冗余访问。
- 构建 **PixelEyes-6K** 数据集，通过重合成已有数据中的专家轨迹，将掩码搜索与 BFS 逻辑内化到模型中。
- 提出 **Pinpoint-Bench** 零提示视觉搜索基准，提供实例级掩码和边界框，可分离定位失败与推理失败，诊断“注意盲视”等细粒度错误模式。

**关键结果**：在 Pinpoint-Bench 上，前沿 MLLM 与视觉 Agent 方法均表现不佳，PixelEyes 以显著更少的轮次（约 5 步）实现精确定位，达到 SOTA，且周转效率远高于耦合基线。
