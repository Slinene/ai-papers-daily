---
title: Agentic Game Development as a Verifiable Trajectory Data Engine for Scaling
  World Models
title_zh: 智能体游戏开发：作为可验证轨迹数据引擎扩展世界模型
authors:
- Pengfei Zhou
- Hexin Wang
- Zhengfeiyang Zhang
- Yixing Ma
- Zhenglin Wan
- Kaipeng Zhang
- Wangbo Zhao
- Yang You
affiliations:
- National University of Singapore, HPC-AI Lab
- InfRec, Cardinal AI Lab
- University of California, Berkeley
- Hong Kong University of Science and Technology
- Independent Researcher
arxiv_id: '2608.25518'
url: https://arxiv.org/abs/2608.25518
pdf_url: https://arxiv.org/pdf/2608.25518
published: '2026-08-25'
collected: '2026-08-31'
category: Training
direction: 世界模型 · 可验证奖励 · RL post-training
tags:
- World Models
- RL Post-training
- Verifiable Rewards
- Game Engine
- Trajectory Data
- Agentic Generation
one_liner: 提出 RLHEV 后训练范式，用游戏引擎可执行验证与人类隐式接受信号，为世界模型提供可奖励轨迹数据。
practical_value: '- 在电商/Agent 场景，借鉴“可执行验证”思路：用库存、价格、物流时效、广告合规等确定性业务规则作为 dense verifier，替代
  CLIP 这类模糊 proxy；同时用点击/成交/无投诉等隐式人类反馈做 global signal，构建 RL post-training 奖励。

  - 把生产中的长程交互日志（搜索→浏览→加购→下单→售后）当作 trajectory data，回流训练 Agent；类似论文将 game development
  过程转为可验证轨迹。

  - 对跨域/跨环境泛化：论文中发现 transfer learning 对 OOD shift 有正向信号，电商可尝试在相似但不同的域（不同站点、类目、流量渠道）做预训练+微调，并设计可控实验评估。

  - 若业务有模拟器（如供应链仿真、店铺经营模拟），可以低成本合成违规/可玩性等验证信号，给 LLM/Agent 提供递归数据引擎；没有模拟器时，也可从人工审核/退款/纠纷数据中抽取弱监督信号。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有世界模型扩展主要靠更多爬取视频和算力，但空间生成仍依赖 CLIP score 等模糊 proxy，难以支撑 RL post-training。代码智能体之所以成功，是因为可执行代码能提供编译器/运行时的高质量奖励；游戏场景由游戏引擎编码，天然可执行，能高效检查碰撞、物理、导航和可玩性，开发者还能给出全局接受/拒绝信号。

**方法**：提出 RLHEV（Reinforcement Learning with Human-Engine Verification），结合密集的引擎验证信号与开发过程中的隐式人类接受反馈。具体实现为 Agentic World Model (AWoMo)：世界构建 Agent 提出场景编辑，观察人类-引擎验证，将接受或修复后的多模态轨迹转为训练数据。

**结果**：在 UnitySceneBench 200 例 Unity 资产编辑评测上，RLHEV 取得最高分；迁移学习对 OOD shift 有效，并在 Unreal 和 Godot 跨引擎实验中给出正向信号；AWoMo 增广训练还提升了 R2R、Gymnasium MuJoCo、D4RL Gym-MuJoCo 上的 embodied 策略表现。
