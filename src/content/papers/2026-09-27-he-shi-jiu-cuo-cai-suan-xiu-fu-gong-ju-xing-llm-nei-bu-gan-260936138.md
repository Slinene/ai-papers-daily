---
title: When Does Correction Become Repair? Mechanistic Auditing of Internal Interventions
  in Tool-Using LLMs
title_zh: 何时纠错才算修复：工具型 LLM 内部干预的机制审计
authors:
- Jiayi Li
- Ruizhe Li
affiliations:
- University of the Chinese Academy of Sciences, China
- School of Computer Science, University of Birmingham, UK
arxiv_id: '2609.36138'
url: https://arxiv.org/abs/2609.36138
pdf_url: https://arxiv.org/pdf/2609.36138
published: '2026-09-27'
collected: '2026-10-04'
category: LLM
direction: LLM 可解释性 · 工具决策审计
tags:
- mechanistic interpretability
- activation steering
- tool use
- auditing
- statistical licensing
- LLM agents
one_liner: SAKIKO 审计框架揭示激活干预的行为迁移不等于修复，并量化附带损伤
practical_value: '- 评估内部干预或 steering 修复工具调用/动作决策时，不要只看 accuracy / net gain；增加 **destination-resolved
  指标**（如翻转矩阵：被干预改对的 vs 改错的基线正确样本），并在上线前审计 collateral damage。

  - 干预应做成 **router-conditioned**：先定位动作类型决策对应的 router/分类子层或关键 attention head，再对局部 hidden
  state 做方向干预；全局 residual stream steering 容易引入无关动作损伤。

  - 采用 **前瞻冻结统计许可**：预先设定目标增益，将干预方向与同预算随机方向做统计比较；对有限样本下的“看起来不错”的点估计，应报告置信区间/检验结果，避免把噪声当成修复。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：Agentic LLM 在执行工具前需在 K 路动作空间中做决策（调用、澄清、直接回答、拒绝），上游动作类型选择错误是独立于生成内容的失败模式。内部激活干预可改变这些决策，但常规聚合指标掩盖了状态迁移目标和附带损伤。

**方法关键点**：SAKIKO 提出方向性错误发现、router 条件下的干预、目标解析验证、前瞻冻结统计许可四步审计；在 When2Call 与 MetaTool 上对 7 个 LLM 的通道键控干预进行审计，并与预算匹配的随机方向对照。

**关键结果**：5 个模型出现方向特异净增益；3 个密封评估中 59 个随机方向无一达到校准目标增益。目标审计显示行为迁移≠修复：+55 净增益干预损坏超过一半的基线正确决策；Qwen3-4B 与 Gemma-2-9B 的点估计因有限样本不确定性被正式拒绝。
