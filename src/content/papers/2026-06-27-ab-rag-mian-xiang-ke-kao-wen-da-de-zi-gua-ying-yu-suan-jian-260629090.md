---
title: 'AB-RAG: Adaptive Budgeted Retrieval-Augmented Generation for Reliable Question
  Answering'
title_zh: AB-RAG：面向可靠问答的自适应预算检索增强生成
authors:
- Ansh Kamthan
affiliations:
- Manipal University Jaipur
arxiv_id: '2606.29090'
url: https://arxiv.org/abs/2606.29090
pdf_url: https://arxiv.org/pdf/2606.29090
published: '2026-06-27'
collected: '2026-06-30'
category: RAG
direction: 训练无关的自适应预算RAG与置信度估计
tags:
- Adaptive RAG
- Confidence Estimation
- Self-Consistency
- Budgeted Retrieval
- Selective Prediction
- Question Answering
one_liner: 无需训练、骨干无关的自适应RAG框架，用三信号置信度控制检索深度，实现高低置信答案准确率57.6% vs 0%的分离
practical_value: '- **预算可控的自适应检索框架**：可借鉴到需要调用LLM的推荐/搜索系统中，通过置信阈值平衡效果与调用成本，尤其适合按量计费的商业API场景。

  - **闭源API的置信度代理**：对于无法获取token概率的闭源模型，采用self-consistency（多次采样取众数一致性）作为模型确信度的代理信号，直接可用于线上QA或相似度判断任务。

  - **多信号置信度设计思路**：模型内部确信度是最强预测信号，检索得分方差可作为检索质量奖励项，而答案-证据嵌入相似度对短文本任务无效——在构建电商/广告的LLM置信判断时，应优先利用内部概率或采样一致性，并警惕语义相似度在短文本场景的失效。

  - **选择性预测与成本控制**：利用置信度分离高/低质量回答，高置信直接返回，低置信触发额外检索或人工审核，既提升可靠性又控制检索开销，适合对时延和预算敏感的在线推荐系统。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：固定深度的RAG对所有问题分配相同数量的检索段落，简单问题浪费计算和上下文窗口，复杂问题证据不足，且无法给出答案可信度信号。随着大量QA系统建立在付费API之上，一种无需训练、可控制检索开销、能估计答案置信度的方法具有明确的实用价值。

**方法关键点**：
- *自适应预算循环*：从少量证据开始生成答案，通过三信号置信度评估，若低于阈值且未达预算上限则扩大检索证据量并重试，循环最多 T_max 轮。
- *三信号置信度估计*：①模型自身确定性——开源模型用生成 token 的平均概率，闭源 API 用 self-consistency（多次采样答案众数比例）；②答案与证据的嵌入余弦相似度（理论衡量接地性，但实验证明对短答案失效）；③检索得分方差——归一化重排序分数的方差作为检索质量奖励（经校正，高方差表示重排序能清晰区分相关与不相关）。
- *检索栈*：BM25稀疏检索 + BGE稠密检索 → 互惠排序融合（RRF） → 交叉编码器重排序，最后截取 top-K 作为证据集。
- *训练无关、骨干无关*：整个流程无需微调，可直接替换后台生成模型。

**关键实验**：
- 数据集：HotpotQA（多跳，500题）和 TriviaQA（事实型，200题），均为开放池检索设置（非完整维基百科）。
- 模型：Qwen2.5-1.5B（本地，有 token 概率）、Llama-3.2-3B（Ollama，无概率，用 self-consistency）、Claude Haiku（付费 API，无概率，用 self-consistency）。
- 核心结果：
  - 置信度在所有骨干上可靠分离正确与错误答案。Claude 在 TriviaQA 上高置信答案 EM 57.6%，低置信答案 EM 0.0%。
  - 自适应提升在强骨干上显现：Llama-3.2-3B EM 从 39.5% 升至 45.0%；Claude 在 TriviaQA 上从 35.5% 升至 40.0%。
  - 信号消融：模型自身确定性 AUROC 从 Qwen 的 0.607 到 Claude 的 0.776，证据一致性信号 AUROC 在 0.35 附近（比随机差），检索方差信号经符号校正后 AUROC 0.573。
  - 成本可控：所有实验在 4GB 显卡笔记本完成，API 总花费不足几美元。

**核心记忆点**：置信度估计能可靠地将正确与错误答案分开，无需训练即可支持选择性预测，而模型内部确信度（概率或 self-consistency）是最强的单信号。
