---
title: 'NeutronGym: Physics-Graded Neutron Instrument Design for LLM Agents'
title_zh: NeutronGym：面向 LLM Agent 的物理分级中子仪器设计环境
authors:
- Lijie Ding
- Changwoo Do
affiliations:
- Oak Ridge National Laboratory
arxiv_id: '2610.03631'
url: https://arxiv.org/abs/2610.03631
pdf_url: https://arxiv.org/pdf/2610.03631
published: '2026-10-02'
collected: '2026-10-05'
category: Agent
direction: LLM Agent 科学仪器设计与 RL 训练环境
tags:
- LLM Agent
- Reinforcement Learning
- Reward Design
- Simulation
- Benchmark
- MCP
one_liner: 首个可执行中子仪器设计环境，用无 LLM 评判的物理分级奖励训练 8B 模型超越未训练 32B
practical_value: '- 奖励塑形：把最终业务指标拆成可验证的中间层（输入合法→系统可执行→返回结构完整→业务指标达标），每层给部分信用。文中去掉部分信用导致
  pass rate 从 76.7% 暴跌至 16.7%，说明密集课程式奖励是 RL 稳定训练的关键，推荐 Agent 做 RL 时不要只用稀疏 GMV/转化作奖励。

  - 防 reward hacking 的 no-model 基线：上线前用固定答案、读题规则、跨实例迁移三种 probe 检测任务是否可被捷径破解。对应电商场景应先跑规则基线（热门、复制
  prompt 限制、历史均值），避免把“背答案”当成模型能力。

  - 工具调用前置校验：22 个工具在调用时即校验组件与参数合法性，把编译错误前置到工具层。Agent 链路中应对每个工具输入做 schema 校验并返回最近合法选项，减少多轮失败和无效探索。

  - 不要只用成功样本做 SFT：克隆自己成功轨迹的模仿学习在文中让 pass rate 从 40.3% 跌到 31.3%，而 on-policy RL 训练包含失败轨迹效果更好。推荐
  Agent 微调时应保留失败探索轨迹做 RL，避免只喂高转化样本导致分布偏移。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

**动机**  
科学仪器设计要求把规格转化为物理布局，在多个约束间权衡，质量由物理测量而非参考答案决定。中子散射仪器是合适测试床：McStas 仿真速度快、可定量观测，且被动光学守恒律提供参考无关的强度上限。但用模拟器做 LLM Agent 训练面临奖励 hack、基准污染和退化任务三个坑：奖励可被意外满足、模型可能背下公开参考设计、生成的任务可能被固定答案或读题规则破解。

**方法关键点**  
- 环境：通过 MCP 暴露 22 个验证工具，Agent 只能通过这些工具搭建、仿真、读取统计，不能写文件或跑 shell；每次变更调用时校验，编译错误前置。  
- 奖励阶梯：L1 语法/边界、L2 短运行完成、L3 结构（≥500 事件、带约束、相空间上限）、L4 科学指标；每层 0.25 信用，L4 按余量加分，上限 1.25，无 LLM judge。  
- 任务：程序化 families 固定布局、改变数值参数，提供无限实例和 disjoint held-out regimes；McStasBench 含 16 个重建/改进任务，带记忆探针、扰动变体和两个未公开 held-out 仪器。  
- 训练：GRPO 在 300 训练实例的每步状态上训练，包含失败轨迹；对比 SFT 克隆成功轨迹。

**关键结果**  
McStasBench 上最好模型 Claude Sonnet 5 单次完成 7/16，工具循环 5/16，无检索参考，无人达到改进目标；Qwen 无工具时无法生成可解析仪器。RL 将 Qwen3-8B 在 guide match held-out 从 11.3% 提升到 76.7%，超越未训练 32B，第二 seed 69.0%，在四个 gated families 均超过 32B。移除阶梯部分信用 collapse 到 16.7%（下降 60 点）；经典优化器拿到闭式物理达 81.0%，trained 76.7%（不显著），前沿模型零样本 98-99%。模仿自身成功 SFT 从 40.3% 降到 31.3%。

**最值得记住的一句话**  
奖励塑形决定了 RL 能否在小模型上训练；无模型基线和任务准入门槛是防止把捷径当成能力的必要条件。
