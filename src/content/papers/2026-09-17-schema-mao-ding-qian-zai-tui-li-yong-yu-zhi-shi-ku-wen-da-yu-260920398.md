---
title: Schema-Anchored Latent Reasoning for Semantic Parsing-Based Knowledge Base
  Question Answering
title_zh: Schema 锚定潜在推理用于知识库问答语义解析
authors:
- Guangze Gao
- Zixuan Li
- Sikui Zhang
- Chunfeng Yuan
- Wenjuan Li
- Bing Li
- Xiaolong Jin
- Weiming Hu
affiliations:
- Institute of Automation, Chinese Academy of Sciences
- Institute of Computing Technology, Chinese Academy of Sciences
- University of Chinese Academy of Sciences
arxiv_id: '2609.20398'
url: https://arxiv.org/abs/2609.20398
pdf_url: https://arxiv.org/pdf/2609.20398
published: '2026-09-17'
collected: '2026-09-19'
category: Reasoning
direction: LLM 潜在推理 · 知识库问答语义解析
tags:
- KBQA
- Semantic Parsing
- Latent Reasoning
- LLM
- Schema Alignment
- Codebook
one_liner: 在 LLM 隐藏状态进行连续潜在思维，通过 schema codebook 对齐与反馈延迟离散决策，提升 KBQA 语义解析组合问题性能
practical_value: '- 对于需要多步生成结构化输出的任务（如商品筛选、广告定向、query 改写），可以把连续潜在状态作为中间表示，避免在每个推理步过早离散选择类目/属性/Semantic
  ID，降低错误传播。可在 Transformer 中引入专门 reasoning steps，训练时对齐真实结构化标签。

  - 从已有的 query-结构化目标成对数据（query-LF、query-商品条件）自动构造中间对齐信号，类似 schema traces，无需人工推理轨迹标注，用于训练
  codebook 或离散 tokenizer，将连续表示映射到业务 schema（类目体系、属性值、行为事件）。

  - 在 LLM Agent 多工具调用之间维护潜在状态，延迟提交工具参数，并用可学习 codebook 将潜在状态对齐到工具 schema 可提升复杂任务规划成功率。工程上可固定
  LLM 主干，仅训练 codebook 和投影层，实现低成本落地。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

动机：在 KBQA 语义解析中，LLM 需从大规模异构知识库选择关系/类并组合为逻辑形式（LF）；现有方法在中间推理步提前离散化选择 schema 元素，错误决策会传播导致错误 LF。

方法关键点：SALR 利用模型隐藏状态进行多步连续思维，延迟显式 LF 决策；引入 KB schema 元素的 codebook，通过与 gold LF 确定性派生的 schema traces 对齐目标，将连续思维对齐到 schema 编码；把对齐后的 schema code 作为输入注入后续推理步，形成 schema 中介反馈；全程不要求模型输出显式文本推理轨迹。

关键结果：在 GrailQA 和 WebQSP 上相比强基线一致提升；在 GrailQA 组合问题上比 SP 基线 TIARA 高 2.86 F1；分析表明 schema 中介反馈影响 LF 生成，且 schema 信息可从潜在状态恢复。
