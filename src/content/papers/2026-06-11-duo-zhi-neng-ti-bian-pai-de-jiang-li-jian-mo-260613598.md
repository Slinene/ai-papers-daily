---
title: Reward Modeling for Multi-Agent Orchestration
title_zh: 多智能体编排的奖励建模
authors:
- King Yeung Tsang
- Zihao Zhao
- Vishal Venkataramani
- Haizhou Shi
- Zixuan Ke
- Semih Yavuz
- Shafiq Joty
- Hao Wang
affiliations:
- Rutgers University
- Salesforce AI Research
arxiv_id: '2606.13598'
url: https://arxiv.org/abs/2606.13598
pdf_url: https://arxiv.org/pdf/2606.13598
published: '2026-06-11'
collected: '2026-06-12'
category: MultiAgent
direction: 多智体编排 · 奖励建模
tags:
- Reward Modeling
- Multi-Agent
- Orchestration
- Test-Time Scaling
- Bradley-Terry
- GRPO
one_liner: 提出编排级奖励模型 Orch-RM，用自监督偏好对训练，无需人工标注和子 Agent 全量执行，显著提升测试时缩放和编排器训练的效率与效果
practical_value: '- **编排级奖励信号直接用于推理**：Orch-RM 在编排层面评分，无需执行子 Agent 即可选择最优编排方案，将 BrowseComp
  验证成本从 142.8M token 降至 8.26M，准确率还提升 1.5%。电商多 Agent 场景（如客服路由、推荐流程编排）可借鉴，在低延迟要求下用轻量奖励模型筛选高质量协作图。

  - **利用训练中间产物构造偏好对**：从训练检查点和轨迹中自动构造“专用优于基础”和“正确优于错误”两类偏好对，无需人工标注。业务中若已有多 Agent 训练日志，可直接复用该自监督构造方法，大幅降低评估器标注成本。

  - **奖励模型指导继续训练**：Orch-RM 替代全轨迹 GRPO 的稀疏奖励，在 AIME 24&25 上使用约 1/10 的训练 token 取得 3%
  的 majority vote 提升，BrowseComp 上更以 1/46 token 量实现 2% 提升。对于需要频繁迭代的编排策略模型，可大幅节省训练算力。

  - **域特定奖励模型可迁移**：论文训练了数学、Web QA 等域特定奖励模型，并在 GPQA（科学推理）上验证了跨域泛化能力。电商多域（推荐、搜索、客服）可分别训练编排评估器，或探索多域融合的统一奖励模型，降低重复训练成本。'
score: 9
source: arxiv-cs.LG
depth: full_pdf
---

**动机**  
多智能体系统（MAS）的性能高度依赖编排器的质量，但训练编排器面临两大瓶颈：① 编排策略与任务、子 Agent 能力强耦合，高质量人工标注几乎不可得；② 现有 RL 训练（如 MAS-Orchestra）需要执行完整的子 Agent 轨迹，计算开销极大（100 步更新消耗 10 亿 token）。此外，在测试时通过 self-consistency 等缩放方法提升性能时，也因重复执行子 Agent 而效率低下。  

**方法关键点**  
- **编排级奖励建模**：不依赖全轨迹，而是对编排计划 z 直接评分，训练一个 Bradley-Terry 奖励模型 rϕ(x,z)。  
- **自监督偏好构造**：利用 MAS-Orchestra 训练过程中产生的中间产物（检查点、轨迹）自动构建两类偏好对：① “专用优于基础”（πθ≻π0），来自训练过和未训练的编排器；② “正确优于错误”（z+≻z−），基于最终答案的正确性。混合比例 3:1 达到最佳。  
- **推理应用**：Best-of-N 中选择奖励最高的编排，再执行子 Agent，避免全轨迹多次采样，token 消耗降低 10 倍以上。  
- **训练应用**：用 Orch-RM 替代最终答案正确性作为奖励信号，通过 GRPO 进行编排器继续训练或从头训练，消除子 Agent 滚动的启动开销。  

**关键实验结果**  
- AIME 24&25：Orch-RM 的 Best-of-N 准确率 68.33%，超过所有编排级基线（LLM-as-a-Judge、Skywork 等），且 token 仅 2.38M，比 trajectory-level GPT-5-mini (70% acc) 更高效。  
- BrowseComp+：准确率 14.00%，超过 trajectory-level GPT-5-mini (12.50%)，验证 token 从 142.8M 降到 8.26M。  
- 继续训练：在 AIME 上 majority vote 从 63.33% 提升到 68.33%，且训练 token 仅需 GRPO 的约 1/10；BrowseComp 上从 9.50% 提升到 11.00%，token 消耗为 1/46。  
- 数据混合消融：仅用 CoI 或域比较均次优，1:3 的 CoI:SoO 混合实现最佳分离正确与错误编排。  

**一句话亮点**  
“Orch-RM 证明了编排级奖励信号足以替代昂贵的全轨迹执行反馈，使多智能体系统的测试时缩放和训练效率提升一个数量级，同时保持或超越性能。”
