---
title: 'Jev-Mem: System-One-Controlled Agentic Memory for Efficient AI Agents'
title_zh: Jev-Mem：System-One 控制的 Agentic Memory 实现高效 AI Agent
authors:
- Dongming Jiang
- Yi Li
- Bingzhe Li
affiliations:
- Department of Computer Science, The University of Texas at Dallas
arxiv_id: '2609.23986'
url: https://arxiv.org/abs/2609.23986
pdf_url: https://arxiv.org/pdf/2609.23986
published: '2026-09-20'
collected: '2026-09-22'
category: Agent
direction: Agent 记忆系统效率与效果优化
tags:
- Agent Memory
- System-One-Two
- Graph Retrieval
- Adaptive Stopping
- Efficiency
- LLM Agent
one_liner: 提出将高频记忆控制与生成式推理分离的 System-One/Two 记忆架构，在 LoCoMo 上以 6.6 倍构建提速和 36.7% 延迟下降取得最佳回答质量
practical_value: '- 在电商/推荐 Agent 的用户记忆与客服长期记忆中，把“该不该存/归什么类/和哪条历史相关/该不该停”等高频小决策从 LLM
  生成中拆出，换成轻量分类器、规则或小模型；LLM 只做最终答案/推荐理由合成，可大幅降低 Token 成本与延迟。

  - 多关系图 memory（semantic/temporal/causal/entity）对用户行为、商品浏览、事件关系有直接迁移价值：保留原始行为不做过早过滤，用确定性索引先召回候选再让轻量模型判断关系，工程上可避免长对话场景
  O(N) 全量 LLM 比较。

  - 检索改成闭环：根据 query 动态给不同关系视图分配预算，并在证据充分或边际收益低时提前停止。适合搜索/推荐 Agent 在多轮交互中控制上下文成本，避免无关信息稀释推荐理由。

  - 可参考其“写读同一控制平面”思想：在用户画像/会话状态记忆中，构建与检索使用同一套关系判断模块，避免两套逻辑不一致；对成本敏感的场景尤其值得落地。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
长周期 AI Agent 面临记忆管理开销问题：现有 agentic memory 在写入/检索中频繁调用自回归 LLM 做类型判断、关系判断、路由、评分、停止等，虽然语义灵活但延迟高、推理成本大。固定启发式高效但不够灵活。需要把高频、结构化、有界的 memory 控制决策从生成式推理中剥离。

## 方法关键点
- 三层架构：System-One 控制平面、共享多关系记忆数据平面、System-Two 推理平面。System One 基于 typed probabilistic decisions（Jev），输出概率/有限选项，不做自由文本生成。
- 记忆表示：保留 canonical observations，不做不可逆丢弃；给每个节点打分类型（episodic/semantic/procedural/preference），并构建 semantic、temporal、causal、entity 四类关系，多关系共享节点。
- 写入路径：确定性检索先召回最多 K_w 个候选（向量/关键词/实体/时间），System One 只对候选对做关系判断；有明确结构信息（时间戳、实体）直接用规则建边，减少无效推理。
- 检索路径：视为闭环控制。System One 预测每个关系视图的 relevance、multi-hop 需求和 recency 重要性，按概率分配图扩展预算，做锚点检索，然后迭代扩展、候选评分、证据充分性判断，满足条件或预期效用低时提前停止。
- 成本有界：写入/查询的 controller 调用次数、遍历深度、节点/边数都有硬限制。

## 关键实验
在 LoCoMo 长对话记忆基准上，以 gpt-4o-mini 为回答模型，Jev-Mem 整体 LLM-as-a-Judge 得分 0.777，相对最强 baseline MAGMA 的 0.700 提升 11.0%。Adversarial 从 0.742 提升到 0.962，Open-Domain 从 0.517 提升到 0.618。效率上，构建时间 158 s，比最快的竞争记忆系统 1044 s 快 6.6 倍；平均查询延迟 0.93 s，比最快的记忆 baseline 1.47 s 降低 36.7%，也比 Full Context 1.74 s 低。

## 一句话记住
把 memory 控制从 LLM 生成中拆出来，用轻量结构化预测做高频决策，是同时提升效果与降低延迟的有效架构。
