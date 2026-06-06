---
title: 'AdaPlanBench: Evaluating Adaptive Planning in Large Language Model Agents
  under World and User Constraints'
title_zh: AdaPlanBench：LLM代理在动态双重约束下的自适应规划评测
authors:
- Jiayu Liu
- Cheng Qian
- Zhenhailong Wang
- Bingxuan Li
- Jiateng Liu
- Heng Wang
- Jeonghwan Kim
- Yumeng Wang
- Xiusi Chen
- Yi R. Fung
affiliations:
- University of Illinois Urbana-Champaign
arxiv_id: '2606.05622'
url: https://arxiv.org/abs/2606.05622
pdf_url: https://arxiv.org/pdf/2606.05622
published: '2026-06-03'
collected: '2026-06-06'
category: Eval
direction: Agent 自适应规划评估
tags:
- Adaptive Planning
- LLM Agent
- Constraint Elicitation
- Benchmark
- Interactive Evaluation
- Progressive Disclosure
one_liner: 首个动态交互式基准，评估LLM代理在逐步揭示的世界与用户双重约束下的自适应重规划能力。
practical_value: '- **交互式约束揭示机制可用于推荐系统用户偏好挖掘**：论文中代理仅当规划违反隐藏约束时才收到反馈，这种按需揭露的方式可迁移至对话式推荐，动态获取用户隐式偏好，避免一次性询问过多问题。

  - **双重约束框架适用于电商场景的策略规划**：用户约束（如偏好、预算）和世界约束（如库存、物流）的分离建模，可作为多约束下商品组合、优惠券分发的决策训练范式。

  - **约束累积导致的性能衰退提示需设计健忘缓解策略**：实验表明代理在交互中期容易遗忘已揭示约束，推荐系统在多轮对话中同样需要维护约束记忆，可借鉴其显式约束追踪模块的设计，但需注意仅追踪仍不足以最终成功，还需配合重规划能力。

  - **用户约束的难度显著高于世界约束**：在推荐或Agent业务中，应更加注重用户偏好的建模与动态更新，例如引入专门的用户偏好消化模块，或对用户约束赋予更高优先级。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
现实中的规划任务（如家用任务、电商决策）常同时涉及环境限制（世界约束）与用户偏好（用户约束），且这些约束并非一次性完整给出，而是在交互中逐步暴露。现有基准多只关注单侧约束或静态设定，缺乏对双重约束下自适应重规划能力的系统评测。为此，本文提出 AdaPlanBench，一个面向家用领域的动态交互式基准，专门考察 LLM 代理在约束逐步揭示时的自适应规划能力。

## 方法
- **数据构造**：基于 MacGyver 数据集筛选 307 个家用任务，通过多智能体流水线为每个任务自动生成世界约束（工具不可用、空间限制等）和用户约束（偏好、厌恶等），并分成低/中/高三个难度级别。
- **交互协议**：代理每轮提出一个规划，约束法官判定是否违反隐藏约束，违反时才通过用户模拟器揭示具体约束，代理据此重规划，直至满足所有约束或触发终止（最大轮次或连续两轮无新约束被违反）。
- **评测指标**：最终规划准确率（Acc）、有效规划率（VPR）、平均轮次、重复违反率、触发约束密度等，并辅以规划质量的多维度评判（可行性、物理合理性、有效性、安全性）。

## 关键结果
- 在 Emid 设置下最强模型 GPT-5 准确率仅 67.75%，开源模型普遍低于 30%；重复违反约束频繁，平均 17.91% 的查询因连续重复违反而过早终止。
- 性能随约束密度上升显著下降，且交互后期规划质量滑坡明显。
- 用户约束带来的难度远大于世界约束，双约束组合最具挑战。
- 显式提供已揭示约束或给予维度级反馈仅微弱提升准确率，反而可能导致约束有效性下降。

> 当前 LLM 代理在逐渐展开的双重约束环境下可靠重规划仍极具挑战，纯记忆增强难以弥补能力短板。
