---
title: 'BiSCo-LLM: Lookup-Free Binary Spherical Coding for Extreme Low-Bit Large Language
  Model Compression'
title_zh: BiSCo-LLM：面向大语言模型极端低比特的无码本二进制球形编码压缩
authors:
- Yuantian Shao
- Peisong Wang
- Zhilei Liu
- Chuangyi Li
- Yuanteng Chen
- Pengcheng Xie
- Yiwu Yao
- Zhihui Wei
- Jian Cheng
arxiv_id: '2607.08643'
url: https://arxiv.org/abs/2607.08643
pdf_url: https://arxiv.org/pdf/2607.08643
published: '2026-07-09'
collected: '2026-07-10'
category: LLM
direction: LLM 极端低比特压缩
tags:
- LLM Compression
- Spherical Coding
- Quantization
- Codebook-Free
- LoRA
one_liner: 提出无码本二进制球形编码框架，结合残差编码与恢复蒸馏，在 2 比特/权重下保持 LLM 性能
practical_value: '- 推荐系统部署大型 Transformer 模型时，可借鉴球形编码将权重压缩至 2 比特，显著减少显存和带宽压力，且无需存储码本，避免查找开销，适合在线推理。

  - 采用残差编码路径可灵活控制压缩率与精度，工程上可按模块重要性分配比特，优先保证敏感层精度，适用于参数量大的生成式推荐模型。

  - 敏感通道保护策略（保留少量 8 比特通道）与 LoRA 适配器联合使用，可在极低比特下稳定模型行为，推荐系统在压缩特征交叉网络或用户编码器时可复用。

  - 恢复蒸馏直接在模块替换后对齐输出分布，优于逐层重建，能更好保持端到端推荐效果，对压缩后微调流程有直接参考价值。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：大语言模型部署受限于内存带宽和存储容量，传统量化在 2 比特/权重下表示能力骤降，而矢量量化引入码本和索引查找，增加实现复杂度。需要一种既保持低比特率又避免码本开销的压缩方法。

**方法关键点**：
- 将权重块映射到单位超球面并二值化为紧凑球形码（BSQ），主体为比特打包的符号流，无需显式码本。
- 引入残差 BSQ 阶段编码基码重构误差，提供无码本的显式率失真控制。
- 逐类替换 Transformer 模块后进行类别级恢复蒸馏，减小局部重构与全局行为偏差。
- 少量敏感通道保留 8 比特作为保护路径，与 BSQ 载荷分计，辅以 LoRA 适配器补偿。

**关键结果**：在 Qwen3-8B 上，WikiText-2 困惑度仅从 FP16 的 9.73 升至 10.18，7 任务平均下游准确率从 69.92 稍降至 68.05，证实无码本球形编码在极端低比特下可有效保持模型能力。
