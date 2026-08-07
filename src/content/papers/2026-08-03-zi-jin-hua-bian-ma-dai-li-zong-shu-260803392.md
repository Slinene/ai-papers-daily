---
title: Self-Evolving Coding Agents
title_zh: 自进化编码代理综述
authors:
- Hao Zhou
- Haichuan Hu
- Ye Shang
- Quanjun Zhang
affiliations:
- Nanjing University of Science and Technology
- Nanjing University
arxiv_id: '2608.03392'
url: https://arxiv.org/abs/2608.03392
pdf_url: https://arxiv.org/pdf/2608.03392
published: '2026-08-03'
collected: '2026-08-07'
category: Agent
direction: Agent 自进化机制与框架
tags:
- self-evolving
- coding agents
- survey
- feedback loops
- tool use
- memory
one_liner: 系统综述自进化编码代理，定义概念并提出对象为中心的演变分类法，分析软件工程的天然演进特征与挑战。
practical_value: '- **记忆驱动的推荐策略优化**：借鉴编码代理利用历史轨迹复用经验的方法，推荐Agent可记录用户反馈（点击/转化/停留）和推荐上下文，构建可检索的记忆库，在下一次相似场景中直接复用成功策略，减少重复探索成本。

  - **工具使用的在线自适应**：推荐Agent集成多种工具（如搜索API、用户画像查询），可监控工具调用成功率与业务效果，自动调整工具选择策略或微调调用参数，实现工具链的自进化。

  - **反馈驱动的提示词在线更新**：将A/B测试或在线指标作为反馈信号，自动优化Agent链路中的提示词（如召回、排序、文案生成），形成闭环自进化，避免人工调参滞后。

  - **多Agent协作的动态分工**：在多智体系统中（如广告竞价、多目标推荐），根据全局收益定期调整各Agent的权重或协作模式，类似编码代理更新协作结构，实现整体效率演进。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：LLM驱动的编码代理虽能辅助软件开发，但部署后大多静态不变，无法像人类工程师一样从交互反馈中持续学习。软件工程天然的动态性（代码演化、测试失败、修复经验累积）催生了自进化编码代理的研究方向。

**方法**：该综述首次明确自进化编码代理的定义，并与传统编码代理、通用自进化代理做了概念区分。核心贡献是提出**对象为中心的演变分类法**：明确**什么在演变**（框架、记忆、技能、工具、模型、协作结构），配合**何时演变**（在线/离线）和**驱动证据**（可执行反馈、仓库级上下文、编码轨迹）两个正交维度，形成系统框架。通过广泛文献调研，梳理了各维度下的典型工作。

**关键结果**：软件工程中的可执行反馈（如测试通过/失败）、代码仓库丰富上下文和长程任务轨迹，为代理自进化提供了独特条件，但也面临反馈可靠性、基准过拟合、安全性、维护成本、泛化能力等挑战。该综述为设计更自适应、可靠、软件敏感的Agent系统提供了概念基础和结构化参考。
