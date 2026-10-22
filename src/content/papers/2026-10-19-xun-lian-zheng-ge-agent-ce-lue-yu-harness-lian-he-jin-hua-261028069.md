---
title: Training the Whole Agent, Not Just the Model
title_zh: 训练整个 Agent：策略与 Harness 联合进化
authors:
- Lingxiao Tang
- Wei Tao
- Yiwen Guo
- Lingfeng Bao
affiliations:
- Zhejiang University
- LIGHTSPEED
- Independent Researcher
arxiv_id: '2610.28069'
url: https://arxiv.org/abs/2610.28069
pdf_url: https://arxiv.org/pdf/2610.28069
published: '2026-10-19'
collected: '2026-10-22'
category: Training
direction: Agent 训练 · RL 联合优化工具/hooks
tags:
- Reinforcement Learning
- Agent Harness
- Tool Evolution
- GRPO
- SWE-bench
- Coding Agent
one_liner: HarnessAdapt-RL 在强化学习中同时训练策略模型与工具/hooks，显著提升 coding agent 的 pass@1
practical_value: '- 搜索/推荐 Agent 训练不应只更新 LLM 参数，可将工具描述、hooks、检索接口等视为可学习组件，在 RL 中与策略共同迭代；尤其适合电商
  Agent 中 API 调用、query 改写、商品召回等工具链的联合优化。

  - 借鉴其变更接受条件：每个工具/hook 变更只有在离线评估中提升 pass rate 或可训练率且不降低另一方才保留。业务上可对应“商详页点击率/转化率提升，同时训练样本有效率不下降”的门控机制。

  - 任务特定的机制级技能可由 frozen teacher 生成，训练时注入引导，上线前移除，降低部署复杂度，同时保留策略泛化增益；适合将专家规则或人工 SOP
  转化为训练期辅助信号。

  - 对反复出现的交互问题（如失败重试、上下文截断、工具返回格式错误）可进化 tools/hooks 而非硬编码，并让策略学习与新 harness 协调，避免过早冻结早期版本的优化陷阱。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：coding agent 训练通常固定 harness 只更新 policy，但训练轨迹会暴露因任务而异、且随策略学习变化的修复策略缺陷与跨任务交互问题，固定的 harness 会限制最终性能。

方法关键点：HarnessAdapt-RL 在强化学习中同时训练 policy 和 harness。针对修复策略缺陷，冻结的 teacher 模型生成任务特定的机制级技能；针对跨任务反复出现的交互问题，单独的 teacher 模型进化 tools 和 hooks，每项变更仅在提升观察到的 pass rate 或 trainable rate、且不降低另一方时保留。policy 使用适配后的 harness 训练，新轨迹再指导进一步适配，形成策略与 harness 的协同迭代。

关键结果：9B 基础模型上，HarnessAdapt-RL 在 SWE-bench Verified、Multilingual、Pro 的 pass@1 分别比 GRPO 提高 9.8、12.6、6.4 个百分点，并优于使用人工设计 OpenHands harness 的 GRPO。机制级技能在评估时移除后增益仍存在；随策略变化重进化 tools/hooks 优于冻结早期版本；部署时移除这些进化组件最多损失 7.7 个百分点。最终产物是「训练后的 policy + 进化的 tools/hooks」，技能在部署时移除。
