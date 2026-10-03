---
title: 'JuryFlow: Disagreement-Guided Human-in-the-Loop Multi-Agent Evaluation'
title_zh: 'JuryFlow: 分歧引导的人在环多智能体评估框架'
authors:
- Mufeng Yang
- Junwei Yu
- Yepeng Ding
affiliations:
- University of Tsukuba
- The University of Tokyo
- Hiroshima University
arxiv_id: '2609.40103'
url: https://arxiv.org/abs/2609.40103
pdf_url: https://arxiv.org/pdf/2609.40103
published: '2026-09-30'
collected: '2026-10-03'
category: Eval
direction: 多智能体评估与人在环分歧消解
tags:
- Multi-Agent Evaluation
- LLM-as-Judge
- Disagreement Resolution
- Human-in-the-Loop
- Rubric Learning
- Entropy
one_liner: 把多智能体评判分歧视为 claim 级不确定性信号，人只选择关键分歧点，通过图传播与 rubric 归纳实现自改进评估
practical_value: '- 在电商/Agent 场景评估 LLM 输出质量时，先把回复拆成 atomic claims 逐条 verdict，而不是整体打分；用
  verdict entropy 定位不一致点，优先处理高熵 claim，可显著降低人工标注量。

  - 把人从“重新标注整条回复”改成“只选一个 focal disagreement 做最小干预”：单个决策点即可触发后续重评，适合需要人工审核但预算有限的业务评审流。

  - 构建 disagreement graph 并用结构相似性传播修正到历史相似 case，再抽象成 rubric 条目让所有 judge 继承：可复用于持续迭代的评估标准管理，避免每次规则更新都要重新训或重写
  prompt。

  - 自动消融协议可借鉴：评估框架上线前用 entropy ranking 自动选点，分别消融 targeted re-evaluation、propagation、rubric
  induction，定位真正带来提升的组件。'
score: 7
source: arxiv-cs.HC
depth: abstract
---

**动机**：LLM 作为自动评判不可靠，多评委多数投票会丢弃分歧而非解决分歧，留下不确定区域。

**方法**：JuryFlow 将候选回复分解为 atomic claims，异质评委对每个 claim 给出 verdict；计算 verdict entropy 构建 disagreement graph，节点分数为熵，边为 claim 间结构相似性。人只作为结构引导者，选择最需要解决的分歧点（实验中自动用 entropy ranking 代替），做单次最小干预；随后 focal claim 重新评估，修正沿图边传播到历史相似 case，并固化为可复用 rubric 条目，所有评委继承，形成闭环自改进。

**结果**：在 MT-Bench 和 LLMBar 上，JuryFlow 相比单 judge 和 majority-vote panel 提升与 gold labels 的一致性；消融证明 disagreement-targeted re-evaluation、propagation、rubric induction 各自有贡献。
