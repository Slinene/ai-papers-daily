---
title: 'RESOURCE2SKILL: Distilling Executable Agent Skills from Human-Created Multimodal
  Resources'
title_zh: 多模态资源蒸馏：为软件智能体构建可执行技能库
authors:
- Yijia Fan
- Zonglin Di
- Zimo Wen
- Yifan Yang
- Mingxi Cheng
- Qi Dai
- Bei Liu
- Kai Qiu
- Yue Dong
- Ji Li
affiliations:
- Microsoft Research
- University of California, Santa Cruz
- Shanghai Jiao Tong University
arxiv_id: '2606.29538'
url: https://arxiv.org/abs/2606.29538
pdf_url: https://arxiv.org/pdf/2606.29538
published: '2026-07-15'
collected: '2026-07-21'
category: Agent
direction: 多模态技能蒸馏与智能体执行
tags:
- Agent Skills
- Multimodal
- Procedural Knowledge
- Skill Wiki
- Resource Distillation
- Software Agents
one_liner: 从视频、代码、文章等资源蒸馏可执行技能，以层次化多模态技能维基提升智能体在7个创作领域的表现，平均总分提升11.9个百分点
practical_value: '- **Agent 技能库构建范式**：在电商场景中，可将商品详情页生成、广告创意制作、活动页面搭建等重复性任务拆解为技能，从现有的视频教程、设计模板、代码仓库等多模态资源中自动蒸馏出可执行技能，而非手工编写。

  - **多模态技能表示 trick**：每个技能条目同时包含结构化文本（步骤描述）、代码片段（可执行工具调用）、视觉示例（关键帧截图）和元数据，这种多信号互补的设计能显著提升
  Agent 对操作流程的理解和生成质量，值得在涉及视觉/交互的任务中借鉴。

  - **层次化组织与按需检索**：技能库采用树状层次结构，Agent 在推理时根据任务目标动态检索并组合子技能；当现有技能覆盖不足时，还能在线从资源中实时获取新技能——这种“存量+增量”的机制可迁移到需要持续扩展能力的电商
  Agent 系统中。

  - **消融实验结论复用**：多模态格式、层次组织、多源资源、选择策略和在线获取都对性能有显著增益，说明在构建类似的 Agent 技能系统时，这些组件都有必要保留。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有软件智能体的技能库多为手工编写、以文本为中心或从智能体轨迹中提取，未能充分利用视频教程等丰富的多模态人类创作资源。这些资源蕴含时序操作、视觉反馈、可执行代码模式和概念风格等互补信号，可大幅提升智能体在复杂创作任务中的表现。

**方法**：提出 RESOURCE2SKILL 框架，将多模态资源（视频、代码仓库、文章等）蒸馏为可执行技能，并以**层次化多模态技能维基**形式组织。每个技能条目融合结构化文本、可执行代码、视觉示例、元数据和出处信息，保留不同资源的互补优势。推理时，智能体从维基中检索并组合相关技能；当覆盖不足时，同一构造算子可在线获取新技能。

**关键结果**：在幻灯片、电子表格、网页、3D 场景、CAD 设计、音频项目等 7 个实用创作领域，平均总分较无技能智能体**提升 11.9 个百分点**，在 28 个模型-领域主聚合测试中的 26 个上超越强基线。消融实验证实多模态格式、层次组织、源多样性、选择策略和在线获取均对性能有显著贡献。
