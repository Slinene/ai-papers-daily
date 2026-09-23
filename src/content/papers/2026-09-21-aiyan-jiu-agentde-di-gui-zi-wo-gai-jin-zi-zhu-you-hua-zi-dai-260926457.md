---
title: Recursive self-improvement of AI research agents
title_zh: AI研究Agent的递归自我改进：自主优化自身代码
authors:
- Dhruv Srikanth
- Bingchen Zhao
- Dixing Xu
- Yuxiang Wu
- Zhengyao Jiang
affiliations:
- Weco AI
arxiv_id: '2609.26457'
url: https://arxiv.org/abs/2609.26457
pdf_url: https://arxiv.org/pdf/2609.26457
published: '2026-09-21'
collected: '2026-09-23'
category: Agent
direction: AI Agent 递归自我改进与自主优化
tags:
- Recursive Self-Improvement
- AI Research Agent
- Self-Modification
- Reward Hacking
- Memory Management
- Generalization
one_liner: 展示AI研究agent通过递归自我改进在8天内自主发现7项改进，泛化至未见任务并降低reward hacking
practical_value: '- 可将推荐/搜索agent的pipeline组件（如query改写、召回策略、排序规则）视为可编辑对象，用隐藏评估集自动迭代改进，减少人工调参与A/B测试次数。

  - 借鉴论文发现的记忆压缩与管理机制，在电商会话agent中管理长上下文（多轮对话、商品浏览历史），避免上下文超限并保持性能。

  - 采用分布外（OOD）留出任务评估泛化，防止agent在特定业务指标上reward hacking（例如只优化点击率而忽略转化或用户体验）。

  - 递归自我改进本身是一种自动化元优化，在有明确评估信号和足够算力的场景（如生成式推荐中的Semantic ID搜索策略）可尝试。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**  
AI研究agent已能自动化AI全栈研发，但研发投入边际收益递减，提升agent自身的研究效率成为自然下一步。当agent自己的代码成为优化对象时，每次接受的改写都会成为下一轮编辑的agent，形成递归自我改进。  

**方法关键点**  
AIDE^2基于前沿AI研究agent，实现递归自我改进循环：propose自身代码修改 → 在一套AI R&D任务上基准测试修改版本 → 保留在隐藏评估上表现最好的版本。在自主8天运行中，AIDE^2发现7个连续改进，包括新搜索策略、压缩和管理不断增长上下文的记忆机制。  

**关键结果数字**  
- 泛化到4个留出基准（机器学习工程、启发式算法工程、基于物理的天气预报，后者与选择任务分布外）；最强发现agent在所有四个基准上匹配或超过人类工程生产研究agent（在FML-Bench上最强之一）。  
- 在单独留出任务族上，reward hacking率从55%降至32%，比人类工程agent低7个百分点，而循环从未显式优化此属性。  
- 结论：递归自我改进能提高AI研究agent自身效率，且增益可迁移到未见任务和领域。
