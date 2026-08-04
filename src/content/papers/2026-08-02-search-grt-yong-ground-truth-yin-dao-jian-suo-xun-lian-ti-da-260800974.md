---
title: 'Search-GRT: Guided Retrieval Training of Search Agents to Optimize for Complex
  Question Answering'
title_zh: Search-GRT：用 ground truth 引导检索训练，提升搜索 Agent 多跳问答能力
authors:
- Aounon Kumar
- Sudipta Paul
- Vivek Kulkarni
- Vijay Srinivasan
- Srinivas Chappidi
affiliations:
- Samsung Electronics AI Center-Mountain View
arxiv_id: '2608.00974'
url: https://arxiv.org/abs/2608.00974
pdf_url: https://arxiv.org/pdf/2608.00974
published: '2026-08-02'
collected: '2026-08-04'
category: Agent
direction: 搜索 Agent 强化学习训练优化
tags:
- Search Agent
- Reinforcement Learning
- Multi-hop QA
- Guided Retrieval
- LLM
- Training
one_liner: 在 RL 训练中利用 ground truth 约束检索候选集，提供更强学习信号，多跳 QA 性能提升超 40%
practical_value: '- **利用业务 ground truth 缩小检索空间以提升 RL 训练效率**：在电商搜索或推荐多跳推理场景，若拥有用户点击/购买日志等强相关
  item 集合，可构造受限检索池，集中训练信号，缓解早期稀疏奖励问题。

  - **将“检索约束”作为课程学习策略**：在复杂 query 改写或对话式推荐训练初期，用已知正确文档或商品限制候选范围，待 agent 学会提取有效子 query
  后逐步放开，类似 GRT 仅在训练时约束，推理时仍用全量索引。

  - **借鉴 GRT 的奖励设计**：基于答案绝对匹配的 0/1 奖励简单高效，结合检索准确率与最终答案准确率的监控，能快速诊断 agent 的检索与合成短板。

  - **工程实现上可复用文本嵌入相似度构建受限语料**：用业务中已有的 query/商品/文档 embeddings，基于 ground truth 答案或关键信息，动态选取
  top-k 相似文档作为训练时的检索池，无需额外标注。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

**动机**：
LLM 驱动的搜索 Agent 在复杂多跳问答中容易因初始检索错误导致级联失败；强化学习能端到端优化搜索策略，但早期 reward 稀疏，agent 生成的子 query 质量差，难获有效反馈。

**方法关键点**：
- **Guided Retrieval Training (GRT)**：在 RL 训练阶段，用 ground truth 信息限制搜索引擎的检索范围，只从与 ground truth 高度相似的 top-κ 文档中检索，提供更密集的训练信号。
- **检索约束构造**：对 HotpotQA 直接使用提供的 ground truth 段落；对 NQ 将 query 与答案拼接作为 ground truth 信息，利用 E5 文本嵌入的余弦相似度选取 top-300 文档构成受限语料。
- **Agent 生成格式**：遵循 Search-R1 的 `<think>`、`<search>`、`<information>`、`<answer>` 标签，交替进行推理与检索。
- **RL 框架**：基于 PPO，奖励为答案是否与任一标准答案精确匹配（0/1），并加入 KL 惩罚项防止策略偏离过远。

**关键结果**：
- 在 NQ (0.435 vs 0.392) 和 HotpotQA (0.371 vs 0.293) 上均优于 Search-R1；多跳 QA 平均性能从 0.206 提升到 0.297，相对提升超 40%。
- 检索准确率与正确检索后的答案合成准确率均持续高于 Search-R1。
- 训练中 reward 曲线更高，即使验证时恢复到全量 Wikipedia 检索，仍优于基线，表明模型学会了更好的检索与推理，而非过拟合受限语料。

**值得记住的一句话**：GRT 通过在训练初期用 ground truth 构建“温室”检索环境，让搜索 Agent 先学会产生有效子 query 和正确推理模式，再迁移到真实开放检索场景。
