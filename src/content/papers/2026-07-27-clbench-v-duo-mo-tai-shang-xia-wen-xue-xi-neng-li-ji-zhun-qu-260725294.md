---
title: 'CLBench-V: Evaluating Multimodal Context Learning from Grounding to Knowledge
  Acquisition'
title_zh: CLBench-V：多模态上下文学习能力基准，从定位到知识获取
authors:
- Lai Wei
- Chengqi Li
- Jiapeng Li
- Ruina Hu
- Yue Wang
- Weiran Huang
affiliations:
- Shanghai Jiao Tong University
- Zhongguancun Academy
- Shanghai Innovation Institute
arxiv_id: '2607.25294'
url: https://arxiv.org/abs/2607.25294
pdf_url: https://arxiv.org/pdf/2607.25294
published: '2026-07-27'
collected: '2026-08-01'
category: Eval
direction: 多模态上下文学习基准与能力分析
tags:
- Multimodal
- Context Learning
- Benchmark
- Vision-Language
- LLM Evaluation
- Grounding
one_liner: 首个多模态上下文学习基准，解耦上下文定位、信息应用与知识学习三维度，揭示模型严重不足
practical_value: '- **多模态RAG与Agent的评估方法论**：可借鉴三维度分类（上下文定位、新信息应用、新知识学习）来诊断Agent在电商商品详情页、广告落地页等多模态上下文中的能力瓶颈，比单纯端到端准确率更细粒度。

  - **自动构建评估任务的低成本流水线**：论文的自动构造+过滤方法可直接用于生成商品描述理解、图文手册合规性检查等领域的评测数据，降低人工标注成本。

  - **模型选型参考**：InternVL 3.5 在上下文定位和知识学习上更强，Qwen3.5-Plus 擅长信息应用，指导选型：若业务强依赖从图中提取新规则（如活动规则解读），宜选前者；若侧重直接应用给定信息（如表格问答），后者更优。

  - **长多文上下文评估启示**：论文分析了上下文长度、图片数量对性能的影响，可启示在商品详情页多图、长文档检索场景下，需针对性优化模型的长上下文窗口和跨图推理。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有上下文学习评测集中在纯文本，而真实场景多为多模态（科学图表、财务报告、地图、网页等），模型从多模态上下文中提取并应用信息的能力系统性评估缺失。

**方法**：构建基准CLBench-V，将任务解耦为三个维度——上下文定位（回答从哪里来）、新信息应用（基于上下文执行规则/格式转换）、新知识学习（从上下文学习全新概念并推理）。结合经改造的公开基准和新构造数据集，覆盖科学、金融、长文档、空间推理、网页VQA等领域，采用自动构造与过滤减少人工成本。共3443个实例，使用LLM-as-judge评估六款最新多模态模型。

**关键结果**：六模型最佳总分仅0.2847，多模态上下文学习远未饱和。InternVL3.5-30B-A3B在上下文定位和新知识学习上最优，Qwen3.5-Plus在新信息应用上最优；模型普遍在从多模态上下文提取并精确应用信息的环节存在短板，尤其在长上下文和多图场景下表现恶化。
