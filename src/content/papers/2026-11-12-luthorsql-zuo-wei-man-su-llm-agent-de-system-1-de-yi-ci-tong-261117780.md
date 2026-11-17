---
title: 'LuthorSQL: A One-Pass Text-to-SQL Model as System 1 for a Slower LLM Agent'
title_zh: LuthorSQL：作为慢速 LLM Agent 的 System 1 的一次通过 Text-to-SQL 模型
authors:
- Ibrahim Memon
- Armin Karamzade
- M. Hanif Jhaveri
- Roy Fox
affiliations:
- UC Irvine
- Independent Researcher
arxiv_id: '2611.17780'
url: https://arxiv.org/abs/2611.17780
pdf_url: https://arxiv.org/pdf/2611.17780
published: '2026-11-12'
collected: '2026-11-17'
category: Agent
direction: Agent 工具使用降本 · 快速 gate
tags:
- Text-to-SQL
- System 1-System 2
- LLM Agent
- Non-autoregressive
- Cost Reduction
- Confidence Cascade
one_liner: 7B 非自回归模型单次前向生成候选 SQL 并验证，作为快速 System 1 gate 升级到慢速 LLM Agent，节省成本且保持精度
practical_value: '- **用 7B 小模型做 System 1 gate 承接高频简单查询**：电商/广告内部报表、运营自助取数、数据问答等场景，可用本地单
  GPU 部署的量化模型直接处理常见查询，仅将低置信度请求升级到外部大模型 agent，能显著降低 API 成本与敏感数据外泄风险。

  - **非自回归 + 候选执行验证的架构值得迁移到生成式推荐/搜索**：一次前向预测 bounded grammar 上的 slot scores，批量编译执行
  32 个候选 SQL/计划，再用轻量 validator 选优，比逐 token 自回归快一个量级。对应到推荐系统，可生成多个候选 query/文案/商品标题，用执行结果或轻量排序器快速筛选，避免大模型多次采样。

  - **置信度级联（confidence cascade）可直接用于 LLM 调用频次高的环节**：设定小模型置信度阈值，低于阈值才升级到大模型，结合业务数据校准阈值可保证精度不降。适用于搜索
  query 改写、广告文案生成、商品属性抽取等，可省 30%+ 外部 API 调用成本。

  - **8-bit 量化后小模型 9GB 显存可跑，零样本迁移多方言 SQL**：本地推理可行性高，且迁移到 Snowflake/BigQuery/MySQL/PG/DuckDB
  精度损失 <3.1 点，说明可低成本维护多引擎适配。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**

前沿 LLM agent 工具查询数据库虽准确，但每次调用托管模型慢、贵，且暴露组织敏感查询。例如 Claude Opus 5.5 agent 每天服务 1 万次查询，年成本超 7 万美元。核心问题：能否利用组织现有本地硬件卸载负担且不牺牲精度？

**方法关键点**

LuthorSQL 是一个 7B 非自回归 Text-to-SQL 模型，作为快速 System 1 gate，与慢速 LLM agent（System 2）组成级联，仅在不确定时升级到外部模型。模型单次前向在 bounded grammar 上预测 slot scores，编译并执行最多 32 个候选 SQL 计划，用训练得到的 validator 选择最终答案。

**关键结果**

单独使用时，LuthorSQL 在 BIRD hidden test 上 execution accuracy 达到 68.03%，单 GPU 延迟 0.84 秒/问题；8-bit 量化后 9GB 显存保持精度；零样本迁移到 Snowflake、BigQuery、MySQL、PostgreSQL、DuckDB 精度与原生 SQLite 相差 3.1 点以内。与 Claude Opus 5.5 在 227 个 post-cutoff 数据库问题上做预注册置信度级联，本地回答近一半问题，API 成本降低 33.3%，精度不变。污染探测显示 Opus 无 schema 时逐字复现 48–92% 公开基准 gold queries，但 tool-assisted 精度在改名 schema 上保持，在 post-cutoff 数据库上达 95.6–97.4%。
