---
title: 'Autodata: An agentic data scientist to create high quality synthetic data'
title_zh: Autodata：代理式数据科学家自动生成高质量合成数据
authors:
- Ilia Kulikov
- Chenxi Whitehouse
- Tianhao Wu
- Yixin Nie
- Swarnadeep Saha
- Eryk Helenowski
- Weizhe Yuan
- Olga Golovneva
- Jack Lanchantin
- Yoram Bachrach
affiliations:
- FAIR at Meta
arxiv_id: '2606.25996'
url: https://arxiv.org/abs/2606.25996
pdf_url: https://arxiv.org/pdf/2606.25996
published: '2026-06-23'
collected: '2026-06-25'
category: Training
direction: 代理式数据合成 · 迭代自我改进
tags:
- synthetic data
- agentic AI
- meta-learning
- self-instruct
- data curation
- training data
one_liner: 提出代理式数据科学家框架，通过迭代生成、评估与元优化，将推理算力转化为高质量模型训练数据
practical_value: '- **搭建推荐数据飞轮**：借鉴Autodata的循环流程（生成→定性检验→定量评估→优化配方），构建自动化合成数据管线，尤其在长尾商品/查询等欠缺真实样本的场景，持续产出难例。

  - **用下游指标反馈优化生成策略**：把离线模型性能（如AUC）或线上AB指标作为reward，元优化数据生成agent的prompt或采样策略，让生成的数据更贴合业务模型需求，类似自动超参调优。

  - **在搜索推荐中迁移Agentic Self-Instruct**：将任务定义为“生成搜索词-商品对”或“对话推荐场景”，通过self-instruct +
  反思迭代，自动扩写训练集，尤其适合冷启动和少样本领域。

  - **工程落地上注意成本控制**：论文通过增加推理计算换取数据质量，实际部署时可对复杂任务才启用agent迭代，简单任务用固定模板，避免线上生成延迟过高；合理设置评估检查点与早停机制。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：AI模型训练越来越依赖高质量合成数据，现有方法难以自动生成兼具多样性、挑战性与正确标注的样本，尤其是长尾和边缘场景。

**方法**：提出Autodata框架，让大型语言模型扮演“数据科学家”角色，自主执行迭代优化：<br>① 根据数据生成配方（recipe）产生一批合成样本；<br>② 通过定性检查（如数据分析、错误分析）和定量评估（下游模型性能）生成反馈；<br>③ 整合洞察，更新生成配方，进入下一轮循环。<br>具体实现之一Agentic Self-Instruct扩展了经典self-instruct，引入反思与演进机制。进一步，可对数据科学家agent本身进行元优化，使用与外层循环相同的评估准则训练agent的提示或策略，使其生成的数据越来越好。

**关键结果**：在计算机科学研究、法律推理、数学推理三类任务上，Autodata相比经典合成方法提升显著；对agent进行元优化后，性能进一步大幅跃升。实验证明，投入更多推理算力可转化为更高训练数据质量，开拓了“用计算换数据”的新范式。
