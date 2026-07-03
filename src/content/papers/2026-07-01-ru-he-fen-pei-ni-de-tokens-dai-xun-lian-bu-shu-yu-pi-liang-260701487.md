---
title: How to Allocate Your Tokens? Scaling Laws with Training Steps and Batch Size
title_zh: 如何分配你的 Tokens？带训练步数与批量大小的缩放律
authors:
- Fabian Schaipp
affiliations:
- Inria, École Normale Supérieure, PSL Research University, Paris
arxiv_id: '2607.01487'
url: https://arxiv.org/abs/2607.01487
pdf_url: https://arxiv.org/pdf/2607.01487
published: '2026-07-01'
collected: '2026-07-03'
category: Training
direction: 训练缩放律 · 显式分离步数与批量大小
tags:
- Scaling Law
- Batch Size
- Training Steps
- LLM Training
- Optimal Compute Allocation
one_liner: 提出三项式缩放律，显式分离训练步数和批量大小，用更少实验恢复最优批量并推导次优批量缩放律
practical_value: '- 在推荐/搜索大模型训练中，可利用三项式缩放律预测最优批量大小，减少超参搜索成本，直接根据总 token 预算分配模型大小、步数和批量。

  - 当训练数据（如用户行为序列）总量固定时，通过权衡训练步数和批量大小，可在有限资源下达到更优损失，例如在生成式推荐模型微调时，若数据稀缺，可减小批量以增加步数来提升效果。

  - 该缩放律允许利用次优批量下的实验点进行拟合，工程上只需少量试跑即可估算资源最优配置，适合多业务线（广告、搜索、推荐）快速探索。

  - 推导的次优批量缩放关系可用于设计动态批量策略，例如在训练前期用小批量快速收敛，后期加大批量稳定训练，提升整体效率。'
score: 7
source: arxiv-stat.ML
depth: abstract
---

**动机**：现有 LLM 缩放律通常将训练数据量 D 作为整体，未区分训练步数和批量大小，导致无法指导在固定 token 预算下如何分配步数与批量。实践中，最优批量大小随计算量增加而增大，但缺乏理论公式。

**方法关键点**：提出三项式缩放律 L(N, T, B) = E + A/N^α + B'/T^β + C/B^γ，将测试损失建模为模型大小 N、训练步数 T 和批量大小 B 的函数。通过拟合大量不同（N, T, B）组合的训练运行数据，显式分离步数与批量的影响。

**关键结果**：该律能正确恢复最优批量大小随计算量增加的幂律关系（指数约为0.5），且即使使用次优批量下的部分实验点也能稳健拟合，大幅减少所需训练运行数量。进一步推导出次优批量下的缩放律，并验证了与“临界批量大小”现象的一致性，即存在一个临界批量值，超过后增加批量收益递减。
