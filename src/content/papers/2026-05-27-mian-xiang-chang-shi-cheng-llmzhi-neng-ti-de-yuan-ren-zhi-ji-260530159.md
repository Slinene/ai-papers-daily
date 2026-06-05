---
title: Meta-Cognitive Memory Policy Optimization for Long-Horizon LLM Agents
title_zh: 面向长时程LLM智能体的元认知记忆策略优化
authors:
- Ziyan Liu
- Zhezheng Hao
- Yeqiu Chen
- Hong Wang
- Jingren Hou
- Ruiyi Ding
- Yongkang Yang
- Wence Ji
- Wei Xia
- Feng Liu
affiliations:
- University of Science and Technology of China
- Zhejiang University
- Tencent
arxiv_id: '2605.30159'
url: https://arxiv.org/abs/2605.30159
pdf_url: https://arxiv.org/pdf/2605.30159
published: '2026-05-27'
collected: '2026-06-05'
category: Agent
direction: 记忆策略优化 · 元认知信念熵
tags:
- Memory-Augmented Agents
- Belief Entropy
- Reinforcement Learning
- Long-Horizon Reasoning
- POMDP
one_liner: 用信念熵(Belief Entropy)为中间记忆状态提供密集监督，解决长期记忆压缩的信用分配问题
practical_value: '- 电商对话助手、推荐Agent等长交互场景可借鉴：用**信念熵**为记忆压缩步骤提供中间反馈，替代仅依赖最终结果的稀疏奖励，缓解“不知哪个总结环节出错”的信用分配问题。

  - 设计**锚定探测问题**（如“基于当前记忆，任务进展如何，还缺什么信息？”），通过模型响应熵来量化记忆清晰度，可作为模块化奖励信号插入已有记忆策略训练中。

  - 奖励构造方式可复用：将信念熵经sigmoid归一化为(0,1)奖励，再与最终任务奖励相加，实现放缩匹配与数值稳定；训练采用**群组相对优势估计**（GRPO风格），免学值函数，适合快速实验。

  - 工程启发：推理时可用信念熵做**最佳记忆轨迹的筛选**，不额外训练即可提升性能；训练开销仅增加约12%，推理时可选关闭，适合在线系统。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
长时程LLM智能体需要将交互历史递归压缩成紧凑记忆。现有方法通过最终结果奖励（RLVR）训练记忆策略，但稀疏反馈无法定位哪一步压缩引入了语义噪声，导致信念偏离累计，最终推理崩溃。本文从部分可观测马尔可夫决策过程（POMDP）视角出发，指出记忆优化的本质是**保存摘要诱导的信念清晰度**，而非仅看最终成功。  

**方法**  
1. **信念熵 (Belief Entropy)**：设计锚定问题（如“基于当前记忆，任务进展与仍缺信息？”），让LLM基于记忆作答，计算响应熵。熵低表示记忆对任务状态表达清晰，熵高表示模糊或有噪声。  
2. **MMPO训练**：每步计算记忆的信念熵，经sigmoid变换得到密集奖励，与最终结果奖励加和；在轨迹组内标准化得到轮次级别优势，再用PPO更新记忆策略。这样既保留结果锚定，又为中间质量提供了细粒度信号。  

**实验结果**  
- 在RULER-HotpotQA极端长上下文测试中（7B/14B模型），MMPO相对RL-MemAgent平均提升约3.1%准确率，在896K长度下最大提升+5.47%。  
- 在MEM1框架的多目标QA和WebShop任务中同样超越原基线，说明监督信号兼容不同记忆框架且适用于交互式决策。  
- 信念熵动力学显示成功轨迹持续下降，失败轨迹停滞或上升，且熵降幅与最终任务准确率高度相关（Pearson r=−0.68）。  

**核心洞见**：保存清晰的记忆信念，比单纯追求最终成功，更能稳定长时程推理。
