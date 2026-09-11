---
title: 'EvoSafeHarness: Evolving Model- and Domain-Specific Harnesses for Securing
  Agents'
title_zh: 演化式模型与领域特定安全 Harness 框架
authors:
- Nanxi Li
- Yingzi Ma
- Yulong Cao
- Edward Suh
- Bo Li
- Dawn Song
- Chaowei Xiao
affiliations:
- Johns Hopkins University
- University of Wisconsin–Madison
- NVIDIA
- University of Illinois Urbana–Champaign
- UC Berkeley
arxiv_id: '2609.05903'
url: https://arxiv.org/abs/2609.05903
pdf_url: https://arxiv.org/pdf/2609.05903
published: '2026-09-04'
collected: '2026-09-11'
category: Agent
direction: Agent 安全防御与自动化 harness 合成
tags:
- LLM Agent
- Safety
- Harness
- Optimization
- Adversarial Robustness
one_liner: 自动合成针对冻结模型与目标领域的安全 harness，联合搜索自然语言策略和可执行代码逻辑，在保障效用下大幅降低攻击成功率
practical_value: '- 在推荐/搜索 Agent 中增加独立安全层：将安全 harness 与推荐逻辑解耦，自动生成针对特定模型和业务域的策略与代码，避免手工编写规则，可快速适配不同推荐模型（如
  LLM 推荐生成式商品描述）。

  - 模型-领域特定的安全阈值自动调优：借鉴其联合搜索策略，为每个推荐模型和场景（如电商导购、广告文案生成）自动发现最优的安全约束强度，平衡过度拦截与安全漏洞，节省人工调优成本。

  - 将领域合规要求嵌入可执行代码：类似地提取电商/广告领域的业务安全关系（如广告法违禁词、价格合规），编译为可执行的过滤逻辑，并集成到 Agent 的动作执行前检查中。

  - 对抗性评估与在线迭代：在发布推荐 Agent 前，使用类似 PAIR 的自适应攻击模拟恶意输入或提示注入，评估防御有效性；将对抗审查作为持续集成的一部分，动态更新安全
  harness。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：LLM Agent 将语言转化为真实世界行动，面临间接提示注入和直接有害请求双重威胁。系统级安全 harness 是补充防御层，但现有设计通常一次专家设计并跨模型、跨领域通用，导致对某些模型过度阻断、对特定领域遗漏关键安全关系。

**方法关键点**：EvoSafeHarness 是安全专用优化框架，对冻结模型和目标领域自动合成可部署 harness。它联合搜索自然语言策略和可执行代码逻辑，利用模型行为反馈、领域规范（效果、状态、动作序列）以及新鲜上下文对抗审查，避免过拟合基准特定规则。

**关键结果**：在四个 Agent benchmark 上实现更强的安全-效用前沿。DecodingTrust-Agent 上平均攻击成功率从 45.6% 降至 10.0%，效用代价仅 3.3，15 个单元中 14 个最佳；AgentDojo 上达到 82.8% 效用且 0.0% ASR，是 CaMeL 同工作点效用的两倍，并可零样本迁移到未见 AgentDyn 套件；Agent-SafetyBench 上每个受害模型均获最佳分数；自适应 PAIR 攻击下（细化预算 16）平均 ASR 保持在 20% 以下。分析表明领域语义决定所需安全关系和轨迹状态，模型与运行时行为决定这些关系的执行位置和方式。
