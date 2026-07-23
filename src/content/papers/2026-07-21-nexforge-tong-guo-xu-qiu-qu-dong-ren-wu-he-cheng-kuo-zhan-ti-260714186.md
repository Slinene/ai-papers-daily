---
title: 'NexForge: Scaling Agent Capabilities through Requirement-Driven Task Synthesis
  for LLMs'
title_zh: NexForge：通过需求驱动任务合成扩展 LLM 智能体能力
authors:
- Jiarong Zhao
- Zhikai Lei
- Zhiheng Xi
- Rui Zheng
- Hang Yan
- Jie Zhou
- Qin Chen
- Liang He
affiliations:
- East China Normal University
- Fudan University
- Shanghai Qiji Zhifeng Co., Ltd
arxiv_id: '2607.14186'
url: https://arxiv.org/abs/2607.14186
pdf_url: https://arxiv.org/pdf/2607.14186
published: '2026-07-21'
collected: '2026-07-23'
category: Agent
direction: 需求驱动的 Agent 训练数据合成
tags:
- agent training
- task synthesis
- requirement-driven
- SFT
- data scaling
- LLM agent
one_liner: 提出需求驱动的任务合成框架 NexForge，自动生成多样化可执行 agent 训练数据，显著提升 LLM agent 性能
practical_value: '- 借鉴需求驱动思想，根据业务能力需求（如“自动处理退换货”“批量更新商品库存”）自动生成多样化的终端/办公任务，用于微调内部
  Agent 模型，降低人工构造成本

  - 采用分布感知编译（基于真实需求日志构建情景和任务概况），使训练数据分布更贴近线上实际，减少偏差，可应用于电商搜索广告 Agent 的训练数据生成

  - 框架不依赖领域特定基建，可快速跨场景迁移，例如从终端操作扩展到电商后台、广告投放工具等新工具领域，降低工程门槛

  - 利用合成的高质量专家轨迹进行 SFT，验证了数据规模和多样性对提升 Agent 任务成功率的重要性，启示我们可通过自动化管线持续扩展 Agent 能力边界'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：LLM Agent 的后训练缺乏高质量、多样化的可执行训练数据，现有方法将任务生成绑定在预定义工具或知识图谱上，扩展需人工设计基础设施，新领域需定制管线，且任务分布常偏离真实需求。

**方法**：NexForge 采用需求驱动的范式，首先调研真实世界需求，构建代表性场景与任务概况；然后进行分布感知编译，生成多样化的任务指令；每一条指令自动检索或构造所需的文件、依赖和运行时配置；最后合成专家执行轨迹，形成 SFT 训练数据。该流程不依赖领域特定基础设施。

**结果**：在 Terminal-Bench 2.0 上，仅用 3.6K 终端任务+2K 办公任务微调 Qwen3.5-35B-A3B Base，准确率从 22.5% 提升至 52.0%；GDPval 上 Elo 从 813 升至 1338。终端任务增至 43.2K 时达到 58.4%，与配备 Claude Code 的 Claude Opus 4.6 持平。进一步扩展数据训练的 Nex-N2 模型在 Terminal-Bench 2.1 达 75.3%，GDPval 达 1585 Elo，达到开源 SOTA，超越多个前沿闭源系统。
