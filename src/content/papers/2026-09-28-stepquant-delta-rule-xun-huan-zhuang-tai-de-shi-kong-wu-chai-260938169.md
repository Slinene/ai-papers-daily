---
title: 'STEPQuant: When and Where Errors Matter in Delta-Rule Recurrent State Quantization'
title_zh: STEPQuant：Delta-rule 循环状态的时空误差感知量化
authors:
- Bingchen Yao
- Haobo Xu
- Haokun Lin
- Yichen Wu
- Ziyu Guo
- Renrui Zhang
- Zhichao Lu
- Zhenan Sun
- Ying Wei
affiliations:
- Zhejiang University
- NLPR & MAIS, Institute of Automation, CAS
- Tsinghua University
- City University of Hong Kong
- Harvard University
arxiv_id: '2609.38169'
url: https://arxiv.org/abs/2609.38169
pdf_url: https://arxiv.org/pdf/2609.38169
published: '2026-09-28'
collected: '2026-10-08'
category: LLM
direction: 线性注意力循环状态量化压缩
tags:
- Linear Attention
- Recurrent State
- Post-Training Quantization
- Delta-Rule
- Serving Memory
one_liner: 提出时空感知的循环状态量化框架，按误差幅度与记忆寿命分配精度，并联合拟合 key-row/value-column 尺度
practical_value: '- 若在线推荐/Agent 部署了 Qwen3.8-27B、Kimi-Linear-48B-A3B-Instruct 等混合线性注意力模型做生成式召回、query
  改写或工具调用，可直接采用 STEPQuant 对循环状态做 6-bit 后训练量化，在接近 FP32 精度下获得 5× 状态压缩和大幅显存下降，适合大并发服务。

  - 可借鉴其时空混合精度分配思想：在维护 user state / memory 时，不对所有维度一视同仁，按“记忆寿命”和“对输出误差的敏感度”做非均匀量化；长期偏好或高敏感维度保留
  FP16/INT8，短期临时状态可降到 4-bit。

  - 联合拟合 key-row 与 value-column 缩放系数的做法，对推荐模型里矩阵型状态（如 user embedding × topic embedding、长期兴趣矩阵）有启发：先离线估计各行列对最终
  loss/输出的影响，再定制 scale 而非全局 uniform。

  - 如果团队自研推理框架，可参考它在 SGLang 中的 GPU kernel 集成方式，将状态压缩与 serving 显存核算结合，上线前用长/短生成 benchmark
  做精度-显存回归。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：线性注意力以固定大小循环状态替代随序列增长的 KV cache，但在并发推理时循环状态仍可能成为显存瓶颈；直接量化误差会在状态迭代更新中不断累积放大，导致精度崩溃。

关键观察：量化误差的影响具有时空异质性。时间上，长寿命记忆中的误差会跨多步持续传播；空间上，不同 key rows 对最终输出的扰动差异明显，且状态值在行、列方向上幅度分布高度不均。

方法：提出 STEPQuant，面向 Delta-rule 循环状态的 post-training 量化框架。依据误差幅度与记忆生命周期分配比特精度；结合状态分布和 key-row 对输出误差的影响，联合拟合 key-row 与 value-column 缩放系数，而非简单 uniform 量化。

结果：在 Qwen3.8-27B 与 Kimi-Linear-48B-A3B-Instruct 上，6-bit 名义预算下接近 FP32 状态准确度；其 4-bit 配置超过 uniform INT8。集成 SGLang 后 6-bit 循环状态压缩超 5×，总服务显存最高降低 68.7%。
