---
title: 'IMFuse: Instance-Aware Multi-Layer Fusion for LLM-Enhanced Sequential Recommendation'
title_zh: IMFuse：面向LLM增强序列推荐的实例感知多层融合
authors:
- Yuheng Zheng
- Yu Cui
- Bin Wu
- Jian Zhang
- Ye Feng
- Can Wang
- Jiawei Chen
affiliations:
- Zhejiang University
- Zhengzhou University
- University of Science and Technology of China
arxiv_id: '2607.27002'
url: https://arxiv.org/abs/2607.27002
pdf_url: https://arxiv.org/pdf/2607.27002
published: '2026-07-29'
collected: '2026-07-30'
category: RecSys
direction: 实例感知多层融合 · LLM增强序列推荐
tags:
- Sequential Recommendation
- Multi-Layer Fusion
- LLM Embedding
- Instance-Aware
- Dimensional Collapse
- Semantic Enhancement
one_liner: 自适应聚合LLM多层语义表示，以全局维度偏好与实例感知调制解决最终层坍塌，提升推荐质量
practical_value: '- **多层语义融合即插即用**：现有LLM增强推荐只取最终层，容易丢失中间层互补信息。IMFuse 作为轻量插件（+0.03M参数），可在不改动下游模型的情况下，将多层的维度级全局偏好与物品实例调制接入现有
  pipeline，直接提升 item embedding 质量，适合快速上线验证。

  - **处理不同品类/属性物品的语义深度差异**：通过 instance-aware 专家调制，动态为每个 item 分配不同的层融合权重。在电商推荐中，标品（如电子产品）与非标品（如服饰）可能需要不同粒度的语义，可借鉴该思路为不同品类或生命周期阶段（新品、成熟品）定制层选择策略。

  - **初始化策略与训练技巧**：采用深度偏置初始化（层深度越高初始权重越大）提供弱先验，可稳定训练并加速收敛。在实际业务中，可以先从最终层权重为主开始，再让模型自主学习调整层偏好，避免随机初始化带来的不稳定。

  - **参数效率与推理开销可控**：训练与推理耗时相比基础方法仅增加约3~4%，适合在线服务。若担心多层编码的计算压力，可预先计算并缓存各层 embedding，融合只在
  forward 时做一次加权求和，成本极低。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
现有 LLM 增强的序列推荐通常直接使用 LLM 最终层隐藏状态作为物品语义表示，忽略了中间层可能编码的互补信息。作者通过实验分析发现：深层表示维度坍塌严重（Top-K 奇异值占比更高）；不同层之间的语义相似度随层距增大而显著下降，说明各层捕捉不同粒度的语义；此外，不同物品组的层间表示演化模式存在明显异质性（如某些品类在深层迅速坍塌，某些平缓变化），表明固定单一层对全体物品并非最优。

**方法关键点**
- **全局维度级层偏好学习**：引入可学习矩阵 W∈R^(d×(L+1))，经 softmax 得到每个语义维度对不同层的偏好权重，实现维度级的自适应层选择。
- **实例感知专家调制**：将最终层表示作为物品语义摘要，通过路由器生成一组共享层偏好模板的权重，动态调整各物品的层融合系数，既避免每个物品独立学习参数的灾难，又实现物品级自适应。
- **融合与即插即用**：加权求和多层变换后的 embedding 得到最终语义表示，再与 ID embedding 融合（如拼接或相加），下游推荐模型无需改动。

**关键结果**
在 Amazon Clothing、Beauty、Toy、Office 四个数据集上进行评估。与四个语义增强基线（RLMRec、LLM-ESR、LLMInit、SpecTran）结合时，IMFuse 在 SASRec和 HSTU 上平均相对提升 6.72%；与三个多层融合基线（LAEF、CASE-MLP、VA-HS）相比平均相对提升 3.91%。消融实验表明，去掉多层信息或去掉实例感知调制都会导致性能明显下降。效率方面，仅增加 0.03M 可训练参数，训练和推理成本几乎不变，且在 LLaMA-3-8B 和 Qwen3-8B 两个 LLM 编码器上均取得一致增益。
