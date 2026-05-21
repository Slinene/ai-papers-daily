---
title: 'Divergence Meets Consensus: A Multi-Source Negative Sampling Framework for
  Sequential Recommendation'
title_zh: 发散与共识：面向序列推荐的多源负采样框架
authors:
- Yuanzi Li
- Lingjie Wang
- Jingyu Zhao
- Zihang Tian
- Yuhan Wang
- Lei Wang
- Xu Chen
affiliations:
- Renmin University of China
- Shandong University
- Peking University
arxiv_id: '2605.19651'
url: https://arxiv.org/abs/2605.19651
pdf_url: https://arxiv.org/pdf/2605.19651
published: '2026-05-19'
collected: '2026-05-21'
category: RecSys
direction: 序列推荐 · 多源负采样协同优化
tags:
- NegativeSampling
- SequentialRecommendation
- HardNegativeMining
- KnowledgeDistillation
- MultiSourceScoring
- DivergenceReranking
one_liner: 提出“教师-伙伴-自我”多源负采样框架，通过发散重排序和共识蒸馏突破自引导硬负采样的三大瓶颈
practical_value: '- **多模型协作打破自反馈循环**：使用一个结构不同的peer模型（如主模型用SASRec，peer用Mamba4Rec）提供外部负样本打分，可以注入异质信号，防止模型自引导退化。电商序列推荐可在线上训练时同时维护两个异构模型，互相提供负样本候选。

  - **利用预测分歧提升负样本多样性**：计算self与peer对同一item的打分差异，选择分歧大的item作为负例，既能保证困难度又带来多样性，相比单纯取预测最高分的方法，更能覆盖物品空间。可直接应用于召回粗排模型的负抽样，提高长尾物品的暴露率。

  - **共识蒸馏充分复用计算**：将teacher模型在候选池上的打分分布通过KL散度蒸馏到self模型，作为额外训练损失。这一做法在不增加前向推理的前提下，把原本丢弃的候选打分变成了知识迁移信号。在实际推荐系统中，每次负采样时不妨加一个蒸馏loss，几乎零成本提升泛化能力。

  - **即插即用的通用框架**：方法对MLP、RNN、Transformer、Mamba等主流序列模型均有效，且同时适配BCE和BPR损失。在已有训练流程中引入peer模型和teacher蒸馏头即可，部署成本低，可直接作为负采样模块嵌入现有电商推荐训练管线。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
当前主流的自引导硬负采样（如DNS、DNS+）虽然能动态适配模型状态，但暴露出三个核心缺陷：（1）**负自强化循环**——采样与模型更新紧密耦合，一旦选错负例，梯度更新进一步恶化模型，形成恶性循环，陷入局部最优；（2）**采样多样性受限**——仅依赖当前模型参数，采样集中在模型当前关注的狭窄区域，全局物品空间探索不足，损害泛化性；（3）**计算资源浪费**——为挑选一个硬负例需对整个候选池打分，但绝大多数评分被丢弃，信息增益与计算开销严重失衡。  

**方法关键点**  
受维果茨基“最近发展区（ZPD）”理论启发，提出**MDCNS**框架，构建“教师-伙伴-自我”三视角协同的负采样范式，包含三个核心组件：  
- **多源评分**：除待训练的self模型外，引入一个结构不同的peer模型和集成两者分数的teacher模型，各自对候选池打分，打破自反馈闭环，引入外部学习信号。  
- **发散重排序**：计算self与peer的预测差异（绝对差值）作为发散分，与原始评分相加得到“发散感知分”，据此选出Top-M个候选，再随机采样一个作为该视角的负例。这让负例同时具备挑战性和视角多样性，且缓解假阴性问题。  
- **共识蒸馏**：将teacher模型在候选池上的分数经温度参数化的softmax转化为概率分布，用KL散度将其蒸馏到self模型，作为补充的蒸馏损失。这充分复用了计算开销，将全局排序知识迁移到self，提升训练信号利用率。  
最终优化目标为三个视角负例对应的推荐损失（BPR或BCE）之和加蒸馏损失。  

**关键实验结果**  
在6个真实数据集（Amazon Beauty/Toys/Sports/Health，LastFM，KuaiRand）上，以SASRec为self、Mamba4Rec为peer进行评测。MDCNS在所有数据集和全部指标（Recall@5/10/20、NDCG@5/10/20）上均稳定优于8个基线，包括RNS、DNS、MixGCF、AdaSIR、SRNS、DNS+等。在Beauty数据集上，Recall@20提升27.29%，NDCG@20提升36.44%。此外，该方法在FMLP4Rec、GRU4Rec、LinRec等多种骨干模型及BCE/BPR两种损失函数下均取得一致显著提升，且即便peer模型较弱（如GRU4Rec）也能保持竞争力，展现出强泛化性。消融实验证实多源评分、发散重排序和共识蒸馏缺一不可。训练曲线显示蒸馏损失在训练过程中持续增大，说明机制持续提供有用梯度。  

**一句话记忆**：用“教师-伙伴-自我”多源视角打破自引导死结，以发散选样保证多样性，以共识蒸馏充分复用计算，把负采样从纯消耗件升级为知识协同件。
