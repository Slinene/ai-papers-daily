---
title: 'MolLean: A Process-Verifiable Language for Chemical Reasoning'
title_zh: MolLean：化学推理的过程可验证语言
authors:
- Jiatong Li
- Yatao Bian
affiliations:
- National University of Singapore
arxiv_id: '2610.20459'
url: https://arxiv.org/abs/2610.20459
pdf_url: https://arxiv.org/pdf/2610.20459
published: '2026-10-13'
collected: '2026-10-26'
category: Reasoning
direction: LLM 推理 · 可验证工具接口
tags:
- Process Verification
- LLM Reasoning
- Tool Use
- MCP
- Chain-of-Thought
one_liner: MolLean 将化学 CoT 转为可执行状态转换，通过分层检查和 MCP 逐步验证减少幻觉并提升推理
practical_value: '- 用可执行 trace 替代自由文本 CoT：在电商/广告场景中，可为商品属性生成、推荐理由、促销文案等定义领域约束（类目、价格、库存、合规规则），让
  LLM 输出可检查的状态转换，而非仅靠 prompt 约束。

  - 有状态工具接口与拒绝不变原则：类似 MolLean-MCP 的设计可迁移到 Agent 工具调用，工具校验失败时不修改状态，避免错误动作污染后续上下文，对搜索
  query 改写、组合优惠计算等多步交互尤其有用。

  - 全过程细化 + 分步验证反馈：先让模型生成完整 trace 再整体修正，适合离线批量生成；对实时要求高、状态约束严的任务，可引入逐步验证反馈，在反应类/多步推理任务中往往能获得额外提升。

  - typed witness protocol 分离原生结构检查与外部测量：可借鉴为区分数据库已有事实与模型生成内容，防止模型把未经验证的属性当成事实写入推荐理由或广告文案。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：化学 chain-of-thought 容易在中间步骤幻觉结构或属性声明，例如虚构官能团、丢失键信息、未经证明就声称性质改善；这些错误发生在自由形式解释中，难以自动发现和修正。

方法关键点：MolLean 把化学推理锚定在显式分子状态上，基于 Lean 构造分层内核，从原始图编辑到复合变换逐层检查状态转移和分子读数的断言。typed witness protocol 将原生结构检查与外部提供的测量分离，避免混淆。MolLean-MCP 是一个有状态工具接口，在生成过程中暴露状态转移、检查和读数：模型收到反馈后决定下一步动作，被拒绝的动作保持状态不变。系统支持一次性 trace 执行、全过程细化（whole-trace refinement）以及通过 MCP 进行交互式推理。

关键结果：在 12 个分子生成、编辑、优化和反应任务上，构建 8800 个匹配示例，使用 Qwen3.6-27B 评估。全过程细化在所有 12 个任务上都优于直接 chain-of-thought；MolLean-MCP 通过逐步验证反馈进一步补充，在反应类任务中取得更好性能。结果表明可执行基础能让显式化学承诺得到检查和修正，而非停留在自由形式解释中。
