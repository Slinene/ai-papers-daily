---
title: 'Parser States Already Know: Structure-Conditioned KV Persistence for Structured
  Generation'
title_zh: 解析器状态指导的结构化生成 KV 缓存持久化
authors:
- Linze Wu
- Xinrui Chen
affiliations:
- Hangzhou Institute for Advanced Study, University of Chinese Academy of Sciences
arxiv_id: '2608.28276'
url: https://arxiv.org/abs/2608.28276
pdf_url: https://arxiv.org/pdf/2608.28276
published: '2026-08-28'
collected: '2026-08-31'
category: LLM
direction: LLM 推理优化 · 结构化生成 · KV 压缩
tags:
- KV Cache Compression
- Structured Generation
- Constrained Decoding
- Parser States
- LLM Serving
- Function Calling
one_liner: 利用约束解码的解析器状态设计离线校准的 KV 持久化策略，大幅提升结构化生成在压缩推理下的可靠性
practical_value: '- 电商 Agent 中大量 JSON/function call 输出，可直接复用 constrained decoding
  暴露的 parser states 作为 KV 保留信号。例如将必需字段、枚举值、参数名标记为高保护 bucket，避免压缩导致关键 schema 信息丢失，降低下游调用失败率。

  - 借鉴「离线校准 + 线上查表」的工程化方式：用开发集离线测量每个结构标签+层组的任务错误敏感性和注意力失真，生成策略表；线上只做轻量查找和常量预算状态更新，适合低延迟、高并发推荐/搜索
  Agent 服务。

  - 任务错误敏感性设置保护下限比单纯依赖注意力分数更可靠。在推荐理由生成、商品参数抽取等结构化任务中，优先保护影响最终可执行性的 token（如字段名、枚举值），可以显著提升压缩后的可靠性。

  - 分层分组思路：同一结构角色在不同 Transformer 层采用不同精度（低层低精度、高层高精度），可迁移到长上下文推荐模型或多轮 Agent 对话的 KV
  管理，进一步节省显存。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

## 动机
结构化生成是 LLM Agent 执行 JSON、SQL、function call 的核心，一个字段错误就会导致下游动作失败。约束解码虽能保证语法合法，但解析器状态中暴露的 token 结构角色（必需字段、枚举值、参数名等）在决定合法 token 后就被丢弃。现有 KV 压缩主要依靠注意力显著性、量化误差或最近性，未利用这种任务级结构化风险，导致模型侧 KV 重要性与结构化任务失败风险不匹配。

## 方法关键点
- **PASK**（Parser-Aware Structural KV Persistence）将约束解码产生的 parser 转移结构标签（class, role, state, next）与 Transformer 层组结合，形成持久化 bucket；每个 bucket 分配 RELEASE / RETAIN-LOW / RETAIN-HIGH 三种动作。
- **离线校准**：用任务错误敏感性设置保护下限（确保关键结构不被过早丢弃），用注意力输出失真排序分配剩余 KV 容量；在开发集上选择满足可靠性容忍度的最低成本策略，编译成查找表。
- **在线查表**：解码时只做结构条件查找和常量预算状态更新，无需在线重要性估计，开销极低。另有轻量 prefill companion 对 prompt token 做类似压缩。

## 关键实验
在 BFCL 非 live 和 Live 子集上评估 Qwen3-4B 和 Qwen3-14B。总 KV 预算约 0.33 时，Qwen3-4B 上 PASK 在 8 个子类别平均比最强压缩基线 TriAxialKV 高 17.39 个百分点；非 live 总体准确率 88.00%（Full KV 91.83%，TriAxialKV 78.67%），Live 总体 72.01%（Full KV 75.22%，TriAxialKV 58.57%）。端到端 serving 峰值 GPU 内存约为 Full KV 的 0.53×（降低约 47.5%），吞吐量最高提升 2.2×，TPOT 最高降低 3.3×。消融显示移除任务错误保护下限后，满足相同可靠性门限所需 decode 预算从 50.08% 增至 98.49%，验证了保护下限的关键作用。

**最值得记住的一句话**：Parser states 已经包含结构化风险信息，用任务错误敏感性设置保护下限、注意力失真做剩余分配，可在低 KV 预算下显著保住结构化生成可靠性。
