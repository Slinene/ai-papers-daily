---
title: 'xHC: Expanded Hyper-Connections'
title_zh: 扩展超连接：突破流数瓶颈实现高效大模型预训练
authors:
- Xiangdong Zhang
- Xiaohan Qin
- Sunan Zou
- Tuo Dai
- Xiaoming Shi
- Huaijin Wu
- Yebin Yang
- Zhuo Xia
- Shaofeng Zhang
- Lin Yao
affiliations:
- School of AI, Shanghai Jiao Tong University
- Dots Studio, Xiaohongshu Inc.
- University of Science and Technology of China
- School of CS, Peking University
- The Chinese University of Hong Kong
arxiv_id: '2607.14530'
url: https://arxiv.org/abs/2607.14530
pdf_url: https://arxiv.org/pdf/2607.14530
published: '2026-07-15'
collected: '2026-07-20'
category: LLM
direction: LLM架构优化 · 残差流扩展
tags:
- Hyper-Connections
- Residual Stream Expansion
- Sparse Architecture
- MoE
- Memory Efficiency
- LLM Pretraining
one_liner: 通过时间特征增强和稀疏残差流（仅更新k=4/N=16）突破HC的N=4瓶颈，在MoE模型上大幅提升性能并降低计算开销
practical_value: '- 稀疏更新策略：xHC 每层只更新 k=4 条流但读取全部流，类似推荐系统中大规模 Embedding 表或状态存储可采用“稠密读取-稀疏更新”模式，仅刷新部分高频/重要行，降低训练更新开销。

  - 多流残差结构：多条并行残差流可视为不同变换路径的集成，该思想可迁移到推荐模型的多模态、多任务学习，用不同流编码用户、商品、上下文等异构特征，再通过可学习的混合机制融合。

  - 内存带宽优化：xHC-Flash 通过融合流维度与批次维度的矩阵乘法减少中间状态传输，对推荐模型部署中的显存带宽瓶颈有借鉴意义，尤其适用于大规模特征交叉或
  Embedding 交互层的显存优化。

  - 高效扩展范式：在有限训练预算下通过架构改进提升大模型性能，对电商搜索/推荐场景中自行预训练 LLM 的团队，提供了一条除增加模型尺寸外的算力友好扩展路径。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：Hyper-Connections (HC) 将 Transformer 残差流扩展为 N 条并行流，获得超越宽度和深度的额外记忆扩展维度，但现有方法止步于 N=4。实验发现继续增大 N 会导致性能收益递减与训练开销激增，瓶颈在于：（1）写回信息不足以为增多的流提供有效更新；（2）残差混合生成的计算量与 N 的立方成正比。

**方法**：提出 xHC，首次将 N 扩展至 16 并保持有效训练。关键设计：（1）时间特征增强：将前一层输出特征融入当前写回信息，丰富每条流的更新信号；（2）稀疏残差流架构：仅更新 k=4 条流，其余保持历史状态，但所有流均可被稠密读取，将复杂度从 O(N³) 降至 O(kN²)。此外，xHC-Flash 通过融合流维度与批次维度的矩阵乘法，将每子层内存流量从 73.5C 降至 40C。

**结果**：在 18B 和 28B MoE 模型上，xHC 比 mHC 平均下游得分提升 4.0 分，训练 FLOPs 仅略高于 vanilla 基线。Scaling-law 实验表明，达到相同损失时，vanilla 和 mHC 分别需 xHC 1.50 倍和 1.19 倍计算量。xHC-Flash 在保持性能的同时，将内存流量降至与 N=4 的 mHC 相当。
