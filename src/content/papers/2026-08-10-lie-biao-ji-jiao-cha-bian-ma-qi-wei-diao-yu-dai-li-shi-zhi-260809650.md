---
title: 'Listwise Cross-Encoder Fine-Tuning vs. Agentic Instruction Tuning for LLM
  Rerankers: A Systematic Study in Medical Procedure Reranking'
title_zh: 列表级交叉编码器微调与代理式指令微调的LLM重排序对比研究
authors:
- Matan Fainzilber
- Shlomit Plavner
affiliations:
- Healthee
arxiv_id: '2608.09650'
url: https://arxiv.org/abs/2608.09650
pdf_url: https://arxiv.org/pdf/2608.09650
published: '2026-08-10'
collected: '2026-08-11'
category: RecSys
direction: 重排序系统 · 小模型微调 vs 大模型指令调优
tags:
- reranking
- cross-encoder
- instruction tuning
- listwise LTR
- medical IR
- scalability
one_liner: 109M参数的交叉编码器微调ListNet后，NDCG@3比4B指令重排序模型高2.6点，参数仅1/37
practical_value: '- 在电商搜索/推荐重排序中，若资源及延迟敏感，可优先考虑小参数交叉编码器+ListNet 微调，性能可能反超大模型。

  - 利用 GPT-4 等大模型自动构建查询-商品/文档对的数据集管道，可低成本构建领域训练数据。

  - 代理式提示优化（agentic prompt optimization）的思路可迁移至推荐系统提示工程，自动化调优 LLM 重排序器的提示词。

  - 部署时权衡延迟——小模型推理成本低，适合实时重排序；大模型可留作离线评估或数据生成。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

## 动机
患者用日常语言查询医疗覆盖，而保险系统使用临床术语，词汇鸿沟导致重排序困难。需比较不同重排序范式的实际效果。

## 方法
1. **小模型微调**：使用 MedCPT 和 MiniLM-L12（最多 109M 参数），冻结不同层，用 ListNet 等列表级损失微调交叉编码器。
2. **大模型指令调优**：使用 Qwen3-Reranker-4B，通过 GPT-4.1 驱动的代理优化循环迭代优化提示。
3. 构建包含 2647 个查询、708 个保险服务的专用数据集。

## 结果
- 109M 参数交叉编码器用 ListNet 微调后，NDCG@3 比 4B 模型高 2.6 个百分点，Spearman 相关性高 13.3 点。
- 参数量仅为对方的 1/37，推理成本更低。
- 研究还提供了可扩展的 LLM 数据集构建方案及部署权衡。
