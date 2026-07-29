---
title: 'The Case Against Generation for Retrieval: Discriminative Language Models
  as Effective Retrievers'
title_zh: 判别式LLM反击：用双塔模型替代生成式推荐检索
authors:
- Zhe Xu
- Prachi Agrawal
- Kavosh Asadi
- Tianyi Chen
- Carl Hu
- Justin Johnson
- Wuwei Lan
- Mingfu Liang
- Xi Liu
- Tik On Lui
affiliations:
- Meta
arxiv_id: '2607.25346'
url: https://arxiv.org/abs/2607.25346
pdf_url: https://arxiv.org/pdf/2607.25346
published: '2026-07-28'
collected: '2026-07-29'
category: RecSys
direction: LLM双塔检索 · 判别式推荐
tags:
- LLM
- Two-Tower
- Knowledge Distillation
- Retrieval
- Recommender System
- Discriminative
one_liner: 将LLM作为共享背板的双塔检索器，配合蒸馏与连续思考，性能匹敌生成式推荐且可规模化部署
practical_value: '- **双塔+LLM的务实路线**：放弃生成式检索的Token解码，改用LLM编码器生成用户和物品的向量，通过ANN检索。对于物料量大的电商/广告系统，这种方案更易落地，无需担心Token到物品ID的映射错误和自回归延迟。

  - **蒸馏技巧：从Cross-Encoder教师转移动态排序知识**：用Cross-Encoder对同一候选集计算更准确的分数分布，然后以KL散度蒸馏到双塔学生。实操中可使用“yes/no”输出头计算logit差作为分数，同时加一个以用户历史为条件的Token预测辅助任务来增强教师，提升蒸馏上限。

  - **Token级特征压缩与层剪枝**：将连续特征用有限标量量化（FSQ）离散化为少量Token，减少输入长度，提升QPS 19.7%；对Transformer进行层剪枝（搜索代理指标评估重要性）再知识迁移，可再提速10%，几乎无损。

  - **数据效率与模型时效性**：LLM双塔在仅用0.5%训练数据下即可匹敌生产DLRM基线；模型冻结后连续数天性能几乎不降，而传统DLRM因物品ID分布漂移损失严重，该特性可大幅降低重训成本，适合推荐系统频繁更新的场景。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
生成式LLM推荐（如TIGER、OneRec）受限于自回归解码延迟、Token到物品ID映射错误，难以在工业级检索中实时服务。经典的DSSM双塔模型虽然高效，但缺乏LLM级语义表达。本文探索以LLM作为双塔编码器的可行性，用判别式表示取代生成式检索，保持高效检索的同时获得现代语义理解。

**方法关键点**  
- **教师增强**：Cross-Encoder用“yes/no”输出头通过比较“yes”和“no”的logit差作为相关性分数；增加用户条件下的物品文本逐Token预测辅助损失，强化领域理解。  
- **学生结构**：共享LLM编码器分别编码用户和物品，采用**EOS Token池化**获得序列级表示（优于均值池化）。  
- **知识迁移**：**跨数据集迁移学习**：在多个推荐数据集上先联合训练，再在目标任务微调；**候选集分数分布蒸馏**：教师Cross-Encoder在相同候选集上生成软标签，学生双塔最小化KL散度。  
- **Coconut式连续思考**：仅用户塔增加一步连续隐状态推理（不解码成Token），保留物品塔的预计算能力，提升用户表示质量。  

**实验结果**  
在三个Amazon数据集（Beauty, Sports, Toys）上，Cross-Encoder教师全面超越OneRec-Think（SOTA），用0.6B模型超过8B模型；双塔学生在Recall@10上分别超出ORT 4.3%、31.6%、35.3%。内部生产测试中，LLM双塔仅用0.5%训练数据即达到DLRM基线，对尾部物品提升5.5%，冻结模型多天零退化，且通过FSQ特征压缩、层剪枝、量化等优化显著提升QPS。
