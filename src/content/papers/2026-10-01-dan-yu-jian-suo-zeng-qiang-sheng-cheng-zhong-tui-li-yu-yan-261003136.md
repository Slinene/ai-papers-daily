---
title: Investigating the Role of Reasoning-Language Alignment in Monolingual Retrieval-Augmented
  Generation
title_zh: 单语检索增强生成中推理语言对齐的作用研究
authors:
- Oliver Hauck
- Mario Sanz-Guerrero
- Katharina von der Wense
affiliations:
- Johannes Gutenberg University Mainz
- University of Colorado Boulder
arxiv_id: '2610.03136'
url: https://arxiv.org/abs/2610.03136
pdf_url: https://arxiv.org/pdf/2610.03136
published: '2026-10-01'
collected: '2026-10-11'
category: RAG
direction: 单语RAG推理语言对齐
tags:
- RAG
- Reasoning Language Alignment
- Multilingual LLM
- German QA
- Agentic RAG
one_liner: 在德语RAG问答中，对齐推理语言与查询文档语言可提升表现，但无法超越无约束英语推理
practical_value: '- 构建多语言RAG评测集时，可采用小众虚构领域（如特定游戏世界）迫使模型依赖检索而非内部知识，避免记忆污染，验证检索能力。

  - 多语言业务（如跨境电商、多语种搜索）中，若需要LLM进行推理回答问题，不强制其推理语言与用户语言一致可能获得最佳性能；但若追求可解释性而强制推理语言，对齐查询/文档语言（如德语对齐德语）优于不对齐的强制语言（如法语），且性能接近无约束英语推理上限。

  - 在agentic RAG循环中，使检索上下文更丰富和结构化（如保留文档结构信息）会增强推理语言对齐带来的收益，提示工程中可优先采用结构化文档表示。

  - 可复用结论：模型的语言熟练度并非决定RAG性能的唯一因素，语言对齐本身有独立贡献，因此在实际系统中应根据业务需求在可解释性与性能之间权衡，不必盲目强制英语推理。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有推理模型主要用英语生成推理链，已有研究表明强制模型使用非英语推理会降低准确率，但该结论仅在短提示上下文中验证。RAG场景要求模型读取和整合大量目标语言证据，推理语言对齐的作用未知。

**方法**：构建了完全德语单语的RAG问答测试平台，基于桌面角色扮演游戏《The Dark Eye》的虚构世界。该领域有丰富的德语文档但过于小众，模型无法凭记忆回答，必须依赖检索。在agentic RAG循环中，强制推理语言分别为德语、英语、法语或无约束，比较问答准确率。

**关键结果**：推理语言与查询和检索文档对齐有助于性能提升。强制德语推理优于强制法语推理，尽管模型在法语基准上表现更高，说明收益来自对齐而非语言熟练度。当检索上下文更丰富、具有结构感知时，对齐优势进一步增大。不过，强制德语推理仅达到无约束英语推理的水平，未能超越，表明当前模型仍需原生多语言推理能力才能完全发挥RAG潜力。
