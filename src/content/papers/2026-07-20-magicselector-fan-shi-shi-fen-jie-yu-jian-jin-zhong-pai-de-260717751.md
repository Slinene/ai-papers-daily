---
title: 'MagicSelector: Joint Optimization for Agent Tool Selection via Counterfactual
  Decomposition and Progressive Reranking'
title_zh: MagicSelector：反事实分解与渐进重排的Agent工具选择联合优化
authors:
- HONOR Agentic Search Team
- Zhengzong Chen
- Lei Tang
- Lijun Liu
- Chuandi Jiang
- Fan Yang
- Keyun Chu
- Chu Zhao
- Shihao Liu
- Minghang Li
affiliations:
- HONOR
arxiv_id: '2607.17751'
url: https://arxiv.org/abs/2607.17751
pdf_url: https://arxiv.org/pdf/2607.17751
published: '2026-07-20'
collected: '2026-07-21'
category: Agent
direction: Agent工具检索与任务分解优化
tags:
- Tool Retrieval
- Counterfactual Decomposition
- Reranking
- Dynamic Top-K
- Hard Negative Mining
- Agent Planning
one_liner: 提出反事实任务分解、自蒸馏重排和动态Top-K，联合优化Agent工具检索，显著提升精度和效率
practical_value: '- 反事实奖励可迁移至电商搜索的query分解/意图识别模块，避免在复杂多意图query下生成无关子查询，通过量化分解对下游召回/排序的边际增益提供因果级训练信号。

  - 自蒸馏难负例挖掘与渐进式重排（先点式后列表式）可直接用于广告/商品相似品区分，迭代挖掘高分不相关样本，增强模型对功能相似物品的细粒度判别力。

  - 双语义边界感知的动态Top-K截断策略可应用于推荐系统的召回后过滤，自适应截断候选集，减少大模型推理时的token消耗和上下文噪声，避免固定K导致的关键物品遗漏。

  - 多轮交互过程级标注数据集构建思路可迁移至对话推荐场景的评估，提供更细粒度的诊断能力，定位是上下文理解、意图分解还是检索环节失效。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
在手机助手等自主智能体中，用户指令常含多任务、模糊指代与跨轮依赖，而工具库日益庞大，静态注入式检索面临严峻挑战：强化学习分解任务时缺乏因果归因，模型倾向利用浅层特征腐化分解质量；传统重排难以区分功能相似的工具；固定Top-K截断导致召回遗漏或长尾噪声，加剧“迷失在中间”效应。  
**方法关键点**  
- 偏好引导的反事实任务分解：构建反事实基线（不分解时的NDCG），计算分解后的相对检索增益作为奖励，结合过程奖励模型的偏好信号，通过GRPO优化，将优化目标从结果匹配转向过程增益，切断伪相关。  
- 自蒸馏驱动的渐进式重排序：先用点式训练建立基础相关性评分，再以列表式训练优化候选顺序；迭代地将当前模型打分的高分错误工具作为难负例，重新训练检索器和重排器，强化对相似工具的鉴别。  
- 双语义边界感知的动态Top-K：同时监测重排序分数断崖和相邻工具语义相似度断崖，取两者中的最大位置作为截断点，在保证召回的同时最大化上下文纯度。  
- 构建MTDTool基准：面向移动多轮交互、带11种状态机建模和过程级原子任务标注，支持独立诊断分解与检索质量。  
**关键实验**  
在ToolBench、ToolRet和MTDTool上评估。相比提示方法（ReInvoke、ToolReAGt等）和RL方法（ToolQP），MagicSelector在MTDTool域内/域外分别取得97.22/95.33 NDCG@10，域内完整性95.33%，大幅领先；在ToolRet上NDCG@10达59.90；在ToolBench上NDCG@5达90.8。消融和OOD实验证明反事实分解与动态Top-K有效提升泛化性和token效率。
