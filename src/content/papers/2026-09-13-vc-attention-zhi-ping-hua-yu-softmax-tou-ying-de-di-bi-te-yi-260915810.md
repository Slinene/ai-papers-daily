---
title: 'VC-Attention: Value Smoothing and Softmax Casting for Low-bit Attention'
title_zh: VC-Attention：值平滑与 Softmax 投影的低比特注意力
authors:
- Xingyang Li
- Dongyun Zou
- Shining Zhang
- Jiacheng Chen
- Haocheng Xi
- Lvmin Zhang
- Jun-Yan Zhu
- Song Han
- Zhekai Zhang
- Yujun Lin
affiliations:
- Nunchux AI
- MIT
- CMU
- UC Berkeley
- Stanford
arxiv_id: '2609.15810'
url: https://arxiv.org/abs/2609.15810
pdf_url: https://arxiv.org/pdf/2609.15810
published: '2026-09-13'
collected: '2026-09-17'
category: Other
direction: 低比特注意力 · 量化推理加速
tags:
- low-bit attention
- quantization
- softmax
- video generation
- kernel optimization
- FP8
one_liner: 训练免费的低比特注意力框架，用值平滑和融合概率投影同时提升量化和速度
practical_value: '- 低比特激活量化中，value 异常值往往无固定通道/时空结构，可借鉴 V-Smooth：先对 token 做轻量在线聚类，使硬件
  block 内分布更均匀，再对残差（减去块均值）量化，利用 online softmax 维护的 row sum 恢复均值；该方法无需重训，可直接套用到 Transformer
  排序模型或 LLM-based Agent 的 attention 推理加速。

  - softmax 高精度指数是低比特 attention 的非 GEMM 瓶颈，ExpCast-FP8 把 log-domain 分数直接映射为 E4M3 概率码，用一次融合乘加替代
  FP32 指数和格式转换，可迁移到 LLM 推理 kernel，提高 Tensor Core 利用率、降低 pipeline 阻塞。

  - 工程上关注到 block 量化尺度由最大值决定、典型值代表范围窄的问题；通过 token 重排 + 残差量化减少误差，这种思路也适用于 embedding/特征的低比特压缩。

  - 该工作展示了在多种新 GPU 上对 attention kernel 的精细优化，可作为自研推理引擎中 attention 低比特实现的参考基线；但业务侧若以
  CPU/通用 GPU 为主，需要评估移植成本。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：Diffusion Transformers 在视频生成中表现最优，但长时空序列使 attention 成为主要部署成本。低比特 kernel 必须同时满足精度和速度：精度受 outlier 影响，value 异常值没有固定通道或时空结构，是输出误差的主要来源；速度受 softmax 限制，高精度指数计算位于两次矩阵乘之间，在数据中心 GPU 上成为最长 pipeline 阶段。

**方法关键点**：提出 VC-Attention，训练免费。V-Smooth 对 value tokens 做轻量在线聚类，使同一硬件 block 内的 token 量化更均匀；只量化残差（减去 block 均值），并利用 online softmax 维护的 row sum 恢复均值。ExpCast-FP8 将 log-domain 分数直接映射为 E4M3 概率码，通过一次融合乘加消除 FP32 指数和格式转换。实现覆盖 B200、B300、H200、RTX PRO 6000、RTX 5090。

**关键结果**：在 Wan2.2、LongCat-Video、HunyuanVideo-1.5、MiniMax-H3 上，VC-Attention 相比低比特基线提升保真度；attention kernel 相对 BF16 FlashAttention-4 在数据中心 Blackwell/Hopper 上加速 1.46–1.59x，工作站卡上加速 2.3–3.6x；端到端生成分别快 1.13–1.19x 和 1.36–1.70x。对比 SageAttention2 8-bit，PSNR 为 20.2 dB vs 19.9 dB，attention speedup 为 1.60x vs 0.29x。
