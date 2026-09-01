---
title: 'EvoUndo: Recoverability-Constrained Self-Evolution for LLM Agent Harnesses'
title_zh: EvoUndo：LLM Agent 自进化的可恢复性约束框架
authors:
- Tanmay Sah
- Dolly Sah
- Harshul Jain
- Tanya Sah
affiliations:
- Independent Researcher
arxiv_id: '2608.28363'
url: https://arxiv.org/abs/2608.28363
pdf_url: https://arxiv.org/pdf/2608.28363
published: '2026-08-27'
collected: '2026-09-01'
category: Agent
direction: LLM Agent 自进化安全与恢复性验证
tags:
- Self-Evolution
- Recoverability
- Agent Harness
- Counterfactual Verification
- Recovery Language
- LLM Agents
one_liner: 提出 EvoUndo，将 witness 捕获、反事实验证、效应合约与分层恢复语言结合，使 LLM 自修改 harness 可验证回滚
practical_value: '- 给业务里的自进化 Agent（自动改 prompt、改工具注册、改配置、改中间件）增加恢复性验证：每个 mutation 必须同时提交
  witness capture 和 recovery program，并用 counterfactual states 做 round-trip 验证，不能只看
  forward capability 提升。

  - 把 effect contract 和运行时副作用 diff 引入 admission：未声明副作用直接拒绝，可防止自动修改静默污染线上状态；这对广告/电商
  Agent 的配置、路由、工具热更新尤其有用。

  - 恢复语言分层设计：L0 覆盖配置/prompt/路由/工具，L1 增加中间件顺序、listener、文件、socket 等结构化状态；诊断粒度不必越细越好——语言受限时给精确
  state address 很关键，语言丰富时粗分类反馈在 gpt-oss-120b 上反而更优，可避免过度分解和序列倒置。

  - 用 Wilson score LCB 作为小样本准入门槛，并隔离 hidden counterfactual 状态；发展集 OOD 增强会把误收率从 16.8%
  压到 0%，但会损失约 15pp yield，需要在 precision-coverage 间显式权衡。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
LLM Agent 现在不只是选择动作，还会在运行时修改 prompt、工具、中间件、配置、资源和执行 harness。这类自进化通常只优化 forward capability，但一个成功的 mutation 可能覆盖配置、重排中间件、创建临时文件或泄漏资源，之后无法安全回滚。更关键的是，正确恢复往往依赖 pre-mutation 状态信息，不是简单静态逆操作能解决。因此需要把 recoverability 作为自进化的硬约束：能力提升的 mutation 必须在 counterfactual states 下也能恢复观测等价状态。

**方法关键点**  
- EvoUndo 把候选表示为 4 元组 `(m, w, u, C_e)`：forward mutation、witness capture、recovery program、effect contract。修复阶段 `m` 严格冻结，只允许改 `w/u/C_e`。
- 用 typed observational equivalence 评估恢复：按 state target 做类型化比较，语义 canonicalization 处理 dict key、volatile identifier、文件 SHA-256。
- Counterfactual round-trip：在 development 和 hidden 状态上执行 `s -> w(s) -> m(s) -> u(m(s), w(s)) -> s_hat`，要求 `s_hat ≃ s`。
- 恢复语言分 L0/L1：L0 覆盖 config/prompt/tool/routing，L1 增加 middleware sequence、listener、文件、socket 和有序多表面恢复。
- 诊断粒度分 coarse typed diagnosis 和 exact-address diagnosis。准入用 95% Wilson score LCB ≥ 0.85，fail closed。

**关键实验与结果**  
在 600 个 unseen one-shot self-evolution 任务中，197 个 mutation 能力提升但 recovery 验证失败。原恢复表示下，常规修复 0/197；deterministic oracle 在 L0 只能恢复 48/197，L1 提升到 191/197。2×2 factorial 显示：L0 下 exact-address grounding 把 S0 恢复从 0/48 拉到 38/48（79.2%）；L1 在 S1 上把恢复从 0/143 拉到 142/143（99.3%）；但主模型 gpt-oss-120b 上 exact-address 叠加 L1 反而下降到 133/143（93.0%），Qwen3.8-27B 复现中没有这个负面交互。控制基准中 typed diagnosis 修复 114/120，独立重生成仅 4/120。Fresh holdout 300 任务中，发展集 counterfactual 多样性从 Q2 提到 Q20 可把 false positive 从 16.8% 降到 0%，但 yield 从 49.7% 降到 35.0%。

**最值得记住的一句话**  
安全的自进化不能只靠迭代 prompt 或更多推理，必须把验证、state grounding、witness 语义和恢复语言表达能力联合设计。
