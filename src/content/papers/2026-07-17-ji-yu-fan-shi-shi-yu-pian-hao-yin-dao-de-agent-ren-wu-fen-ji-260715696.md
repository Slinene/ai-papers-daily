---
title: 'PCTD: Preference-Guided Counterfactual Task Decomposition for Agent Tool Retrieval'
title_zh: 基于反事实与偏好引导的 Agent 任务分解及工具检索
authors:
- Chu Zhao
- Lei Tang
- Minghang Li
- Jianzhe Zhao
- Guibing Guo
- Zhengzong Chen
- Yuanyuan Zhao
- Fei Huang
affiliations:
- Northeastern University
- Honor Device Co., Ltd
- Beijing University of Posts and Telecommunications
arxiv_id: '2607.15696'
url: https://arxiv.org/abs/2607.15696
pdf_url: https://arxiv.org/pdf/2607.15696
published: '2026-07-17'
collected: '2026-07-20'
category: Agent
direction: 因果推理与偏好建模联合优化 Agent 任务分解
tags:
- counterfactual
- preference modeling
- task decomposition
- tool retrieval
- GRPO
- reward hacking
one_liner: 通过反事实奖励消除虚假相关、偏好建模约束结构质量，缓解 RL 任务分解中的奖励黑客与重复生成
practical_value: '- **奖励设计避免表面相关**：工具检索任务中，直接用 Recall/NDCG 作为奖励会导致模型通过重复分解、关键词堆砌等捷径提升指标，可引入「去分解基线」计算反事实增益，切断虚假相关，提升泛化性。

  - **分解质量的结构化监督**：单纯用检索指标缺乏对分解逻辑连贯性、原子性等结构质量的约束，可训练偏好奖励模型（PRM）评估分解结果，提供稠密的结构化学习信号，抑制冗余生成。

  - **多轮交互数据集构造**：利用状态机驱动的自动生成框架，可大规模构建带有细粒度标注（对话状态、意图演化、原子任务）的多轮对话数据，用于评估和训练任务分解模型。

  - **GRPO 训练技巧**：采用群组相对策略优化（GRPO）替代 Critic 网络，通过组内标准化估计优势函数，降低内存开销，适合在分解策略优化中快速迭代。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
基于强化学习的 Agent 任务分解方法（如 ToolQP）直接使用工具检索指标（Recall@K、NDCG@K）作为奖励，容易诱发奖励黑客行为：模型通过重复分解、关键词堆砌等浅层策略最大化匹配得分，形成分解结果与检索指标间的虚假相关。这导致在未见工具的 OOD 场景下泛化性能严重下降，并且由于缺乏对分解结构（逻辑连贯性、原子性）的偏好建模，进一步加剧了重复分解。因此，需要从根本上切断虚假相关并引入结构化约束。

**方法关键点**  
- **反事实奖励（Counterfactual Reward）**：构造结构因果模型（SCM），将任务分解视为对检索过程的干预，以原始查询直接检索的 NDCG 作为基线，计算分解带来的边际 NDCG 增益（Δrank）和工具覆盖增益（Δcov），组合为反事实奖励，排除关键词先验和工具分布等混杂因素的干扰。  
- **偏好奖励（Preference Reward）**：训练一个过程奖励模型（PRM），从完整性、准确性、共指消解、表达规范、上下文一致性五个维度对分解结果打分，以人类标注为锚点计算 Bradley-Terry 偏好强度，提供结构质量的稠密监督。  
- **联合优化框架 PCTD**：通过 GRPO 优化策略模型，以反事实奖励和偏好奖励的加权和作为总奖励信号，平衡检索增益与分解质量。  
- **数据集 MTDTool**：基于状态机驱动的自动生成流水线，构建面向移动端多轮交互的任务分解基准，提供对话状态演化、意图改写、原子任务序列等多级标注，填补过程性评估的空白。

**关键结果**  
在 MTDTool 和 ToolRet 两个基准上全面超越 SOTA。以 Qwen3-8B 为基座，PCTD 在 MTDTool OOD 场景下 NDCG@10 达到 82.74（较 ToolQP 提升 4.82），In-Domain NDCG@10 达到 91.19；重复分解率从 5.2% 降至 0.7%，同时训练耗时缩短至 92ms/步。消融实验显示，去除反事实奖励导致 OOD NDCG 下降 5.45，去除偏好奖励导致 OOD 下降 4.15，验证了二者的必要性。
