---
title: Evaluating Open-Weight LLMs for Turkish Domain Documents Under Retrieval and
  Hardware Constraints
title_zh: 评估土耳其语领域文档中开放权重 LLM 的检索与硬件约束表现
authors:
- Imtiaz Ul Hassan
- Öykü Akbulut
- Onur Kaya
- Ardhendu Behera
- Swagat Kumar
- Peter Matthew
- Yonghuai Liu
affiliations:
- Edge Hill University, United Kingdom
- Ermetal Otomotiv ve Eşya San. Tic. A.Ş., Türkiye
arxiv_id: '2609.28007'
url: https://arxiv.org/abs/2609.28007
pdf_url: https://arxiv.org/pdf/2609.28007
published: '2026-09-23'
collected: '2026-09-27'
category: RAG
direction: RAG 评估与本地硬件约束
tags:
- RAG
- LLM-Evaluation
- Turkish-NLP
- Quantization
- Document-QA
one_liner: 提出证据标注评估协议，分离检索失败与推理失败，发现 4-bit 量化下字符 TF-IDF 检索基线足够强
practical_value: '- **证据标注评估协议可复用**：为每个问题标注证据位置，不增加额外模型调用即可把错误拆成「检索没召回」和「模型读到了但答错」。电商/推荐场景做
  RAG 或知识库问答评估时，直接照搬这套标注方式，能快速定位是召回侧还是 LLM 生成侧的问题。

  - **不要盲目追复杂检索器**：7 种 lexical、dense、hybrid 检索配置在统计检验下都没显著超过字符 TF-IDF 基线。业务上如果文档量不大、语言形态丰富（如土耳其语、商品标题/详情），可以先上字符
  TF-IDF，再逐步验证 dense/hybrid 的真实增益。

  - **4-bit 量化 + 6GB VRAM 本地部署可行**：7B-8B 模型在 RTX 3050 上可跑文档问答，端到端准确率 49%-75%。对需要数据隐私或低成本推理的电商客服/选品分析场景，有参考价值；但要注意模型间差异和证据召回饱和现象。

  - **统计检验优于看平均分**：用 95% Wilson 区间和配对 McNemar 检验比较检索配置，能避免少量样本上的假增益。做策略 AB 测试或检索方案对比时，建议引入同类显著性检验。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：现有土耳其语 LLM 多用通用基准评估，缺乏面向长、结构复杂领域文档的真实评测；同时本地硬件约束下开放权重模型的表现也缺少系统分析。

**方法关键点**：
- 构建 100 道人工验证题目，分别来自 109 页工业 R&D 报告和 112 页公共部门报告。
- 提出证据标注评估协议：每个问题标注证据位置，从而在不额外调用模型的情况下区分检索失败与下游推理失败。
- 5 个 7B-8B 开放权重模型，在 NVIDIA RTX 3050 6GB VRAM 上，使用受控 prompting、decoding 和 4-bit 量化本地评估。
- 比较 7 种 lexical、dense、hybrid 检索配置，用 95% Wilson 区间和配对 McNemar 检验做统计比较。

**关键结果**：
- 主基准端到端准确率在 49%-75% 之间。
- 没有任何检索配置显著超过字符 TF-IDF 基线。
- 证据召回饱和程度在两份报告上表现不同，说明检索和有效上下文容量可能成为某些文档的瓶颈，但并非所有文档都受限。
