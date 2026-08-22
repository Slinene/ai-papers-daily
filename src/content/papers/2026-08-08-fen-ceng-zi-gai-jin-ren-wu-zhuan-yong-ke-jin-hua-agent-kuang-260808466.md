---
title: 'Hierarchical Self-Improvement: A Framework for Task-Specific Evolvable Agent
  Harnesses'
title_zh: 分层自改进：任务专用可进化 Agent Harness 框架
authors:
- Tailin Zhou
affiliations:
- HKUST
arxiv_id: '2608.08466'
url: https://arxiv.org/abs/2608.08466
pdf_url: https://arxiv.org/pdf/2608.08466
published: '2026-08-08'
collected: '2026-08-22'
category: Agent
direction: Agent 分层自改进与 harness 进化
tags:
- Agent Harness
- Self-Improvement
- Meta-Evolution
- Frozen LLM
- BALROG
- Task-Specific
one_liner: 单个冻结 LLM 通过任务 harness、evolver、meta-evolver 三层自改进，在 BALROG 上实现显著提升并揭示能力边界
practical_value: '- **把 agent scaffold 当可进化资产**：在电商/搜索推荐 Agent 中，不要只调 prompt；把 prompt、tool
  编排、memory、state tracking、验证逻辑打包成 task-specific harness，按任务族（如导购、query 改写、push 文案）分别维护，并通过固定
  `using_harness` 接口热更新。模型权重保持冻结，避免每次策略调整都重训或换模型。

  - **评估 harness 迭代要防过拟合和高方差**：用 held-out 任务 split 而不是全量同一批任务评估；候选版本用 LCB reward（μ
  - 0.5·σ/√n）排序，允许保留多分支 commit pool，最终用 validation 选择泛化最优版本。这可比直接选单次最高分可靠得多。

  - **把“怎么改 harness”也变成可学习策略**：meta-evolver 不是直接改任务表现，而是改 seed 选择、explore/exploit、commit
  规则。对应到搜索/推荐 Agent，可以把人工的“何时探索新品/何时重启策略/如何维护版本档案”作为上层可优化策略，而不是硬编码。

  - **先判断两个边界再投入**：如果模型在任务上初始 reward 近零或反馈极稀疏，harness 进化收益极低（NLE 案例）。业务上应先确认有非零、可区分的
  reward 信号；harness 进化只能放大既有能力，不能替代模型升级。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：LLM agent 性能对 harness（prompt、工具编排、记忆、验证逻辑等）高度敏感，但当前自改进主要改模型权重或依赖外部强模型设计 harness，缺少对“冻结模型内生修改自身 harness”的清晰边界与归因研究。

**方法关键点**
- 三层 scopes 共享一个冻结 LLM：task harness `H` 执行任务；evolver 重写 `H`；meta-evolver 重写 evolver 策略 `Σ`，但 meta-evolver 自身执行逻辑固定为 outer anchor，避免无界自指。
- 任务 harness 热插拔：每个 task family 维护独立 harness，通过固定 task-injection seam 更新，内部组件可变但接口不变。
- thinking on/off：任务执行阶段关闭推理，固定每步能力上限；仅进化阶段开启推理，隔离“测试时搜索”混淆。
- 五阶段循环：seed selection → main evolution → commit selection → meta-evolution → best-version selection；候选选择用 LCB reward `r=μ-0.5σ/√n`，保留多分支 commit pool。

**关键结果**
在 BALROG 上，以 DeepSeek-V4-Flash-Preview 为冻结 backbone，meta-on 相比 init harness 的 raw % Progress：BabyAI +39.3（42.0→81.3）、Crafter +33.0（11.6→44.6）、TextWorld +25.0（40.0→65.0）、MiniHack +15.0（0.8→15.8）；NLE 几乎无改善（0.0→0.2）。BabaIsAI 20% held-out 测试：BreakStop 0.98、GoTo 1.00，Make 仅 0.36。元进化消融显示：去掉 meta-evolver 后 TextWorld 下降 19.0、MiniHack 下降 10.0，表明优化搜索策略本身有独立收益。

**最值得记住的一句话**：harness evolution 能放大冻结模型既有能力，但存在 feedback-fidelity 和 backbone capability 两个硬边界——先看模型是否能在任务上产生有用的 reward 信号。
