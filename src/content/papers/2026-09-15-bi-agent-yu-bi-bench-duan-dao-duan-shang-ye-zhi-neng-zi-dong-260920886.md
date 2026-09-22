---
title: 'BI-Agent and BI-Bench: Towards Automating End-to-End Business Intelligence'
title_zh: BI-Agent 与 BI-Bench：端到端商业智能自动化 Agent 与评测基准
authors:
- Chuxuan Hu
- Yeye He
- Penny Zhou
- Wee Hyong Tok
- Daniel Kang
- Surajit Chaudhuri
affiliations:
- UIUC
- Microsoft Research
- Microsoft
arxiv_id: '2609.20886'
url: https://arxiv.org/abs/2609.20886
pdf_url: https://arxiv.org/pdf/2609.20886
published: '2026-09-15'
collected: '2026-09-22'
category: Agent
direction: LLM Agent + 数据管理工具 + 后训练
tags:
- BI
- Agentic Tools
- Post-training
- Benchmark
- Data Management
- LLM
one_liner: 构建首个真实 BI 端到端基准 BI-Bench，并设计工具增强 Agent 与后训练框架，使 8B 模型以 50 倍低成本匹敌大模型
practical_value: '- 将数据管理专用算法（join 预测、表重塑、表检索）封装成工具，由 LLM 负责编排调用，而不是让它直接编写所有数据处理代码；电商场景做多表特征拼接、宽表生成、指标口径治理时可复用这种“领域工具
  + 通用 LLM”分工。

  - 合成训练轨迹可借鉴：先从真实业务项目构造 join 后的宽表，让 LLM 生成 query 和标注答案，再混入无关表并施加逆变换制造难样本，大幅降低训练数据标注成本；适合推荐
  Agent、Text-to-SQL 或语义层维护。

  - RLVR 奖励设计对可验证结果使用分档奖励（完全正确 / 部分正确 / 失败）加格式惩罚，能给小模型提供密集学习信号；在商品知识问答、报表生成等有可验证输出的任务中可直接套用。

  - 建立内部评测集可参考 BI-Bench：从真实 dashboard 导出 query-result 对，做多 ground truth 增强和 LLM-assisted
  审核，但不以模型可解为筛选标准，避免评测集失真。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：传统 BI 工作流要求用户完成表选择、数据转换、join 关系定义等前置步骤，耗时且对非技术用户不友好。现有 NL2SQL 基准聚焦干净表上的最终分析，无法反映真实 BI 端到端挑战。

**方法关键点**：
- BI-Bench：抓取 3000+ 个公开 Power BI 项目，从真实 dashboard 手工提取 100 个 (查询, 答案表) 对；每个项目平均 10.6 张表、12.75 个 join 关系，最大 52 张表、700 万行，覆盖销售、金融、教育等领域。
- BI-Agent：以 LLM 为编排器，提供四个工具——代码执行、transform（表重塑预测）、join（面向雪花/星型 schema 的连接预测）、search（保守表筛选）。将数据管理专用算法工具化，降低 LLM 在处理复杂表结构时的失败率。
- 后训练：从真实 BI 项目合成训练任务。先按项目的 join 图采样子图并物化成宽表，让 LLM 生成 query 和可执行代码得到答案表；再混入无关表、以一定概率施加逆表重塑变换制造难样本；最后生成多步轨迹，仅保留执行结果与答案表一致的轨迹做 SFT。RL 采用 GRPO，奖励分档：完全正确 +1-0.1n、部分正确 -0.5-0.1n、失败 -1-0.1n，并只对 tool-call 块优化。

**关键结果**：仅用 SQL 时，最强前沿模型 o4-mini 在 BI-Bench 上准确率只有 48.2%；在 BIRD/Spider 排行榜靠前的 NL2SQL 系统准确率骤降至 6.0-26.3%。BI-Agent 的工具设计使前沿 LLM 平均提升超 10 个百分点，最高 40 个点；对 Qwen3-8B 做 SFT+RL 后，准确率可与 GPT-5.5 等大模型相当，成本最高降低 50 倍，后训练最高再提升 30 个点。

**最值得记住的一句话**：把领域专用数据管理算法封装成可调用工具，并用合成轨迹做域内后训练，是让中小模型在复杂端到端数据任务上以极低成本追平大模型的有效路径。
