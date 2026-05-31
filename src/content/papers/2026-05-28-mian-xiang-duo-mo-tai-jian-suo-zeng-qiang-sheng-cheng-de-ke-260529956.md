---
title: Uncertainty Quantification for Multimodal Retrieval Augmented Generation
title_zh: 面向多模态检索增强生成的可学习不确定性量化
authors:
- Simon Binz
- Heydar Soudani
- Faegheh Hasibi
affiliations:
- Radboud University
- German Research Center for Artificial Intelligence (DFKI)
arxiv_id: '2605.29956'
url: https://arxiv.org/abs/2605.29956
pdf_url: https://arxiv.org/pdf/2605.29956
published: '2026-05-28'
collected: '2026-05-31'
category: RAG
direction: 多模态RAG · 不确定性量化
tags:
- Uncertainty Quantification
- Multimodal RAG
- Vision-Language Models
- Token Probabilities
- AUROC
one_liner: 提出LeMUQ，通过分析输入扰动下的token概率信号来量化多模态RAG的不确定性，AUROC平均提升3.8%
practical_value: '- 输入扰动策略（去除图像/检索上下文）生成多视角概率信号，再通过微调模型集成这些信号，可用于电商多模态RAG系统的答案置信度估计，辅助拒识或人工审核。

  - 将 token 概率编码为特殊概率 token 的设计可迁移至生成式推荐的不确定性建模，例如为 Semantic ID 序列生成添加置信度 token 以控制多样性。

  - 方法对检索噪声鲁棒，跨检索器泛化实验表明适合电商搜索增强的问答，能缓解错误检索导致的不可靠回答。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：多模态检索增强生成（RAG）结合视觉-语言模型（VLM）与外部知识，但生成答案可能错误或误导。现有不确定性量化（UQ）方法专为纯文本设计，难以捕捉多模态RAG中检索、视觉理解和生成阶段产生的复合不确定性。

**方法**：提出 LeMUQ，一种可学习的多模态 UQ 方法。核心思路是**有目的地移除输入模态或检索上下文**（如去掉图像、去掉检索到的文本），收集 VLM 在多个扰动下的 token 概率信号。这些信号被编码为特殊的“概率 token”，输入到微调过的 VLM 中，使模型能显式建模模态与检索交互带来的不确定性。

**结果**：在多个数据集、检索器和 VLM（如 LLaVA、InstructBLIP）上，LeMUQ 平均 AUROC 提升 3.8%，优于基线 UQ 方法和微调方法。对检索器变化具有强泛化能力，但跨 VLM 迁移时效果存在差异。
