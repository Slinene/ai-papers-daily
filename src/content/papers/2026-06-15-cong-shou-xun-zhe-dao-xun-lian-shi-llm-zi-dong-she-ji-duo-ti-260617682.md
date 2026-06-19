---
title: 'From Trainee to Trainer: LLM-Designed Training Environment for RL with Multi-Agent
  Reasoning'
title_zh: 从受训者到训练师：LLM 自动设计多智体强化学习训练环境
authors:
- Chao Chen
- Chengzu Li
- Zhiwei Li
- Yinhong Liu
- Zhijiang Guo
affiliations:
- LARK, HKUST (GZ)
- University of Cambridge
- HKUST
arxiv_id: '2606.17682'
url: https://arxiv.org/abs/2606.17682
pdf_url: https://arxiv.org/pdf/2606.17682
published: '2026-06-15'
collected: '2026-06-19'
category: MultiAgent
direction: LLM 辅助多智体强化学习环境自动设计
tags:
- LLM
- Reinforcement Learning
- Multi-Agent
- Environment Design
- Curriculum Learning
- Failure Analysis
one_liner: 让当前策略 LLM 分析失败轨迹并自动提议下一阶段训练环境配置，小模型超越大模型
practical_value: '- **自适应环境工程**：借鉴 `LLM-as-Environment-Engineer` 范式，在推荐系统或搜索决策 RL
  训练中，将用户行为日志、推荐失败案例作为上下文，让模型自动调整仿真环境参数（如用户偏好分布、商品流行度），实现无需手工调参的课程学习。

  - **失败驱动优化**：验证了失败轨迹是最有效的环境更新信号；在业务 Agent 开发中，可周期性收集策略失败案例并结构化描述，让 LLM 生成下一次迭代的环境或训练数据修正，聚焦弱点针对性训练。

  - **小模型超越大模型**：发现当前 RL 微调后的 checkpoint 比原始基模型更适合做环境诊断；在资源受限的业务场景，可采用领域微调的小模型进行训练环境设计，成本更低且效果更好。

  - **上下文摘要工程**：文中使用的结构化总结（策略行为统计 + 失败案例 + 环境统计）可作为提示设计模板，用于任何需要 LLM 根据系统状态做决策的场景，如广告投放策略的自动调整。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：RL 训练 LLM 时，阶段间环境配置依赖手工调整，效率低且难以最优。提出让当前策略模型自动分析失败轨迹并设计下一阶段训练环境，减少人工干预。

**方法关键点**：
- 定义 `LLM-as-Environment-Engineer` 框架，用结构化的策略行为总结、失败案例和环境统计作为上下文，让 LLM 输出环境配置的修改指令。
- 引入可控测试床 MAPF-FrozenLake，公开多维环境配置参数，便于基准测试。
- 在 Qwen3-4B 骨干上迭代：环境工程师生成新配置 → RL 策略在新环境下训练 → 收集新的轨迹和统计，循环前进。

**关键结果**：
- Qwen3-4B 作为环境工程师，总体性能超越 GPT、Gemini 等大模型及固定环境基线。
- 有效的环境更新依赖失败证据，并保留已有的有效配置。
- 当前 RL checkpoint 比原始基模型更擅长环境诊断，说明策略学习可提升自我弱点分析能力。
