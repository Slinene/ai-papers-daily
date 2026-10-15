---
title: 'Retrieve What Helps, Only When It Helps: Agentic Reinforcement Learning for
  Selective Retrieval-Augmented Machine Translation'
title_zh: 按需检索有用信息：选择性检索增强机器翻译的智能体强化学习
authors:
- Shijun Li
- Yang Liu
- Najmeh Sadoughi
- Dongmei Wang
- Xinjie Li
- Zhu Liu
- Rohith Mysore Vijaya Kumar
- Yuzong Liu
affiliations:
- The University of Texas at Austin
- Amazon
arxiv_id: '2610.19528'
url: https://arxiv.org/abs/2610.19528
pdf_url: https://arxiv.org/pdf/2610.19528
published: '2026-10-14'
collected: '2026-10-15'
category: RAG
direction: 选择性检索增强 · 强化学习
tags:
- Selective Retrieval
- RAG
- Machine Translation
- Reinforcement Learning
- Plackett-Luce
- Contrastive Retriever
one_liner: 提出 SRAT，将检索作为可学习翻译动作，用 GRPO 与检索器对齐实现选择性检索增强
practical_value: '- **把“是否调用外部知识”变成策略动作**：不要固定 always-retrieve 或 never-retrieve，用
  GRPO 以最终业务指标（如转化率、用户满意度）为奖励，让模型学习何时检索、生成什么查询。可以用于商品文案生成、客服回复等场景，避免无关知识干扰。

  - **检索器要与下游质量对齐，而不是语义相似度**：当知识库检索难度高、语义相似度不够时，用翻译/生成质量对比训练检索器，让正样本由“哪个文档能提升最终输出”决定。这可以迁移到推荐解释生成、广告标题生成等任务，直接用最终打分函数提供监督。

  - **黑盒模型也能受益**：训练一个独立的轻量检索策略（如 Qwen 小模型），用闭源大模型（Claude/GPT）的输出质量作为奖励，不动主模型参数也能提升其生成效果。适合在已有黑盒生成服务之上加一层自适应检索。

  - **课程学习避免策略退化**：先用高质量检索轨迹做 SFT 初始化，再 RL 时加临时检索惩罚防止模型退化成 never-retrieve。这个 trick
  对任何需要学习“何时调用工具”的 Agent 场景都适用。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：现有 RAG 翻译系统对所有输入统一检索，但翻译是“部分证据”任务——很多输入靠 LLM 参数知识已足够，检索只在少数情况有益，且基于语义相似度的检索可能引入噪声甚至损害翻译。因此需要学习何时检索、检索什么。

**方法关键点**：
- **策略建模**：将翻译过程建模为轨迹，动作包括推理（<think>）、检索（<tool_call>）、翻译（<answer>）。策略可自由选择直接翻译或检索，从最终翻译质量学习。
- **GRPO 训练**：对每个源句采样多条轨迹，用 COMET+LLM 评判混合质量作为奖励，组内竞争学习何时值得检索、生成什么查询。
- **检索探索课程**：先用高质量检索轨迹 SFT 初始化，再 RL 时临时加检索惩罚防止模型塌缩到从不检索。
- **检索器对齐**：提出两种方法。联合 Plackett-Luce 策略梯度：将 top-k 检索改为有序采样，使文档选择有对数概率，轨迹奖励可反向更新检索器；翻译质量对比训练：固定翻译器，用每个候选文档对翻译质量的实际影响构建正负样本，提供低方差直接监督。

**关键实验**：在 IdiomKB、RAGtrans、Document-MT-LLM 三个数据集上，SRAT 均超过 never-retrieve 和 always-retrieve 基线。例如 IdiomKB Zh→En 上 COMET 从 0.812 升至 0.822，MQM 从 -4.01 升至 -2.74；RAGtrans En→Zh 上 GRF 从 0.920 升至 0.939，MQM 改善 0.82。检索率按任务自适应（30.6%~88.6%）。对比训练在默认检索准确率仅 56.3% 的 RAGtrans 上提升最明显（准确率升至 70.7%，MQM 改善 6.8%）。冻结 Claude 作为翻译器时，训练独立的检索策略也能提升其翻译质量（RAGtrans MQM 改善 12.4%~16.8%）。

**最值得记住的一句话**：检索应被视为可学习的翻译动作，通过最终翻译质量对齐检索器和策略，而不是固定的预处理步骤。
