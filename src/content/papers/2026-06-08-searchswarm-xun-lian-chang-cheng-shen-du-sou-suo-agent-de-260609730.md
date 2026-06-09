---
title: 'SearchSwarm: Towards Delegation Intelligence in Agentic LLMs for Long-Horizon
  Deep Research'
title_zh: SearchSwarm：训练长程深度搜索 Agent 的委托智能
authors:
- Pu Ning
- Quan Chen
- Kun Tao
- Xinyu Tang
- Tianshu Wang
- Qianggang Cao
- Xinyu Kong
- Zujie Wen
- Zhiqiang Zhang
- Jun Zhou
affiliations:
- Ant Group
- Tsinghua University
- Peking University
- Renmin University of China
arxiv_id: '2606.09730'
url: https://arxiv.org/abs/2606.09730
pdf_url: https://arxiv.org/pdf/2606.09730
published: '2026-06-08'
collected: '2026-06-09'
category: Agent
direction: Agent 长程任务委托与上下文管理
tags:
- Delegation Intelligence
- Multi-Agent
- Deep Research
- Context Management
- SFT
- Search Agent
one_liner: 通过 harness 引导主 Agent 分解并委托子任务，再用 SFT 内化委托行为，在 30B 规模实现长程搜索 SOTA
practical_value: '- **Harness 设计可直接迁移到电商多 Agent 场景**：主 Agent 负责商品调研、竞品分析等长程任务时，借鉴「写简报必须含任务背景、已确认事实、未解决疑点」的原则，让子
  Agent 有足够上下文产出高质量结果，减少主 Agent 令牌消耗和重复探索。

  - **SFT 数据合成策略**：利用强模型当主 Agent 搭配弱模型当子 Agent 收集轨迹，迫使主模型学会更严谨的任务分解与结果验证，可用于训练电商客服、供应链优化等场景中的协调
  Agent。

  - **委托能力泛化证明单 Agent 推理也能受益**：即使去掉子调用工具，训练后的模型在单 Agent 任务上表现仍有提升，说明通过多 Agent 轨迹 SFT
  可增强模型的结构化问题分解能力，适用于推荐系统复杂查询的逐步推理。

  - **强制引用报告可提升溯源可信度**：要求子 Agent 报告附带行内引用，主 Agent 最终回答也需附来源，这对电商商品推荐、信息核查等需要可解释输出场景有直接借鉴意义；实现方式是在
  prompt 中约束输出格式并以此过滤训练数据。'
score: 9
source: arxiv-cs.AI
depth: full_pdf
---

**动机**：大模型用于长程深度研究时，上下文窗口有限，被动压缩或丢弃历史信息容易丢失关键证据。主动委托（main-distributes, sub-executes）能让主 Agent 只保留摘要，但需要一种“委托智能”——知道何时分解任务、如何写简报、如何整合子结果。该类训练数据在自然文本中稀缺，如何系统性合成并训练模型获得该能力尚属开放问题。

**方法关键点**：
- 设计一套 **harness**（工具集+系统 prompt），引导主 Agent 使用 `call_sub_agent` 工具将检索密集子任务委派给子 Agent，同时贯彻四条原则：鼓励委托、写全面简报（含背景、已确定事实、未解决疑点）、保留核心判断（主 Agent 独立决策方向）、要求子 Agent 报告附来源引用。
- 利用 harness 在开源查询集上收集 Agent 轨迹，其中主 Agent 正确作答且行为规范的正确轨迹被保留成 **SFT 数据**；还采用强弱模型配对（强主弱子）收集轨迹，迫使主模型加强任务分解与验证。
- 对基座模型 Tongyi DeepResearch-30B-A3B 做 full-weight SFT（仅计算模型输出 token 的损失，环境返回被 mask），得到 **SearchSwarm-30B-A3B**。

**关键结果**：
- 在 BrowseComp（68.1）、BrowseComp-ZH（73.3）、GAIA（82.5）、xbench-DeepSearch（80.8）上全面超越同规模轻量模型，其中 BrowseComp 超 MiroThinker-1.7-mini 0.2 点，超基座模型 24.7 点。
- 能力泛化：即使禁用子 Agent 工具，SearchSwarm 在 BrowseComp 子集上仍比基座提升 8.5 点；在开放域长回答基准 ScholarQA-v2 等上也平均提升 14.2 点，证明委托训练赋予的结构化分解与证据综合能力具有迁移性。

**核心设计思想**：通过周密 harness 引导委托行为，再将成功轨迹精炼为训练数据，让模型权重直接学会“何时委托、如何委托、如何整合”——这是一条可复现的从行为引导到能力内化的技术路线。
