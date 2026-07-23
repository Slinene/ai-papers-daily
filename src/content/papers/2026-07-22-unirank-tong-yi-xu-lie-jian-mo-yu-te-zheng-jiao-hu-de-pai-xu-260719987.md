---
title: 'UniRank: Benchmarking Ranking Models for Unified Sequential Modeling and Feature
  Interaction'
title_zh: UniRank：统一序列建模与特征交互的排序模型基准
authors:
- Honghao Li
- Xianquan Wang
- Zibin Zhang
- Yi Zhang
- Kangyi Lin
- Yiwen Zhang
affiliations:
- Anhui University
- University of Science and Technology of China
- Tencent Inc.
arxiv_id: '2607.19987'
url: https://arxiv.org/abs/2607.19987
pdf_url: https://arxiv.org/pdf/2607.19987
published: '2026-07-22'
collected: '2026-07-23'
category: Eval
direction: 统一排序模型基准测试
tags:
- Ranking Models
- Sequential Modeling
- Feature Interaction
- Benchmarking
- Multi-Task
- Reproducibility
one_liner: 首个面向 Token 化统一排序模型的开放基准，标准化多任务点式自回归评估并降低训练成本
practical_value: '- **Tokenization 策略选择**：Field 保留语义边界、Auto 学习全局交互、Chunk/Random 引入高熵分组表征，应根据特征场数量与交互需求选取；电商场景下
  Auto 通常更稳，Chunk 在特征较多时可能带来多样性增益。

  - **注意力激活函数**：GeLU 和 SiLU 作为注意力 logits 激活在两个数据集上平均 AUC 提升最显著（KuaiRand +0.51, MerRec
  +0.38），优于传统 Softmax；Sigmoid 对点赞等稀疏任务有利，可针对不同目标 task 单独配置。

  - **即插即用的 AttGate**：在注意力后加一个可学习的 sigmoid 门控，是所有实验中唯一在两个数据集的所有任务上都有提升的组件（KuaiRand
  平均 AUC +0.88, MerRec +0.99），可作为通用即插即用模块嵌入现有排序模型。

  - **优化器与缩放定律**：稠密参数优化器 AdamW 并非最优，LaProp、SOAP、Muon 在不同数据集上分别带来 0.6~1.9 个点的平均 AUC
  提升；缩放时栈式模型提升 token 维度即可，层式模型需同时增加序列长度和深度，架构决定了有效扩展方向，不能只看 FLOPs。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现代排序模型日趋将序列建模与特征交互统一在 Token 化架构中，但多数工作依赖闭源数据、私有代码和工业基础设施，学术研究难以复现对比，也无法系统研究缩放定律、长序列建模与多任务排序。

### 方法关键点
- **统一基准框架**：提出 UniRank，提供标准化数据流程、评估指标、训练流水线，对 15 个统一排序模型在 5 个大规模公开数据集上进行了公平对比。
- **点式自回归训练范式**：采用按时间序的完整反馈序列构建样本，每个 instance 从过去行为预测当前目标，使梯度更稠密，充分利用长序列与多任务标签。
- **优化工具包**：集成 DDP、混合精度训练、Flash Attention、Flex Attention、激活检查点、稀疏/稠密参数分离优化等，在四卡 H20 上实现 14.24 倍训练加速且单卡显存降低 69%。
- **实用手册研究**：系统地比较了 Tokenization 策略（Chunk、Auto、Field、Random）、注意力激活函数（GeLU、SiLU 等）、架构增强（AttGate、QKNorm、RoPE 等）以及稠密优化器（LaProp、SOAP、Muon）的效果。

### 关键结果
- **数据规模**：最大数据集 QK-Video 含超 7 亿实例，KuaiRand 最长行为序列超 22.8 万次。
- **模型表现**：没有单一模型在所有数据集所有任务上最优；EST 和 HeMix 在电商平台 Taobao/MerRec 占优，UltraHSTU、LONGER 等短视频模型在 QK-Video/KuaiRand 更好；TokenFormer 在广告数据集 TAAC-25 竞争力强。
- **激活函数**：GeLU 将 OneTrans 在 KuaiRand 平均 AUC 从 0.8548 提至 0.8599，MerRec 从 0.8051 提至 0.8089，SiLU 效果相近。
- **架构增强**：AttGate 在 KuaiRand 和 MerRec 分别将平均 AUC 提升 0.88 和 0.99 个百分点，是唯一跨数据集全面增益的组件。
- **优化器**：SOAP 在 MerRec 上使 RankMixer 平均 AUC 提升 1.93 个百分点，LaProp 在 KuaiRand 提升 0.61 个百分点。
- **缩放定律**：栈式模型 RankMixer 仅受益于更宽的 token 维度；层式模型 OneTrans 需同时扩 token 维度、序列长度和层数才能有效扩展。

**最值得记住的一句话**：统一排序模型的性能高度数据集依赖，且实用提升往往来自精心选择的 Tokenization、注意力激活函数和即插即用门控等小改动，而非单纯扩大模型容量。
