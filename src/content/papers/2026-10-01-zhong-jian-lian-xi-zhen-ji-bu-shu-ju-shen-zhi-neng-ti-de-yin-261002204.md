---
title: 'Reconstruct, Practice, Go Real: Guided Self-Improvement for Embodied Agents'
title_zh: 重建、练习、真机部署：具身智能体的引导式自我改进
authors:
- Yen-Jen Wang
- Haozhe Jiang
- Shuying Deng
- Haoru Xue
- Weirui Ye
- Rocky Duan
- Nika Haghtalab
- S. Shankar Sastry
- Pieter Abbeel
- Haozhi Qi
affiliations:
- UC Berkeley
- Amazon FAR
- MIT
- University of Chicago
arxiv_id: '2610.02204'
url: https://arxiv.org/abs/2610.02204
pdf_url: https://arxiv.org/pdf/2610.02204
published: '2026-10-01'
collected: '2026-10-04'
category: Agent
direction: 具身智能体自我改进
tags:
- Self-Improvement
- Embodied Agent
- Skill Library
- Prompt Revision
- Sim-to-Real
- Multimodal LLM
one_liner: RPG 不更新模型权重，在仿真中重构练习任务并自我改进技能与提示，22 项操作成功率从 28.6% 提升至 95.0%
practical_value: '- 借鉴“不更新权重、用可复用符号技能库 + 系统提示修订”的固化系统做法：在电商 Agent 中把高频操作抽象成工具/skill，LLM
  只负责调度和组合，降低每次推理成本与非确定性。

  - 用“执行反馈 + 离线日志重构练习任务”做自举：从历史成功/失败会话中自动生成回归任务和仿真环境，每次修改 prompt 或 skill 前先在跨任务集上评估，避免局部过拟合。

  - 借鉴“候选变更先单测、再合并回归”的变更管理：对 prompt 模板、工具定义、规则库做 A/B 和 cross-task evaluation，只保留被验证有效的修订，形成
  Agent 系统的 CI/CD。

  - 具身/机器人特有的 privileged simulator state 与 sim-to-real calibration 在电商场景不可直接复用；主要价值在于自我改进流程、技能复用与跨任务验证机制。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

## 动机
构建跨任务可靠的机器人能力通常需要大量人工：开发技能、设计奖励、集成感知与控制。RPG 面向无需更新模型权重的自主改进，减少人工维护成本。

## 方法关键点
RPG 分为三步：

- **Reconstruct**：从离线数据集识别可操作能力，并构建相关仿真练习任务。
- **Practice**：利用执行反馈、仿真器特权状态和可用数据集视频诊断失败；据此开发新的可复用符号技能、优化现有技能、修订系统提示。所有候选变更先做跨任务评估，测试单个变更和合并后的修订，通过后才保留复用。
- **Go Real**：系统经统一标定和硬件适配后冻结部署。测试时，多模态 LLM 根据系统提示和技能库协调感知与控制。

## 关键结果
在 22 个操作任务的 held-out initializations 上，第一轮练习后成功率 28.6%，15 轮后达 95.0%，超过 ASPIRE 的 75.5% 和 GPT-6 Astra Pro 驱动的 CaP-Agent0 的 60.0%。经统一标定与硬件适配后，冻结系统在 30 次真实机器人试验中全部成功，覆盖 3 个任务各 10 次。
