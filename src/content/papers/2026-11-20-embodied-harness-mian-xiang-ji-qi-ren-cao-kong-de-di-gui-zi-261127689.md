---
title: 'Embodied-Harness: Towards Recursive Self-Improvement for Robotic Manipulation'
title_zh: Embodied-Harness：面向机器人操控的递归自改进框架
authors:
- Zhenxuan Fan
- Zhuoya Wang
- Yuqian Yuan
- Wenqiao Zhang
- Juncheng Li
- Jun Xiao
- Siliang Tang
- Yueting Zhuang
affiliations:
- Zhejiang University
- Huazhong University of Science and Technology
arxiv_id: '2611.27689'
url: https://arxiv.org/abs/2611.27689
pdf_url: https://arxiv.org/pdf/2611.27689
published: '2026-11-20'
collected: '2026-11-23'
category: MultiAgent
direction: 多智能体协作 · 具身自改进
tags:
- VLM Agent
- Multi-Agent
- Reflection
- Memory Architecture
- Self-Improvement
- Robotic Manipulation
one_liner: 提出双智能体框架，通过层次化记忆与基于证据的反思实现无参数更新的递归自改进，显著提升机器人操控成功率
practical_value: '- **双智能体分工**：执行 Actor 与反思 Reflector 分离，电商推荐 Agent 可将决策与评估/归因解耦，避免同一模型既做动作又做评判导致偏差，提升策略迭代的客观性。

  - **层次化记忆架构**：短期工作记忆存执行轨迹、长期经验记忆存跨任务知识，可借鉴用于推荐 Agent 维护用户会话上下文（短期）与历史策略成功经验（长期），增强个性化与复用。

  - **基于证据的失败归因**：Reflector 依据环境交互证据（如碰撞、方向错误）定位失败原因，而非凭空猜测；推荐系统调试中可引入真实用户反馈（点击、转化）进行归因分析，提高策略优化效率。

  - **无参数更新自改进**：通过 refine harness/guidance 而非重训模型实现迭代提升，适合 LLM 推荐 Agent 的低成本在线优化，如更新
  prompt 模板或策略库，避免频繁训练大模型。'
score: 6
source: arxiv-cs.CV
depth: abstract
---

**动机**：基于 VLM 的机器人操控 Agent 受限于记忆组织不当、失败归因不确定和执行经验复用不足，难以在复杂环境中稳定泛化。

**方法关键点**：提出 Embodied-Harness 双智能体框架，不更新模型参数，通过改进执行 harness 实现自改进。Actor 通过机器人控制接口与环境交互，Reflector 将执行证据转化为可重用的操作指导。引入层次化记忆架构：短期工作记忆保留执行上下文，长期经验记忆存储跨任务知识。基于证据的经验反思从观测交互中定位失败原因，递归 harness 自改进在多次尝试中逐步精化操作指导。

**关键结果数字**：在 RoboTwin 2.0、RoboSPA、RMBench 三个基准上成功率分别达到 82.4%、76.7%、94.4%，显著超越对比方法；真实世界三项操作任务平均成功率 96.7%。
