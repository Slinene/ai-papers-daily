---
title: 'FinanceComplexQA: Benchmarking Agentic Reasoning on Industrial-grade Financial
  Documents'
title_zh: FinanceComplexQA：面向工业级金融文档的代理推理基准
authors:
- Xianfu Cheng
- Shiwei Zhang
- Jiyu Zhao
- Jian Yang
- Xinyuan Wang
- Ming Zhou
- Weixiao Zhou
- Xiangyuan Guan
- Xiang Li
- Zhenhe Wu
affiliations:
- Beihang University
- Microsoft, China
- Multilingual-Multimodal-NLP
- Langboat Technology
- Shenzhen Intelligent Strong Technology Co.,Ltd.
arxiv_id: '2607.19238'
url: https://arxiv.org/abs/2607.19238
pdf_url: https://arxiv.org/pdf/2607.19238
published: '2026-07-20'
collected: '2026-07-25'
category: Eval
direction: Agent 评估基准 · 金融文档 QA
tags:
- Agentic Reasoning
- Financial QA Benchmark
- RAG
- Complex Layouts
- Agent-as-a-Judge
- Synthetic Data Generation
one_liner: 提出一个包含2026道深度研究题、2000份合成专业文档的金融文档QA基准，用于评测Agent与RAG系统的复杂推理能力
practical_value: '- **复杂场景评测构建**：可借鉴其基于领域专家知识合成高难度文档与QA对的流水线，为电商搜索推荐中的Agent评测构建真实、多维度的测试集，尤其关注多跳推理、数值计算和业务分析能力。

  - **Agent-as-a-Judge自动化评估**：对于电商Agent的开放式生成输出（如推荐理由、用户洞察），可直接复用其多维指标+LLM评判方式，替代昂贵的人工标注。

  - **复杂布局处理**：论文对表格、图文混排等复杂文档的解析与推理评估，提醒我们在商品详情页、用户评论等非纯文本场景的RAG系统需强化布局感知能力。

  - **失败案例分析驱动迭代**：借鉴其按能力维度（数值、多跳等）归类失败案例的方法，系统性地定位推荐Agent的短板，指导架构优化。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：金融文档分析要求数值精准、领域知识和事实可靠，但现有基准缺乏复杂布局、深度推理和真实场景覆盖，Agent性能差异巨大。为此，需构建一个贴近工业级应用的评测集，系统诊断代理推理的薄弱环节。

**方法**：设计 Finance-LaTeX SKILL，基于专家知识合成带复杂版式的金融文档，并通过Agent工作流生成2000份专业文档及6000对高质量QA。在此基础上构建FinanceComplexQA基准，包含2026个深度研究任务，覆盖六大金融场景和七类任务（如多跳推理、数值计算、行业分析），支持中英双语。评估采用Agent-as-a-Judge机制，结合多维指标实现自动化、稳定评分。

**结果**：对前沿RAG系统与代理推理工具进行全面评测，揭示在数值计算、多跳推理、内容摘要等任务上的普遍失败模式，为后续提升提供了清晰的能力雷达图。
