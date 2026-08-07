---
title: 'EnvACE: Internalizing Environment Dynamics via World Rehearsal for Agentic
  Reinforcement Learning'
title_zh: EnvACE：通过世界排练内化环境动力学用于智能体强化学习
authors:
- Zishan Xu
- Zhiyuan Yao
- Yuxin Chen
- Yifu Guo
- Zhengxi Lu
- Yuquan Lu
- Jinyang Huang
- Yan Xu
- Yasheng Wang
- Weinan Zhang
affiliations:
- Shanghai Jiao Tong University
- Zhejiang University
- National University of Singapore
- Sun Yat-sen University
- Tencent Inc.
arxiv_id: '2608.06197'
url: https://arxiv.org/abs/2608.06197
pdf_url: https://arxiv.org/pdf/2608.06197
published: '2026-08-05'
collected: '2026-08-07'
category: Agent
direction: Agent强化学习 · 世界模型内化
tags:
- World Rehearsal
- Agentic RL
- LLM Agent
- Tool Use
- World Model
- Test-Time Scaling
one_liner: 让策略自身扮演环境生成响应，内化交互动力学，实现不依赖外部环境的智能体RL训练
practical_value: '- **训练范式迁移**：将环境响应生成的角色交给策略自身，省去构建昂贵的外部仿真环境。对于电商工具调用 Agent（查询库存、下单、修改订单）的训练，可直接用历史交互数据让模型同时学习“动作+响应”，大幅降低环境搭建成本。

  - **角色明智 GRPO**：对 acting 和 rehearsal 两个角色分别计算基线，但共享参数梯度更新。电商 Agent 训练时可将用户模拟、工具返回模拟作为
  rehearsal 角色，与真实 action 角色联合优化，让策略更深刻理解交互因果关系。

  - **测试时安全排练**：在正式执行前，策略内部进行多次“想象推演”，汇总反馈后指导实际动作。适用于高风险场景（如退款、取消订单、修改支付方式），提前预测错误并修正参数，避免真实环境错误操作。

  - **数据效率提升**：世界排练允许在无外部反馈的条件下持续改进策略，可在离线数据上预训练 Agent，或结合少量真实交互微调，提升 RL 样本效率。'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有 LLM 智能体训练常依赖真实环境或外部模拟器进行交互，真实环境构建成本高、扩展困难，外部模拟器响应可能不准确且仍需真实环境监督。本文提出 EnvACE，通过“世界排练”让策略自身扮演环境角色，在训练时无需外部环境即可生成交互轨迹，将环境动力学内化到策略参数中。

### 方法关键点
- **世界排练**：策略交替扮演演员（生成工具调用等动作）和排练者（预测环境响应），生成的响应直接拼接到交互历史中，使轨迹自我展开而不依赖外部环境。
- **角色明智 GRPO 优化**：对同一指令采样 K 条完整轨迹，每条轨迹中所有输出继承同一个任务奖励；为 ACT 和 REHEARSE 两个角色分别计算基线，角色内归一化计算优势，共享策略参数进行联合更新。
- **测试时扩展**：在真实执行前，策略进行 N 次排练尝试（并行或顺序），生成想象轨迹和自评估反馈，汇总成排练记忆以指导单次提交执行，避免不当操作。

### 关键实验
在四个多轮工具交互基准（BFCL V4、τ2-Bench、VitaBench、FinMCP-Bench）上评估。EnvACE-8B 在三基准综合得分 32.91%，超过 EnvScaler-8B（31.92%）和 AWM-14B（32.54%）；FinMCP-Bench 上 TF1 达 46.78% 最高。消融显示世界排练较标准 GRPO 在 τ2-Bench 上平均提升 5.5 个百分点（31.2→36.7），参数共享比分离策略提升 1.2 个百分点。测试时排练使 τ2-Bench 平均从 31.4% 升至 38.0%（N=2 并行）。模型规模从 1.7B 扩展到 8B 时增益保持。

> 核心思想：**让策略自己扮演环境，内化动作-响应间的因果关系，从而实现在无外部环境下的高效 RL 训练和测试时安全增强。**
