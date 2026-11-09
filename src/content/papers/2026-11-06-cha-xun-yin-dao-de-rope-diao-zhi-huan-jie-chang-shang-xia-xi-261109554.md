---
title: Query-Guided RoPE Modulation for Lost-in-the-Middle Mitigation in Long-Context
  LLMs
title_zh: 查询引导的 RoPE 调制缓解长上下文 LLM 中间信息丢失
authors:
- Peiyu Zhang
- Heng Ping
- Shinibali Bhattacharyya
- Anwesan Pal
- Nikos Kanakaris
- Kevin Cheang
- Shixuan Li
- Wei Yang
- Paul Bogdan
affiliations:
- University of Southern California
- Amazon Web Services
arxiv_id: '2611.09554'
url: https://arxiv.org/abs/2611.09554
pdf_url: https://arxiv.org/pdf/2611.09554
published: '2026-11-06'
collected: '2026-11-09'
category: LLM
direction: 长上下文 LLM 的 RoPE 位置调制
tags:
- Lost-in-the-Middle
- RoPE
- Long-Context
- Positional Encoding
- Training-Free
one_liner: 提出训练免费方法 QGPM，利用查询相关性重塑 RoPE 位置，缓解长上下文 LLM 的 lost-in-the-middle 问题
practical_value: '- 电商场景处理长商品描述、长用户评论或长对话历史时，可尝试 QGPM 思路：基于查询相关性对 RoPE 位置进行调制，无需训练即可缓解中间关键信息被忽略的问题。

  - 该方法是训练免费且利用模型自身注意力头，适合快速集成到现有基于 RoPE 的 LLM（如 LLaMA 系列）推理流程中，无需额外标注数据或微调成本。

  - 分层相关图构建（低层广泛、高层尖锐）可借鉴到多粒度注意力机制中：在排序或召回模型里，低层保留较多候选信息，高层聚焦强相关证据，提升长序列建模效果。

  - 对于跨领域 long-context 任务（如广告文案生成、用户行为序列建模），可验证该方法在检索类任务上的增益，尤其当关键信息位于输入中部时。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

## 动机
长上下文 LLM 常出现“lost-in-the-middle”现象，部分原因在于 RoPE 的长程衰减削弱了远距离 token 之间的位置信号。现有输入压缩和注意力重加权发生在 RoPE 信号衰减之后，RoPE 层方法虽直接调整位置，但对所有查询使用同一重映射，缺乏灵活性。

## 方法关键点
提出 QGPM（Query-Guided Positional Modulation），一种训练免费的方法，利用模型自身注意力头中的查询相关性重塑 RoPE 位置。具体做法：在低层构建宽泛的相关图，在高层构建锐利的相关图；低相关性 token 在快速旋转平面上前进不到一个位置，从而将相关证据拉向查询；慢速旋转平面保持原始布局，确保整体位置结构不变。这种分层策略既增强了重要 token 的位置信号，又避免了全局重映射带来的信息扭曲。

## 关键结果
在 NoLiMa 和 RULER 基准上，跨多个上下文长度，QGPM 均优于基线和强基线方法，尤其在检索任务上增益最大，并且在不同骨干模型上表现出良好的泛化性。代码已开源。
