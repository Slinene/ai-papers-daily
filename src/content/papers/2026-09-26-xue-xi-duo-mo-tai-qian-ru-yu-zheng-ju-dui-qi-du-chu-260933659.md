---
title: Learning Multimodal Embeddings with Evidence-Aligned Readout
title_zh: 学习多模态嵌入与证据对齐读出
authors:
- Zirong Chen
- Fuda Ye
- Enjun Du
- Junfu Pu
- Xinlei Wang
- Xinyu Zuo
- Lisheng Duan
- Haijin Liang
- Jin Ma
- Jiachuan Wang
affiliations:
- The Hong Kong University of Science and Technology (Guangzhou)
- Tencent Yuanbao
- Tsinghua University
- ARC Lab Tencent
- The University of Hong Kong
arxiv_id: '2609.33659'
url: https://arxiv.org/abs/2609.33659
pdf_url: https://arxiv.org/pdf/2609.33659
published: '2026-09-26'
collected: '2026-10-08'
category: Multimodal
direction: 多模态嵌入检索 · 证据对齐读出
tags:
- Multimodal Embeddings
- Evidence Generation
- Contrastive Retrieval
- Boundary Readout
- MLLM
one_liner: EviAlign 将语义证据生成与边界读出耦合，在共享 MLLM 中按语义单元边界读取状态，提升多模态检索嵌入质量
practical_value: '- 可借鉴「生成证据 + 边界读出」的嵌入训练方式：让 MLLM 先按语义单元（如实体、属性、关系、场景）生成结构化证据，在每个单元边界读取
  hidden state 后 mean pooling 作为最终向量，相比只取末尾 hidden state 能提升检索 Recall@1，且保持单向量索引，线上
  ANN 检索成本不变。

  - 在电商/搜索的多模态商品或内容表示中，可以用生成任务强制模型在特定语义边界产生可读状态，联合 contrastive retrieval 目标训练；生成部分不一定要作为最终特征，但能起到对齐读出位置、增强表示的作用。

  - 若业务中已经使用 LLM 生成 CoT、标签或文案，不建议只把生成文本作为额外特征输入；利用生成过程的中间状态做读出，可能获得更紧凑、更适配检索的单向量表示。

  - 论文发现仅靠证据组织本身增益有限，需与证据边界读出共同设计；因此在工程实现时，要同时调整训练目标的证据 span 和读出位置，不能只改 prompt 或只改
  pooling。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：多模态大语言模型能生成任务相关证据，但证据如何进入检索嵌入并未被有效利用；希望检验证据的语义组织能否决定向量读出位置。

方法关键点：EviAlign 在共享 MLLM 中将语义证据生成与边界读出耦合。证据被组织为五个语义单元，模型在每个单元边界读取 contextualized state，再聚合成一个归一化嵌入。训练时同时使用生成损失和对比检索损失联合优化。

关键结果：使用相同 trailing readout 时，语义证据与自由形式 CoT 的检索性能几乎相同，说明证据组织本身不解释全部增益。受控 2×3 实验中，在一致的语义组织下，五个读出状态与 mean pooling 相比 length-based 训练位置的 0.65 点优势提升到证据边界读出的 2.39 点，获得 1.74 点 co-design 交互增益。在 12 个 MMEB 检索任务上，EviAlign 使用 500K 训练对达到平均 76.9 Recall@1，同时保持单向量索引和评分。
