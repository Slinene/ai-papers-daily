---
title: 'MobileForge: Annotation-Free Adaptation for Mobile GUI Agents with Hierarchical
  Feedback-Guided Policy Optimization'
title_zh: MobileForge：移动 GUI 智能体的无标注适应与分层反馈策略优化
authors:
- Guangyi Liu
- Pengxiang Zhao
- Gao Wu
- Yiwen Yin
- Mading Li
- Liang Liu
- Congxiao Liu
- Zhang Qi
- Mengyan Wang
- Liang Guo
affiliations:
- Zhejiang University
- Kuaishou Technology
- Tsinghua University
arxiv_id: '2606.19930'
url: https://arxiv.org/abs/2606.19930
pdf_url: https://arxiv.org/pdf/2606.19930
published: '2026-06-18'
collected: '2026-06-20'
category: Agent
direction: 移动 GUI Agent · 无标注适应与策略优化
tags:
- Mobile GUI Agent
- Annotation-Free
- GRPO
- Hierarchical Feedback
- Curriculum Mining
- MLLM
one_liner: 提出无标注适应框架 MobileForge，通过分层反馈引导的步骤级 GRPO 将开源 MLLM 提升至接近闭源移动 GUI 智能体水平
practical_value: '- **无标注任务生成与课程挖掘**：通过探索真实 App 自动生成多样化任务，并按难度课程化，可在电商搜索/推荐 Agent
  的模拟环境搭建中复用，降低人工构造训练数据成本。

  - **步骤级过程反馈驱动优化**：HiFPO 将 rollout 结果、步骤级过程信号和纠正性提示联合用于策略更新，可借鉴到对话式推荐/导购 Agent 的强化学习训练，利用每轮对话的过程质量信号替代粗粒度成功/失败奖赏。

  - **GRPO 的 hint-contextualized 扩展**：将纠正提示作为上下文增强 GRPO 更新，可在 LLM 驱动的推荐解释生成或查询改写任务中，使用用户反馈（如点击、修改查询）作为
  contextual hint 进行在线策略改进。

  - **跨领域迁移能力验证**：在 AndroidWorld 适应后在 MobileWorld 仍有 41% 成功率，提示无标注适应可泛化到新 App 环境，对在多个电商平台或不同垂直领域的
  Agent 迁移有一定参考价值。'
score: 6
source: arxiv-cs.HC
depth: abstract
---

**动机**：多模态大语言模型（MLLM）在移动 GUI 智能体上已显著进步，但适配真实 App 仍需大量人工标注任务、演示或奖励。现有无标注方法缺乏统一框架连接目标 App 探索、课程挖掘、执行与反馈，策略优化多依赖孤立 rollout 和稀疏奖励，难以形成可靠提升信号。

**方法核心**：提出 MobileForge，包含两部分：
1) **MobileGym**：自动在真实移动 App 上生成任务并评估 rollout，提供无标注交互基础；
2) **HiFPO**（Hierarchical Feedback-Guided Policy Optimization）：将轨迹最终结果、步骤级过程反馈以及纠正性提示融合为 hint-contextualized 的步骤级 GRPO 更新。通过探索-课程挖掘-rollout-反馈的闭环，仅用自动生成的无标注数据完成智能体适应。

**关键结果**：用自动生成数据将 Qwen3-VL-8B 适配至 AndroidWorld 上的 67.2% Pass@3，接近闭源专用模型 GUI-Owl-1.5-8B 的 69.0%。进一步适配的 ForgeOwl-8B 达到 77.6% Pass@3，并在跨领域 MobileWorld GUI 子集上取得 41.0% 成功率，成为当前最强开源移动 GUI 智能体。
