---
title: 'Theoria: Rewrite-Acceptability Verification over Informal Reasoning States'
title_zh: Theoria：基于重写-可接受性验证的非形式化推理状态验证架构
authors:
- Ben Slivinski
- Michael Saldivar
affiliations:
- Independent Researchers
arxiv_id: '2607.01223'
url: https://arxiv.org/abs/2607.01223
pdf_url: https://arxiv.org/pdf/2607.01223
published: '2026-07-01'
collected: '2026-07-02'
category: Eval
direction: 结构化推理验证 · 可审计证明痕迹
tags:
- reasoning-verification
- LLM-judge
- proof-trace
- auditability
- structured-verification
- adversarial-robustness
one_liner: 将LLM推理改写为显式状态转换链，强制每一步必须有可审计的理据，暴露隐藏前提与编造引用
practical_value: '- **推荐理由可审计**：将推荐系统的解释生成建模为多步状态转换，每步必须关联可验证的理据（如商品属性、用户行为序列），避免幻觉式推荐语。

  - **Agent 行动序列验证**：在电商 Agent 链式决策中，要求每一步环境状态变化都有明确许可依据（工具返回、规则引用），未授权变动立即报警，提升可靠性。

  - **对抗鲁棒性增强**：借鉴“完整性约束”思想，对搜索推荐流水线中 LLM 输出进行结构化后验，重点检测隐藏假设与编造信息，尤其适用于高可信场景如金融推荐或处方建议。

  - **人机协同审查**：生成可独立挑战的证明轨迹，支持人工审核员快速定位推理瑕疵，可集成至推荐系统的可解释性审核环节。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：LLM 的解答缺少可信赖的审计机制，整体评分法官输出不透明且存在一致性问题。需一种可验证、可追溯的推理验证方法，使决策步骤能独立挑战。

**方法**：提出 Theoria 架构，将候选解答重写为一系列类型化的**状态转换**，每个转换必须附带**显式理据**（引用、计算或给定事实）。核心不变式是**变化完整性**：连续证明状态间的任何差异都必须被说明，否则未授权突变会暴露隐藏前提。每步转换可独立审计，生成人类可读的证明轨迹。

**结果**：在 HLE-Verified Gold（185 道专家级文本题）上认证 105 题，严格精确率 91.4%（Wilson 95% CI [84.5%, 95.4%]）。整体 LLM 法官在匹配覆盖上精确率相近，但解决不同问题，形成互补。在 95 道对抗性中毒证明上，结构化法官捕获率 94.7% vs 整体法官 83.2%（p=0.0017），差距集中在隐藏前提（90.6% vs 62.5%）和编造引用（100% vs 90%）。在 GPQA Diamond（65 题）上认证精确率 97.1%。
