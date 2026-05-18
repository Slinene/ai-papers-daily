---
title: 'FORGE: Self-Evolving Agent Memory With No Weight Updates via Population Broadcast'
title_zh: FORGE：群体广播实现无权重更新的Agent自进化记忆
authors:
- Igor Bogdanov
- Chung-Horng Lung
- Thomas Kunz
- Jie Gao
- Adrian Taylor
- Marzia Zaman
affiliations:
- Carleton University
- Defence R&D Canada
- Cistel Technology
arxiv_id: '2605.16233'
url: https://arxiv.org/abs/2605.16233
pdf_url: https://arxiv.org/pdf/2605.16233
published: '2026-05-15'
collected: '2026-05-18'
category: Agent
direction: Agent 记忆演化与群体广播
tags:
- Population-Based Training
- Memory Evolution
- Prompt-Only Learning
- Agent Self-Improvement
- CybORG CAGE-2
- POMDP
one_liner: 通过种群冠军广播和失败触发反思，无梯度更新下将LLM Agent在POMDP中的表现提升1.7-7.7倍
practical_value: '- **冠军广播机制加速多Agent学习**：在Agent集群中，定期选出表现最优实例的文本记忆，替换掉所有其他实例的记忆。这一群体级选择压力能显著压缩策略方差，对电商推荐Agent或对话Agent的群体自改进场景非常实用。

  - **文本记忆表示的选择与成本权衡**：规则（Rules）型记忆成本低（~40%更少token），示例（Examples）型记忆性能更优（3/4模型取得最高返回），混合型居中。在生成式推荐或商品搜索Agent中，可根据计算预算灵活选择记忆形式。

  - **毕业制度节省大规模Agent训练成本**：提前冻结已收敛（解决任务）的实例，避免在后续广播中被覆盖或继续消耗token，可直接迁移到需要大量并行Agent训练的电商场景，如多路策略探索后的收敛管理。

  - **无梯度、无强模型的自改进范式**：利用Reflexion循环从失败轨迹自动提炼结构化知识，完全依赖同模型反思，适合无法微调基座模型的业务环境，例如基于闭源API的智能客服Agent的持续优化。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**：LLM Agent在随机、部分可观测、长时程的序贯决策任务（如网络防御）中，缺乏可靠的记忆与学习机制——零样本表现灾难性，梯度更新又往往不可行。现有prompt-only自改进方法多限于单实例反射，缺乏群体层面的知识传播与选择压力，且缺乏对记忆表示的系统性对比。

**方法关键点**：
- 提出FORGE协议，含三个阶段组件：(1) 层级式ReAct Agent架构，规划器下挂分析师和动作选择子Agent，动态注入文本记忆；(2) 内部Reflexion循环：当单步奖励低于阈值时，中止episode并调用反思Agent（相同LLM）分析失败轨迹，生成规则（Rules）或示例（Examples）等知识artifact，追加到记忆；(3) 外部种群循环：N个实例并行训练，每阶段结束后选出评估最高的实例作为冠军，将其全部记忆广播给所有活跃实例，并冻结超过毕业阈值的实例以节省计算。
- 三种记忆表示：Rules（条件启发式文本）、Examples（结构化交互演示）和混合形式，均通过提示注入。

**关键实验**：
- 在CybORG CAGE-2（13主机网络防御POMDP，30步，对抗B_line攻击者）上评估。四种模型家族（Gemini-2.5-Flash-Lite, Grok-4-Fast, Llama-4-Maverick, Qwen3-235B）。零样本平均奖励严重为负（-103至-190）。
- FORGE提升平均奖励1.7-7.7倍（最强配置下Gemini从-189.6到-24.5），比Reflexion单实例基线提升29-72%（所有12种模型-表示组合）。
- Examples表示在3/4模型中取得最佳返回（如Gemini -24.5），Rules表示token成本低约40%且毕业率更高。
- 消融实验表明冠军广播是性能增益的核心，移除广播后退化为Reflexion; 毕业主要降低计算量（活跃实例数减半）。
- 弱模型受益更显著：基线越差的模型改善倍数越高（Gemini 7.7× vs Grok 1.7×）。

**最值得记住**：在无法更新LLM参数时，通过群体层面的冠军记忆广播，能让Agent群凝聚到少数高效策略上，大幅提升决策性能，这种机制适用于任何多Agent并行探索的文本策略优化任务。
