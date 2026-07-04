---
title: Logit-Contribution Scoring Identifies Non-Literal Retrieval Heads
title_zh: 基于逻辑值贡献评分识别非字面检索头
authors:
- Aryo Pradipta Gema
- Beatrice Alex
- Pasquale Minervini
affiliations:
- University of Edinburgh
- Heriot-Watt University
- Miniml.AI
arxiv_id: '2607.01002'
url: https://arxiv.org/abs/2607.01002
pdf_url: https://arxiv.org/pdf/2607.01002
published: '2026-06-30'
collected: '2026-07-04'
category: LLM
direction: LLM 可解释性 · 检索头检测
tags:
- retrieval-heads
- non-literal-retrieval
- OV-circuit
- logit-contribution
- mechanistic-interpretability
- long-context
one_liner: 提出写感知的 LOCOS 方法，通过 OV 电路输出投影检测非字面检索头，消融时性能崩溃远快于注意力基线
practical_value: '- 对长上下文 Agent 中检索增强生成（RAG）的故障诊断有价值：可通过 LOCOS 定位哪些注意力头真正参与「理解上下文语义并合成答案」，而非字面复制，帮助调试上下文利用不全或幻觉问题。

  - 在电商推荐理由生成或搜索结果摘要等需要从长文本中提取关键信息并改写输出的场景，可以借鉴「写感知」检测的思路，评估模型内部是否有效融合了商品描述、用户评价等非结构化信息，而不仅是复制片段。

  - 方法本身只需一次性前向传播，计算轻量，适合在生产环境中对模型行为进行可解释性审计，但不直接改变推荐策略，迁移需与下游任务头部微调结合。'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有检索头检测方法（如基于注意力权重与生成 token 的匹配度）隐含假设检索是字面复制，无法识别那些「理解上下文含义并合成答案」的非字面检索头。这类头仅靠注意力模式无法与普通头区分，需从输出值（OV）电路角度捕获其写入贡献。

### 方法
提出 Logit-Contribution Scoring (LOCOS)，一种「写感知」检测器：对每个注意力头，计算其 OV 电路输出在答案 token 的 unembedding 向量上的投影，作为该头对正确答案的 logit 贡献；通过比较信息源位置（needle）与非信息源位置（off-needle）的贡献差异得到分数，仅需一次前向传播即可完成所有头的评分。

### 关键结果
- 在非字面检索基准 NoLiMa 上，消融 LOCOS 选出的顶层头使性能快速崩溃：Qwen3-8B 消融 50 个头时 ROUGE-L 从 0.401 降至 0.000，而最佳基线（注意力累加方法）仍保留 0.292。
- 所选头具有检索特异性：相同消融不影响参数化知识问答和算术推理；在复杂的多跳检索任务 MuSiQue（0.55→0.08）和 BABI-Long（0.62→0.20）上也显著下降，随机头消融则下降不超过 0.05。
