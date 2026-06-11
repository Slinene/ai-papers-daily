---
title: 'CORE-Bench: A Comprehensive Benchmark for Code Retrieval in the Era of Agentic
  Coding'
title_zh: 面向智能编码的代码检索综合基准 CORE-Bench
authors:
- Fuwei Zhang
- Yanzhao Zhang
- Mingxin Li
- Dingkun Long
- Lexiang Hu
- Pengjun Xie
- Zhao Zhang
- Fuzhen Zhuang
affiliations:
- Beihang University
- Peking University
arxiv_id: '2606.11864'
url: https://arxiv.org/abs/2606.11864
pdf_url: https://arxiv.org/pdf/2606.11864
published: '2026-06-10'
collected: '2026-06-11'
category: Eval
direction: 代码检索基准与Agent编码评估
tags:
- code retrieval
- benchmark
- agentic coding
- embedding models
- fine-tuning
one_liner: 提出三层级代码检索基准，揭示Agent编码场景下检索性能急剧下降，微调可显著提升
practical_value: '- 对于电商智能体（如自动化客服、商品信息管理）需要从代码库或结构化知识库中检索上下文时，可借鉴 CORE-Bench 的三层级评估框架（代码理解、问题定位、广泛上下文）来设计更全面的检索评估指标。

  - 实验表明在 Agent 检索场景下，对通用嵌入模型简单微调即可大幅提升性能，这提示在构建垂直领域检索系统（如商品描述与用户意图匹配）时，可基于少量领域标注数据微调现有嵌入模型，低成本提升上线效果。

  - CORE-Bench 揭示了传统代码搜索与 Agent 状态化检索之间的显著差距，类似地在电商推荐 Agent 中，从单纯文本匹配到需要结合会话状态、库存状态的上下文检索也存在鸿沟，需专门构建评测与优化方案。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：现有代码检索基准局限于独立片段的自然语言匹配，无法反映 Agent 编码场景中基于仓库状态定位文件、函数及上下文的需求。
**方法**：构建 CORE-Bench，涵盖代码理解、问题到编辑定位、广泛上下文检索三个层级，基于代码搜索任务和 SWE-bench 实例，包含超 18 万条查询和 10.6 万条上下文相关性标签。
**结果**：代表性嵌入模型在该基准上的性能相较传统代码搜索大幅下降，而简单监督微调后可显著提升，表明 Agent 编码检索仍有巨大改进空间。
