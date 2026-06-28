---
title: 'From Structure to Synergy: A Survey of Vision-Language Perception Paradigm
  Evolution in Multimodal Large Language Models'
title_zh: 从结构到协同：多模态大模型中视觉语言感知范式演进综述
authors:
- Haoxiang Sun
- Tao Wang
- Li Yuan
- Jian Zhao
- Jiancheng Lv
affiliations:
- Sichuan University
- Peking University
- China Telecom
- Northwestern Polytechnical University
arxiv_id: '2606.26196'
url: https://arxiv.org/abs/2606.26196
pdf_url: https://arxiv.org/pdf/2606.26196
published: '2026-06-24'
collected: '2026-06-28'
category: Multimodal
direction: 多模态感知范式 · 统一视角演进
tags:
- MLLMs
- Vision-Language Perception
- Paradigm Evolution
- Survey
- Multimodal Intelligence
one_liner: 首次以统一视觉语言视角系统梳理 MLLM 感知范式的五阶段演进，为多模态智能提供路线图
practical_value: '- 业务中构建商品图文理解模型时，可参照该综述的五阶段（独立结构→浅层融合→深层交互→统一预训练→自主协同），判断当前模型所处阶段并规划升级路径；例如从双塔独立编码升级为交叉注意力融合，提升图文匹配精度。

  - 在 Agent 多模态感知模块设计中，借鉴「协同感知」思想，让文本指令与视觉输入的交互不再仅发生在高层语义空间，而是允许低层视觉特征直接受语言引导，提高空间推理与指令遵循能力。

  - 综述中梳理了各阶段代表方法（如 CLIP、BLIP-2、LLaVA、GPT-4V 等）的架构与训练 trick，可快速了解不同范式的工程实现取舍（如是否冻结视觉编码器、是否采用
  Q-Former 桥接），为技术选型提供参考。

  - 未来方向指出：统一感知需要解决幻觉、细粒度理解与效率瓶颈，这些同样制约电商场景下的多模态搜索/推荐，可提前关注稀疏 MoE、结构化知识注入等应对策略。'
score: 6
source: arxiv-cs.MM
depth: abstract
---

**动机**：现有多模态大模型综述多将视觉与语言割裂看待，未从统一感知角度梳理演进脉络。该文提出将 MLLM 感知定义为内在的、统一的视觉语言能力，仿照人类天生感知，以此为主线回顾范式演变。

**方法**：提出五阶段分类法：(1) 结构独立期——视觉与语言模型独立预训练，仅通过简单线性投影或检索连接；(2) 浅层交互期——通过注意力机制或 adaptor（如 Q-Former）实现跨模态浅层对齐；(3) 深层融合期——视觉特征深度注入语言模型各层，以 LLaVA 为代表；(4) 统一预训练期——从数据与任务层面统一多模态预训练，如 Unified-IO、BEiT-3；(5) 自主协同期——模型具备动态调度与推理时自适应融合能力，如 GPT-4V、O-series，体现感知与推理的深度协同。每个阶段列举里程碑方法与关键创新。

**结果与展望**：现有 MLLM 在粗粒度图文理解上成绩显著，但仍面临幻觉、细粒度感知不足、推理效率低等挑战。未来方向包括：更高效的多模态感知架构（如 MoE）、统一模态原生感知、具身交互中的实时感知融合等，为通用多模态智能绘制了路径。
