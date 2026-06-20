---
title: Multi-Agent Transactive Memory
title_zh: 多智能体交互记忆：群体级轨迹共享与检索
authors:
- To Eun Kim
- Xuhong He
- Dishank Jain
- Ambuj Agrawal
- Negar Arabzadeh
- Fernando Diaz
affiliations:
- Carnegie Mellon University
- University of California, Berkeley
arxiv_id: '2606.19911'
url: https://arxiv.org/abs/2606.19911
pdf_url: https://arxiv.org/pdf/2606.19911
published: '2026-06-18'
collected: '2026-06-20'
category: MultiAgent
direction: 多智能体轨迹共享与学习排序检索
tags:
- Multi-Agent Systems
- Transactive Memory
- Trajectory Retrieval
- Learning to Rank
- RAG for Agents
- Interactive Environments
one_liner: 提出MATM框架，使智能体共享交互轨迹以提升任务效果与效率，无需协同训练
practical_value: '1. **Agent 经验复用范式**：在电商导购、对话式推荐等交互场景，大规模部署 Agent 后，可将成功轨迹（如商品搜索导航、多轮对话决策链）存储在共享记忆库，新实例直接检索复用，避免重复探索，降低推理成本与延迟，类似“群体缓存”。

  2. **状态条件检索设计**：借鉴 key‑value 索引方案——用最近 k 步交互历史作 query，检索后续操作片段作为 context，适合需要动态感知当前页面/对话状态的推荐
  Agent，比仅凭任务描述检索更精准。

  3. **学习排序个性化轨迹选择**：引入 lightweight LTR 重排序，融合生产者可信度（如模型能力分）、消费者标识、轨迹统计特征，实现“信任建模”与“消费者差异化”，能直接迁移到多
  Agent 协作的生成式推荐系统，根据下游转化率等业务指标训练重排序模型。

  4. **增量记忆构建 + 边际效用标签**：通过分支回滚和边际效用评估自动生成训练数据，无需人工标注，可在上线后持续扩充记忆库且同时优化检索效果，对需要长期进化的推词、素材生成类
  Agent 极具实操价值。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
现有 LLM Agent 在交互式任务中产生的轨迹（action‑observation 序列）通常被丢弃或仅由原 Agent 私用，新实例不得不重复探索以发现已有解决方案，导致群体低效。论文提出 Multi‑Agent Transactive Memory (MATM)，将轨迹视为群体级共享资源，生产者贡献成功经验，消费者检索复用，以提升整体任务效果与效率，无需集中协调或联合训练。

**方法关键点**
- **共享记忆构建**：预填充公开轨迹后，通过增量更新运行新任务，将成功轨迹加入索引；同时利用分支回滚技术生成边际效用标签，用于训练重排序器。
- **索引与检索**：采用状态条件的 key‑value 方案，取最近 l 步交互历史编码为查询向量，检索相似轨迹的后续 l 步作为上下文。第一阶段用 E5‑Base 做密集检索（top‑20），第二阶段用 LTR 重排序输出最终 1 条最有用轨迹。
- **LTR 重排序**：构建 44 维特征，覆盖生产者元数据（如基准分数）、消费者身份、检索相似度、轨迹长度等，训练点态 FFN、对偶 LambdaMART 和 SVMRank，以预测轨迹注入后带来的下游成功率提升。
- **检索策略**：由 RetrievalPlanner 子 Agent 在每步决策是否调用 MATM，避免不必要检索稀释上下文。

**关键结果**
在 ALFWorld 和 WebArena 两个交互式基准上，使用 35‑37 个生产者、34 个消费者模型测试。
- 单阶段检索：ALFWorld 成功率从 47.1% 提升至 55.1%，平均步数从 11.77 降至 11.18；WebArena 成功率从 18.2% 提升至 20.5%，步数从 22.0 降至 20.3。
- 加入 LTR 重排序后：ALFWorld 上 SVMRank 成功率达 64.3%（+17.2 pp），步数降至 10.35；WebArena 上 FFN 重排序保持 20.5% 成功率且步数进一步降至 19.91，取得最高效率。
- 收益分布与泛化：消费者从弱于或强于自己的生产者处均能获益，且跨任务类型检索仍有显著增益；记忆库规模越大，性能持续提升。

**核心结论**
“群体级轨迹共享记忆 + 基于下游效用的轻量重排序”是一种可扩展的多 Agent 经验复用范式，能同时提高任务效果与效率，且对生态中的异质 Agent 普遍有效。
