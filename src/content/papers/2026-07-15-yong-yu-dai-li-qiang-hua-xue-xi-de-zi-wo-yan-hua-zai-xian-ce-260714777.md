---
title: 'SEED: Self-Evolving On-Policy Distillation for Agentic Reinforcement Learning'
title_zh: 用于代理强化学习的自我演化在线策略蒸馏
authors:
- Jinyang Wu
- Shuo Yang
- Zhengxi Lu
- Fan Zhang
- Yuhao Shen
- Lang Feng
- Haoran Luo
- Zheng Lian
- Shuai Zhang
- Zhengqi Wen
affiliations:
- Tsinghua University
- Zhejiang University
- The Chinese University of Hong Kong
- Nanyang Technological University
- Tongji University
arxiv_id: '2607.14777'
url: https://arxiv.org/abs/2607.14777
pdf_url: https://arxiv.org/pdf/2607.14777
published: '2026-07-15'
collected: '2026-07-17'
category: Agent
direction: 自我演化技能蒸馏 · 代理强化学习
tags:
- on-policy distillation
- reinforcement learning
- agent learning
- hindsight skills
- self-evolving
- LLM agent
one_liner: SEED通过从在线轨迹提取后见之明技能并蒸馏为密集token级信号，弥补了结果奖励与token策略之间的监督鸿沟
practical_value: '- 在训练对话式推荐或工具使用 Agent 时，可从在线轨迹自动提取成功模式/失败规则，蒸馏回策略，缓解稀疏奖励问题

  - 用当前策略作为技能分析器实现自我演化，辅助监督与策略分布同步更新，避免离线方案中的分布偏移

  - 技能增强的分数重计算（概率偏移）作为密集的 token 级蒸馏信号，可与 RL 损失联合优化，无需额外人工标注

  - 提升模型在未见场景的泛化能力，对搜索推荐 Agent 处理长尾查询或复杂对话有一定参考价值'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：LLM 作为交互代理执行长程任务时，基于结果的强化学习（RL）仅提供稀疏轨迹级奖励，对中间决策缺乏有效指导，导致学习困难。

**方法**：提出 SEED 框架，首先微调策略使其能分析完整轨迹并生成自然语言描述的“后见之明技能”，如可复用工作流、关键观察或避错规则。在 RL 过程中，当前策略同时负责收集轨迹和提取技能，实现技能随策略共同进化。训练时，对采样的动作在普通上下文和技能增强上下文下重新评分，将技能引起的概率偏移转化为密集的 token 级在线蒸馏信号。该信号与基于结果的 RL 损失联合优化，使辅助监督始终保持在当前策略的轨迹分布上。

**关键结果**：在多个基于文本和视觉的代理任务上，SEED 一致地提升了任务成功率和样本效率，并在未见过的新场景下表现出稳健的泛化能力，验证了方法在不同任务和模型规模上的有效性。
