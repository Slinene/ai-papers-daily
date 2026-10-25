---
title: 'AfterDeleteBench: Auditing Post-Deletion Information Persistence in LLM Agents'
title_zh: AfterDeleteBench：审计 LLM Agent 删除后信息持久化
authors:
- Ehsan Saleh
- Roozbeh Nahavandi
- Sama Salarian
- Raef Bassily
- Andrew Perrault
affiliations:
- The Ohio State University
arxiv_id: '2610.31366'
url: https://arxiv.org/abs/2610.31366
pdf_url: https://arxiv.org/pdf/2610.31366
published: '2026-10-22'
collected: '2026-10-25'
category: Agent
direction: LLM Agent 记忆删除审计
tags:
- LLM agents
- memory deletion
- benchmark
- privacy
- post-deletion persistence
one_liner: 用对照实验量化 LLM Agent 删除记忆后仍可从派生状态恢复秘密的比例
practical_value: '- 删除审计必须覆盖派生状态：用户删除原始对话或记忆后，摘要、向量库、RAG 索引、日志等仍可能泄露；上线“被遗忘权”前应建立“暴露后删除
  vs 从未暴露”对照行为回归测试，不应只看存储层记录是否消失。

  - 用来源感知闭包做级联清除：维护每条记忆的 provenance，删除源记录时同步移除或重生成其派生摘要和嵌入，能显著降低删除后的可恢复性；仅做精确字面写过滤无法擦除已经扩散的信息。

  - 评测接口本身会影响恢复率：自动化合规审计或红队测试需统一输出格式与解析器，避免目标内容实际存在但因格式不符被误判为未泄露，影响安全指标可信度。

  - 对 Agent 记忆系统引入行为级隐私视角：即使模型权重固定、无逐字留存，分离存储的敏感组件在公开组合规则下也可被模型重建；设计记忆存储时不要保留可组合的敏感片段。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

动机：LLM agent 通常维护外部持久记忆，并派生摘要等额外状态。删除原始记忆记录后，其派生状态可能仍携带信息，使敏感内容在后续会话中可被恢复，但缺乏系统性审计基准。

方法：AfterDeleteBench 构建固定权重 LLM agent 的对照行为审计。对每个合成秘密，比较“暴露后删除”agent 与“从未暴露”但其他条件匹配的 agent；恢复成功可归因于原始暴露。测试单一查询恢复、组件分离存储下的组合重建、格式/解析器对齐对测量影响，以及写回过滤与新鲜会话回忆的关系。

关键结果：基础设置中，单次查询从 Qwen2.5-7B-Instruct 恢复已删除秘密的比例约 2/3，从未暴露对照恢复率为 0。即使完整秘密字符串不存在，仅各组件分开存储并依赖公开组合规则，跨 Qwen、Mistral、Phi-3 的精确重建成功率达 62–99%。响应接口与解析器不匹配会把含目标回复误判为失败。来源感知闭包在测试的正基线设置中消除了观测到的恢复；精确字面写过滤可阻止重插入，但不能抹除已存在信息。结论：源删除应作为 agent 及其记忆系统层面的行为审计，而非仅存储操作。
