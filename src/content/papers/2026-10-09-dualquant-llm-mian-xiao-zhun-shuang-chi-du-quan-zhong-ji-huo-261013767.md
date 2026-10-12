---
title: 'DualQuant: Dual-scale Calibration-free Weight-and-Activation Quantization
  for LLMs'
title_zh: DualQuant：LLM 免校准双尺度权重激活量化
authors:
- Mahsa Salmani
- Sayeh Sharify
- Hesham Mostafa
affiliations:
- d-Matrix
arxiv_id: '2610.13767'
url: https://arxiv.org/abs/2610.13767
pdf_url: https://arxiv.org/pdf/2610.13767
published: '2026-10-09'
collected: '2026-10-12'
category: LLM
direction: LLM 量化 · 免校准 W4A4
tags:
- PTQ
- Quantization
- W4A4
- MX-NVFP4
- Calibration-free
- Dual-scale
one_liner: 用权重重构误差最小化导出的列尺度兼作激活重缩放，实现免校准 W4A4 量化，支持 INT4/MX/NVFP4
practical_value: '- 在电商客服机器人、端侧推荐模型等隐私敏感或无法稳定获取校准数据的场景，可直接用 DualQuant 替代 SmoothQuant，省去校准集采集和分布敏感问题；其纯权重驱动特性也适合模型频繁更新、快速验证低比特推理的迭代节奏。

  - 借鉴双尺度思路：对推荐模型中的 Embedding 或 MLP 层做量化时，引入列尺度抑制异常值，并让该列尺度同时作用于激活输入，可有效降低激活量化误差；工程上把列尺度融合进激活量化
  kernel，避免额外 kernel launch。

  - 格式感知投影是关键：如果硬件支持 MX 或 NVFP4（如 Blackwell），务必把尺度投影到格式允许的离散集合（E8M0/FP8 UE4M3），否则会出现
  SINQ+ 那种尺度越界导致的完全发散；投影可在每次闭式更新后做最近邻取值。

  - 离线量化成本极低：BCD 每次更新是闭式表达式，无需 Hessian 或反向传播，可以快速对新上线模型进行量化，适合电商/广告侧需要频繁部署新 LLM 或量化多版本模型的场景。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

## 动机
现代推理加速器提供原生 4-bit 矩阵乘，但完整吞吐量增益要求权重和激活都量化。激活量化比权重更难，通常依赖校准数据（如 SmoothQuant），存在数据敏感、隐私与访问开销；免校准旋转方法（QuaRot）不支持 MX/NV 格式。DualQuant 针对这一空白，用纯权重驱动的双尺度优化实现免校准联合 W+A 量化。

## 方法关键点
- 双尺度参数化：W ≈ Diag(α)^{-1} Q(Diag(α) W Diag(β)) Diag(β)^{-1}，行尺度 α 吸收行内动态范围，列尺度 β 捕获跨列结构。
- 非可微权重重构 MSE 目标通过变量分裂和块坐标下降（BCD）求解，每个子问题闭式更新；尺度投影到格式允许集合（INT4→BF16，MXINT4/MXFP4→E8M0，NVFP4→FP8 UE4M3）。
- 关键洞察：最小化权重重构误差得到的列尺度 β 自动衰减高幅值权重列，同时作为激活重缩放（eX = X Diag(β)^{-1}），起到类似 SmoothQuant 校准尺度的作用，但无需激活统计。
- 推理时行尺度 α 折叠到反量化尺度，列尺度 β 融入激活量化 kernel，无额外 kernel launch，量化开销仅占 GPU 时间 4.3-6.1%。

## 关键实验
- 模型：Llama-2-7B, Llama-3.1-8B, Llama-3.2-1B, Qwen2.5-7B, Qwen3-0.6B, Qwen3-14B；格式：INT4(G=64), MXINT4(G=32), MXFP4(G=32), NVFP4(G=16)。
- 基准：RTN, AWQ+, SmoothQuant, SINQ+, QuaRot；评估 WikiText-2/C4 PPL 和 MMLU/HellaSwag/PIQA/ARC-Easy/WinoGrande 零样本。
- 结果：在大多数模型和格式上，DualQuant 匹配或超过校准的 SmoothQuant，并显著优于免校准 baseline；NVFP4 上 DualQuant 全面领先，SINQ+ 和 QuaRot 发散。
- 真实 packed W4A4 部署：Llama-3.1-8B 在 RTX 4090 上，相对 BF16 内存减少 2.51-2.61×，吞吐提升 1.39-2.46×，WikiText-2 PPL 6.74 与 fake 量化 6.73 差 0.01。

## 最值得记住的一句话
权重重构 MSE 最小化导出的列尺度可以兼作激活重缩放，从而无需任何校准数据就能实现与 SmoothQuant 相当或更好的 W4A4 量化。
