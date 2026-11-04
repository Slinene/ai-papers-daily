---
title: 'LEANGUARD: Lean-Verified Guardrails for Tool-Using Agents'
title_zh: LeanGuard：面向工具调用智能体的 Lean 验证护栏
authors:
- Sreehari Sankar
- Debargha Ganguly
- Vikash Singh
- Mohsen Hariri
- Weicong Chen
- Yanyan Zhang
- Shouren Wang
- Wang Yang
- Chaoda Song
- Alexander Nemecek
affiliations:
- Case Western Reserve University
- UT Austin
arxiv_id: '2611.02332'
url: https://arxiv.org/abs/2611.02332
pdf_url: https://arxiv.org/pdf/2611.02332
published: '2026-11-01'
collected: '2026-11-04'
category: Agent
direction: LLM Agent 形式化护栏与自动修复
tags:
- LLM Agents
- Formal Verification
- Runtime Guardrails
- Prompt Injection
- Tool Calling
- Lean 4
one_liner: 在 LLM 智能体与工具之间嵌入 Lean 4 策略运行时，以形式化证明保证每次工具调用合规，并支持反馈或证明引导修复
practical_value: '- 在电商导购/售后 Agent 的写操作（改订单、退款、发券）上，可借鉴“外部策略运行时 + 可信证据”架构：把业务规则写成
  permits/requirements/forbids，所有工具调用先做 fail-closed 校验；关键点是不信 LLM 输出的文本，只信后端快照和监控日志，用户确认绑定到具体提案和状态版本，防止注入礼品卡/收款账户等越权操作。

  - 将拒绝从“调用未执行”改为“失败规则 + 修复提示”，可减少重复试错并提高恢复率；论文中反馈使阻塞调用从 983 降到 719，恢复动作从 34 增至 48。售后场景可返回具体缺失条件（如需先读订单、需用户确认）而非笼统拒绝。

  - 证明引导修复对参数值类违规很实用：当金额超预算、支付方式不合规、选错券时，可在规则引擎中预计算最近合规参数并随拒绝返回，或直接替换；论文在 252 个参数值拒绝中证明修复
  88 个，中位 2ms，表明部分修复不必让模型重试。

  - 若业务涉及支付、退款、隐私等强保障环节，可考虑用可验证语言编写核心策略，并检查证明无 sorry/非标准公理；但维护成本高，适合核心高风险写操作而非全量策略。'
score: 8
source: huggingface-daily
depth: full_pdf
---

动机：工具调用智能体在真实业务中经常违反领域策略——要么被工具输出中的注入指令诱导（如把差价打到攻击者礼品卡），要么在缺少确认、未读资源或状态不满足时执行写操作。现有护栏缺少对策略语义的形式保证，拒绝后也没有有效的恢复机制。

方法关键点：
- LeanGuard 作为运行时位于 LLM 与工具之间，所有调用先经 Lean 4 策略评估，fail-closed 拒绝。
- 策略由 permits / requirements / forbids 三类规则组成，结合状态谓词和过去时态算子（PREVIOUS / ONCE / SINCE），可表达“先读后写”“最多修改一次”等时间依赖；支持按 principal、conversation、resource 过滤历史。
- 可信证据来自后端快照和记录日志，模型输出文本不作为证据；用户确认绑定具体提案、状态版本和一次性使用，防止重放或换参。
- 可执行评估器与独立 LeanLTL 语义证明等价，构建时检查，拒绝 sorry 和非标准公理。
- 两种纠正：反馈返回失败规则与提示，由模型修复；证明引导修复用 Lean 元编程搜索附近调用并返回 kernel 检查的可采纳证明，无需模型。

关键实验：
- τ²-bench 五个 Qwen 模型：未护栏时执行至少 33 个被 Lean 策略禁止的调用；LeanGuard 执行 0 个；反馈下任务成功率 72.7% vs 70.9%，无显著下降。
- DTap 直接提示注入成功率从 57.9% 降至 5.9%，间接从 22.3% 降至 3.8%；电信良性任务成功率不变。
- 反馈减少重复阻塞调用（983→719），恢复动作从 34 增至 48，四个模型任务成功提升。
- 证明引导修复在 252 个参数值拒绝中证明修复 88 个，中位 2ms。

最值得记住的一句话：对 Agent 的写操作，把策略校验放在工具边界并做成形式化、fail-closed 的运行时，才能把合规从“模型自觉”变成“外部可验证”。
