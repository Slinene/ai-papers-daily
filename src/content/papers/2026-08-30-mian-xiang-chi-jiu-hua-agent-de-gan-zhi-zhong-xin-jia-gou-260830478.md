---
title: 'Agents in the Large: Perception-Centered Architecture for Persistent Agents'
title_zh: 面向持久化 Agent 的感知中心架构
authors:
- Shihan Dou
- Haoxiang Jia
- Shichun Liu
- Feng Chen
- Chenhao Huang
- Yujiong Shen
- Shaofan Liu
- Jiayi Chen
- Jiahang Lin
- Honglin Guo
affiliations:
- NLP Lab, Fudan University
- PL Lab, Peking University
- CCDS, Nanyang Technological University
- Hunyuan Team, Tencent
arxiv_id: '2608.30478'
url: https://arxiv.org/abs/2608.30478
pdf_url: https://arxiv.org/pdf/2608.30478
published: '2026-08-30'
collected: '2026-09-03'
category: Agent
direction: 持久化 Agent 感知中心架构
tags:
- Persistent Agents
- Perception-Centered Architecture
- Language Agents
- Lifecycle Tasks
- Agent Architecture
one_liner: 提出 Pera 架构，用感知与控制组件持续感知任务执行、内部上下文和环境变化，构建生命周期任务驱动长期服务的自适应
practical_value: '- 在电商/广告的对话式推荐或搜索 Agent 中，可以引入独立的“感知层”，持续收集任务执行日志、用户上下文变化（点击、收藏、加购）和环境信号（库存、竞价、大促），而不是每次请求都从零开始；这能显著提升长期用户陪伴和策略自适应性。

  - 借鉴 Pera 的“生命周期任务”抽象，把一次性推荐/出价/文案生成改造成可监控的长期任务：例如用户兴趣漂移检测、商品生命周期管理、广告创意衰退检测，由感知事件触发重优化，适合电商场景中的持续运营。

  - 采用感知与控制分离的工程实现：感知组件聚合 episodic memory 和外部信号，控制组件只负责把信号转化为待办任务队列，避免把记忆、工具、决策逻辑耦合在单个
  LLM prompt 里，便于在推荐系统中做在线策略迭代和灰度。

  - 如果已有 RAG 或 memory 增强的推荐 Agent，可按 Pera 思路补充“环境变化感知”通道（如商品下架、价格变动、用户实时行为），驱动生命周期任务更新推荐候选与话术，提升实时性和成交转化。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有认知语言 Agent 大多围绕用户指定的、有界任务设计，缺乏面向长期、持久服务场景的统一架构。当用户需求、上下文和服务流程随时间持续变化时，Agent 需要跨多次交互保持有用并自适应。

**方法关键点**：提出 Pera（Perception-Centered Architecture for Persistent Agents）。核心是围绕感知和控制组件组织持久 Agent：感知组件持续从三类信号源收集服务相关信号——① episodic 任务执行过程；② 内部上下文（自身状态、历史、记忆）；③ 周围环境变化（外部数据、工具、平台状态）。控制组件把这些感知信号转化为“生命周期任务”，这些任务反过来驱动服务流程的持续运行和自适应。这与软件工程从“programming in the small”到“programming in the large”的演化类似，把语言 Agent 的演进框架化为长期运行的自适应智能系统。论文用 Pera 回顾和归类了近期工作，并通过案例研究展示架构如何解释已有系统的组织方式。

**关键结果数字**：该论文为架构/框架类工作，未提供实验数字；贡献主要在概念框架、已有工作的回溯组织以及面向未来构建更强的持久 Agent 的定性洞察。
