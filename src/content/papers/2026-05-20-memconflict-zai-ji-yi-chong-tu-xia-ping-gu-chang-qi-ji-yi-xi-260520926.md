---
title: 'MemConflict: Evaluating Long-Term Memory Systems Under Memory Conflicts'
title_zh: MemConflict：在记忆冲突下评估长期记忆系统的诊断框架
authors:
- Zhen Tao
- Jinxiang Zhao
- Peng Liu
- Dinghao Xi
- Yanfang Chen
- Wei Xu
- Zhiyu Li
affiliations:
- Renmin University of China
- Shanghai University of Finance and Economics
- MemTensor (Shanghai) Technology
arxiv_id: '2605.20926'
url: https://arxiv.org/abs/2605.20926
pdf_url: https://arxiv.org/pdf/2605.20926
published: '2026-05-20'
collected: '2026-05-23'
category: Eval
direction: 长期记忆评估 · 记忆冲突诊断
tags:
- Long-term memory
- Memory conflict
- Evaluation
- Retrieval
- Ranking
- LLM agents
one_liner: 提出记忆冲突诊断框架，评估系统在动态、静态、条件冲突下检索与排序有效记忆的能力
practical_value: '- 在推荐/对话Agent的用户画像管理中，不能仅看最终回答准确率，需要白盒检查记忆检索与排序，确保模型使用了正确的用户信息。

  - 借鉴MemConflict的冲突分类：对用户偏好变化（动态）、矛盾信息（静态）、条件性偏好（条件）分别设计记忆更新与查询策略，避免因冲突导致错误推荐。

  - 通过注入语义相似的干扰记忆（如其他用户的相似信息）测试记忆系统的鲁棒性，可以迁移到电商推荐中模拟竞争商品描述或相似用户画像的干扰。

  - 工程实现上可采用"冲突感知"排名机制：对检索到的记忆候选进行时间有效性、事实一致性、上下文适用性的打分，提升长期用户建模的可靠性。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
现有长期记忆评估主要关注对话结果或简单的信息更新，无法诊断在存在时间变化、矛盾信息、情境依赖时系统如何检索和排序有效记忆。为此，本文从信息质量中“适合使用”的角度出发，将记忆有效性定义为查询条件下的时间有效性、事实正确性和上下文适用性，并构建MemConflict诊断框架。

**方法关键点**  
- 基于Persona Hub种子生成结构化用户画像，包含动态状态（如居住地）、不变属性、条件偏好及相关实体。  
- 模拟2022-2025年以月为粒度的多会话时间线，在更新会话中引入真实状态变化以构建动态冲突；在不变属性上注入矛盾提及构建静态冲突；为条件偏好插入不同条件-值对构建条件冲突；同时从相关实体抽取语义相似信息作为干扰项。  
- 两阶段对话生成：先合成会话提纲，再扩展为多轮对话，确保所有冲突信息自然嵌入，经人工校订。  
- 评估协议包含黑盒答案准确率（AA）和白盒支持证据命中率（SEH@K）、支持排名分数（SRS），并针对动态/静态冲突增加更新顺序一致性（UOCS）和冲突识别分（CRS）。

**关键实验与结果**  
在A-Mem、LangMem、Letta、MemOS、Mem0、Memobase六种代表性长记忆系统上测试，12个虚拟用户平均52.33个会话、2349轮对话、20.4万tokens。主要发现：①各系统在不同冲突类型下表现参差，答案准确率常与记忆检索命中率脱节，说明仅看最终回答会掩盖记忆层面的失败；②更长历史、语义干扰、隐式查询和更大冲突距离均显著降低性能；③失败主要源于支持记忆缺失与已检索记忆利用不当。这些结果为设计证据感知、冲突感知的长期记忆系统提供了明确方向。  

**核心结论**  
记忆系统的可靠性不仅取决于最终答案是否正确，更取决于是否检索并高置信度地使用了正确的记忆证据。
