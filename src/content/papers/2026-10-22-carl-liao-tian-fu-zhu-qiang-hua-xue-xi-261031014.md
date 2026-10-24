---
title: 'CARL: Chat Assisted Reinforcement Learning'
title_zh: CARL：聊天辅助强化学习
authors:
- Sanjiv Das
- Harshad Khadilkar
- Sukrit Mittal
- Daniel Ostrov
- Jacob Sisk
affiliations:
- Santa Clara University
- Franklin Templeton
arxiv_id: '2610.31014'
url: https://arxiv.org/abs/2610.31014
pdf_url: https://arxiv.org/pdf/2610.31014
published: '2026-10-22'
collected: '2026-10-24'
category: Other
direction: LLM 辅助 RL 规范工程
tags:
- Reinforcement Learning
- LLM
- Human-AI Collaboration
- Specification Engineering
- Tool Use
- Reward Design
one_liner: 通过人机协同的十步规范工作流与自主工具循环，解决 RL 的规范与性能差距，避免奖励黑客和状态混叠
practical_value: '- 在推荐/广告的强化学习项目中，reward hacking 与状态混叠是常见翻车点。可借鉴 CARL 的“先交互式确认 MDP
  + 奖励项权重，再生成训练代码”流程，让业务专家在建模前明确状态、动作、约束及多目标权重，减少上线后目标漂移。

  - LLM 助手 persona + 步骤级 skill files 结构能引导非 RL 背景的业务/产品参与 RL 任务规范，适合内部自动化建模平台；紧凑决策摘要可跨迭代保留业务约束，避免长对话上下文过载，可直接复用到多轮需求澄清工具。

  - 自主工具循环（生成-测试-调试）加训练后诊断重访，适合封装成半自动 RL pipeline 工具，把算法工程师从工程实现中解放出来，聚焦奖励设计与业务验证。

  - 论文示例偏金融/控制，但工作流与 persona/skill 机制可迁移到电商强化学习系统的策略调试与参数治理。'
score: 7
source: arxiv-cs.HC
depth: abstract
---

**动机**：应用强化学习失败常源于两类差距——规范差距（专家意图被错误翻译为数学目标/约束/奖励）与性能差距（奖励项权重/超参选择不当、解无法验证）。

**方法**：CARL 采用人机协同设计接口，在代码生成前强制交互式规范，之后通过迭代进行验证和参数修改。每个迭代包含十步结构化工作流，使用步骤专用 skill files；助手 persona Trillian 提供领域感知建议；紧凑决策摘要跨迭代保留上下文且避免过载。专家确认 MDP 后，CARL 的自主工具循环自动生成、测试、执行并调试端到端 RL 训练管道；训练后支持诊断与重访，可在下一轮迭代前修改参数。

**结果**：在两个路径依赖优化领域（金融目标导向财富管理、航空航天动态压力约束 Goddard 火箭控制）验证，交互式规范工程解决了奖励黑客、状态混叠等关键失败模式，在完全自主代码生成失败处稳定产出可行策略。
