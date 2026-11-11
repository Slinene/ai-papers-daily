---
title: 'Auriga Technical Report: A Task-Agnostic Agent Harness for Zero-Shot Embodied
  Manipulation'
title_zh: Auriga：面向零样本具身操作的任务无关智能体框架
authors:
- Chengcheng Wang
- Yuheng Shi
- Siyu Xu
- Yutong Wang
- Jinjing Zhao
- Chenghao Xia
- Jinqi Liao
- Jiankun Peng
- Ligong Bi
- Yuechuan Ma
affiliations:
- StellarEdge AI Technical Team
arxiv_id: '2611.01112'
url: https://arxiv.org/abs/2611.01112
pdf_url: https://arxiv.org/pdf/2611.01112
published: '2026-10-30'
collected: '2026-11-11'
category: Agent
direction: 具身智能 Agent 控制框架
tags:
- Agent Harness
- Zero-Shot
- VLM
- Tool Use
- Planning-Execution Gap
one_liner: 提出任务无关的Agent harness，解耦规划与执行并引入预览校验，零样本操作成功率RoboDojo第一
practical_value: '- **规划与执行解耦**：LLM/VLM 只负责高层任务决策与工具调用/代码生成，执行由 harness 提供校准的 3D 测量、统一入口和底层控制；电商
  Agent 可借鉴，将 LLM 生成的 SQL/查询/策略先经过校验层再执行，避免模型直接产出底层动作导致误差。

  - **执行前预览验证**：在真实执行前，利用仿真/沙箱环境让模型检查视觉轨迹预览或中间结果，提前发现错误；推荐/广告 Agent 可对生成的召回策略、排序逻辑或文案先做离线模拟或小流量预览，降低线上风险。

  - **执行中容差检查与原地恢复**：为每个阶段设定明确的数值容差或边界，检测到偏差即停止执行并返回差异，支持原地修正；在出价 Agent、搜索改写 Agent
  中可设置 CTR 偏差阈值、预算上限等断路器，避免错误持续放大。

  - **跨任务能力迭代而非场景调参**：开发阶段只用失败来改进通用感知、控制与校验工具，不针对固定场景反复调参；推荐 Agent 评估时应避免在固定测试集上过度调优，保持泛化能力。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：VLM 能理解指令做高层规划，但直接作为机器人策略执行时性能骤降。RoboDojo 上移除手臂执行后，GPT-6 Astra 成功率从 22.5% 升至 76.2%，暴露出明显的计划-执行鸿沟。零样本、无目标任务试错条件下缩小这一鸿沟是核心挑战。

**方法**：Auriga 是一个任务无关的 Agent harness，将高层决策与物理执行解耦。模型在显式任务信念上做决策，通过直接工具调用或合成多步 Python 程序行动；harness 提供校准的 3D 测量、手指参考双臂控制和单一准入网关。运动前，模型在仿真暂停时检查视觉轨迹预览；执行中，harness 校验声明的阶段容差和抓取边界，一旦发散即停止机器人并返回测量差异，支持原地恢复。开发过程经历 13 个跨任务能力迭代并冻结评估。

**结果**：在 RoboDojo leaderboard 上，Auriga 以 57.7% 成功率（64.0 Score）排名第一，比同模型参考 harness 翻倍以上；场景随机化下仍保持第一，而学习策略最多下降 33.9%。在 RoboCasa365 上，同一冻结 harness 达到 73.2% 成功率，复合任务上比 VLA 辅助智能体最高超出 23.1%。
