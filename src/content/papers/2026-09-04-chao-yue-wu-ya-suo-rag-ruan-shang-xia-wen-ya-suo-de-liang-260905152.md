---
title: 'Compression Beyond the Uncompressed: A Two-Stage Training Recipe for Soft
  Context Compression in RAG'
title_zh: 超越无压缩：RAG 软上下文压缩的两阶段训练配方
authors:
- Shuyu Guo
- Shuo Zhang
- Zhaochun Ren
affiliations:
- Shandong University
- Bloomberg
- Leiden University
arxiv_id: '2609.05152'
url: https://arxiv.org/abs/2609.05152
pdf_url: https://arxiv.org/pdf/2609.05152
published: '2026-09-04'
collected: '2026-09-07'
category: RAG
direction: RAG 软上下文压缩 · 蒸馏+RL 训练
tags:
- Soft Context Compression
- RAG
- Knowledge Distillation
- Reinforcement Learning
- Inference Acceleration
one_liner: 用正确样本蒸馏 + 失败样本强化学习两阶段训练，让 16 倍压缩的 RAG 软上下文效果反超无压缩基线
practical_value: '- 若在商品知识问答、客服 RAG、广告文案检索增强等场景用 LLM 消费长文档，可尝试 soft context compression：把
  top-N 商品详情/用户评价/知识条目编码成少量 embedding，替代原始文本，换取 4×–24× 的推理提速。

  - 训练配方的可迁移点在于：蒸馏时只用教师 RAG 回答正确的样本，避免把无压缩模型的错误模式蒸馏进压缩模型；然后专门在教师失败的 query 上做 RL，让压缩模型学习更适配压缩表示的计算路径，而不是只模仿教师上限。

  - 对推荐/搜索中的 LLM ranker 或生成式 item 描述，若需压缩长用户行为序列或 item 文本，可以用类似两阶段：先用正确输出 warm-start，再对
  hard case 做策略探索，可能比直接 SFT 或全量蒸馏更稳。

  - 评估时值得像论文一样扫不同 retrieval depth（top-5 到 top-30），确认压缩方案在长上下文下是否仍保持收益，而不是只在单点设置上调优。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

动机：RAG 检索上下文过长会推高输入长度和推理延迟；soft context compression 将每篇文档编码为更短的 embedding 序列，但现有方法大多只用无压缩 RAG 做蒸馏，性能天然受限于教师模型。

方法关键点：DEX-Comp 提出两阶段训练。第一阶段 Pure Distillation：仅在无压缩 RAG 回答正确的 query 上蒸馏，避免错误信号干扰；第二阶段 Hard Exploration：只在无压缩 RAG 失败的 query 上做强化学习，迫使压缩模型探索更适合压缩表示的计算模式，突破教师上限。

关键结果：在 5 个开放域 QA 基准、top-5 到 top-30 检索深度下，DEX-Comp 将检索上下文压缩 16×，推理加速 4×–24×，效果与无压缩 RAG 基线相当或更好；消融和跨数据集/backbone 评估验证了各阶段贡献与泛化性。
