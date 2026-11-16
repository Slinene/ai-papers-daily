---
title: 'MEM-SQL: Memory-Empowered Text-to-SQL'
title_zh: 记忆赋能 Text-to-SQL：历史查询复用与按需 Schema 链接
authors:
- Xiaoqi Wang
- Wenqi Pei
- Shizheng Hou
- Yilai Liu
- Han Chen
- Boyan Li
- Yuyu Luo
- Hongyang Du
affiliations:
- NICE Lab, The University of Hong Kong
- National University of Singapore
- The Hong Kong University of Science and Technology (Guangzhou)
arxiv_id: '2611.18338'
url: https://arxiv.org/abs/2611.18338
pdf_url: https://arxiv.org/pdf/2611.18338
published: '2026-11-12'
collected: '2026-11-16'
category: LLM
direction: Text-to-SQL · 分层历史记忆复用
tags:
- Text-to-SQL
- Memory
- History Reuse
- Schema Linking
- Cost Efficiency
- LLM
one_liner: 分层历史 SQL 记忆与按需 schema 链接，在 HARE 上提升执行准确率并大幅降低 token 与延迟
practical_value: '- 将已验证的历史生成结果（SQL / query 改写 / 广告文案）分层缓存：整句模板 / 可复用片段 / 领域概念到 schema
  映射；每层只在其匹配度阈值达标时使用，有效避免每次从零生成并降低 token 成本。

  - 借鉴 On-demand Schema Linking：当记忆缓存命中且生成器判断证据充分时跳过完整 schema 注入，只回退到全量 schema 当无层匹配或证据不足；类似在
  query 推荐中优先使用历史相似 query 及其结构化信息，降低大模型输入长度和延迟。

  - 工程实现中可记录每次生成结果由哪些组件复用、哪些需要编辑，构建请求难度画像；针对“多查询组合/共享 join”类复用做专门训练或设计更强的重排/合并模块，因为这类场景准确率下降明显。

  - 该记忆架构对成本敏感的大规模生成服务（电商搜索推荐文案、商品描述改写）有直接迁移价值：在 6 个 LLM 上平均 token 减少 76.6%、延迟降 68.8%，同时准确率提升。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有 Text-to-SQL 基准独立评估每个问题，忽略同一数据库上的历史查询可为新问题提供 join 和计算逻辑。论文提出 HARE 基准，由 823 个已验证查询构建 1600 个请求，标注保留组件和编辑类型，衡量历史 SQL 复用的准确率和成本。

**方法关键点**：MEM-SQL 将历史 SQL 组织为三层记忆：整查询模板、可复用 SQL 块、领域概念到 schema 元素映射。每层仅在所有要求匹配度超过该层阈值时使用；On-demand Schema Linking (OSL) 只有在无层达标或生成器判断证据不足时才查询 schema，大幅减少输入长度。请求按可重用程度区分整查询适配、部分复用等场景。

**关键结果**：在 6 个语言模型上，HARE 平均执行准确率从无历史直接生成的 37.1% 提高到 50.0%，输入 token 减少 76.6%，延迟降低 68.8%。进一步分析表明，复用多个已验证查询的请求仍是瓶颈，准确率从 56.7% 降至 29.7%，尤其当复用组件需要重新排列结构或合并共享 join 时。OSL 应用于其他记忆设计都能降低成本，但准确率收益取决于记忆设计。
