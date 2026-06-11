---
title: Toward Generalist Autonomous Research via Hypothesis-Tree Refinement
title_zh: 通过假设树精化实现通用自主研究框架
authors:
- Jiajie Jin
- Yuyang Hu
- Kai Qiu
- Qi Dai
- Chong Luo
- Guanting Dong
- Xiaoxi Li
- Tong Zhao
- Xiaolong Ma
- Gongrui Zhang
affiliations:
- Renmin University of China
- Microsoft Research
arxiv_id: '2606.11926'
url: https://arxiv.org/abs/2606.11926
pdf_url: https://arxiv.org/pdf/2606.11926
published: '2026-06-09'
collected: '2026-06-11'
category: MultiAgent
direction: 自主研究 · 假设树精化 · 分层 Agent 协作
tags:
- Hypothesis Tree Refinement
- Autonomous Research
- Multi-Agent
- Tree Search
- Self-Improvement
one_liner: 提出 Arbor 框架，用持久协调器与孤立执行器配合假设树精化，把长期研究转化为累积性探索与验证
practical_value: '- **复杂 Agent 任务的持久状态管理**：Arbor 将多步探索组织成一棵假设树，每次实验的结论和约束向上抽象传播，可以作为电商/推荐场景中连续
  A/B 实验、策略迭代的状态记忆方案，避免仅靠对话历史丢失关键因果。

  - **分层决策与隔离执行**：Coordinator 负责全局策略与树更新，Executor 在独立 worktree 中实现单条假设并返回结构化证据。这种分离可用于多智体商品选品
  / 生成式推荐流程——策略 Agent 规划方向，执行 Agent 独立测试文案或召回路线，结果写回共享记忆，隔离失败污染。

  - **基于证据的搜索前沿控制**：树的 Select/Prune/Merge 决策不只看指标，还结合祖先洞察、兄弟节点结果，类似多臂 Bandit 的树形版本。在自动化推荐排序策略搜索或
  prompt 工程中，可借鉴这种结构化探索，利用失败实验反向约束后续假设生成。

  - **“开发-测试”门控防止过拟合**：Arbor 严格区分开发反馈与最终准入，只有提升 held-out 评估的候选才被合并。做离线推荐算法优化时可复用此思想：将历史数据切分为探索集和验证集，避免代理在开发集上投机取巧，保证线上泛化。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：自主科学研究需要长时间维持探索状态，不断根据实验反馈修正假设。现有 LLM 代理能长时间执行任务，但缺少将多次试验转化为累积研究进展的机制，容易陷入局部试错。论文提出 Autonomous Optimization（AO）范式，并设计 Arbor 框架，让代理能够持续记录、比较、精化假设，将研究变成一棵不断生长的证据树。

**方法关键点**：
- **假设树（Hypothesis Tree）**：每个节点绑定一个假设、对应代码/制品版本、开发分数、失败原因及抽象洞察。树内部分为方向节点（抽象研究路线）和叶节点（可执行干预）。
- **分层结构**：持久协调器（Coordinator）负责全局策略，观察树状态，选择父节点生成并派遣子假设；短寿执行器（Executor）在独立 git worktree 中实现具体假设并返回结构化报告，不修改全局状态。
- **六步循环**：Observe（读取树前沿）、Ideate（基于证据生成新假设）、Select（选择叶节点）、Dispatch（并行执行）、Backpropagate（将实验结果抽象为洞察并向上传播）、Decide（根据 held-out 测试决定合并、剪枝或继续）。
- **开发-测试门控**：只在候选分支通过 held-out 评估后才合并到主分支，防止过拟合开发集。

**关键实验**：
- 在 6 个真实研究任务（模型训练、Harness 工程、数据合成）上，Arbor 均获得最佳 held-out 结果，平均相对增益是 Codex 和 Claude Code 的 2.5 倍以上。
- 在 MLE-Bench Lite 上，用 GPT-5.5 时获得 86.36% 的 Any Medal，所有对比系统中最高；消融实验验证了树结构和洞察反馈的共同作用。
- 跨任务迁移：在 BrowseComp 上优化的搜索 harness 直接迁移到 DeepSearchQA 和 HLE 上仍有提升。

**核心记忆句**：Arbor 不是更会写代码，而是把研究方向、实验证据和失败教训结构化存进树里，让长期探索变成可回溯、可复用的研究过程。
