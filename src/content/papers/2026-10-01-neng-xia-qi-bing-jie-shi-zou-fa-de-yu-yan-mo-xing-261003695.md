---
title: Language Models that Play Chess and Explain Their Moves
title_zh: 能下棋并解释走法的语言模型
authors:
- Adithya Bhaskar
- Jeffrey Cheng
- Danqi Chen
affiliations:
- Princeton Language and Intelligence, Princeton University
arxiv_id: '2610.03695'
url: https://arxiv.org/abs/2610.03695
pdf_url: https://arxiv.org/pdf/2610.03695
published: '2026-10-01'
collected: '2026-10-06'
category: Training
direction: LLM 与专家编码器融合训练
tags:
- LLM
- expert encoder
- iterative distillation
- cross-attention
- reasoning
- chess
one_liner: 4B 模型结合沉默专家棋类编码器与迭代 Bellman 式自蒸馏，棋力达 2697 Elo 且可解释走法
practical_value: '- 电商推荐中已有的高精度但不可解释模型（如精排 CTR/CVR、向量召回）可作为 silent expert encoder，用
  cross-attention 接入指令微调的小型 LLM，低成本生成推荐解释或决策理由

  - 采用“候选决策—结果分析—整合解释—蒸馏回模型”的迭代 self-distillation：让 LLM 分析推荐列表 top 候选的用户后续行为并蒸馏回模型，可同时提升策略质量与解释一致性

  - 先做概念级 QA 课程（如“用户为何点击该商品”）再进入完整解释生成，能稳定从专家表示中抽取可读知识，避免直接生成错误解释

  - 4B 模型达到 frontier 水平，说明用领域 expert encoder + 小模型蒸馏可大幅降低线上推理成本，适合电商高 QPS 场景'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现代国际象棋引擎是沉默专家——棋力超人类但不给解释；语言模型能生成看似合理的解释，但棋力弱导致解释不可信。需要同时具备强棋力与可解释性的模型。

**方法关键点**：提出 Queen，4B 参数 chess-language model。架构上，将沉默专家棋类编码器（Lc0）与指令微调 LM 通过 cross-attention 集成，用问答课程训练 LM 从编码器表示中提取棋类概念。训练上，采用自然语言版 Bellman update 的迭代蒸馏：对当前局面 top 候选走法后的局面做分析，整合成当前局面的解释，再蒸馏回模型；共七轮迭代。

**关键结果**：Elo 从 1782 提升到 2697，提升超 900 分，超过所有 frontier models 的棋力与谜题准确率，参数量少三个数量级；LM 评估显示解释流畅，coherence 接近 GPT-5.6-Sol (high)。这种架构与训练流程可泛化到具有沉默专家编码器的领域，如游戏、机器人、计算机使用。
