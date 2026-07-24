---
title: 'Adaptive Depth Sparse Framework: Similarity-Driven Resource Allocation for
  Pre-Trained LLMs'
title_zh: 自适应深度稀疏框架：基于相似度驱动的预训练LLM推理加速
authors:
- Yidu Wu
- Xiang Wang
- Kejie Zhao
- Zhangchi Wang
- Qinghai Guo
- Xiaoying Tang
affiliations:
- Southern University of Science and Technology
- Huawei Technologies Co., Ltd.
arxiv_id: '2607.21291'
url: https://arxiv.org/abs/2607.21291
pdf_url: https://arxiv.org/pdf/2607.21291
published: '2026-07-23'
collected: '2026-07-24'
category: LLM
direction: LLM推理加速 · 深度稀疏化
tags:
- Depth Sparsity
- Adaptive Token Retention
- Cosine Similarity
- Inference Acceleration
- Alignment Training
- LLM
one_liner: 利用层间余弦相似度自适应分配token保留率，将预训练LLM转为深度稀疏模型，无需全量微调即大幅降低推理FLOPs
practical_value: '- **动态层稀疏用于推荐模型推理**：电商搜索推荐中常部署深层Transformer（如DIN、SIM、HSTU），可借鉴层间余弦相似度自动识别冗余层，为高延迟模块（如长序列建模）分配不同token保留率，降低在线推理耗时。

  - **轻量router做自适应输入裁剪**：router逐层选择信息量大的token，类似门控机制。在推荐系统中可用于对用户行为序列、多域特征进行动态重要性采样，尤其适合计算广告中候选物料池较大时的粗排或召回阶段。

  - **特征对齐损失稳定稀疏化训练**：在蒸馏或模型压缩时，引入中间层与最终输出的表示对齐损失，可缓解稀疏化带来的性能损失，适合将大容量推荐模型压缩为轻量线上模型。

  - **免全量微调的快速适配**：仅需少量校准数据即可将预训练LLM转为稀疏模型，此方法可推广到电商Agent或query生成模型，当目标任务变更时快速压缩模型，降低迭代成本。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：LLM在真实部署时推理成本高，现有加速方法多需任务特定微调或从头训练，跨任务可用性差。观察到Transformer各层对表示变换的贡献不均，可据此动态分配计算资源。

**方法**：提出AdaDSF框架，将现成预训练LLM直接转换为深度稀疏模型。核心是利用层输入与输出hidden states的**余弦相似度**刻画该层的表示变换强度，从相似度统计值中得出每层的token保留率（相似度越高，变换越小，可保留越少token）。在每层插入一个**轻量路由器**，根据保留率动态选择信息量大的token继续向上传递，其余token提前退出。同时引入**特征保存对齐目标**，使稀疏模型的中间层表示和最终输出与原始稠密模型对齐，仅需少量校准数据训练路由器和对齐层。

**结果**：在GPT-NeoX和Qwen2.5上的语言建模和常识推理任务中，AdaDSF显著降低推理FLOPs，性能接近稠密基线；在同等稀疏度下，精度下降幅度始终小于MoD、D-LLM、DLO等强基线。
