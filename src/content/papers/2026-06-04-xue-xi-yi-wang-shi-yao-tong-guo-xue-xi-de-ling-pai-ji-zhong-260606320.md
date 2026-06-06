---
title: 'Learning What to Forget: Improving LLM Unlearning via Learned Token-Level
  Importance'
title_zh: 学习遗忘什么：通过学习的令牌级重要性改进LLM遗忘
authors:
- Gizem Yüce
- Giorgos Nikolaou
- Nicolas Flammarion
affiliations:
- Theory of Machine Learning Lab, EPFL
arxiv_id: '2606.06320'
url: https://arxiv.org/abs/2606.06320
pdf_url: https://arxiv.org/pdf/2606.06320
published: '2026-06-04'
collected: '2026-06-06'
category: Training
direction: LLM 遗忘学习 · 令牌重要性学习
tags:
- LLM Unlearning
- Token Weighting
- Machine Unlearning
- Alternating Optimization
- Forget-Retain Trade-off
one_liner: 提出交替令牌加权遗忘（ATWU），通过可学习的令牌重要性评分实现无监督、轻量级的选择性遗忘，达到SOTA的遗忘-保留权衡。
practical_value: '- 对于电商推荐或Agent中基于LLM的组件，若需遗忘用户隐私数据、过时知识或有害内容，可采用ATWU思路：从隐藏状态学习每个令牌的遗忘特异性评分，无需外部标注，轻量且可嵌入现有微调流程。

  - 交替优化策略（冻结模型参数更新评分器、冻结评分器更新模型）可稳定联合学习，避免单步耦合带来的训练不稳定，适合在线持续遗忘场景。

  - 线性评分器仅增加微小计算开销，可以在推荐模型的序列令牌（如用户行为序列、生成式推荐中的Semantic ID序列）上复用，实现选择性遗忘或知识更新。

  - 该方法定义的“遗忘特异性”基于与保留目标的冲突程度，这一准则可迁移到多任务学习中：识别哪些样本或令牌对主任务关键而对辅助任务不冲突，用于动态样本加权。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：LLM遗忘要求擦除特定知识的同时保留通用能力。遗忘样本中并非所有令牌对遗忘同等重要：仅涉及敏感内容的令牌需要遗忘，而通用词应保留。现有方法或忽略令牌级异质性，或依赖辅助模型、启发式规则或外部标注来估计重要性，缺乏直接与遗忘目标对齐的无监督学习机制。

**方法**：本文提出从保留（retain）目标的角度定义令牌遗忘特异性：如果最小化某个令牌的遗忘损失不与保留最优性冲突，则该令牌是遗忘特异性相关的。将此视角形式化为参数与令牌权重的联合优化问题，并在自然分离条件下，所求解可恢复oracle遗忘特定令牌集合。基于此，设计交替令牌加权遗忘（ATWU）框架：使用一个简单的线性评分器，以隐藏状态为输入，为每个令牌输出遗忘重要性权重；然后交替冻结模型与评分器，分别用加权的遗忘损失和保留损失更新参数。整个过程无需外部令牌级监督。

**结果**：在TOFU和RWKU基准上，ATWU取得最佳的遗忘-保留权衡，显著优于样本级方法、基于概率的令牌加权启发式和辅助模型方法。学习到的分数与真实遗忘片段高度对齐，表明其捕捉到了语义上有意义的遗忘信号。该方法仅增加极小计算开销，验证了基于保留冲突的准则能有效指导语言模型应该遗忘什么。
