---
title: Infinite Worlds with Versatile Interactions
title_zh: 无限世界与多样交互
authors:
- Zelin Gao
- Qiuyu Wang
- Jiapeng Zhu
- Jingye Chen
- Zichen Liu
- Qingyan Bai
- Jiahao Wang
- Yufeng Yuan
- Hanlin Wang
- Yichong Lu
affiliations:
- Robbyant
arxiv_id: '2607.07534'
url: https://arxiv.org/abs/2607.07534
pdf_url: https://arxiv.org/pdf/2607.07534
published: '2026-07-07'
collected: '2026-07-13'
category: MultiAgent
direction: 世界模型·多代理实时交互生成
tags:
- World Model
- Real-Time Generation
- Multi-Agent
- Causal Pretraining
- Model Distillation
one_liner: 支持无限时长实时交互的世界模型，通过因果预训练、模型蒸馏与双代理架构实现丰富动作与环境生成
practical_value: '- 因果预训练保证长序列生成质量一致，可借鉴到电商推荐中的用户长期行为序列建模或生成式推荐的长序列解码。

  - 从大模型蒸馏出低延迟实时变体的方法，可直接用于推荐系统在线推理，平衡效果与延迟。

  - 双代理架构（规划代理+执行代理）可复用到对话式推荐或交互式搜索中：一个代理解析用户意图并规划步骤，另一个代理生成推荐结果或操作。

  - 多样化交互元素扩增的思路，可用于推荐系统多模态内容生成，增加物料多样性。'
score: 6
source: huggingface-daily
depth: abstract
---

动机：现有交互世界模型难以同时兼顾无限交互时长、实时响应与丰富动作，限制了实际应用。
方法关键点：
- 设计因果预训练范式，使模型在任意长度交互序列上均能保持稳定生成质量，打破时长限制。
- 从14B基础模型蒸馏出1.3B实时变体，支持720p@60fps视频流，单GPU可部署。
- 大幅扩展动作空间（攻击、射箭、法术等）与文本驱动事件类型，提升交互多样性。
- 首次引入双代理框架：pilot代理负责角色行为规划与执行，director代理根据场景进展动态合成新环境元素。
结果：实现了一个支持多玩家共享的无限世界模拟器，14B与1.3B模型组合兼顾效果与效率。
