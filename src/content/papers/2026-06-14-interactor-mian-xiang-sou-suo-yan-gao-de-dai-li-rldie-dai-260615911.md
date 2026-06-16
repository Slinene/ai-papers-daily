---
title: 'Interactor: Agentic RL oriented Iterative Creation for Ad Description Generation
  in Sponsored Search'
title_zh: Interactor：面向搜索广告的代理RL迭代描述生成框架
authors:
- Penghui Wei
- Jiayu Wu
- Chao Ye
- Zhi Guo
- Shuanglong Li
- Lin Liu
affiliations:
- Baidu Inc.
arxiv_id: '2606.15911'
url: https://arxiv.org/abs/2606.15911
pdf_url: https://arxiv.org/pdf/2606.15911
published: '2026-06-14'
collected: '2026-06-16'
category: GenRec
direction: Agent RL优化广告描述生成
tags:
- Ad Description Generation
- Agentic RL
- Iterative Creation
- Generative Reward Models
- Knowledge Capacity
- Landing Page Consistency
one_liner: 多轮迭代生成框架，利用生成奖励模型的细粒度反馈强化学习，显著提升广告描述的知识性与忠实度
practical_value: '- 将单轮生成改为多轮迭代，利用细粒度反馈（不仅是标量奖励）修正错误，可迁移到商品详情页、推送文案等长文本生成，提升内容质量。

  - 基于规则的生成奖励模型（GenRM）能输出二分判断和结构化推理，可作为自动内容审核或AIGC质量保障组件，在电商文案评估中直接复用。

  - 在生成式推荐中引入外部知识检索（如搜索引擎），将检索结果作为上下文补充，类似RAG但通过RL优化融入生成循环，可增强商品描述的知识准确性。

  - 代理RL训练采用GSPO算法，仅对动作token计算梯度并屏蔽环境token，适合大规模异步训练，对同类多步交互生成场景（如对话式推荐）有工程参考价值。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：搜索广告描述具有更长文本承载量，可融入世界知识回应用户意图，并呈现落地页的精细卖点。现有方法多为单轮生成，仅依靠标量奖励优化，难以有效修正长文本中的细微错误，缺乏细粒度改进引导。为此，需一种能持续自我修正的生成范式。

**方法关键点**：
- **多轮交互生成**：将LLM策略视为代理，每轮可执行知识检索（`<retrieve>`）、生成描述（`<create>`）和请求奖励（`<reward>`）等动作，环境返回观察（检索结果、奖励模型的推理反馈）和奖励信号。
- **定制环境**：包含两个生成式奖励模型，分别评估「知识容量」与「落地页一致性」。二者基于预定义评分标准（rubrics）输出二元判断和细粒度原因（如指出缺失知识、不一致短语）；同时接入CTR预测模型和内部搜索引擎，提供吸引力奖励与世界知识。
- **代理RL优化**：使用组序列策略优化（GSPO），基于多轮rollouts，以最终轮奖励计算组内优势并全局归一化。仅对LLM生成的动作token计算梯度，屏蔽环境观察token，避免奖励碎片化。
- **迭代完善**：策略先生成初始描述，若不达标则根据反馈在下轮修正（如补充缺失知识、修正与落地页不符的表达），直到输出最终描述。

**关键结果**：
- 工业数据集（100万训练样本）上，INTERACTOR全面超越CTOP、DIVER及单轮RL基线，尤其忠实度（faithfulness）达0.872，远超单轮RL的0.726；知识性（informativeness）0.715 vs 0.693。
- 消融实验表明，去除推理反馈后性能急剧下降（knowledge capacity 0.636→0.715，faithfulness 0.706→0.872），验证细粒度反馈的核心作用。
- 线上A/B测试覆盖14万广告主，广告收入相对提升+0.74%，内容质量top-grade率提高7个百分点。

**核心启示**：**让生成模型根据结构化诊断反馈进行多轮自我迭代，是解决开放域长文本生成质量控制的有效范式。**
