---
title: 'VideoGen-Agent: Reinforcing Video Generation Agents'
title_zh: VideoGen-Agent：强化视频生成智能体
authors:
- Binxu Li
- Haoyi Duan
- Yuhui Zhang
- Yaohui Zhang
- Zihao Lin
- Kaituo Feng
- Suozhi Huang
- Xiangyi Li
- Yu Li
- Chunyuan Li
affiliations:
- Princeton University
- Stanford University
- UC Davis
- MMLab, CUHK
- Independent
arxiv_id: '2609.24997'
url: https://arxiv.org/abs/2609.24997
pdf_url: https://arxiv.org/pdf/2609.24997
published: '2026-09-20'
collected: '2026-09-22'
category: Agent
direction: 多模态 Agent 工具使用与强化学习
tags:
- Video Generation
- Tool Use
- Reinforcement Learning
- Multimodal Agent
- VABench
one_liner: 通过多任务智能体强化学习训练多模态 Agent 协调外部工具，显著提升复杂视频生成任务的指令遵循能力。
practical_value: '- 多工具 Agent 的「检索/增强 → 生成 → 验证」闭环可迁移到电商导购 Agent：先搜索增强获取商品知识，再生成推荐理由/文案，最后校验属性一致性与用户意图覆盖，提升复杂需求满足率。

  - 奖励函数分解为工具调用合法性、任务适配性、内容质量三类，并做类别平衡与类别感知加权，可借鉴到推荐/广告文案生成 Agent 的训练中，避免只优化点击或转化导致工具滥用或内容偏置。

  - 先 SFT 教师轨迹再 RL 精调，且生成工具可独立升级无需重训 Agent，这种解耦架构在业务中可大幅降低迭代成本：底层生成模型或检索库更换后，策略网络无需重新训练。

  - VABench 的评估维度（专业知识、身份保持、物理一致性、场景构图、多镜头时序）可迁移为电商视频/商品描述生成的评测框架，尤其多实体身份一致性和时序事件逻辑值得借鉴。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有视频生成模型在需要专业知识、特定身份保持、物理一致性或有序事件提示上表现不佳，直接文本到视频（T2V）生成难以满足复杂指令。

**方法关键点**：提出 VideoGen-Agent，一个多模态 Agent，通过多任务智能体强化学习训练使用外部工具。Agent 协调增强（augmentation）、生成（generation）、验证（verification）三类工具，在多轮交互中依据用户提示与中间观测进行决策。训练流程：先在教师生成的轨迹上做监督微调（SFT）建立工具使用行为，再用强化学习精调。奖励采用类别感知混合奖励，分别评估工具调用合法性、任务适配性及最终视频质量，并在六类任务上构建类别平衡数据集。同时引入 VABench，包含 600 个提示，覆盖程序性知识、单/多实体身份保持、物理一致性、场景构图、多镜头时序结构。

**关键结果**：在 VABench 上，VideoGen-Agent 比基础 T2V 生成器得分从 56.5 提升至 75.6，提高 19.1 分；仅升级底层生成工具（无额外 Agent 训练）后进一步提升至 86.1；人类评估中，升级版配置在 84.3% 的比较中优于最强独立基线。结果表明多任务工具使用学习可迁移到更强的底层生成模型。
