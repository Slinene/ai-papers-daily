---
title: 'VIG-RL: Learning to Search and Insert for Verified Image Grounding'
title_zh: VIG-RL：用强化学习学习搜索与插入以验证图像基础
authors:
- Qinhan Yu
- Jun Guang
- Chong Chen
- Wentao Zhang
affiliations:
- Peking University
- Huawei Cloud BU
arxiv_id: '2607.28055'
url: https://arxiv.org/abs/2607.28055
pdf_url: https://arxiv.org/pdf/2607.28055
published: '2026-07-30'
collected: '2026-08-02'
category: Agent
direction: Agent 强化学习动态搜索插入图文证据
tags:
- Agent
- Reinforcement Learning
- Multimodal
- Image Grounding
- ReAct
- Retrieval-Augmented Generation
one_liner: 将验证性图像基础建模为动态决策过程，用强化学习优化搜索-选择-插入的 agent 循环
practical_value: '- 电商商品文案生成中，可借鉴动态决策何时检索并插入商品实拍图或证照截图，提升可信度与转化率。

  - 强化学习驱动的多步 agent 决策（何时搜、选哪张图、插在何处）可迁移到购物助手主动补全多模态信息。

  - 复合奖励（步骤级工具使用评价 + 最终图文对齐）可用于优化推荐解释生成中的多工具调用组合。

  - ReAct 式动作-观察循环可集成搜索工具，在对话推荐中自适应地引入外部证据（如用户评价截图、商品对比图）。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：在知识密集型场景中，生成可信的图文交错回答要求精确插入检索到的真实视觉证据（验证性图像基础，VIG）。现有方案依赖静态解耦的检索-生成管線，无法动态判断何时需要外部知识、图像应插在何处，导致图文失配或缺乏事实支撑。

**方法**：提出 VIG-RL，一个自主 agent 框架，将搜索-选择-插入流程形式化为主动决策过程。agent 在 ReAct 风格循环中运行，通过强化学习优化，奖励机制综合评估每一步的工具执行质量以及最终的多模态对齐度，从而学习最优的搜索时机与插入位置策略。

**结果**：VIG-RL 在验证性图像基础任务上全面超越现有静态基线，达到新的最佳性能，验证了动态决策与强化学习联合优化的有效性。
