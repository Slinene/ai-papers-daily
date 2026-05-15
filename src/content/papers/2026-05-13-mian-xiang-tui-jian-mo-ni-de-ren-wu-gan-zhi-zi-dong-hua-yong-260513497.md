---
title: Task-Aware Automated User Profile Generation for Recommendation Simulation
  Using Large Language Models
title_zh: 面向推荐模拟的任务感知自动化用户画像生成
authors:
- Xinye Wanyan
- Chenglong Ma
- Danula Hettiachchi
- Ziqi Xu
- Jeffrey Chan
affiliations:
- RMIT University
arxiv_id: '2605.13497'
url: https://arxiv.org/abs/2605.13497
pdf_url: https://arxiv.org/pdf/2605.13497
published: '2026-05-13'
collected: '2026-05-15'
category: RecSys
tags:
- RecSys
- User Simulation
- LLM
- Profile Generation
- Agent
- Evaluation
one_liner: 提出无需手动Schema的三阶段框架，自动生成任务对齐、鲁棒的用户画像，显著提升模拟行为对齐与泛化性
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
基于大语言模型的推荐系统模拟中，现有工作多聚焦记忆与动作模块，忽视用户画像生成，而画像直接决定模拟行为的真实性与可迁移性。手工定义属性schema导致信息瓶颈、行为不对齐且难以跨领域泛化，因此需要一种自动化、不依赖模板且能适应不同任务的画像生成方法。

**方法关键点**  
APG4RecSim为训练无关的三阶段框架：  
- **阶段1：提取与初始化**：从用户交互历史出发，并行生成3组候选属性，构建高召回原始属性池，避免遗漏潜在偏好。  
- **阶段2：上下文感知语义合并**：利用数据集schema、任务描述与示例构成的上下文，对原始属性进行语义去重和领域对齐，得到紧凑的任务无关画像。  
- **阶段3：因果映射与精炼**：实例化任务决策路径（如识别、排序、评分），通过反事实扰动测试，将画像属性映射到具体决策步骤，生成可执行的决策政策。  
整个过程无需训练，仅依赖LLM推理。

**关键实验与数字**  
在ML-1M、Amazon-Book、Amazon-Beauty三个数据集上，对比RecAgent、Agent4Rec、直接使用交互历史及无画像四种基线。在识别、排序、评分三个任务上，APG4RecSim在24个评估指标中有16个最优、7个次优。关键提升：排序nDCG@10相比基线最高提升7%，评分分布的Jensen-Shannon散度（JSD）降低8%，表明宏观行为分布更贴近真实用户。消融与鲁棒性分析显示，框架对位置偏差和流行度偏差具有强抵抗力，且能在Llama、GPT、DeepSeek等不同LLM上保持性能，验证了领域与模型泛化能力。

**核心启示**  
结构化、任务对齐的画像生成不仅能提升单点指标，更重要的是通过将决策路径显式建模，使模拟行为真正摆脱对全局统计先验（如流行度）的依赖，实现更可靠、可解释的用户模拟。
