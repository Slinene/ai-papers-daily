---
title: 'Stage-Replay Divergence Follows the KV Cache: Fixed-Prefix Precision Controls
  and Bidirectional Cache Transplantation'
title_zh: 阶段回放分歧跟随KV缓存：固定前缀精度控制与双向缓存移植
authors:
- Alexander Boesgaard Lorup
affiliations:
- Openhagen
arxiv_id: '2607.28495'
url: https://arxiv.org/abs/2607.28495
pdf_url: https://arxiv.org/pdf/2607.28495
published: '2026-07-30'
collected: '2026-08-02'
category: LLM
direction: LLM推理诊断·KV缓存与数值精度
tags:
- KV Cache
- Numerical Precision
- Stage Replay
- Causality
- Divergence
one_liner: 发现推理阶段回放的分歧由KV缓存状态决定，FP32可消除BF16下的解码分歧，双向缓存移植证实因果性
practical_value: '- 在需要严格复现生成结果的场景（如Agent多步推理、离线评估、A/B测试）中，必须保持KV缓存位的精确一致，仅依赖相同token
  ID和贪婪解码还不够；若使用BF16混合精度，意外分歧可能被误判为模型行为变化。

  - 推荐使用FP32进行关键路径的推理或缓存存储，以避免因精度导致的隐性分歧；若必须使用BF16，需通过逐令牌桥接验证缓存等价性。

  - 双向缓存移植技术可用于诊断生产环境中不可复现的生成轨迹，能快速定位分歧源头是模型权重还是缓存状态。

  - 在构建基于LLM的推荐Agent时，若采用中间状态暂停-继续的策略，应固定前缀缓存并控制精度，避免因缓存重建引入不可控的推荐结果漂移。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：阶段回放诊断常用新鲜预填充的KV缓存来模拟原始解码器在中间点的延续，但假设未经严格验证。作者审计了这一假设，在Qwen2.5类系统中检查了推理阶段边界的缓存与新鲜预填充的等效性。

**方法关键点**：
1. 匹配200个样本，比较保留的实时缓存与相同token的一次性预填充，发现BF16下虽然token完全相同，但166个后缀和20个正确性标签出现分歧，准确率差异仅1点（95% CI [-3.5, +5.5]）。
2. 固定前缀2×2交叉实验，控制token状态不变，变换缓存构建方式（实时/新鲜）与数值精度（BF16/FP32）。BF16分歧复现，FP32则无解码分歧（95% Wilson上界1.88%）。
3. 逐令牌桥接技术使增量缓存与保留缓存在12/12行上达到位精确一致。
4. 双向KV缓存移植（所有48层K/V）：24/24和43/43的测试中，每个分歧的延续都跟随缓存供体，证明边界KV缓存是分歧轨迹的因果充分载体。

**关键结果**：FP32精度可消除阶段回放中的解码分歧；KV缓存状态是生成分歧的主要因果因素，而非token序列本身；通过缓存移植可实现精确复现。
