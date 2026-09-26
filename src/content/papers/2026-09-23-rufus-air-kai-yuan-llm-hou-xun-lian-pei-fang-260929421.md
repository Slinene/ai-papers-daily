---
title: 'Rufus-Air: An Open LLM Post-Training Recipe'
title_zh: Rufus-Air：开源 LLM 后训练配方
authors:
- Chia-Yuan Chang
- Renyuan Cheng
- Rui Feng
- Xiaotian Han
- Yuan He
- Hongye Jin
- Linwei Li
- Shiyang Li
- Fenglin Liu
- Xin Liu
affiliations:
- Amazon
arxiv_id: '2609.29421'
url: https://arxiv.org/abs/2609.29421
pdf_url: https://arxiv.org/pdf/2609.29421
published: '2026-09-23'
collected: '2026-09-26'
category: Training
direction: LLM 后训练全流程配方
tags:
- Post-Training
- RLVR
- MoE
- Agentic RL
- Difficulty Filtering
- Reward Design
one_liner: 公开 GLM-4.5-Air-Base 的完整后训练配方，以难度过滤和奖励可靠性排序驱动 8 阶段训练，显著超越官方 release
practical_value: '- **SFT 配比看 token 而非 sample**：长轨迹类别（Math、Coding Agent）在 sample 占比不高但贡献近半训练
  token。业务上做生成式模型 SFT 时，应按 loss-contributing tokens 评估数据配比，避免被 sample count 误导。

  - **难度过滤作为自动课程**：RL 阶段统一剔除“已解决”和“不可学”的 prompt，只保留策略当前可进步的区间，随策略提升自动滚动。此思路可直接用于电商文案生成、query
  改写、Agent 工具调用的 RL 训练，减少无效 rollout 和梯度噪声。

  - **按奖励可靠性排阶段**：先跑可验证奖励（规则、执行测试），后跑 judge/model-based 奖励，缩短奖励被 hack 的暴露时间。多阶段 RLHF
  或对齐训练时，可借鉴该顺序，把 IF 类接近已有能力的软奖励提前，把开放偏好奖励放最后。

  - **基础设施也是配方**：统一 chat template、token-in/token-out rollouts、Rollout Routing Replay、可靠
  sandbox 服务对 MoE 稳定训练至关重要。搭建内部 RL 框架时，这些工程细节应作为一等公民，而非实现细节。'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
开放权重 checkpoint 降低后训练门槛，但完整可复现的 recipe 仍稀缺，多数报告只给结果不给可操作细节。本文给出的 Rufus-Air 基于 GLM-4.5-Air-Base（106B-A12B MoE），全程使用开源组件和公开数据，无新增人类标注，计算量可控，为业界提供可复用的后训练工程经验。

### 方法关键点
- **8 阶段串行管线**：SFT → Reasoning RL → Coding RL → Instruction-Following RL → General Agent → Coding Agent → Search Agent → RLHF。
- **SFT 是能力地基**：9.01M samples / 27.0B 有效训练 token，覆盖 General Agent、General Chat、STEM、Math、Code、Coding Agent 六类；重点保证格式一致、多轮、长程能力，使后续 RL 不需要从零教格式化。
- **难度过滤**：RL 各阶段统一丢弃策略已解决（pass rate >0.8）和完全不可解（zero success）的 prompt，保留当前可学习区间，形成自动课程。
- **奖励可靠性决定阶段顺序**：先跑硬验证奖励（数学、代码执行），再跑 judge/model-based 软奖励（IF、Agent、RLHF），最小化 reward hacking 暴露时间。
- **基础设施**：FP8 rollout + BF16 training 混合、Rollout Routing Replay 稳定 MoE 训练、统一 chat template、可靠 sandbox 服务支撑长 Agent 轨迹。

### 关键实验
与官方 GLM-4.5-Air 相比，Rufus-Air 在多数指标大幅领先：IFEval 95.4 vs 83.0，IFBench 76.9 vs 33.6，Multi-challenge 65.8 vs 36.0，Arena-Hard v2 (HP) 89.1 vs 55.0，Tau2-Telecom 93.0 vs 32.7，HLE-Verified Gold 51.1 vs 20.2，SWE-bench Verified 65.6 vs 50.6。阶段增量上：Reasoning RL 使 GPQA +5.3，Coding RL 使 LiveCodeBench v6 +7.3，IF RL 使 Multi-challenge +24.7，General Agent 使 MCP-Atlas +7.8 / Tau2-Retail +9.8，Search Agent 使 BrowseComp +3.0 / HLE-V +3.4。与同规模开放模型 INTELLECT-3、Nemotron-3-Super 相比具备竞争力。

### 最值得记住的一句话
SFT 不是热身，而是建立后续 RL 所需格式与能力的地基；难度过滤与奖励可靠性排序是可复用的后训练核心原则。
