---
title: 'Plans Don''t Persist: Why Context Management Is Load Bearing for LLM Agents'
title_zh: 计划不持久：为何上下文管理对LLM代理至关重要
authors:
- Aman Mehta
- Anupam Datta
affiliations:
- Snowflake AI Research
arxiv_id: '2606.22953'
url: https://arxiv.org/abs/2606.22953
pdf_url: https://arxiv.org/pdf/2606.22953
published: '2026-06-21'
collected: '2026-06-26'
category: Agent
direction: Agent 上下文管理 · 计划衰减测量
tags:
- context management
- plan decay
- replay pairing
- reasoning models
- hidden state
- strict stripping
one_liner: 发现标准LLM代理将计划存于上下文而非内部状态，计划信号4-12倍衰减，且推理模型存在重推导污染
practical_value: '- 在构建电商搜索/推荐代理时，若采用ReAct等框架，长任务中切勿轻易压缩或驱逐计划文本——计划信号会因上下文丢失而快速衰减，导致任务失败率陡增34.7pp。

  - 可通过 replay pairing 方法诊断关键信息（如约束、工具schema）是上下文驻留还是内部持久化，避免上下文压缩时的隐蔽损坏。尤其对推理模型（DeepSeek-R1等）需使用
  strict stripping 去除 <think> 重推导污染，否则测量失真。

  - 计划衰减探针（如L32 Ridge回归）可提前4-5步预警行为偏差，适合用作代理的上下文监控器，在计划信号低于阈值时主动回注计划，无需等到动作偏离。

  - 推理模型的 <think> 痕迹会不断重推导计划内容，可作为自然冗余，但依赖其完全恢复仍不现实；在压缩关键上下文前，需先验证代理是否已将信息内化。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：长时程LLM代理常需压缩、摘要或驱逐旧上下文以适配有限窗口。但若被驱逐的信息（如任务计划）未被模型内化，则行为会无声崩溃。计划通常最早写入、最常使用、最早被驱逐，因此是检验上下文管理可信度的尖锐用例。

**方法关键点**
- 提出 **replay pairing**：对同一轨迹运行两次，A保留计划，B重放相同动作与观察但移除计划，计算隐藏状态余弦距离作为计划忠信度信号。
- 区分上下文记忆（重读文本）与持久内部状态（内容离开窗口后仍存活），并设计 **strict stripping** 修复推理模型的实验污染：因推理模型的 `<think>` 块会重推导计划内容，标准配对会低估信号；去除B侧完整 `<think>` 块后恢复真实信号。
- 在 Llama-3.1-70B/8B、DeepSeek-R1-Distill-70B、Qwen3-32B 等上用 ALFWorld（文本家庭环境）和 HotpotQA 进行跨领域/跨模型验证，并训练 Ridge 探针进行衰减检测。

**关键结果**
- 在 ALFWorld 上，计划信号在步骤+1 跳至 0.453，一回合作观循环内衰减 4.1×（HotpotQA 达12.4×），5步后趋于零。
- 探针 AUROC 0.999（含步骤泄漏），但跨领域迁移零样本 AUROC 1.000，表明方向具领域不变性。
- 推理模型经 strict stripping 后信号恢复 +163%，且 R1 自探针 AUROC 1.000，但其编码方向与 Llama 相差 89.3°。
- 压缩压力测试：朴素驱逐计划使任务成功率从 56.7% 降至 22.0%（-34.7pp），单纯保护计划或探针回注均无法恢复，说明计划防护是必要诊断但非充分修复策略。

**最值得记住的一句话**：在标准 LLM 代理中，计划是上下文驻留对象，没有权重层面的备份；任意压缩都可能瞬间破坏代理的连贯性。
