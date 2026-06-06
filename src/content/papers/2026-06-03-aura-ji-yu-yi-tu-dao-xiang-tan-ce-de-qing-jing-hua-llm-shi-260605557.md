---
title: 'AURA: Intent-Directed Probing for Implicit-Need Surfacing in Situated LLM
  Agents'
title_zh: AURA：基于意图导向探测的情景化LLM Agent隐式需求浮现
authors:
- Yang Li
- Jiaxiang Liu
- Jiang Cai
- Mingkun Xu
affiliations:
- Guangdong Institute of Intelligence Science and Technology
arxiv_id: '2606.05557'
url: https://arxiv.org/abs/2606.05557
pdf_url: https://arxiv.org/pdf/2606.05557
published: '2026-06-03'
collected: '2026-06-06'
category: Agent
direction: Agent意图推断与探测控制
tags:
- Implicit-Need Surfacing
- Proactive Probing
- Intent Inference
- Situated Agents
- LLM Agents
- Tool Use
one_liner: 在工具使用前插入IntentFrame推断，用gap分控制探测预算，提升隐式需求覆盖率。
practical_value: '- 在对话式推荐或客服Agent中，显式建模用户字面查询与隐式需求之间的gap：由LLM输出结构化IntentFrame，根据gap值决定后续信息检索预算（如调用商品详情、评价、库存API的步数），避免对显式需求已获满足的查询过度探查。

  - 将探查与回答生成解耦：探查结果作为紧凑的上下文传入最终生成，支持缓存和跳过；一旦探查结果已满足隐式需求即提前停止，减少API调用和延迟。

  - 利用gap分触发预警（heads-up alert）：当gap较高时，向用户主动提示推断出的潜在需求（如商品库存紧张、同类目的替代品、价格波动），提升交互主动性。

  - 工具白名单机制确保隐私合规：通过工具注册表和基于pattern的allow/deny策略，低gap查询自动跳过禁止工具，隐私敏感场景可零违规。可借鉴至需要控制数据访问权限的推荐/客服系统。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
LLM Agent常只回答用户字面查询，忽略背后的隐含信息需求（例如“林伟在哪？”可能隐含“她有空吗？”）。现有ReAct等方法在推理时调用工具，没有显式推断并量化这一差距。这导致决策上下文缺失、回答编造细节。AURA旨在让Agent在回答前先推断隐含需求，并据此控制探查预算，从而有选择地获取私有状态。

**方法**  
- 提出**IntentFrame**：一个由LLM在场景感知后、工具调用前生成的JSON结构，包含字面需求、隐含需求列表、gap分（0-1）、推荐探针工具集、预警标志、置信度等。  
- **gap路由探查**：gap分按阶梯函数映射为探查步数上限（如0～0.2→0步，0.8～1→5步），探测器（Explore阶段）根据预算和推荐工具进行目标导向的有限多步调用，拿到结果后提前停止。探查结果总结后供推理使用。  
- **两阶段流水线**：确定性上下文组装（感知→场景→记忆）→LLM控制推理（意图推断→探查→推理→行动→交互）。记忆基于重近度、重要性、词法相似性加权检索。

**实验与关键结果**  
- 在自建的**100查询四场景隐式需求基准**（AURATown多Agent模拟）上，AURA-Intent的隐式需求覆盖率达到**0.804**，显著优于ReAct式NoIntent的0.733（∆=+0.071, p<10⁻⁶），三个场景单独显著，两外一个场景持平（夜间场景公共状态已暗示可用性）。  
- 消融实验：①将LLM意图推断替换为启发式规则，分数从0.803骤降至0.368；②去除few-shot示例导致gap校准失效，增益不显著——说明LLM校准是性能核心。  
- 事实性查询中，AURA不是准确率最优（Fixed-Probe FA=0.766 vs AURA GapRouted 0.696），但实现了**82%更少的探针调用**（1.40 vs 8.00）和**零禁止工具违规**，成为访问成本Pareto最优点。  
- 人类评估AURA在环境觉察力、回复有用性、Agent拟真度、事实准确性四个维度均显著优于基线。  

**一句话总结**：在工具调用前推算表面查询与隐含需求的gap并据此分配探查预算，让Agent从被动回答升级为主动补全上下文，是隐式需求场景可泛化的控制点。
