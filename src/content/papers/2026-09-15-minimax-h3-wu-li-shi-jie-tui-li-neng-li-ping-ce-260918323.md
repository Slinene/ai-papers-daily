---
title: Can MiniMax-H3 Reason About the Physical World? An Evaluation of Omni-Modal
  Generative Model
title_zh: MiniMax-H3 物理世界推理能力评测
authors:
- Haoyu Zhao
- Zihao Zhao
- Tianyu Deng
- Ziqin Xu
- Zihao Zhang
- Xudong Wang
- Jinxiang Guo
- Chen Gao
- Ziyi Ye
- Yeying Jin
affiliations:
- National University of Singapore
- Fudan University
- Tencent
arxiv_id: '2609.18323'
url: https://arxiv.org/abs/2609.18323
pdf_url: https://arxiv.org/pdf/2609.18323
published: '2026-09-15'
collected: '2026-09-19'
category: Eval
direction: 多模态生成模型物理推理评测
tags:
- Omni-Modal
- World Reasoning
- Evaluation
- Audio-Visual
- Multimodal
one_liner: 构建四个互补维度的评测框架，揭示全模态生成模型 MiniMax-H3 在物理推理任务上总体成功率仅41.97%，音频消歧最弱
practical_value: '- 评测范式可迁移：设计多模态 Agent 或生成推荐评测时，避免让提示与目标内容过度显式匹配；可以构造“单模态信息不足、需跨模态联合推理”的任务，更真实地暴露模型整合能力弱点。

  - 结果提示音频-视觉融合是薄弱环节（27.40%）：在电商语音购物、短视频商品讲解等场景，若依赖多模态生成推荐，需重点强化音频与视觉语义对齐与消歧。

  - 视频决策推理相对强（56.00%），但整体成功率仍低，说明物理一致性推理尚未成熟，生成式推荐直接产出商品视频/图文时要增加事实与物理合理性校验环节。

  - 评测框架的四个维度可作为产品中生成内容质量评估的模块化参考，例如分别测试隐式文本+多图、音视频联合输入下的推理能力。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：全模态生成模型（Omni-Models）统一处理文本、图像、视频、音频，MiniMax-H3 是代表。现有视频生成和世界模型评测受限于输入模态单一、提示与目标内容高度匹配，无法考察跨模态联合推理。作者设计评测框架，围绕物理世界推理的四个互补维度。

**方法关键点**：评测包含四类任务：隐式提示+多帧、音频-图像、前缀视频、音频-视频输入。每个模态只提供部分线索，要求模型融合互补语义推断潜在事件状态和未来动态。构建 517 个评测实例。

**关键结果**：MiniMax-H3 总体成功率 41.97%；视频决策推理最高 56.00%；音频消歧推理最低 27.40%。结果表明多模态整合仍是瓶颈。
