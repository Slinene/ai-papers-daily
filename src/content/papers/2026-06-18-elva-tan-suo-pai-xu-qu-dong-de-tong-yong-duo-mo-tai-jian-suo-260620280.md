---
title: 'ELVA: Exploring Ranking-Driven Universal Multimodal Retrieval'
title_zh: ELVA：探索排序驱动的通用多模态检索
authors:
- Yuhan Liu
- Pei Fu
- Hang Li
- Yukun Qi
- Chao Jiang
- Jingwen Fu
- Zhen Liu
- Bin Qin
- Zhenbo Luo
- Jian Luan
affiliations:
- National Key Laboratory of Human-Machine Hybrid Augmented Intelligence, Xi'an Jiaotong
  University
- MiLM Plus, Xiaomi Inc
- Zhongguancun Academy, Beijing, China
arxiv_id: '2606.20280'
url: https://arxiv.org/abs/2606.20280
pdf_url: https://arxiv.org/pdf/2606.20280
published: '2026-06-18'
collected: '2026-06-19'
category: Multimodal
direction: 通用多模态检索 · 排序驱动强化学习
tags:
- Multimodal Retrieval
- Reinforcement Learning
- Grain Blindness
- Contrastive Learning
- Ranking Reward
- LLM
one_liner: 用排序驱动强化学习缓解多模态检索模型对比训练中的“粒度盲目”，在复杂查询上提升13.1%
practical_value: '- **排序感知的奖励设计可迁移至推荐 / 搜索重排**：将 NDCG 类连续排名奖励与 margin 约束结合，无需人工标注即可在强化学习训练中细化物品间层级关系；在电商多模态搜索、视频推荐重排中可复用该思路优化候选列表的全局次序。

  - **生成式 embedding 提取范式增加 RL 探索方差**：让 MLLM 先自回归生成输入的文字摘要，再从专用 [RET] token 的隐状态取嵌入，可产生足够的表示方差，支持
  GRPO 等策略优化。这一 trick 可直接用于基于 LLM 的语义 ID 生成或 query 改写 RL 训练。

  - **平衡负采样策略保障 RL 训练稳定**：通过过滤过高相似度的负样 + 混合随机负样，扩大奖励方差并防止过拟合。在召回模型训练或 LLM Ranker 的对齐阶段，该采样思想可提高训练的收敛速度和最终效果。

  - **多粒度查询基准 MRBench 的构建方法具有借鉴意义**：利用 VL model 自动筛选多粒度属性查询再人工检验，可用于评估自家多模态搜索系统对复杂意图（如“红色连衣裙配银色高跟鞋”）的召回完整性。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
现有通用多模态检索（UMR）将 MLLM 经对比学习适配为检索器时，普遍存在“粒度盲目”（grain blindness）问题：模型只抓住查询中最显著的一两个粒度，忽略次要但关键的细粒度信息，导致在多属性复杂查询（如实体的同时要求动作）上表现差。其根源在于对比损失将所有负样本等同对待，无法利用不同负样本所携带的差异化信号。  

**方法**  
提出 **ELVA**（Exploratory Ranking-Driven UMR framework），把检索转化为排序驱动强化学习任务，核心改动有三：  
- **生成式嵌入提取**：要求 MLLM 先生成输入的文字摘要，再以特殊 token [RET] 的隐状态作为检索嵌入，为 RL 策略探索提供必要方差。  
- **双维度可验证奖励**：  
  - *Margin Reward*：强制正样本与最难负样本保持最小相似度 gap，避免正负混淆。  
  - *Ranking Reward*：连续化 NDCG 式排序奖励，鼓励正样本排在前列，并依据相似度给负样本分配不同惩罚，从而优化负样本间的层级结构，让模型感知不同粒度的差异。  
  - 两者加权联合，无需人工排序标签。  
- **平衡负采样策略**：过滤掉过于相似的负样后，再混合 50 个 top 相似负样与 50 个随机负样，扩大奖励方差，保证 RL 训练稳定。  
训练分三阶段：NL I 预训练→M-BEIR 指令微调→RL 微调。  

**结果**  
- M-BEIR 16 项子任务平均：ELVA-7B 达 58.7% Recall，比 LamRA-7B 高 2.1%，2B 版本也超过多数 7B 模型。  
- 多粒度专门基准 MRBench 上相对 SOTA 提升 13.1%，定性显示能同时抓住实体和动作等多粒度信息。  
- 未见数据集与任务上的泛化性显著，如图文匹配任务提升 9.7%，可作为即插即用的 RL booster 应用到其他检索模型。  
- 消融证实排序奖励、margin 奖励和各负采样策略均贡献明显。  

**核心洞见**：将 NDCG 式连续排序奖励引入 RL 训练，使模型在学习区分正负的同时学习负样本间的相对顺序，是消除检索模型粒度盲区的关键。
