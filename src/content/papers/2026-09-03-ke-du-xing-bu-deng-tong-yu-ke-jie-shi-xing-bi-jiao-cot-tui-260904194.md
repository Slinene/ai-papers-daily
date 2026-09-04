---
title: 'Legibility is Not Interpretability: Comparing Judged and Actual Importance
  in Chain-Of-Thought Reasoning'
title_zh: 可读性不等同于可解释性：比较 CoT 推理中判断重要性与实际重要性
authors:
- Kevin Du
- Alexander Hoyle
- Laura Ruis
- Acyr Locatelli
affiliations:
- ETH Zürich
- MIT
- Cohere
arxiv_id: '2609.04194'
url: https://arxiv.org/abs/2609.04194
pdf_url: https://arxiv.org/pdf/2609.04194
published: '2026-09-03'
collected: '2026-09-04'
category: Reasoning
direction: CoT 推理步骤重要性的可解释性评估
tags:
- Chain-of-Thought
- Interpretability
- Process Reward Model
- LLM Judges
- Monte Carlo Rollouts
- Step Importance
one_liner: 实证表明 CoT 步骤文本只部分编码其功能重要性，LLM judge 与微调 critic 识别高优势步骤能力远低于噪声上限。
practical_value: '- 在电商/Agent 场景中用 LLM 评判推理步骤或生成过程（如诊断错误、提供中间奖励）时，要警惕文本看起来合理但实际未必对应功能重要性：文本可读性不等于可解释性。

  - 过程奖励模型（PRM）在正确响应上识别关键步骤能力有限，建议不要仅依赖 PRM 做细粒度信号，可结合蒙特卡洛 rollout 估计的 advantage 作为更可靠的地面真值。

  - 如果需要训练步骤级 critic，注意其对错误样本提升明显，但对正确样本效果欠佳；可考虑将 critic 用于纠错或筛选而非全面解释。

  - 在生成式推荐或 Agent 流水线中，对中间步骤做剪枝或加权时，基于文本判断的权重可能不可靠，需要验证“看起来关键”的步骤是否真的影响最终结果。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

动机：Chain-of-thought 推理轨迹看似可读，大量工作使用 LLM judge 诊断错误、评估忠实性、提供步骤级监督（如过程奖励模型）。但文本是否编码了步骤的功能重要性？

方法关键点：将步骤重要性操作化为 advantage——包含该步骤带来的期望奖励变化（如最终答案正确率），通过 Monte Carlo rollouts 估计作为 ground truth。在此基础上评估 LLM judge 识别高 advantage 步骤的能力，并微调一个步骤级 critic。

关键结果：足够能力的 LLM 能超过 prevalence baseline，但远低于 noise ceiling；微调 critic 在错误响应上提升显著，在正确响应上仍与 ceiling 差距大。表明步骤重要性仅部分可从推理文本中恢复，警示不要将文本可读性视为可解释性，尤其对过程奖励建模有直接影响。
