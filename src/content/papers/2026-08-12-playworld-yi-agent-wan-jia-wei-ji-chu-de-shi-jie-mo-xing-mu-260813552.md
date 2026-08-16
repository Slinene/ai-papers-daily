---
title: 'PlayWorld: Benchmarking World Models with Agent Players over Long-Horizon
  Objectives'
title_zh: PlayWorld：以 Agent 玩家为基础的世界模型长程目标基准
authors:
- Kaixin Ding
- Xi Chen
- Minghong Cai
- Zhiyuan Xu
- Yiyang Wang
- Yuxiang Lu
- Junyi Li
- Shuyang Chen
- Yuan Gao
- Xin Tao
affiliations:
- The University of Hong Kong
- Kling Team, Kuaishou Technology
- The Chinese University of Hong Kong
- Zhejiang University
arxiv_id: '2608.13552'
url: https://arxiv.org/abs/2608.13552
pdf_url: https://arxiv.org/pdf/2608.13552
published: '2026-08-12'
collected: '2026-08-16'
category: Eval
direction: 世界模型评估 · Agent 自适应交互
tags:
- world models
- evaluation
- agent players
- long-horizon
- video generation
- benchmark
one_liner: 用多模态 Agent 玩家按长期目标交互评测世界模型，揭示当前模型长程一致性与状态演化不可靠
practical_value: '- 评估思路迁移：在推荐/Agent 系统中，用“目标驱动的模拟用户”评估长程交互（如多轮对话推荐、会话搜索），而非固定脚本；Agent
  自适应调整动作，更接近真实用户行为，能暴露固定序列评测掩盖的问题。

  - 维度拆分：借鉴其将评估拆为几何一致性、交互保真度、状态演化等维度，可对应推荐系统的会话一致性、用户反馈建模、记忆/状态保持等维度，分别设计测试场景，避免单一指标失真。

  - 工程实现：使用多模态 Agent 根据观察帧和动作历史动态决定下一步，可复用到对话式推荐评测中，构建“用户模拟器”用于离线评估，降低人工标注成本。

  - 注意局限：世界模型与电商场景有距离，但这类“目标驱动交互评估”对评估生成式推荐和个性化 Agent 的长程一致性有一定启发，业务落地需改造。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：视频世界模型虽然能生成一致且可控的长序列，但公平比较仍困难。人类玩家通常通过追逐长期目标来评估世界模型（如 360° 环视、走入水中观察涟漪），而不同模型实现同一目标所需的动作序列可能差异很大，固定动作条件评测不适合跨模型比较。

**方法**：提出 PlayWorld 基准，引入多模态 Agent Players 与世界模型交互，按指定长期目标动态调整动作。基准包含 171 个场景，每个场景有明确目标。评估覆盖四个核心维度：几何一致性、交互保真度、视野外演化、洞察演化，并加入视频质量和可控性等基础能力指标。

**结果**：在九个 SOTA 世界模型上实验，当前模型在长期交互目标上仍不可靠，尤其保持空间一致性和持续状态演化方面表现较差。例如突然出现物体、脚漂浮、切开的番茄恢复、背景静默等问题。代码与数据已开源。
