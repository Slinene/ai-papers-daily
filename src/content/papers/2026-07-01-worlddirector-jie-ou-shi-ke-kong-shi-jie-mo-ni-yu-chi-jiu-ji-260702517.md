---
title: 'WorldDirector: Building Controllable World Simulators with Persistent Dynamic
  Memory'
title_zh: WorldDirector：解耦式可控世界模拟与持久动态记忆
authors:
- Hanlin Wang
- Hao Ouyang
- Qiuyu Wang
- Wen Wang
- Qingyan Bai
- Ka Leong Cheng
- Yue Yu
- Yixuan Li
- Yihao Meng
- Zichen Liu
affiliations:
- HKUST
- Ant Group
- ZJU
- CUHK
arxiv_id: '2607.02517'
url: https://arxiv.org/abs/2607.02517
pdf_url: https://arxiv.org/pdf/2607.02517
published: '2026-07-01'
collected: '2026-07-06'
category: Other
direction: 世界模型 · 视频生成与模拟
tags:
- World Model
- Video Generation
- LLM
- 3D Trajectories
- Controllable Generation
- Persistent Memory
one_liner: 将3D语义运动编排与视频生成解耦，用LLM生成控制轨迹，实现持久动态对象记忆与高可控长视频合成
practical_value: '- 解耦控制与生成的思路可迁移至生成式推荐：先用 LLM 编排用户意图阶段或促销节律，再控制具体物品生成，提升推荐结果的可控性与逻辑性。

  - 持久动态记忆模块启发长期用户兴趣建模：即使某类商品长期无交互，仍维持其隐状态，在重新出现时快速恢复相关性，可改进长序列召回。

  - 利用 LLM 生成结构化控制信号（如行为路径）的方法，可用于模拟用户交互序列，生成高质量仿真数据，辅助离线策略评估和训练。

  - 因果块自回归生成方式可类比于推荐中的分阶段决策，将推荐列表分块生成并保持块间一致性，避免一次性输出过长序列导致的逻辑断裂。'
score: 6
source: huggingface-daily
depth: abstract
---

动机：现有视频世界模型常将物理动态与像素生成耦合，依赖连续视觉观测维持运动，对象一旦离开视野便失去记忆，无法保证再入后的身份一致性。为此，需要一种将动态记忆与视觉生成解耦的框架。

方法：提出 WorldDirector，显式分离语义运动编排和视觉生成。首先，LLM 根据文本描述推理生成 3D 物体轨迹与相机移动路径，构成结构化控制信号；随后，以这些轨迹为条件，通过潜扩散视频模型按因果块自回归式生成视频。该解耦设计确保物理逻辑和外观稳定，即使对象长时间离开画面，再次出现时也能精确保留其视觉身份。

结果：实验定性展示，该方法可合成复杂、长时事件，具有此前方法无法达到的可控性和持久动态对象记忆，支持任意视角漫游与对象再入的一致性。
