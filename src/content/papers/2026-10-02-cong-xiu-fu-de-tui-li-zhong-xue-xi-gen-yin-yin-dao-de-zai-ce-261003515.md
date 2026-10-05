---
title: 'Learning from Repaired Reasoning: Root-Cause-Guided On-Policy Distillation'
title_zh: 从修复的推理中学习：根因引导的在策略蒸馏
authors:
- Chenglei Shen
- Haoyang Yao
- Weijie Yu
- Song Jin
- Xiao Zhang
- Jun Xu
affiliations:
- Gaoling School of Artificial Intelligence, Renmin University of China
- School of Software and Microelectronics, Peking University
- School of Information Technology and Management, University of International Business
  and Economics
arxiv_id: '2610.03515'
url: https://arxiv.org/abs/2610.03515
pdf_url: https://arxiv.org/pdf/2610.03515
published: '2026-10-02'
collected: '2026-10-05'
category: Training
direction: LLM 推理训练 · 根因修复蒸馏
tags:
- LLM reasoning
- on-policy distillation
- self-distillation
- error repair
- reasoning mismatch
- training
one_liner: 提出 RC-OPD，用学生失败推理的根因修复和锚点引导，缓解自蒸馏的推理错配与蒸馏陷阱
practical_value: '- 在训练电商/Agent 多步推理或工具调用链时，不要只用固定 reference trajectory 做 SFT；可以收集模型自己的失败轨迹，定位最早错误步骤，只做局部修复并保留有效前缀，既降低全量重写成本，也能提升样本针对性。

  - 将训练目标拆成两类：对错误段用 root-cause 信号强化纠错，对有效前缀用 anchor-guided 信号维持正确行为。这种分段蒸馏思路可迁移到推荐解释、查询改写、广告文案生成等需要保留中间正确约束的任务。

  - 诊断-修复-续写循环可形成自动化 on-policy 数据管线：用诊断模型或规则框定错误片段，设置固定 repair budget，通过 continuation
  验证修复效果，适合工程化迭代训练 LLM ranker/agent。

  - 对生成式推荐中的 CoT/推理链，可以用 valid prefix anchor 避免不必要的约束冲突，减少“模型只抄结论但错误未消”的情况。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：On-policy self-distillation（OPSD）用 reference solution 做事后监督，但参考解只解释“正确做法”，不解释学生自己的推理为何失败；且全程使用同一条 hindsight，会约束有效推理，导致 distillation trap。

**方法关键点**：RC-OPD 对每个失败轨迹定位最早实质性错误，做局部 correction，将修正后的中间结果作为有效前缀的 anchor；通过迭代 diagnosis–repair–continuation，在固定 repair budget 内用学生 continuation 检验修复，并继续发现后续错误。对最终能到达正确答案的 repair chain，root-cause-guided distillation 用失败诊断和纠错目标监督错误段；anchor-guided distillation 则用能到达修复中间结果的链来支持有效前缀。

**关键结果**：在多个数据集和模型规模上取得显著性能提升；消融与分析显示该方法能缓解 reasoning mismatch 和 distillation trap。
