---
title: 'Enhancing Virtual Agents through SLMs and Edge-Computing: An Exploratory Evaluation
  of Think and Memory Processes'
title_zh: 基于小语言模型与边缘计算的虚拟Agent思考与记忆过程探索
authors:
- Aimilios Hadjiliasi
- Louis Nisiotis
affiliations:
- University of Central Lancashire, Cyprus
arxiv_id: '2608.13420'
url: https://arxiv.org/abs/2608.13420
pdf_url: https://arxiv.org/pdf/2608.13420
published: '2026-08-13'
collected: '2026-08-16'
category: Agent
direction: 边缘SLM驱动的Agent认知架构评估
tags:
- Small Language Models
- Edge Computing
- Agent Memory
- Virtual Agents
- Cognitive Architecture
one_liner: 在边缘设备上用小语言模型实现虚拟Agent的Think与Memory组件，验证路由、记忆读取与延迟的可行性
practical_value: '- 边缘部署小模型分担路由与记忆读取任务，可降低电商客服/推荐Agent的云端依赖和响应延迟，适合实时交互场景。

  - 将Agent认知拆分为Think、Memory等独立组件，分别用不同尺寸SLM处理，按延迟和准确率权衡选型，可作为线上Agent架构设计参考。

  - 记忆驱动对话系统的设计：SLM负责判断是否需要读取记忆、检索相关信息并生成回复，可用于多轮推荐解释或用户偏好追踪。

  - 评估维度可直接复用：路由准确率、记忆读取成功率、端到端延迟，用于对比不同SLM在业务Agent中的性能。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

动机：元宇宙/虚拟世界中的具身Agent需要持久、自适应、上下文感知的认知能力，但云计算方案存在延迟和隐私问题，边缘计算配合小语言模型（SLM）可能提供低成本、低延迟的部署路径。

方法：基于CEAA（Cognitive Embodied Agent Architecture）框架，聚焦其Think与Memory两个核心认知过程，开发边缘虚拟Agent网关系统。硬件采用NVIDIA Jetson Orin NX，模型使用Qwen2.5系列不同尺寸。系统将服务请求路由到对应SLM处理，并实现记忆驱动的对话：SLM判断是否需要读取长期记忆、抽取相关记忆并生成回复。

结果：通过模拟实验评估路由准确性、记忆读取性能和端到端延迟。原型系统展示SLM可部分实现CEAA的认知组件，在边缘设备上运行具备可行性与上下文响应能力，为沉浸式虚拟世界的具身Agent开发提供了工程参考。
