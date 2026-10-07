---
title: Harness Engineering for Software Engineering via Modular Executable Dev-Primitives
title_zh: 通过模块化可执行开发原语进行软件工程智能体框架设计
authors:
- Haibo Jin
- Xinjie Li
- Peng Kuang
- Haohan Wang
affiliations:
- University of Illinois Urbana-Champaign
- The Pennsylvania State University
arxiv_id: '2610.07832'
url: https://arxiv.org/abs/2610.07832
pdf_url: https://arxiv.org/pdf/2610.07832
published: '2026-10-05'
collected: '2026-10-07'
category: MultiAgent
direction: Agent 多智体协作与模块化架构
tags:
- LLM Agent
- MultiAgent
- Modularity
- Context Management
- Software Engineering
- Heterogeneous LLM
one_liner: 提出 Dev-Primitives 与 HERMES，用依赖感知动态激活的模块化 LLM 原语降低长程软件工程任务的上下文爆炸与语义漂移
practical_value: '- 将电商推荐/搜索 Agent 流水线拆分为多个“原语”模块（召回、排序、创意生成、知识检索等），每个模块携带小型 resident
  LLM，提供自然语言接口与局部自我修改能力，避免单体 Agent 的上下文爆炸。

  - 借鉴依赖感知动态激活：根据任务依赖图只唤醒相关模块，例如商品类目变更时仅激活商品理解与召回模块，而非加载完整系统上下文。

  - 引入执行证据回流的诊断机制：将线上指标、bad case、日志等作为证据映射到需要修改的具体模块，进行局部微调或策略调整，降低全链路重训练成本。

  - 采用异构 LLM 分层：强模型（如 GPT-5 级）负责全局激活与诊断决策，便宜小模型（如 Qwen3-8B）配置在模块内部执行局部修改，在保持效果接近的同时减少推理成本。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：LLM 软件工程 Agent 在长程工作流中需反复重建散落在源码、配置、测试、依赖和运行时中的程序状态，导致交互历史膨胀、上下文爆炸与语义漂移；大仓库还加剧了相关组件定位的难度。

**方法关键点**：
- Dev-Primitives：将仓库组件从被动软件构件变为主动参与者，每个原语配对仓库物件与一个 resident LLM，提供基于自身实现与依赖的 agent-native 接口，支持自然语言推理、组件间通信和局部自修改。
- HERMES 框架：在仓库规模实例化原语，通过依赖感知动态激活机制只唤醒任务相关组件；同时构建 bug 诊断机制，把执行证据映射回必须修改的组件。
- 分层异构配置：强模型负责激活与诊断，便宜小模型作为组件内部 resident LLM。

**关键结果**：在四个软件工程基准上，HERMES 比匹配基线平均提升 12.4%；配合强激活与诊断模型，即使 Dev-Primitives 用 Qwen3-8B，HERMES 与同构 GPT-5.6 Sol 配置的差距保持在 4.5% 以内，并在 Terminal-Bench 4.0 上降低 26.2% 推理成本。
