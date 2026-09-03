---
title: UE5M3 FP4 Block Scaling for Stable Language Model Pretraining
title_zh: UE5M3 FP4 块缩放实现稳定语言模型预训练
authors:
- Robert Hu
- Carlo Luschi
- Paul Balanca
affiliations:
- Graphcore Research
arxiv_id: '2609.02846'
url: https://arxiv.org/abs/2609.02846
pdf_url: https://arxiv.org/pdf/2609.02846
published: '2026-09-02'
collected: '2026-09-03'
category: Training
direction: FP4 低精度预训练 · E5M3 block scaling
tags:
- FP4
- quantization
- pretraining
- E5M3 block scale
- LLM
- efficiency
one_liner: 用 E5M3 块缩放替代 RHT 与 BF16 末层豁免，更简单的 FP4 预训练配方，8B 模型 190B tokens 表现优于 NVFP4
practical_value: '- 若团队有自研 LLM 或大规模召回/广告模型持续预训练，可尝试 UE5M3 block scale 代替 RHT：用更宽标度范围减少额外矩阵变换，简化
  FP4 训练管线。

  - 选择性 stochastic rounding 只作用于 backward gradients，可作为低比特训练/微调 trick 保留优化信号，适合资源受限的广告/内容模型训练。

  - 移除 BF16 末层豁免，所有 eligible internal linears 用 FP4，实测吞吐 +21.2%；在做 FP4/NVFP4 推理或训练部署时可以直接复现这个算子策略。

  - 若在实时推荐/Agent 中需要 FP4 量化 LLM serving，考虑软件模拟 UE5M3 块缩放，可能降低 pre-processing 延迟并提升
  quantized-inference 精度。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

动机：FP4 的 E2M1 有效数字范围窄，难以稳定预训练；NVIDIA Transformer Engine NVFP4 需 current-tensor scaling、随机 Hadamard 变换（RHT）和 BF16 末层，额外开销大。

方法：改用 unsigned E5M3（UE5M3）block scale 配 E2M1 payload，用更宽标度范围做周期性 tensor scaling；省略 RHT；只对 backward gradients 做 selective stochastic rounding；所有 eligible internal linears 均使用 FP4；基于 Nemotron-H 8B 预训练近 190B tokens。

结果：与 NVFP4 相比，block-16 配方 final-window training loss 更低；在各自量化推理策略下验证集 NLL 更低；量化推理 downstream 三个聚合指标更高；消融中同时移除 RHT 与 BF16 final-block 豁免，模型主体 token 吞吐提升 21.2%。
