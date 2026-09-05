---
title: Hardware-Aware FP4 FlashAttention-4
title_zh: 硬件感知的 FP4 FlashAttention-4：全 FP4 前向推理与量化反向传播
authors:
- Robert Hu
affiliations:
- Graphcore Research
arxiv_id: '2609.04105'
url: https://arxiv.org/abs/2609.04105
pdf_url: https://arxiv.org/pdf/2609.04105
published: '2026-09-03'
collected: '2026-09-05'
category: Training
direction: Transformer 注意力 FP4 量化加速
tags:
- FP4
- FlashAttention
- Quantization
- Training
- Blackwell
- Attention
one_liner: Direct-P 将注意力分数直接映射为 FP4 概率，GB200 上前向吞吐达 BF16 的 2.13 倍，8B 模型训练更新加速 1.14
  倍
practical_value: '- 推荐/广告场景中大量使用 Transformer 处理用户行为序列，注意力算子是性能瓶颈；Direct-P 将 softmax
  后的概率直接量化为 FP4，避免中间 FP32/FP16 转换，可显著提升在线推理吞吐、降低时延。

  - 训练侧采用“前向量化 Q/K，反向重建概率并使用 FP8 梯度操作数”的混合精度方案，比直接使用 FP4 概率/值更稳定；实际部署时可借鉴该方案避免训练发散，同时获得
  1.14 倍的 8B 模型更新加速。

  - 若业务使用长序列注意力（如用户行为序列、会话建模），可评估 FP4 注意力对精度的影响；论文结果表明概率 FP4 量化在非因果推理下可行，但训练中 MXFP4
  概率/值易发散，需谨慎验证。

  - 工程实现上，可将注意力中间结果（概率矩阵）显式量化并落到片上存储，减少 HBM 读写，类似 FlashAttention 的 tiling 策略与 FP4
  结合能榨取 Blackwell 张量核性能。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

动机：Blackwell 的 FP4 张量核虽快，但注意力中的 softmax 转换、片上依赖在矩阵乘缩小后成为瓶颈，单纯替换矩阵乘精度无法自动加速注意力。

方法关键点：
- 非因果推理路径：提出 Direct-P，将注意力分数直接映射为 FP4 概率，跳过先计算 softmax 再量化的环节，使 Q、K、P、V 四个操作数均可用 FP4。
- 因果训练路径：前向保存量化后的 Q、K，反向时从量化张量重建概率；概率和值保持 FP8，梯度计算使用 FP8 操作数，避免 FP4 训练发散。
- 在 NVIDIA GB200 上实现并验证，与 BF16 FlashAttention-4 对比。

关键结果：
- 非因果前向吞吐最高达到 BF16 的 2.13 倍。
- 单 GPU 8B 参数完整更新加速最高 1.14 倍。
- 分布式训练中，FP8 概率/值可稳定收敛；所有测试的 MXFP4 概率/值训练轨迹均发散。
