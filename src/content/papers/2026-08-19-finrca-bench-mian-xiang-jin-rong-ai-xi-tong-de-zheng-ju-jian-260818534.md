---
title: 'FinRCA-Bench: Benchmarking Evidence Retrieval and Reasoning for Financial
  AI Systems'
title_zh: FinRCA-Bench：面向金融 AI 系统的证据检索与推理基准测试
authors:
- Pratik Ghawate
arxiv_id: '2608.18534'
url: https://arxiv.org/abs/2608.18534
pdf_url: https://arxiv.org/pdf/2608.18534
published: '2026-08-19'
collected: '2026-08-23'
category: Eval
direction: RAG 证据检索与推理分离评估
tags:
- RAG
- benchmark
- evidence retrieval
- reasoning
- root cause analysis
- financial AI
one_liner: 提出 FinRCA-Bench，分离检索失败与推理失败，量化证据检索架构对金融对账根因诊断准确率的影响
practical_value: '- 电商交易纠纷、支付对账、风控诊断等场景中，证据通常分散在订单、支付、履约、客服等多张表且靠事务关系而非文本相似；可借鉴 TPGR
  思路，用 Typed Provenance Graph 沿订单号、支付单号等持久化关系做受限遍历，而不是纯语义检索，能显著减少噪声 token、提高必需证据召回。

  - 评估系统时不要只看最终答案准确率：把证据召回、证据契约覆盖率与推理正确性分开打点，定位瓶颈。论文发现检索失败远多于推理失败（95 vs 15），业务上应优先优化
  retrieval 结构而非反复调 prompt 或换模型。

  - 对结构化程度高的问题，Rules/SQL 和经典 ML 仍很强（95.44%），不要盲目上 LLM；LLM 更适合处理规则难覆盖的非结构化和需要解释的场景，结构化部分用确定性规则或
  GBDT 等传统模型保证稳定可审计。

  - 可复用 evidence contract 评估方法：为每个 case 标注必需的 record 级证据集合，独立评估返回证据的精确性与完整性；对推荐/排序解释、广告归因等需要审计的业务，也可以建立证据契约，避免“正确结论但不可解释”。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：LLM 用于金融运营诊断时，证据分散在发票、采购订单、付款、台账、银行流水等多张表中，靠事务关系而非文本相似连接。仅看最终答案会把证据获取能力与推理能力混淆。

**方法**：构建 FinRCA-Bench，包含 2,250 个应付账款到银行对账案例，覆盖 14 张操作表，注入 1,500 个失败案例（15 类根因）和 750 个合法/难负例。根因标签和 record 级证据契约对模型隐藏，独立评估检索与推理。对比 Rules/SQL、经典 ML、稠密语义检索、关系扩展和 Typed Provenance Graph Retrieval（TPGR，默认拒绝的 typed 遍历，仅允许持久化事务关系）。

**结果**：Rules/SQL 准确率 84.97%，经典 ML 达 95.44%。固定推理模型、prompt 和生成配置，仅改变检索：宏级必需记录召回从 0.83% 提升到 77.70%，16 类精确准确率从 2.05% 提升到 72.44%（配对差异 70.39 个百分点，95% bootstrap CI 66.06–74.72）。TPGR 使用更少记录（19.56 vs 40）和更少源 token。结构检索失败与推理失败的比例为 95:15；254 个正确预测发生在检索不完整时，严格返证契约准确率仅 5.72%。结论：检索架构强烈影响 AI 系统表现，正确根因标签不能保证可审计诊断。
