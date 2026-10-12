---
title: Recurrent Harness for Agentic Continual Learning
title_zh: 循环式 Harness 实现智能体持续学习的反向修订
authors:
- Yuxin Xiao
- Zhiyun Lu
- Jianyu Wang
- Yangtian Zhang
- Yang Song
- Qifan Wang
- Bailin Wang
affiliations:
- Massachusetts Institute of Technology
- Meta MRS Research
- Yale University
arxiv_id: '2610.12668'
url: https://arxiv.org/abs/2610.12668
pdf_url: https://arxiv.org/pdf/2610.12668
published: '2026-10-07'
collected: '2026-10-12'
category: Agent
direction: Agent 持续学习 · 在线反思修订
tags:
- Agentic Continual Learning
- Reflection Revision
- Online Streaming
- Memory
- Textual Feedback
- Harness
one_liner: 在流式持续学习中用下游反馈反向修订已检索反思，闭合前向读写循环，显著提升智能体在线适应与稳定性
practical_value: '- 在电商/搜索推荐的在线 Agent 策略记忆中引入“反向修订”：发现某条策略反思（如“高点击低转化商品应降权”）在新场景失效时，不直接删除，而是用当前交互结果作为反馈修正其适用条件，并要求修订内容只基于原策略来源轨迹，防止未来信息泄漏；这能避免过时规则反复误导后续排序/query
  决策。

  - 严格在线无验证集/无 replay 场景下，反思摘要比原始轨迹更省 token；建议 top-k 取 5 左右，过多修订会导致 reflection drift
  且成本上升。电商活动切换时可优先使用该类机制，同时用 stability/plasticity 分解评估切换后第一轮（无反馈）与后续轮次表现。

  - 复用“修订后的旧反思作为 demonstration 引导新反思生成”的技巧：在线学习时先修正旧经验再写新策略，能让新策略带上更精确的适用条件（例如“只在促销季生效”），减少过度泛化。'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
LLM agent 在处理长期交互流时，需在不更新参数、严格在线流式协议下适应分布漂移。现有 harness 通常只有前向信息流：写入 memory/reflection 后很少根据后续有效性修订；离线优化又依赖额外验证集或 replay，违背在线流式限制。过时或过度泛化的 reflection 会持续误导后续决策。

### 方法关键点
- ReHarness 在传统 forward read/write 之外引入 backward revision，闭环前向与反向路径。
- 每实例流程：Forward Read 检索 top-k 相关 reflection；Backward Revision 用当前轨迹 τ_t 作为反馈修订每个检索到的 reflection R_i，但要求新内容必须 grounded 在源轨迹 τ_i，防信息泄漏；Forward Write 以修订后的 reflections 作为 demonstrations 生成新 reflection。
- 完全文本空间反馈，无梯度、无实例 replay、无验证集，适合 API-only 前端模型。
- 使用 compact reflection 降低决策上下文 token；检索用 Qwen3-Embedding-8B，k=5。

### 关键实验
在 CL-Bench、MemoryBench、MemoryArena 三个持续学习基准（16 个任务），配合 Claude Opus 4.8、GPT-5.5、Gemini 3.7 Flash 三个 backbone，与 Mem0、RBank、DoT、ACE、GEPA-Online、Top-K Raw、Full Raw 对比。
- 平均 normalized gain：ReHarness 0.240，高于所有 baseline；9 个 backbone-benchmark 组合中 8 个第一或并列。
- 统计显著优于最强 raw-context baseline（Top-K Raw p_adj=0.039，Full Raw p_adj=0.043）。
- 修订源 grounded 率 >95%，泄漏率 0.8-2.1%；counterfactual replay 确认修订有实质意义。
- 在稳定性与塑性分解上均最高；token 消耗约为 Full Raw 的 1/3.4，成本低于 Full Raw 且增益更高。
- top-k 扫描显示 k=5 已足够，更大 k 带来边际收益下降和 reflection drift。

### 最值得记住的一句话
> 在严格在线流式协议下，用当前实例的下游结果作为反馈反向修订先前检索到的反思，并强制修订内容只基于源轨迹，可以为无参数更新的 agent 持续学习提供有效且鲁棒的文本记忆更新闭环。
