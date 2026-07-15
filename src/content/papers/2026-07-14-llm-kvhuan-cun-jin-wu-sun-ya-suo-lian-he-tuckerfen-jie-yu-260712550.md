---
title: 'A JoLT for the KV Cache: Near-Lossless KV Cache Compression via Joint Tucker
  and JL-Residual Allocation for LLMs'
title_zh: LLM KV缓存近无损压缩：联合Tucker分解与JL残差分配
authors:
- Rahul Krishnan
- Volker Schulz
arxiv_id: '2607.12550'
url: https://arxiv.org/abs/2607.12550
pdf_url: https://arxiv.org/pdf/2607.12550
published: '2026-07-14'
collected: '2026-07-15'
category: LLM
direction: LLM推理 · KV缓存压缩
tags:
- KV cache
- Tucker decomposition
- Johnson-Lindenstrauss
- compression
- low-rank
- quantization
one_liner: 将KV缓存视为三阶张量，用部分Tucker分解+JL旋转低比特残差联合优化，实现近无损2-3倍压缩
practical_value: '- 对于部署LLM做推荐解释、对话Agent的场景，可直接应用JoLT将KV缓存压缩2-3倍，节省显存、提升批处理大小与吞吐，且保持输出质量几乎不变。

  - Tucker分解+JL残差的联合优化思路（拉格朗日对偶分配秩与比特预算）可迁移到电商搜索推荐中其它高维张量压缩任务，如用户-商品-时间嵌入压缩。

  - FlashJoLT的随机SVD加速策略可作为在线压缩的工程参考，适用于需要动态调整压缩率的推荐模型部署。

  - 该方法在分组查询注意力和多头注意力结构上均有效，证明其对主流LLM架构通用，建议在实际Agent/生成式推荐系统中优先尝试。'
score: 8
source: arxiv-cs.CL
depth: abstract
---

**动机**：长上下文LLM推理中KV缓存成为显存瓶颈，现有低秩或量化方法未充分利用缓存的三阶张量结构（头×token×特征）中不同轴的冗余差异。

**方法**：JoLT直接对每层KV缓存张量采用部分Tucker分解——只在token和特征轴压缩，保持头和层轴不变，避免跨层耦合开销。然后用Johnson-Lindenstrauss（JL）随机旋转将截断残差投影并量化到低比特（如2-4 bit）以恢复能量。通过拉格朗日对偶一次性分配各层组与K/V的Tucker秩和残差比特数，满足总字节预算，实现全局最优。

**结果**：在Mistral-7B-v0.3（GQA）和LLaMA-2-13B（MHA）上，2-3倍压缩下困惑度、GSM8K准确率、RULER长上下文检索性能均与未压缩基线无显著差异（统计噪声内）；正交重建误差仅0.009（K）和0.006（V），比跨层SVD和4-bit量化低约一个数量级。FlashJoLT变体实现5-13倍压缩速度提升而保持质量。
