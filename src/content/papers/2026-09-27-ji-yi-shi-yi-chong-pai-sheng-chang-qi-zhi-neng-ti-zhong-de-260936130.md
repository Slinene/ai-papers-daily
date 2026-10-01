---
title: 'Memory Is a Derivation: The Distributed-Evidence Paradox in Long-Term Agents'
title_zh: 记忆是一种派生：长期智能体中的分布式证据悖论
authors:
- Hongjun Liu
- Chen Zhao
affiliations:
- New York University
arxiv_id: '2609.36130'
url: https://arxiv.org/abs/2609.36130
pdf_url: https://arxiv.org/pdf/2609.36130
published: '2026-09-27'
collected: '2026-10-01'
category: Agent
direction: Agent 长期记忆写入审计
tags:
- Agent Memory
- Memory Verification
- Factuality
- Distributed Evidence
- Admission Control
- LLM Agents
one_liner: 提出 DERIVAUDIT 审计框架，揭示记忆写入中证据分散导致有效记忆被误拒、无效组合更难检测的分布式证据悖论
practical_value: '- 在电商/推荐 Agent 的用户长期记忆系统中，不要只保存单轮抽取事实，应将“写入门控”做成派生验证：对每条候选 memory
  用写入前历史做 BM25 检索补充证据（如 top-12、总 budget 16），避免因 writer 附带 citations 不全而误删有效信息；该方法在论文中使
  provenance-repaired 保留率从 58–86% 提升到 93–98%。

  - 对记忆进行组合语义校验，显式拆解语义义务：区分事实、关系、时态/状态变化，例如用户历史中“计划购买某品类”和“有高消费偏好”不能组合成“已购买该品类”或“因高消费而购买”；可使用
  SUPPORTED / CONTRADICTED / INSUFFICIENT / AMBIGUOUS 四路标签替代简单 yes/no。

  - 注意验证粒度悖论：让 verifier 检查更多细粒度正确事实（增加检查项）可能显著降低有效记忆准入率（Gemma 从 93.3% 掉到 2.6%）。在线上
  admission gate 中，不要盲目增加检查项或抬高 threshold，需按模型分别校准，并监控有效记忆留存率。

  - 下游效果量化：失真记忆和缺失记忆都会大幅降低后续回答/推荐质量（失败率增加 84–100pp）。可借鉴其干预实验，对用户画像或 Agent memory 注入
  distortion / 删除 valid 条目，测量下游任务失败率变化，以确定记忆质量的实际业务影响。'
score: 8
source: huggingface-daily
depth: full_pdf
---

动机：长期运行 LLM Agent 将历史交互压缩为持久记忆，后续任务常把它当作既定事实复用。但记忆写入可能出现两类错误：引文不全使有效记忆看似无据；多个单独成立的事实被组合成历史从未支持的新关系。现有工作多关注记忆召回，少审计写入时历史是否真正支持其完整语义。

方法关键点：
- 定义语义派生完整性，提出 DERIVAUDIT 审计框架，围绕证据范围、组合有效性、准入可靠性三问。
- 证据范围：对比 writer 附带的 citations 与扩展的 pre-write 历史（BM25 检索 top-12，总 budget 16 篇 passage），独立标注同一记忆。
- 组合有效性：将记忆分解为语义义务，要求所有义务均被支持；四路标签 SUPPORTED / CONTRADICTED / INSUFFICIENT / AMBIGUOUS，双模型标注加盲审裁决；比较 holistic、atomic claim、predicate–argument QA 与 compact relation、composition graph、per-obligation 等验证视图。
- 准入可靠性：回放 citation-only、expanded-history holistic、expanded-history obligation-aware 三种写入时验证；引入 accumulated verification noise，要求 verifier 检查更多已知为真的义务。

关键实验与数字：
- 数据：400 个未编辑记忆写入（LoCoMo / HaluMem-Medium 各 200），391 个有 resolved 标签；70 个匹配 family 控制 local/distributed evidence；512 条受控 suite。模型：Qwen3-30B-A3B、Gemma-4-31B、Llama-3.3-70B-Instruct。
- 扩展历史恢复约 60% 因引文不足而不支持的记忆；但仍有约 1/5 在扩展后仍不支持。
- 不支持记忆仍被频繁准入（59–89%），且扩展证据在 Llama 上反而恶化。
- provenance-repaired 保留率在扩展历史下显著提升：Qwen 82.1%→93.8%，Gemma 58.0%→95.5%，Llama 85.7%→98.2%。
- 组合验证存在 trade-off：Qwen 上 compact relation 检测不支持关系 59.5% 同时保留 multi-span 有效记忆 94.9%，而 atomic 检测仅 16.5%；Gemma 的 per-obligation 检测 98.7% 但 multi-span 保留降至 76.9%。
- 分布式证据悖论：分布式证据下，Qwen holistic / obligation-aware 对无效组合检测仅 8.6% / 11.4%；移除充分证据可使拒绝翻转 88–100%。
- 检查 4 个额外正确义务导致 Gemma 准入率 93.3%→2.6%，Llama 97.4%→35.5%。
- 下游：失真记忆增加 83.8–93.0pp 失败率，移除有效记忆增加 92.8–99.5pp 失败率。

最值得记住：记忆写入可靠性的核心不是“找到更多证据”，而是验证证据是否支持进入持久记忆的完整语义；分布式证据同时增加了有效组合的难度与无效组合的伪装性。
