---
title: 'Search-RSI: Expanding Search Worlds Along Multimodal Agents'' Capability Frontier'
title_zh: Search-RSI：沿多模态智能体能力前沿扩展搜索世界
authors:
- Chengchao Lv
- Yin Wang
- Chunzheng Zhu
- Wanli Chang
affiliations:
- Hunan University
- New York University
arxiv_id: '2611.27780'
url: https://arxiv.org/abs/2611.27780
pdf_url: https://arxiv.org/pdf/2611.27780
published: '2026-11-20'
collected: '2026-11-23'
category: Agent
direction: 多模态搜索Agent的递归自我改进
tags:
- Multimodal
- Search Agent
- Self-Improvement
- RAG
- Curriculum Learning
- RL
one_liner: 递归自我改进框架，同步扩展任务与检索证据，避免不可达负样本，提升多模态搜索Agent
practical_value: '- **检索后端与训练任务同步扩展**：在电商/广告场景中，当生成训练样本时，同步补充检索库中缺失的商品、文档或知识片段，避免正样本检索不到导致的虚假负样本。

  - **能力前沿诊断生成课程**：借鉴按hop depth、关系稀有度、干扰密度划分任务空间并定位部分掌握区域的方法，为推荐/搜索Agent设计分阶段训练课程，优先补齐短板。

  - **利用探针分歧进行RL**：对当前策略上多个抽样结果不一致的候选样本进行强化学习，提升决策稳定性；对完全超出能力的样本转为提示引导示范，避免无效探索。

  - **保持策略在线参与数据生成**：在生成训练数据时使用当前策略而非初始模型，能持续适应能力边界，提升3.2个百分点，对在线学习系统有直接借鉴意义。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：多模态搜索Agent在检索增强推理中依赖外部证据，但现有训练配方将搜索世界视为固定，新问题可能正确但证据未入库，导致Agent检索正确却得到空结果并被错误惩罚，不可达负样本随迭代累积。

**方法关键点**：提出Search-RSI，每轮由当前策略诊断任务空间（hop depth、关系稀有度、干扰密度）中部分掌握区域，在该区域生成新任务并同步生成其证据；同一策略决定样本用途：探针输出不一致的候选进入强化学习，超出能力范围的转变为提示引导的自身演示。保持策略在循环内关键，冻结早期模型损失3.2点。无需外部模型，特权任务结构在训练前移除。

**关键结果**：在九个多模态搜索基准上，Search-RSI在静态任务增长饱和后仍持续提升，基于的配方平均准确率在9B和27B模型上分别提升9.8和9.5个百分点，其中7.0个百分点是通过单纯使世界一致无法达到的。计算开销仅为静态增长的1.27倍。
