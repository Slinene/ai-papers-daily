---
title: Effective Reinforcement Learning for Agentic Search by Recycling Zero-Variance
  Queries During Training
title_zh: 回收零方差查询：一种面向搜索代理的强化学习训练优化
authors:
- João Coelho
- João Magalhães
- Bruno Martins
- Chenyan Xiong
affiliations:
- Carnegie Mellon University
- Instituto Superior Técnico and INESC-ID
- NOVA LINCS
arxiv_id: '2606.10709'
url: https://arxiv.org/abs/2606.10709
pdf_url: https://arxiv.org/pdf/2606.10709
published: '2026-06-09'
collected: '2026-06-10'
category: Agent
direction: Agent 搜索·RL训练优化
tags:
- Reinforcement Learning
- GRPO
- Zero-Variance
- Query Recycling
- Search Agent
- Synthetic Data
one_liner: 将GRPO训练中浪费的零方差查询动态回池重采样，使训练分布与策略协同演化，大幅提升LLM搜索代理性能
practical_value: '- **RL训练效率提升**：GRPO训练LLM Agent时，全对或全错的零方差组不产生梯度却消耗算力。回收策略将其放回采样池，后续策略改进后可能变为信号查询，避免浪费。可移植到推荐Agent、对话系统的RL微调中，同等算力下提升有效训练信号比例。

  - **动态难度采样**：零方差状态是策略相关的，不要静态预过滤“简单”或“困难”样本。电商推荐中用户序列的难度随模型能力变化，可借鉴该思想设计自适应课程学习或动态负采样：难以解决的样本暂时降权但不丢弃，能力提升后重新启用。

  - **合成数据构造策略**：通过三种模式（网页图遍历、迭代检索、比较检索）生成多跳查询，诱导出不同搜索行为，提升Agent泛化性。可借鉴用于生成多样化推荐对话、多步信息查找任务，丰富训练覆盖。

  - **权重池管理机制**：将采样池视为带权查询集合，信号查询降权或移除，无信号查询保留，训练分布随策略能力演化。此范式可融入多臂老虎机、在线强化学习的探索策略，用于冷启动或动态流量分配。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：
GRPO已成为训练LLM搜索代理的标准算法，但其组内归一化特性导致当一批rollout全对或全错（零方差）时，优势为零，消耗算力却无梯度信号。现有方法（DAPO过采样后丢弃、GRESO基于历史统计预过滤）假设零方差是静态属性，但作者观察到：随着策略演化，查询会在零方差和信号承载之间翻转。因此，固定丢弃零方差组会损失未来可用的学习信号。

**方法关键点**：
- **动态池管理**：将训练查询池建模为带权集合 \(Q(t)=\{(q_i,w_i^{(t)})\}\)，按权重采样。提出**查询回收**：将被选入梯度更新的信号查询权重置0（移除），其他查询（包括零方差组）权重保持1，可在后续步重新采样。这使得有效训练分布与策略协同演化。
- **与已有方法统一**：标准GRPO固定单次遍历后重置池；DAPO/Bounded-DAPO通过过采样增加信号组，但都一次性消费所有候选。回收通过权重更新规则实现更灵活的重采样。
- **合成查询构造**：在DeepResearchGym的ClueWeb22快照上，用三种生成方式（基于网页图、迭代检索、比较检索）构建10k多跳QA对，覆盖不同检索结构，不依赖评测集。
- **Agent架构**：ReAct式，只有搜索工具（可并行发3个查询），推理阶段可无缝切换到SERPER在线API。

**关键结果**：
- 在7个多跳QA基准上，使用回收策略训练的Qwen3-1.7B达到平均Pass@1 66.0，匹配甚至超越使用评测集标注训练的7B模型。4B模型进一步提升至71.3。
- 回收查询成为训练后期有效批次的主要来源（约3/4来自之前零方差组），包括从太难状态被新能力解救的查询，以及从太易状态因策略漂移重新进入信号区的查询。
- 零方差状态在不同模型容量上表现不同：小模型始终有大量太难查询，大模型则将大量查询转化为太易，验证了零方差是策略相对的，回收均有益。
- 消融实验显示，组大小K=4在计算效率上优于K=8，软回收（权重设为0.1而非0）性能略低于完全移除但优于无回收基线。
