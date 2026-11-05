---
title: 'Kierston & KierstonBench: Simulation of Allentown, PA and Evaluation of Language
  Models in Crime Investigation and Surveillance Tasks'
title_zh: Kierston 与 KierstonBench：模拟阿伦敦市并评估语言模型的犯罪调查与监控能力
authors:
- Andrew Semenov
- Svyatoslav Dorofeev
affiliations:
- Kiz8 Team
arxiv_id: '2611.04785'
url: https://arxiv.org/abs/2611.04785
pdf_url: https://arxiv.org/pdf/2611.04785
published: '2026-11-02'
collected: '2026-11-05'
category: Eval
direction: LLM 在仿真犯罪调查环境下的评估
tags:
- LLM
- Simulation
- Benchmark
- Record Linkage
- Agent Evaluation
- Ground Truth
one_liner: 构建城市级仿真引擎 Kierston 与基准 KierstonBench，评估 LLM 跨源记录关联与案件调查推理能力
practical_value: '- 借鉴仿真环境 + 已知 Ground Truth 的评测思路：在电商/推荐 Agent 中构建用户行为仿真器，生成浏览、购买、广告曝光等多源日志，注入已知目标事件（如转化、欺诈），用于评估
  Agent 的归因与决策能力，而非依赖线上 A/B。

  - 受限记录接口设计可迁移到隐私合规的推荐数据访问：模型只能通过查询接口跨源关联，不直接接触原始全量数据，与联邦/隐私计算场景相似，可作为多源数据融合 Agent
  的工程约束。

  - 任务家族分层（记录关联 → 常规重建 → 事件调查 → 欺骗评估）提供细粒度能力画像：可借鉴用于评估推荐解释、异常检测、用户行为归因等 Agent 的推理链路，尤其关注模型在证据不足时是否弃权，避免幻觉推荐或错误归因。

  - 结论 "frontier model 仍会陷入常见欺骗与假设" 提醒：引入证据链审计和弃权机制，在推荐 Agent 里对低置信度推荐强制输出依据或放弃推荐，防止过度自信。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：LLM 越来越多用于犯罪调查与监控记录分析，但真实场景缺乏 ground truth 难以评测模型结论准确性，缺乏仿真基准。

**方法**：提出 Kierston 城市级仿真引擎，模拟宾夕法尼亚州阿伦敦约 125,000 名居民的日常活动，并生成电信、金融、行政、车牌等多源记录；这些记录源于同一行为时间线，但分散在不同数据源。KierstonBench 基于该环境，模型通过受限记录接口跨源查询和关联证据，无法访问底层仿真。基准包括 32 个任务家族，覆盖记录关联、日常活动重建、事件调查和欺骗性账户评估。

**结果**：评估 16 个 LLM，大多数无法有效开展记录调查，会提交记录不支持的身份认定；少数 frontier 模型解决大部分任务，并在证据不足时选择弃权，但仍会陷入常见欺骗和假设，没有模型能完全替代人类调查员。
