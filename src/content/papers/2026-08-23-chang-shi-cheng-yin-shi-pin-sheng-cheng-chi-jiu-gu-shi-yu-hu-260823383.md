---
title: Long-Horizon Audio-Visual Generation for Persistent Stories and Interactive
  Worlds
title_zh: 长时程音视频生成：持久故事与交互世界
authors:
- Nan Duan
- Haoyang Huang
- Weiyang Jin
- Haoran Li
- Yaowei Li
- Yuming Li
- Yijun Liu
- Xin Lu
- Xiaoxiao Ma
- Yanwen Ma
affiliations:
- Joy Future Academy, JD
arxiv_id: '2608.23383'
url: https://arxiv.org/abs/2608.23383
pdf_url: https://arxiv.org/pdf/2608.23383
published: '2026-08-23'
collected: '2026-08-29'
category: Multimodal
direction: 多模态生成 · 长时记忆与几何控制
tags:
- Audio-Visual Generation
- Cross-Shot Memory
- 6-DoF Camera Trajectory
- Self-Gradient Forcing
- World Model
one_liner: JoyAI-Echo-1.5 用跨镜头记忆与 6-DoF 几何控制实现角色持久和交互世界，并以 Self-Gradient Forcing 训练因果生成器
practical_value: '- 长视频变体的 composable cross-shot memory 聚合多镜头视觉证据和 speech-filtered
  speaker cues，可借鉴到电商短视频广告生成中：显式维护商品/人物外观与音色记忆库，避免多镜头口播或商品展示中的角色漂移，提升跨镜头一致性。

  - 世界模型变体将异构导航输入统一为 calibrated metric 6-DoF 相机轨迹，经 geometry-aware conditioning 注入，可迁移到虚拟直播间、3D
  商品展示或交互式试衣间，使鼠标/键盘/手柄等不同控制信号映射到统一几何表示，简化多端交互接入。

  - 训练技巧 progressive teacher forcing + short/long-horizon Self-Gradient Forcing 在自生成
  rollout 上训练，将一个双向模型转为 causal few-step generator，可借鉴到推荐系统里的用户行为序列生成或 query 序列预测，减少
  teacher forcing 导致的 exposure bias，提升长序列生成一致性。

  - 工程实现上，将 speech-filtered full-shot audio 作为 speaker cues 绑定音色，可复用于电商数字人直播的音画同步与角色一致性，降低对多模态对齐标注的依赖。'
score: 6
source: huggingface-daily
depth: abstract
---

## 动机
视频生成正从孤立片段走向长叙事和交互世界，核心挑战是跨镜头保持角色身份、跟随用户控制、长期 rollout 稳定。现有模型在长时生成中容易出现外观漂移、控制信号不统一和自回归误差累积。

## 方法关键点
JoyAI-Echo-1.5 是一个统一音视频生成系统，包含两个专用变体：
- **长视频变体**：引入 composable cross-shot memory，聚合多个前序镜头的视觉证据，并从 speech-filtered full-shot audio 中提取 speaker cues，从而在文本/图像/记忆的灵活组合下保持角色外观和声音身份。
- **世界模型变体**：将异构导航输入（如键鼠、手柄）转换为 calibrated metric 6-DoF 相机轨迹，通过 geometry-aware conditioning 路径注入，实现 controller-agnostic 的灵活视点交互。
- **训练策略**：将双向音视频 backbone 改造为 causal few-step generator，采用 progressive teacher forcing + short/long-horizon Self-Gradient Forcing，在自生成 rollout 上训练，缓解长时生成中的误差累积。

## 关键结果
- 长视频任务：在 cross-shot consistency、visual quality、text alignment、speech fidelity 上全面超过现有 long-video baselines。
- 世界模型任务：在 WBench 上以平均 81.7 分排名第一；在 SANA-WM-Bench 上取得领先的视觉质量和长时持久性。

结果表明，记忆、几何控制与 rollout-aware 训练为连贯故事生成和持续演化的交互世界提供了实用基础。
