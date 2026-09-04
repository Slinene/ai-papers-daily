---
title: 'Why Gated DeltaNet Survives 4-Bit Quantization: NVFP4 W4A4 for the Recurrent
  Half of a Hybrid 27B LLM'
title_zh: Gated DeltaNet 为何能承受 4-bit 量化：混合 27B LLM 循环部分的 NVFP4 W4A4
authors:
- Sergii Kozyrev
- Davyd Maiboroda
affiliations:
- Minima AI
arxiv_id: '2609.04098'
url: https://arxiv.org/abs/2609.04098
pdf_url: https://arxiv.org/pdf/2609.04098
published: '2026-09-02'
collected: '2026-09-04'
category: LLM
direction: 混合 LLM 循环层 4-bit 量化推理优化
tags:
- Quantization
- NVFP4
- Gated DeltaNet
- Hybrid LLM
- W4A4
- KV cache
one_liner: 对 Qwen3.8-27B 全部 496 个线性层（含 GDN）做 NVFP4 W4A4，精度持平 BF16 且更小更快
practical_value: '- 混合架构中 linear-attention/循环层（Gated DeltaNet）可以激进 W4A4，不必保留 8/16-bit；尤其对
  decay/write-strength 门控投影，softplus/exponential 和 sigmoid 会压缩 GEMM 误差，量化敏感度低。

  - 部署 NVFP4 时若按模块逐层校准，需注意 kernel fusion 后的 global scale 不匹配问题：应统一重算或修正 fused GEMM
  的 scale，否则精度会显著下降。

  - 长上下文场景可以把 KV cache 用 FP8 存并校准 scale，几乎无性能损失，能恢复约 83% 的长上下文 KV 惩罚；这是低成本优化长文本推理的有效手段。

  - 16-element block scaling 能有效控制残差流中的极端 outlier，对电商/Agent 场景下需要低比特推理的混合 LLM 是一条可复用的工程路径。'
score: 7
source: huggingface-daily
depth: abstract
---

## 动机
混合 LLM 将 softmax attention 与 Gated DeltaNet（GDN）等线性注意力层结合，GDN 用固定大小的循环状态总结全上下文。社区担心循环误差会沿序列累积，早期 Qwen3.8-27B 的 4-bit 量化通常保留 GDN 块为 8/16-bit，尤其是 decay 和 write-strength 门控投影。

## 方法与关键结果
构建 Minima：对全部 496 个线性层（包括 GDN）做 NVFP4 W4A4 量化。在 4K/32K perplexity、MMLU-Pro、GSM8K、AIME’25、GPQA-Diamond、LiveCodeBench、RULER 64K 检索上，Minima 与 BF16 差距在种子噪声内（5-task 平均 -0.52），同时体积最小（17.5 GiB）、prefill 速度最快（+14-19%）；其 32K perplexity 差距随上下文位置增大而缩小。

## 机制解释
四部分机制实验说明原因：(i) NVFP4 的 16 元素块缩放能局部化残差流中的极端 outlier，平衡不同层角色的激活误差；(ii) 门控投影最不敏感，softplus/exponential 与 sigmoid 参数化将约 11% 的 GEMM 误差压缩到约 2% 的输出误差；(iii) delta-rule 循环将注入噪声限制在 32K token 的平坦平台，状态脉冲数百步内被遗忘，因为每次写入会沿当前 key 方向覆盖状态；(iv) 单 token 量化成本随上下文长度摊薄而非复利累积。

## 工程修复
还修复了按模块校准的 NVFP4 checkpoint 被融合 kernel 服务时出现的 global-scale 不匹配，并表明校准后的 FP8 KV-cache scale 无损恢复大部分长上下文性能。最终给出实用 recipe：quantize everything, ship KV scales。
