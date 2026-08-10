---
title: 'PACE: Primitive-Aware Code Evolution for Automated Algorithm Design'
title_zh: PACE：基于原语的代码进化实现自动算法设计
authors:
- Zhuoliang Xie
- Ruihao Zheng
- Xiang Xu
- Genghui Li
- Zhengkun Wang
affiliations:
- Southern University of Science and Technology
- Shenzhen University
arxiv_id: '2608.07395'
url: https://arxiv.org/abs/2608.07395
pdf_url: https://arxiv.org/pdf/2608.07395
published: '2026-08-07'
collected: '2026-08-10'
category: Other
direction: LLM驱动的自动算法设计 · 代码进化
tags:
- Automated Algorithm Design
- LLM
- Code Evolution
- Genetic Programming
- Thompson Sampling
- Executable Primitives
one_liner: 将算法局部逻辑解耦为可执行原语，通过原语感知进化和汤普森采样实现代码级复用与有效评估
practical_value: '- **推荐策略部件化与进化复用**：将推荐系统中的排序规则、特征交叉方式、后处理逻辑等代码抽象为可执行原语（EAP），通过类似PACE的原语感知算子进行变异与交叉，自动进化更优策略组合，同时保留历史有效片段，避免重新探索。

  - **基于Thompson采样的无额外数据评估**：对推荐算法迭代中的局部改进，可利用父代相对提升作为奖励信号，通过Thompson采样选择高潜力原语，无需预留大量评估流量，指导在线更新时更具样本效率。

  - **防止LLM生成代码的退化迭代**：在使用LLM进行推荐模型或Agent逻辑自动优化时，借鉴PACE将关键子模块显式物化为原语集合，并以结构性约束保留它们，可缓解完全重新生成带来的性能波动与有用片段的丢失。

  - **跨任务策略迁移的启发**：构建跨场景（如不同广告位、国家站）的通用原语池，利用PACE的迁移机制，可快速将已验证的调整策略适配到新场景，降低冷启动人力成本。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：现有基于LLM的自动算法设计（如FunSearch、EoH）通常将算法视为不可分割的整体程序进行进化。这种方式导致有用的局部逻辑与宿主程序耦合，当整体程序被淘汰时，其中优秀的代码片段也随之丢失，难以衡量单独算法组件的贡献。

**方法**：提出PACE（Primitive-Aware Code Evolution），核心思想是将局部逻辑从完整程序中解耦，表示为持久化的“可执行算法原语（EAP）”。维护一个动态EAP集，并通过原语感知的进化算子（如变异、交叉）保证原语被结构性保留和跨程序迁移。评估EAP时，PACE利用一种基于父代相对性能提升的Thompson采样，从集合中选择原语，无需额外的评估数据集即可估计每个原语的效用。

**关键结果**：在四个任务上，PACE成功发现了具有竞争力的算法，同时相较于整体进化方法，更有效地结构化保留了有价值的算法组件，验证了代码级复用的优势。
