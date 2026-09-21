---
title: 'MintAct: A Unified Visual Agent for Digital Environments'
title_zh: MintAct：统一数字环境的视觉Agent模型
authors:
- Mingfei Gao
- Rui Tian
- Haiming Gang
- Bohan Zhai
- Le Zhang
- Yuanzheng Gong
- Di Feng
- Ege Özsoy
- Kaixin Ma
- Vishwesh Kirthivasan
affiliations:
- Apple
arxiv_id: '2609.22083'
url: https://arxiv.org/abs/2609.22083
pdf_url: https://arxiv.org/pdf/2609.22083
published: '2026-09-17'
collected: '2026-09-21'
category: Agent
direction: 多模态Agent统一数字环境操作
tags:
- UI Agent
- Vision-Language Model
- Reinforcement Learning
- OSWorld
- Tool Use
- Digital Environments
one_liner: 用2B/4B/8B视觉语言模型统一UI定位、跨端多步导航与视觉工具调用，匹配各领域专用模型
practical_value: '- 在电商/广告场景中，可将UI grounding、跨页面多步操作、外部工具调用合并为一个模型，避免为不同端或不同任务维护多个专用Agent，降低部署和迭代成本。

  - 借鉴其异步RL框架：显式控制跨域训练分布，能缓解环境反馈噪声和off-policy漂移；做推荐/Agent在线学习时，可参考这种对训练分布的控制来稳定多任务协同。

  - 用数百个并发实例同时服务轨迹采集和在线RL的做法，适合需要大量交互数据的电商Agent、搜索导购Agent训练。

  - 2B小模型即可在OSWorld-Verified等基准上取得有竞争力的表现，对需要端侧部署的App内助手、广告落地页交互优化有直接参考价值。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：数字设备上的视觉语言Agent通常按能力切分：UI grounding、移动端导航、桌面控制、网页导航、视觉工具使用分别由专用模型完成。维护多个专用模型在服务、扩展和端侧部署上成本高，因此探索用一个模型统一这些能力且不牺牲单域性能。

方法关键点：提出MintAct，2B/4B/8B参数规模的视觉语言模型，统一UI定位、跨移动/桌面/网页的多步导航和视觉工具调用。核心是可扩展环境与RL基础设施：在异构后端上托管数百个并发环境实例，支持轨迹数据采集和在线RL；设计异步RL框架，显式控制跨域训练分布，在噪声环境反馈和off-policy漂移下保持稳定。

关键结果：在OSWorld-Verified上达到48.9，为同规模模型中的SOTA；在多个基准上全面匹配各领域专用模型性能。
