---
title: Structured Transforms for Low-Overhead Quantization of Language Models
title_zh: 用于低开销语言模型量化的结构化变换
authors:
- Daria Cherniuk
- Alexander Rudikov
- Boris Kashin
- Ivan Oseledets
affiliations:
- Institute of Numerical Mathematics
- Steklov Mathematical Institute
arxiv_id: '2609.11687'
url: https://arxiv.org/abs/2609.11687
pdf_url: https://arxiv.org/pdf/2609.11687
published: '2026-09-10'
collected: '2026-09-11'
category: LLM
direction: LLM 权重后训练量化 · Kashin 分解
tags:
- post-training quantization
- Kashin decomposition
- DCT
- low-bit inference
- LLM compression
one_liner: 用符号随机 DCT 替代 Kashin 量化中的稠密正交矩阵，O(N log N) 实现稳定 4-bit LLM 压缩
practical_value: '- 部署 LLM Agent / 生成式推荐时，可尝试用 Kashin-DCT 4-bit PTQ 替代或补充 GPTQ/AWQ；在长尾或压力输入下
  QuIP 类可能发散到高 PPL 或 NaN，该方法数值稳定，适合对稳定性要求高的线上 serving。

  - 若推理硬件支持原生 2-bit，该分解将每个权重存为两个 2-bit factor code，避免 3/4-bit 非原生格式的额外开销，降低内存带宽占用；可评估在广告/电商
  LLM 服务中的收益。

  - 将稠密随机正交变换换成 sign-randomized DCT，复杂度从 O(N^2) 降到 O(N log N)，且 2-bit 聚类中心采用闭式初始化，省去
  multi-restart k-means；这种结构化变换 + 确定性初始化的思路可迁移到其他 VQ/低秩压缩流程。

  - 该方法与 OPTQ 顺序误差补偿、QuIP 非相干预处理组合有效，说明可以作为插件接入现有 GPTQ/QuIP 量化管线，不必重做端到端 pipeline。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

动机：LLM 推理的权重张量主导内存带宽和占用，后训练量化可在不重训情况下压缩权重；但已有 Kashin 分解量化存在稠密随机正交矩阵的 O(N^2) 迭代开销、多次重启 k-means 聚类成本，以及 QuIP 变体在部分模型上的数值不稳定问题。

方法关键：保留 Kashin 分解，将权重分解为两个 ℓ∞ 有界分量；用 sign-randomized DCT 替换稠密随机正交矩阵，单次迭代从 O(N^2) 降至 O(N log N)。提出带交替更新的贪心算法，保证每个因子稳定 2-bit 聚类所需的四峰分布，并给出聚类中心的闭式初始化，移除 multi-restart k-means 瓶颈。整体管线结合 OPTQ 顺序误差补偿与 QuIP 非相干预处理，用 JAX 实现。

关键结果：在 OPT、Llama-2 和 Pythia 上，4-bit per channel 精度与 OPTQ、QuIP、QuIP-RG 及无微调、无 VQ 的 QuIP# 变体竞争，且墙钟扩展更好。压力配置下，QuIP 变体在 Pythia-6.9B 上出现四位数量级 PPL，在 Mistral-7B 上 LDL 回代出现 NaN；Kashin-DCT 保持数值稳定并接近 FP16 baseline。推理时每个权重分解为每通道两个 2-bit factor code，结构上适合原生 2-bit 硬件。
