---
title: Where, When, and How Many Bits? Scaling Laws for SGD with Stochastic Rounding
title_zh: 随机舍入 SGD 的比特数、训练时间与模型规模缩放定律
authors:
- Zhichao Wang
- Michael W. Mahoney
affiliations:
- University of California, Berkeley
- ICSI
- LBNL
arxiv_id: '2610.41074'
url: https://arxiv.org/abs/2610.41074
pdf_url: https://arxiv.org/pdf/2610.41074
published: '2026-10-29'
collected: '2026-11-02'
category: Training
direction: 低精度训练 · 随机舍入 scaling laws
tags:
- stochastic rounding
- low-precision training
- scaling laws
- SGD
- quantization
- compute-optimal
one_liner: 在两层线性网络上证明随机舍入 SGD 预测误差上下界，给出精度、模型规模与训练时间的 compute-optimal scaling 法则
practical_value: '- 在 LLM/推荐模型低精度训练中优先用随机舍入替代就近舍入，尤其前向激活可低至 8bit/4bit，但反向特征需保留更高精度或单独调度，否则会改变
  compute-optimal scaling。

  - 采用 EMA/参数平均时，可重新评估各计算环节精度需求：论文表明参数平均会改变哪一阶段需要更高精度，因此推荐训练中的参数平均（如模型合并、Polyak）可搭配更激进的前向量化而不伤害最终效果。

  - 固定算力预算下，若需要扩模型或加训练时间，可尝试降低精度换取更多 FLOPs/epochs；在电商搜索推荐的大规模模型训练中，这可能优于保持 BF16/FP32
  的小模型。

  - 学习率调度需随反向舍入精度调整：部署低精度反向时，原最优学习率可能失效，需搜索并配合 warmup/衰减，避免训练不稳定或收敛变慢。'
score: 7
source: arxiv-stat.ML
depth: abstract
---

动机：低精度训练能降低计算开销，但引入舍入误差；现有工作缺少对随机舍入（SR）在预测误差上的理论 scaling 分析。方法：考虑两层线性网络，第一层固定随机，使用 mini-batch SGD 在新采样的高斯数据（power-law 谱）上训练，前向和反向特征每步独立随机舍入；证明最终模型和均匀参数平均的预测误差上下界，允许预定义的通用学习率与精度调度。关键结果：在固定精度、常数学习率与参数平均下，推导出最小预测误差随计算预算的下降规律，并识别达到最优计算 scaling 的模型规模与训练时长；仅对前向特征舍入不会破坏精确算术的计算 scaling，反向舍入则会改变 scaling；参数平均会改变哪一阶段需要更高精度；给出满足精度容忍的比特需求，并表明反向舍入影响学习率调度设计；固定计算预算时，降低精度可能在更大模型或更长训练带来的收益超过额外误差时改善预测。模拟与 MLP、小 transformer 实验验证了这些权衡。
