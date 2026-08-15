---
title: 'LittleLearner: Language Models Under Pedagogically Controlled Knowledge Exposure'
title_zh: LittleLearner：基于小学课程受控知识暴露的语言模型
authors:
- Fanfei Li
- Jana Zeller
- Manuel Prada-Corral
- Thaddäus Wiedemer
- Prasanna Mayilvahanan
- Ryan Cotterell
- Wieland Brendel
affiliations:
- MPI-IS
- Ellis Institute
- ETHZ
arxiv_id: '2608.13545'
url: https://arxiv.org/abs/2608.13545
pdf_url: https://arxiv.org/pdf/2608.13545
published: '2026-08-13'
collected: '2026-08-15'
category: Training
direction: 受控课程预训练 · 知识边界与注入评估
tags:
- LLM
- Pretraining Corpus
- Knowledge Boundaries
- Curriculum Learning
- Evaluation
one_liner: 构建88B token K-5语料并训练5B模型，提供研究知识边界与注入的受控沙盒
practical_value: '- 借鉴课程过滤思路构建电商领域语料：用分类器或规则明确排除超出业务范围（如非在售品类、无关知识）的文本，降低模型幻觉与无关能力浪费。

  - 评估知识边界可指导业务 LLM 上线：设计类似“是否知道某品类/政策”的探测题，判断模型是否具备真实业务知识，避免依赖 RAG 或微调误以为能注入新能力。

  - 论文发现 post-training 与 ICL 只能更好地利用已有知识，不能提升 out-of-scope 能力。对电商 Agent 的启示：新品类或新政策若完全未在预训练中出现，仅靠检索或少样本提示可能无效，需考虑持续预训练或数据回灌。

  - 低成本沙盒模型适合快速验证训练策略：业务中可先训一个小规模受控模型做消融，验证数据配比、课程顺序或知识注入方法，再迁移到大模型。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：现代 LLM 在异构网络语料上训练，先验知识暴露难以刻画，导致知识获取研究困难。本文希望创造一个知识边界清晰、可解释的训练环境。

**方法关键点**：
- 构建 LITTLECURRICULUM：从 FineWeb-Edu 中过滤出 88B token，仅保留美国小学 K-5 水平内容，显式排除 5 年级以上概念、事实和词汇。
- 从零训练 5B 参数模型 LITTLELEARNER，得到具有足够语言能力但知识范围严格受限的模型。
- 实验：通过 post-training 和 in-context learning 注入新知识，检验能否突破原有知识边界。

**关键结果**：
- LITTLELEARNER 在开放式评估中表现良好，且能力边界与课程指南对齐，例如能回答简单算术和哺乳动物常识，但对 ln(0) 等超范围问题难以处理。
- 后训练和 ICL 只能让模型更好利用已有知识，不能提升 out-of-scope 能力，说明新知识注入的局限性。
- 发布的语料和模型为后续研究 scaling、post-training 与知识获取提供了受控沙盒。
