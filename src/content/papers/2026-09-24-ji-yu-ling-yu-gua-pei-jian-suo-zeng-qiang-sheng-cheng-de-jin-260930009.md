---
title: Automated Regulatory Compliance Question Answering in Financial Services with
  Domain-Adapted Retrieval-Augmented Generation
title_zh: 基于领域适配检索增强生成的金融合规自动化问答
authors:
- Tobias Deußer
- Abhishek Pillai
- Aurelio F. Bariviera
- Dhananjay Bhardwaj
- Lorenz Sparrenberg
- David Berghaus
- Christian Bauckhage
- Rafet Sifa
affiliations:
- University of Bonn
- Lamarr-Institute for Machine Learning and Artificial Intelligence
- Universitat Rovira i Virgili
- Fraunhofer IAIS
arxiv_id: '2609.30009'
url: https://arxiv.org/abs/2609.30009
pdf_url: https://arxiv.org/pdf/2609.30009
published: '2026-09-24'
collected: '2026-09-25'
category: RAG
direction: RAG 领域适配与忠实性评估
tags:
- RAG
- Legal NLP
- Domain Adaptation
- LoRA
- Retrieval
- Regulatory Compliance
one_liner: 用三阶段领域适配检索器与 RAFT-LoRA 微调紧凑模型，显著提升合规问答召回但暴露 grounding 评估缺口
practical_value: '- 检索器领域适配可采用三阶段训练：entailment tuning 将 question-passage 匹配重构为 premise-hypothesis
  重建，再用 in-batch negatives 做对比学习，最后与 BM25 做 score-level fusion，能大幅提升 Recall@10。

  - 生成侧用 4-bit 量化的 2B-12B 小模型 + RAFT-LoRA 微调可提升答案质量，且对小模型收益更大；适合对延迟和成本敏感的场景，但需注意 RAFT
  需要检索上下文。

  - 评估 RAG 生成质量时，RePASs 这类综合分不能证明忠实性：闭卷模型得分与全 pipeline 仅差 0.011，却不引用且误报义务。业务中必须单独设计
  grounding/citation 评估，不能只看端到端分数。

  - 领域适配后的模型跨域迁移差（文中从 ADGM 规则到澳大利亚判例法失败），若业务要覆盖多法规/多语料，需分别适配或多任务训练。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**
金融机构规则密集且频繁修订，合规问答不仅要求流畅，更需要可验证地锚定权威文本。企业可本地部署的通常是紧凑模型，但紧凑模型容易幻觉义务条款。

**方法关键点**
在 ObliQA（阿布扎比全球市场规则手册构建的 QA 基准）上构建领域适配 RAG pipeline：
- 检索器基于 LegalBERT 分三阶段训练：entailment tuning（把问题-段落匹配重构为前提-假设重建）、对比学习（in-batch negatives）、与 BM25 做分数级融合。
- 生成器为 2B-12B 紧凑模型，4-bit 量化部署；采用提示或 RAFT-LoRA（检索感知微调）适配。

**关键结果数字**
- 三阶段检索器将 Recall@10 从 BM25 的 0.678、E5-large-v2 的 0.758 提升到 0.774，相对初始 LegalBERT 的 0.256 提升约 3 倍。
- RAFT-LoRA 改善所有可适配模型的 RePASs 综合分，最弱模型增益最大。
- 适配模型无法迁移到澳大利亚判例法问题；闭卷模型（无检索）得分与全 pipeline 仅差 0.011，却完全不引用且误报义务。
- 表明检索增益可被直接衡量，但生成增益只是 RePASs 增益而非已证明的 grounding；RePASs 无法评估忠实性。
