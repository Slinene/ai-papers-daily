---
title: 'ODTQA-FoRe: An Open-Domain Tabular Question Answering Dataset for Future Data
  Forecasting and Reasoning'
title_zh: ODTQA-FoRe：面向未来数据预测与推理的开放域表格问答数据集与框架
authors:
- Zhensheng Wang
- Xiaole Liu
- Wenmian Yang
- Kun Zhou
- Yiquan Zhang
- Weijia Jia
affiliations:
- Beijing Normal University
- Beijing Normal-Hong Kong Baptist University
arxiv_id: '2606.02433'
url: https://arxiv.org/abs/2606.02433
pdf_url: https://arxiv.org/pdf/2606.02433
published: '2026-06-01'
collected: '2026-06-02'
category: Agent
direction: 表格问答 · 时间序列预测 · 多Agent协作
tags:
- ODTQA
- Time-series Forecasting
- Agent
- Real Estate
- LLM-based Framework
- SQL Generation
one_liner: 提出首个结合时序预测与表格推理的开放域QA数据集及多Agent框架TimeFore，弥补LLM直接预测的缺陷
practical_value: '- **Agent 角色拆分模式可直接复用**：将复杂开放域预测问答拆为 Retriever（SQL 生成）、Forecaster（调用外部时序模型）、Analyzer（答案标准化）三个
  Agent，每个 Agent 通过 in-context learning + 反馈循环实现可靠输出。在电商销量预测、商品价格趋势问答等场景中，可直接套用此架构，用专门模型弥补
  LLM 预测弱点。

  - **外部预测模型优于 LLM 直接预测**：实验证明 TimeXer 等专用时序模型的 MSE 远低于通用 LLM 的 ICL 预测（2.50e7 vs 6.69e7），因此在实际业务数值预测任务中，无论模型多大，均应通过
  function calling 调用成熟的时序模型，而非强求 LLM 自行拟合。

  - **SQL 生成可用执行反馈自修复**：Retriever 通过执行 SQL 并利用错误信息迭代修正（最多 25 次），能有效提升复杂多表查询的成功率。在电商数据资产查询或报表自动化场景中，这种自校正循环可大幅减少人工介入。

  - **模板生成 + LLM 改写的数据集构建策略**：先用模板生成可验证的 QA 对，再用 LLM 改写以增加语言多样性，保证质量的同时降低人工成本。适合快速构建垂直领域（如房产、金融）的预测型问答评估集。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
当前开放域表格问答（ODTQA）只处理历史数据查询，无法回答“下个月房价会涨吗？”这类需要时序预测和预测后推理的查询。LLM 自身预测能力弱，且缺乏针对未来数据预测的评测基准。为此，论文定义新任务 ODTQA-FoRe，并基于 10 城 2 万+ 房产项目构建首个包含 28,507 条 QA 对的数据集，涵盖直接预测和预测后推理两种问法。

## 方法关键点
- **TimeFore 多 Agent 框架**：将任务分解为三个协作角色：
  1. **Retriever**：先用 LLM 生成表描述，再通过 BM25 检索相关表；然后基于 5-shot 提示生成 SQL，并引入执行-反馈循环修正错误。
  2. **Forecaster**：收到 SQL 历史数据后，通过 function calling 调用 TimesNet 做缺失值填补，再使用 TimeXer 预测未来 12 个月价格，避免 LLM 自身预测不准。
  3. **Analyzer**：先用 BERT 分类问题类型（纯预测 vs. 预测后推理），再选择不同提示模板，最后用 LLM 生成答案，并通过数值抽取模块确保输出简洁数值。
- **数据集构建**：采用 26 套模板生成 QA，保证答案可验证；再用 Qwen2.5-72B 对模板问题改写，提升语言自然度，人工评分从 3.324 提升至 3.936。

## 关键实验
- 对比八种预测模型，TimeXer 在测试集上 MSE=2.50e7，显著优于通用 LLM（Qwen3 30B 为 6.69e7）。
- 在 5 种 LLM 基座上，TimeFore 较 Vanilla（纯 LLM 预测）在预测任务上 MSE 平均降低 30%–50%，在推理任务上 F1 提升 15–30 个百分点（如 Qwen3 30B 上 F1 从 24.87 提升至 60.25）。
- 消融实验显示：给定真实未来数据时推理准确率可达接近上限，指示当前瓶颈主要在预测精度，而非推理能力。

## 一句话总结
“将预测任务外包给专用模型，让 LLM 专注检索与推理的 Agent 分工模式，是破解未来数据问答问题的钥匙。”
