---
title: 'OffQ: Taming Structured Outliers in LLM Quantization by Offsetting'
title_zh: OffQ：用偏移消除LLM量化中的结构化离群值
authors:
- Haoqi Wang
- Lorenz K. Mueller
- Jiawei Zhuang
- Mathieu Salzmann
- Lukas Cavigelli
affiliations:
- EPFL
- Huawei
- ETH Zurich
arxiv_id: '2606.07116'
url: https://arxiv.org/abs/2606.07116
pdf_url: https://arxiv.org/pdf/2606.07116
published: '2026-06-05'
collected: '2026-06-08'
category: LLM
direction: LLM量化 · 后训练均匀精度
tags:
- LLM Quantization
- Activation Outliers
- W4A4KV4
- Offsetting
- Top-1 PCA
- PTQ
one_liner: 提出OffQ，通过Top-1 PCA浓缩离群并在组内用Hadamard旋转转为偏移，实现统一精度W4A4KV4量化，超越SoTA。
practical_value: '- **推理加速**：W4A4KV4量化将模型内存与计算缩减至4-bit，直接降低在线推理成本，适合电商推荐、多Agent对话等延迟敏感场景，OffQ可避免精度损失过多。

  - **离群值处理**：利用Top-1 PCA识别activation离群方向并浓缩到单一通道，然后通过组偏移吸收，该方法可迁移至任何需要消除离群值的量化场景（如模型压缩、KV
  cache量化）。

  - **工程实现**：不依赖反向传播学习旋转或混合精度，仅需标准均匀量化和快速Hadamard旋转，可在现有推理框架中轻量集成，无需定制核函数。

  - **组量化策略**：采用分组偏移和排序分组，平衡量化粒度与开销；每128通道一组时等效位宽仅4.25bits，适合做显存/带宽受限的边缘部署。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**  
LLM中的activation离群值（极少数通道上的超大值）会强制粗粒度的量化步长，导致W4A4KV4量化严重退化。已有旋转方法虽然能改善分布，但残留方差仍限制量化效果，而混合精度或非均匀量化则增加工程开销。因此，需要一种既能彻底消除离群影响、又不牺牲实现简单性的方法。

**方法关键点**  
- **Top-1 PCA浓缩离群**：从校准集的每个序列中选取L∞范数最大的token，构建token矩阵并计算协方差，取第一主成分作为离群方向，通过旋转将activation能量集中到首个通道。相比标准PCA，top-1选择避免正常token干扰，离群捕获更准。  
- **组偏移吸收**：将通道分为多组，每组包含一个离群通道；组内用第一行全1的Hadamard矩阵旋转，使离群值均匀散布为所有通道的常量偏移，该偏移被非对称量化的零点吸收，剩余通道分布平坦，可直接低bit量化。  
- **整体流程**：融合RMSNorm到权重，收集attention/FFN输入activation的Top-1 PCA基U1，对输入做U1旋转、排序分组和组Hadamard旋转H1；将逆变换融合回权重，KV cache也适配类似旋转。最后用GPTQ对权重做4-bit量化，activation采用per-group非对称量化（group size=128）。全程所有矩阵乘法保持均匀4-bit。

**关键实验结果**  
在Llama-3-8B/70B、Qwen2.5-7B等模型上，OffQ在W4A4KV4下WikiText PPL和0-shot精度均优于QuaRot、SpinQuant、KurTail、ResQ等。Llama-3-8B：PPL 6.98 vs. 16-bit 6.1，平均0-shot 65.49% vs. 67.09%；Qwen2.5-7B：PPL 7.66 vs. 16-bit 6.8，远胜其他方法。消融验证了top-1选择、排序分组和Hadamard结构的有效性。

**最值得记住的一句话**  
通过Top-1 PCA将离群值浓缩后，用Hadamard旋转将离群能量转化为组偏移并被零点吸收，OffQ以极简的变换实现了高精度均匀W4A4KV4量化，为低bit推理提供了实用基线。
