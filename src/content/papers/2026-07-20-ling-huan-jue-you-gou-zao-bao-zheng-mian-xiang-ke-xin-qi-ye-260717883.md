---
title: 'Zero Hallucination, by Construction: Hallucination-Aware Layered Oversight
  for Trustworthy Enterprise AI'
title_zh: 零幻觉，由构造保证：面向可信企业AI的幻觉感知分层监查
authors:
- Bogdan Raduta
- Horia Velicu
- Alexandru Preda
- Serban Chiricescu
affiliations:
- FlowX.AI
arxiv_id: '2607.17883'
url: https://arxiv.org/abs/2607.17883
pdf_url: https://arxiv.org/pdf/2607.17883
published: '2026-07-20'
collected: '2026-07-21'
category: RAG
direction: 幻觉感知的多层防御RAG架构
tags:
- hallucination containment
- grounding
- LLM-as-judge
- calibrated abstention
- drift detection
- evidence-based confidence
one_liner: 提出HALO六层防御架构，将幻觉视为可容错系统属性，通过接地生成、证据信心和校准拒答实现企业AI零幻觉
practical_value: '- 电商/广告搜索中LLM生成内容（如商品属性、广告语）易出现幻觉，可借鉴**证据基置信度**：要求输出中事实片段明确对应检索到的原始文档片段，不依赖模型自身置信度，并在验证失败时触发**校准拒答**，避免向用户展示错误信息。

  - 生成式推荐或 Query 推荐系统可采纳**多信号验证层**：同时用LLM裁判和基于源文档的硬校验（如实体匹配、数值对齐）对生成结果打分，双重把关后再决定是否放出。

  - **全链路可追溯**（检索、工具调用、生成）对推荐系统的 debug 和审计极有价值：快速定位究竟是检索错误还是生成错误导致幻影推荐。

  - **持续监查与漂移检测**适合推荐系统线上效果维护：定期采样对比历史基线，发现生成质量下滑或幻觉率超标时自动告警，并触发重生成与统计验证，形成闭环优化。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：企业信任是大模型落地的核心障碍，主要卡点是幻觉。根本原因并非模型规模不够，而是LLM天然能产生无据文本，仅靠事后裁判或精调检索也无法根除。因此目标应从“消除幻觉”转为“系统层遏制幻觉”。

**方法**：提出HALO（幻觉感知分层监查），由六层防御构成：(1) 基于已审核检索内容的接地生成，杜绝自由发挥；(2) 约束性确定性执行，限定模型可能出错的范围；(3) 多信号验证，结合LLM裁判与证据基检查（直接比对源文档）对每条输出打分；(4) 校准拒答，接地不足时直接拒答而非猜测；(5) 全链路可追溯，记录每次检索、工具调用与生成；(6) 持续监查，检测分布漂移并触发阈值告警，通过再生与统计验证闭环。关键创新在证据基置信度：不信任模型自报的信心，而是验证抽取内容是否确实出现在源文档中。

**结果**：以保险理赔提取为示例，展示架构在严格监管场景下实现零幻觉输出的可行性，但未给出量化指标。
