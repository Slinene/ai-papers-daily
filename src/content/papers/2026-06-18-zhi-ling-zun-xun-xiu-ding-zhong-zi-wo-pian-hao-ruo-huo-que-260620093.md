---
title: 'Self-Preference Is Weak or Absent in Verifiable Instruction-Following Revision:
  A Four-Model Test Under Genuine Authorship'
title_zh: 指令遵循修订中自我偏好弱或缺失：四模型真实作者测试
authors:
- William Guey
- Pierrick Bougault
affiliations:
- Tsinghua University
arxiv_id: '2606.20093'
url: https://arxiv.org/abs/2606.20093
pdf_url: https://arxiv.org/pdf/2606.20093
published: '2026-06-18'
collected: '2026-06-22'
category: Eval
direction: LLM 自我偏好偏差评估
tags:
- self-preference
- instruction-following
- revision
- LLM-as-judge
- verifiable evaluation
one_liner: 在可验证指令修订任务中，模型对自己文本的修正接受度与中立模型无显著差异，自我偏好不明显。
practical_value: '- **Agent 自修正流水线可放心使用确定性验证**：当修正的正确性可由规则（如格式检查、字段完整性校验）自动判定时，模型不会因“作者身份”而抗拒改正，此场景下自我审查风险低。

  - **LLM 判定修正质量时仍需警惕自偏**：本结论只适用于可验证修正；若修正优劣靠另一 LLM 判断，则自我偏好仍可能影响决策，应避免闭环自评。

  - **要求模型解释拒绝原因可提升可控性**：实验中拒绝修正时 97% 的理由是“挑错”，这提示在 Agent 拒绝建议后输出解释，有助于人工审核或后续自动过滤。

  - **实验设计可复用到自改进评估**：用确定性检查器作为 ground truth，避开 LLM 自评导致的循环偏倚，适合评估推荐文案生成、搜索 query
  改写等模块的自修正效果。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：LLM 扮演评判者时存在自我偏好（self-preference），倾向于高估自己生成的文本。若此偏好转入修订环节，模型可能抗拒外部对自己的草稿提出的正确修正，从而削弱自修订流水线的可靠性。但此前研究很难隔离“作者身份”效应，因为修正是否“更好”往往仍需 LLM 判断，造成循环偏倚。

**方法**：在可验证指令遵循任务 IFEval 上设计实验。每一步中，模型先生成一段违反某约束的草稿，官方 IFEval 检查器确认该违规并验证候选编辑确实修复了问题。然后让模型以两种身份决定接受或拒绝该编辑：“作者”身份（知道草稿是自己写的）和“中立”身份（仅看到草稿，不被告知来源）。比较两者的拒绝率。覆盖四种中型模型系列，85 次作者-中立配对比较。

**结果**：作者与中立模型的拒绝率差值仅为 -5.1 个百分点（95% CI: -12.9, +2.7），无明显自我偏好。在小规模预实验中出现的“自我怀疑”提示未在大样本中复现。定性分析显示，当作者拒绝一个已验证为正确的修正时，97% 的情形给出的理由是挑出了修正本身的问题（如改变了原本正确的部分或引入新错），而非单纯的偏好。该样本量下不能排除约 13 pp 以下的小效应。
