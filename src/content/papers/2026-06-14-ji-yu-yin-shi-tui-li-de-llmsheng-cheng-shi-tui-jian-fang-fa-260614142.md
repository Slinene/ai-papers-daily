---
title: Implicit Reasoning for Large Language Model-based Generative Recommendation
title_zh: 基于隐式推理的LLM生成式推荐方法
authors:
- Yinhan He
- Liam Collins
- Bhuvesh Kumar
- Jundong Li
- Neil Shah
- Donald Loveland
affiliations:
- University of Virginia
- Snap Inc.
arxiv_id: '2606.14142'
url: https://arxiv.org/abs/2606.14142
pdf_url: https://arxiv.org/pdf/2606.14142
published: '2026-06-14'
collected: '2026-06-16'
category: GenRec
direction: 生成式推荐 · Semantic ID · 隐式推理
tags:
- Implicit Reasoning
- Semantic IDs
- Pause Tokens
- Chain-of-Thought
- Generative Recommendation
- LLM4Rec
one_liner: 用可训练的 <pause> 令牌替代显式思维链，在Semantic ID推荐上效果更好且训练推理更高效
practical_value: '- **用 <pause> tokens 做隐式推理，避免为每个样本生成昂贵且脆弱的文字理由**：直接在输入中插入可训练的暂停令牌，仅通过下一个
  item 预测损失优化，省去教师模型生成、理由对齐和 RL 后训练，训练成本降低 65%，推理速度提升 3.5 倍。

  - **诊断显式 CoT 在 SID 场景下的三大失败原因，避免踩坑**：弱化世界知识 verbalization、文本与 SID 嵌入空间分离、理由质量敏感。若团队正在尝试让
  LLM 生成带推理的推荐，可将这些发现作为前置分析，避免无效投入。

  - **pause token 初始化和预训练策略可复用**：将 <pause> 初始化为全体词嵌入的均值，再在结合文本与 SID 的数据上预训练，使其位于两个嵌入空间的交界处，有效桥接语义。该套路可迁移到其他需要融合离散
  token（如用户行为序列、attribute tokens）的场景。

  - **隐式 latent scratch space 思路不限于推荐**：在输入和输出之间留出 k 个可学习的位置（不需监督），让模型自行决定如何利用这些中间计算，是一种通用的归约推理开销且提升下游任务表现的方法，可尝试用于搜索、广告点击率预估中的用户意图表征。'
score: 9
source: huggingface-daily
depth: full_pdf
---

**动机**：LLM 用于生成式推荐时，物品通常用 Semantic ID (SID) 表示，这些 token 在预训练时未见过，破坏了 LLM 的自然语言推理接口。现有工作引入显式思维链 (CoT) 和多阶段训练（CPT → SFT → CoT SFT → RL），但缺少对各个阶段必要性的理解，且 CoT SFT 单独使用时效果反而不及简单下一物品预测，需昂贵 RL 才能恢复性能。本文系统诊断了 CoT SFT 失败的三个原因，并针对性地提出轻量级隐式推理方案 PAUSEREC。

**方法关键点**：
- 分析揭示显式 CoT 的三大缺陷：(1) CoT SFT 使模型难以用文字表达仍保存在 logits 中的预训练知识；(2) 文本 token 和 SID token 嵌入空间随训练分离，理论证明自然语言理由对 SID 预测的影响有限；(3) 推荐性能对理由文本十分敏感，稍加扰动即大幅下降。
- 提出 PAUSEREC，保留 CPT 和下一物品 SFT 阶段，但用 <pause> 令牌取代 CoT SFT 和 RL。具体做法：在 CPT 后，对 <pause> 令牌做预训练——将其初始化为全词表嵌入均值，混入含有文本和 SID 的序列中训练，使其学会连接两种语义空间。随后在 SFT 模型上，在用户历史与目标 SID 之间插入 k 个 <pause> 令牌，仅对 SID 位置计算损失，让 <pause> 充当隐式推理的 scratch space。
- 推理时同样插入 k 个 <pause> 后直接解码 SID，不产生任何文字理由，极大减少生成 token 数。

**关键实验**：
- 数据集：Amazon Beauty、Sports、Toys。
- 基线：GRU4Rec、SASRec、BERT4Rec、HSTU、TIGER、ReaRec、下一物品 SFT、OneRec-Think（RL 增强的 CoT 基线）。
- 结果：PAUSEREC 在三个数据集上全面超过下一物品 SFT，相对提升最高 8.85%（Toys Hit@5）；与 OneRec-Think 相比，在 12 项指标中 10 项获胜，最高提升 6.22%；同时训练 GPU 小时减少 65%，推理每样本耗时约 3.5 倍加速。
- 消融实验表明，预训练 <pause> 令牌优于直接使用文本均值、SID 均值或默认初始化。注意力分析显示 pause 令牌逐步聚焦于与目标物品相关的历史 SID，证实其有效的隐式信息聚合。
