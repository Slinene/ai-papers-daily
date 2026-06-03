---
title: 'VirtualMLE: A Virtual ML Engineer that Optimizes Sequential Recommenders'
title_zh: VirtualMLE：通过LLM Agent反思与记忆实现序列推荐自动调优
authors:
- Shiteng Cao
- Jingwen Liu
- Junda She
- Zhiheng Li
affiliations:
- Tsinghua University
- Beijing University of Posts and Telecommunications
arxiv_id: '2606.03221'
url: https://arxiv.org/abs/2606.03221
pdf_url: https://arxiv.org/pdf/2606.03221
published: '2026-06-02'
collected: '2026-06-03'
category: Agent
direction: LLM Agent 自动化推荐模型调优
tags:
- LLM Agent
- Sequential Recommendation
- Hyperparameter Optimization
- Reflection
- Memory System
- Cognitive Amortization
one_liner: 用LLM Agent构建反思-记忆闭环，将序列推荐调优转化为可迁移的认知推理，大幅降低试错次数
practical_value: '- **将LLM嵌入模型调优流程**：可借鉴VirtualMLE的“执行-反思-记忆更新”闭环，在推荐模型上线前的调参阶段，用LLM
  agent替代人工或贝叶斯优化，自动分析试验结果并诊断瓶颈，减少工程师重复劳动。

  - **层次化记忆复用调优经验**：长期记忆存储跨数据集的通用启发（如稀疏数据适合强正则化、注意力模块宜用较低学习率），短期记忆记录当前搜索轨迹。在电商多域（首页猜你喜欢、详情页关联推荐等）场景下，可以把已优化域的知识快速迁移到新频道，降低冷启动成本。

  - **反思模块输出因果归因**：每次试验后让LLM生成“哪个改动导致了什么结果”的归因摘要，指导后续搜索方向。实际工作中可嵌入到AutoML pipeline里，作为可解释的搜索记录，辅助人工决策。

  - **认知摘要实现跨任务迁移**：将完整调优轨迹蒸馏为Cognition Summary（如“相对位置编码优于绝对+相对”、“embedding tying对稀疏数据有益”），作为新数据集的初始先验，能在电商多品类推荐中显著加速收敛（论文中跨域迁移只需1/3试验次数）。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：序列推荐模型（如SASRec、HSTU）在新数据集上达到SOTA通常需要数十到数百次手动试错，传统AutoML（网格搜索、贝叶斯优化）将其视为盲搜，无法理解配置变化与性能之间的因果联系。本文希望利用LLM的推理能力，将调优过程转化为带有反思与记忆的智能探索，实现调优知识的复用与跨任务迁移。

**方法**：VirtualMLE 是一个LLM-agent框架，包含四个核心组件：
- **沙盒执行管线**：严格隔离验证集/测试集，保证模型选择无信息泄露；
- **结构化反思模块**：每次试验后，LLM基于结果生成显式的因果归因（如“扩大hidden_dim后收益递减，瓶颈已转向注意力结构”），而非仅记录指标；
- **层次化记忆系统**：长期记忆存储跨数据集的认知摘要，短期记忆记录当前会话的试验序列与反思结果，二者配合实现智能剪枝；
- **认知摘要**：一个完整搜索轨迹被蒸馏为可迁移的启发式规则（如“稀疏数据集优先考虑embedding tying”、“相对位置编码优于绝对位置”），作为新任务的零样本先验。

**实验**：在Amazon Baby、Beauty、Pet三个数据集上，以SASRec和HSTU为骨干模型，对比了大规模生成式推荐（Tiger, ReaRec等）、传统AutoML（Grid Search, Bayesian Optimization）以及仅使用LLM采样的OPRO。结果：VirtualMLE在全部指标上取得最优，SASRec上平均相对提升29.9%-31.9%，HSTU上21.4%-25.4%；相比贝叶斯优化，所需的试验次数从数百次缩减到17-32次（如HSTU/Baby从464次降至32次）；跨数据集迁移后，收敛所需试验次数进一步减少约三分之二。消融实验证明反思与记忆互补，缺少任一模块都会导致性能下降和收敛停滞。
