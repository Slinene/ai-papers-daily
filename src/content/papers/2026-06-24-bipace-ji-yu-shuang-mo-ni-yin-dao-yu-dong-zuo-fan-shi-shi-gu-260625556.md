---
title: 'BiPACE: Bisimulation-Guided Policy Optimization with Action Counterfactual
  Estimation for LLM Agents'
title_zh: BiPACE：基于双模拟引导与动作反事实估计的LLM智能体策略优化
authors:
- Hanyang Wang
- Weijieying Ren
- Yuxiang Zhang
- Ding Cao
- Zhizhao Zeng
- Ke Zeng
- Tianxiang Zhao
affiliations:
- University of Chicago
- Stanford University
- The Hong Kong University of Science and Technology (Guangzhou)
- University of Science and Technology of China
- Meituan
arxiv_id: '2606.25556'
url: https://arxiv.org/abs/2606.25556
pdf_url: https://arxiv.org/pdf/2606.25556
published: '2026-06-24'
collected: '2026-06-25'
category: Agent
direction: LLM Agent 训练 · 分组策略优化
tags:
- LLM Agents
- Reinforcement Learning
- Advantage Estimation
- Bisimulation
- Group-based RL
- Counterfactual
one_liner: 用双模拟聚类和动作反事实基线修复步进分组RL的状态-动作信用失配，将ALFWorld验证成功率从90.8%提升至97.1%
practical_value: '- 在训练对话式推荐、搜索 Agent 等多步决策模型时，可借鉴 BiGPO：使用 Actor 自身隐藏状态的余弦距离在线聚类，替代观测哈希，作为状态近似双模拟关系，大幅减少孤立组，增强组内信号，适用于并行采样多条轨迹的在线训练。

  - PACE 的动作反事实基线：在行为簇内用动作条件化的均值作为基线计算 Q(s,a)-V(s) 风格的优势，避免将状态价值误归因给动作，适用于推荐 Agent
  中相似状态下不同动作（如提问、推品）的精确信用分配。

  - 方法无额外 Critic 网络，只需存储 rollout 中的隐藏状态和分组信息，额外开销仅 11.3% 训练步长，工程实现轻量，可直接替换现有 stepwise
  GRPO/GiGPO 的优势估计器，提升长程任务成功率。

  - 限制：依赖多条并行轨迹构建分组，若系统仅支持单轨迹在线学习，需做适配；但批量离线训练或仿真交互场景可直接受益。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：步进式分组 RL（如 GRPO、GiGPO）训练 LLM Agent 时，假设组内步骤信用等价，但观测哈希分组过细导致大量孤立组（无梯度信号），而组内均值又混合了状态值与动作特定贡献，造成状态-动作信用分配失配。

**方法**：提出 BiPACE，即插即用无 Critic 优势估计器。BiGPO 用 Actor 自身隐藏状态的余弦距离聚类代替观测哈希，作为策略诱导的双模拟代理，显著降低孤立组比率；PACE 在每个行为簇内，用动作条件化的同伴基线重中心化回报，非参数估计局部 Q(s,a)-V(s)，分离动作级贡献。

**结果**：在 ALFWorld/Qwen2.5-7B 上，验证成功率从 GiGPO 的 90.8% 提升至 97.1%±0.9，且三个种子均超过 95%；在 Qwen2.5-1.5B 上从 86.7% 提升至 93.5%±1.2；在 WebShop 和 TextCraft 上同样显著改善。额外计算开销仅占单训练步 11.3% 墙钟时间。
