---
title: 'TPHC: Improving Hyper-Connections with Tensor-Parallel Grouped Updates'
title_zh: 'TPHC: 通过张量并行分组更新改进超连接'
authors:
- Xinying Hu
- You Wu
- Haoyi Wu
- Jianchao Tan
- Kefeng Zhang
- Yuchen Xie
- Kewei Tu
affiliations:
- School of Information Science and Technology, ShanghaiTech University
- Shanghai Engineering Research Center of Intelligent Vision and Imaging
- Meituan
arxiv_id: '2611.23026'
url: https://arxiv.org/abs/2611.23026
pdf_url: https://arxiv.org/pdf/2611.23026
published: '2026-11-16'
collected: '2026-11-18'
category: Training
direction: 大模型架构 · 超连接与张量并行融合
tags:
- Hyper-Connections
- Tensor Parallel
- LLM Training
- Residual Streams
- Model Architecture
one_liner: 把张量并行分片与超连接流集成，提升残差流更新独立性且不增加参数/FLOPs，扩展能力更强
practical_value: '- 若需自研或微调大模型底座，TPHC 提供一种低开销的架构升级：同 stream 数下训练时间仅比 mHC 多 9%，但验证损失降低
  0.7–1.0%，适合资源敏感的业务预训练场景。

  - 多流独立更新的思想可借鉴到推荐/排序模型特征融合：为不同特征域建立并行残差流，每个子层或专家独立混合并写回，增强表达多样性而不增加主计算 FLOPs。

  - 其实现在 tensor parallel 下原生支持 stream sharding，说明新的多流机制可无缝嵌入现有分布式训练框架，对生产环境多卡训练有工程参考价值。

  - 但该方法是通用 Transformer 架构改进，并非直接解决搜索推荐业务问题，落地前需在自身数据上验证收益。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**  
Hyper-Connections (HC) 将 Transformer 残差流扩展为 N 条并行流，manifold-constrained HC (mHC) 虽稳定但超过 4 条流后收益甚微，原因在于每个子层只向所有流写同一输出，限制了流间更新差异性。  

**方法关键点**  
TPHC 集成张量并行(TP)分片与 HC 流：为每个 TP shard 单独路由不同的残差流混合，并在写回时保留各 shard 输出独立，使得每条流可接收这些输出的不同组合。此设计不增加 attention/FFN 子层的参数或 FLOPs，却显著提升残差流更新表达力。同时支持 TP 下的原生流分片，8B 模型四流训练时间仅比 mHC 多 9%，流数从 4 增至 16 训练开销仅增 19%。  

**关键结果数字**  
在 1.1B 模型训练 100B tokens 后，TPHC 相比同流数 mHC (N=4/8/16) 验证损失降低 0.7–1.0%，六个常识推理基准平均零样本准确率提升 0.3–0.7 个百分点。
