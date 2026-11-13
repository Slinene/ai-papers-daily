---
title: 'CARTBench: Rubric-Based Evaluation of Shopping Advice for Complex and Ambiguous
  Requests with Timelines'
title_zh: CARTBench：基于评分准则的复杂模糊时间线购物建议评估
authors:
- Yuqin Dai
- Zhanwei Zhang
- Honghui Yang
- Zhouheng Yao
- Yueqi Zhang
- Jingyu He
- Chaoyang Shi
- Fanding Wei
- Boyuan Pan
- Kai Xu
affiliations:
- Zhejiang University
- Xiaohongshu Inc.
- Tsinghua University
- Shanghai Jiao Tong University
arxiv_id: '2611.05862'
url: https://arxiv.org/abs/2611.05862
pdf_url: https://arxiv.org/pdf/2611.05862
published: '2026-11-03'
collected: '2026-11-13'
category: Eval
direction: LLM 购物助手评估 · Rubric
tags:
- LLM Shopping Assistant
- Benchmark
- Rubric Evaluation
- Timeline
- Product Recommendation
- Safety
one_liner: 构建 CARTBench 基准与原则引导 Prompting，量化 LLM 购物助手理解到执行的差距
practical_value: '- 用 case-specific rubrics 替代单一分数评估复杂购物对话：按 Core / Excellence / Safety
  分层，要求模型链接产品证据、显式处理未解决需求，能更细粒度定位推荐失败原因，适合迁移到电商导购 Agent 的离线评测。

  - Ideal Response Principles 的蒸馏方法：从成功订单的人工精选回复中归纳原则，再作为 prompt 或评分准则，可复用到对话式推荐、售前咨询等场景，低成本提升输出质量。

  - 时间线约束下需求会动态变化（如礼物截止日期、已有物品清单），模型需持续追踪对话状态并校验商品证据；这提示在电商 Agent 中要设计持久化记忆和约束检查模块。

  - 将 Safety 作为独立评估维度，对高风险品类（如孕产、婴儿用品）设置硬性安全准则，可作为上线前的自动质检门禁。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：LLM 购物助手在多轮对话中推荐商品，但可靠评估面临数据稀缺和标准难以统一两大障碍。现有基准缺乏带时间线的复杂、模糊购物需求，且评分主观。

**方法关键点**：构建 CARTBench 基准，从 17 个零售领域真实商业购物需求中整理案例，包含带时间戳的对话和 1,603 条商品记录；提出 Ideal Response Principles，从成功订单的人工精选优秀回复中归纳原则，用于生成 case-specific rubrics，分为 Core、Excellence、Safety 三层，共 1,328 条专家标注准则。这些原则同时指导 Principle-Guided CART Prompting，一种结构化推荐策略。

**关键结果**：在冻结 rubrics 下评测 7 个商业 API 模型（包括 GPT-6.1-Sol 和 Claude-Opus-5）及 35B+ 参数开源模型，10 个模型中 3 个在 Core 超过 90%，但没有任何模型在 Excellence 超过 45%，暴露出理解到执行的差距。诊断发现共同失败集中在产品证据缺失和未解决需求，并与需求随时间变化、决定性未知相关。
