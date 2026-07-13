---
title: 'KronQ: LLM Quantization via Kronecker-Factored Hessian'
title_zh: KronQ：基于Kronecker分解的LLM量化框架
authors:
- Donghyun Lee
- Yuhang Li
- Ruokai Yin
- Priyadarshini Panda
affiliations:
- University of Southern California
- Yale University
arxiv_id: '2607.07964'
url: https://arxiv.org/abs/2607.07964
pdf_url: https://arxiv.org/pdf/2607.07964
published: '2026-07-07'
collected: '2026-07-13'
category: LLM
direction: LLM 后训练量化 · Kronecker 分解
tags:
- PTQ
- Kronecker-Factored Hessian
- Bidirectional Incoherence
- Mixed-Precision
- 2-bit Quantization
one_liner: 引入梯度协方差实现双向非相干处理与混合精度分配，显著提升2-bit量化性能
practical_value: '- 量化推荐系统中的Transformer层时，额外引入梯度协方差HG可弥补仅使用激活协方差HX的不足，极大改善低比特（特别是2-bit）下模型崩溃问题。

  - 双向非相干预处理（对输入和输出维度都应用随机Hadamard旋转+对角缩放）能平滑权重幅度方差，可应用于广告/推荐模型的注意力层或MLP层，减少量化误差。

  - 基于tr(HG)·tr(HX)的混合精度分配方法能够区分共享输入的Q/K/V投影，为不同子层分配合适位宽，可直接用于推荐模型的多层精度调优。

  - 方法计算高效：HG仅需一次反向传播，且量化更新中HG代数抵消，不增加推理开销，适合低延迟在线服务。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：现有LLM后训练量化方法（如GPTQ）仅依赖输入激活协方差HX，忽略输出方向梯度统计量，在2-bit等极低比特时失效。Kronecker分解（K-FAC）下，权重量化误差由HX和梯度协方差HG共同决定，引入HG有望从根本上改善低比特量化。

**方法关键点**
- **Kronecker因子化量化目标**：将HG纳入逐层重建损失，并证明在列式OBS补偿更新中HG代数抵消，保持与GPTAQ相当的校准效率。
- **双向非相干处理（BiIP）**：对权重矩阵同时进行输入侧和输出侧的对角缩放（基于HX和HG），再施加随机Hadamard旋转，使两个维度方向的权重变异系数均降至0.34～0.36，有效抑制异常值。
- **联合Hessian迹的混合精度分配**：定义子层敏感性分数为tr(HG)·tr(HX)，打破Q/K/V投影共享HX的局限，实现更细粒度的位宽分配。

**关键结果**
- 在LLaMA-2/3 7B–70B的W2/W3/W4 weight-only量化中，KronQ几乎在所有配置下达到最优困惑度，尤其2-bit优势巨大：LLaMA-3-70B的GPTQ与GPTAQ均发散（PPL>2000），KronQ仅7.93。
- 分组量化（g=128）2-bit下，LLaMA-2-7B PPL从GPTQ的274降至7.61。
- 消融实验证实双向非相干与基量化器（GPTAQ）互补，单独使用HG侧旋转会导致严重退化。
- 混合精度仅将3个子层升至W3即可在LLaMA-2-7B上获得8.15→6.38 PPL，优于仅基于HX的分配策略。
- 在Gemma-3、DeepSeek-R1等新模型及GPQA、MMLU、LiveCodeBench等困难基准上保持领先。
