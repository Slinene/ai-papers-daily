---
title: 'GAVEL: Graph World Models for Verified and Efficient Long-Horizon LLM Task
  Planning'
title_zh: GAVEL：用于验证与高效长程 LLM 任务规划的图世界模型
authors:
- Ruiyang Wang
- Hao-Lun Hsu
- Swarajh Mehta
- Jiwoo Kim
- Zhihao Dou
- Miroslav Pajic
arxiv_id: '2609.19315'
url: https://arxiv.org/abs/2609.19315
pdf_url: https://arxiv.org/pdf/2609.19315
published: '2026-09-15'
collected: '2026-09-22'
category: Agent
direction: Agent 长程规划验证与修复
tags:
- LLM Planning
- Graph World Model
- Verification
- Repair
- Embodied Agent
- Long-horizon
one_liner: 用显式图世界模型验证并修复 LLM 长程规划，将单任务成功率从 41.2% 提升至 91.8%
practical_value: '- 为 Agent 工作流构建显式状态图模型（对象关系、动作前置条件/效果），在执行 LLM 生成的业务步骤前做符号化执行验证，拦截不可行操作，减少线上执行失败。

  - 将规划错误分成两类：可由世界模型直接推导修复的缺陷（如缺失前置条件、约束违反）和需要语义推理的错误，只把后者回给 LLM，降低高成本模型调用频率。

  - 用概率信念状态表示不确定信息（如库存、用户状态），在多步骤任务中动态重排剩余子任务以最小化期望成本，适用于多目标营销流程或客服工单调度。

  - 用紧凑 LLM（如 Qwen3-8B）搭配显式世界模型即可显著提升长程任务成功率，适合边缘部署或成本敏感的业务场景。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：长程机器人规划中，LLM 生成的计划常违反具身约束、难以从错误恢复，且在部分可观测环境下推理不足。

**方法关键点**：GAVEL 围绕显式图世界模型构建验证与修复机制。图中编码对象关系、动作前置条件/效果，以及未观测对象位置的概率置信分布。该模型在 LLM 生成动作后先预测后果、检测违规，并直接修复可由世界模型推导的缺陷；只有需要语义推理的错误才触发 LLM 重规划。多任务指令下，GAVEL 基于对象位置分布推理，重排剩余子任务以最小化期望搜索成本。

**关键结果数字**：在 BEHAVIOR-1K 上，用 Qwen3-8B，单任务成功率从 41.2% 提升到 91.8%，多任务成功率从 19.9% 提升到 92.6%；分布置信推理比静态变体降低约 5.4% 移动距离。
