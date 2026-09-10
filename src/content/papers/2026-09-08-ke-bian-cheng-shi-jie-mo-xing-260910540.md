---
title: Programmable World Model
title_zh: 可编程世界模型
authors:
- Zheng-Hui Huang
- Guixu Lin
- Jiacheng Lin
- Yi-Chuan Huang
- Ruihan Yu
- Muyao Niu
- Siqi Yang
- Yu-Lun Liu
- Yung-Yu Chuang
- Kaipeng Zhang
affiliations:
- Alaya Lab
arxiv_id: '2609.10540'
url: https://arxiv.org/abs/2609.10540
pdf_url: https://arxiv.org/pdf/2609.10540
published: '2026-09-08'
collected: '2026-09-10'
category: Other
direction: 世界模型 · 显式状态与渲染解耦
tags:
- World Model
- Programmable State
- Video Generation
- Agent
- 3D OBB
- Benchmark
one_liner: 将世界状态演化与视频生成解耦，用可执行程序维护持久全局状态，以3D OBB为中间表示驱动预训练视频模型
practical_value: '- 在生成式推荐或广告文案生成中，可借鉴“显式状态引擎 + 生成渲染器”的架构：将库存、价格、用户状态等业务规则放在符号化状态机中维护，LLM
  只负责生成符合当前状态的文案/推荐理由，避免长对话或多步推荐中事实不一致。

  - 用 LLM 将自然语言策略转成可执行程序（如 on_hit、win/lose 规则）的思路，适合推荐策略的自动化编排：把运营规则（如“库存低于阈值则降低曝光”）用程序表达，可审计、可回滚，比直接让模型隐式学习更可控。

  - 中间表示的做法——将结构化状态（如商品布局、用户行为序列）编译为生成模型的条件信号，可用于可控商品图/视频生成，提升布局、属性与业务约束的像素级对齐。

  - 评估基准设计可迁移：对交互式推荐/对话系统，可采用 Count Accuracy 和 State Accuracy 这类细粒度状态一致性指标，衡量长程交互中的用户状态、上下文跟踪能力。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有视频世界模型能生成逼真交互画面，但缺乏可靠的机制来维护持久世界状态和执行可编程规则，长时交互容易不一致。

**方法关键点**：
- 将世界状态演化与视觉观测生成解耦：Agent 把自然语言指令转成可执行程序，定义实体状态与状态转移规则（如 `on_hit: hp -= damage`、`win: all_enemies_defeated`）。
- 轻量引擎执行程序，维护显式、持久的全局世界状态，包括屏外实体和非视觉属性，实现可编程规则与直接实体控制。
- 为连接状态与视觉生成，引入 state-augmented 3D OBB 作为中间表示；结合目标相机轨迹，确定性地编译为像素对齐的时空条件信号，输入预训练视频模型作为生成渲染器。
- 构建 CombatStateBench 用于评估可编程世界模型。

**关键结果**：在 CombatStateBench 上，该方法达到 94% Count Accuracy 和 98% State Accuracy，显著优于现有交互式视频世界模型，并支持连贯的长时程生成。
