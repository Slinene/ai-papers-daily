---
title: 'Projecting BrowseComp-Plus onto ClimbMix: Toward More Realistic Corpora for
  Agentic Search'
title_zh: 将 BrowseComp-Plus 投影到 ClimbMix：构建更真实的智能搜索评估语料
authors:
- Sahel Sharifymoghaddam
- Lingwei Gu
- Yijun Ge
- Jimmy Lin
affiliations:
- University of Waterloo
arxiv_id: '2608.20317'
url: https://arxiv.org/abs/2608.20317
pdf_url: https://arxiv.org/pdf/2608.20317
published: '2026-08-20'
collected: '2026-08-23'
category: Eval
direction: Agentic search 评估 · 语料投影
tags:
- agentic search
- benchmark construction
- corpus projection
- evidence grounding
- retrieval evaluation
one_liner: 提出数据集无关的投影流水线，把 BrowseComp-Plus 问题证据迁移到 553M 文档的 ClimbMix，得到 57 个高置信评估样本
practical_value: '- 构建离线评估集时，如果现有语料规模小且由 benchmark 自身支持文档和 hard negatives 组成，可以用投影
  pipeline 把问题映射到大规模通用语料，再用自动验证+独立 agent+人工复核筛出证据完整的样本，避免评测泄漏和检索难度失真。

  - 原子 reasoning hop 分解 + 逐 hop 证据定位的流程可以直接迁移到 RAG 或搜索 Agent 的训练/评测数据清洗，确保每个推理步骤都有对应文档支撑，减少幻觉式回答。

  - 检索质量是 agentic search 的瓶颈：即使最终答案准确率只降 5 个点，evidence recall 从 84.3% 跌到 21.4% 说明检索侧严重不足。业务中应把
  evidence recall 作为独立监控指标，与下游任务指标解耦。

  - 发布的 projection pipeline 和 benchmark 可作为固定语料评估的模板，适合需要分离 Agent 推理能力与检索器能力的场景，例如电商搜索、推荐理由生成、客服
  Agent 评测。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：BrowseComp-Plus 用固定语料替代不稳定的网页搜索，但语料只有约 10 万文档，且由 benchmark 自身问题的支持文档和 mined hard negatives 构成，证据和干扰项都按 query 选择，难度不够真实。

**方法关键点**：核心贡献是一个数据集无关的投影流水线：将每个问题分解为原子 reasoning hops，在 ClimbMix（NVIDIA 发布的 400B token、553M 文档通用网页文本混合）中逐 hop 定位证据；只有自动验证、独立 agent 和人工审查三方都确认每个 hop 有支撑时，才保留该问题。投影不依赖任何 benchmark 构造信息，可应用于任何可分解为可验证事实的问答基准。

**关键结果**：对 830 个 BrowseComp-Plus 测试问题投影，得到 57 个完全 grounded 的问题，并带有 question-level 相关性标注。投影后难度明显转向检索：最强 agent 的回答准确率下降 5 个点，evidence recall 从 84.3% 降至 21.4%，搜索调用次数增加 63%。代码、基准和分析已发布。
