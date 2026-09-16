---
title: 'Where Post-Training Quantization Breaks Text Embedders: A Measured Map Across
  Four Embedder Families'
title_zh: 文本嵌入模型的后训练量化失效图谱：四个模型家族的实测研究
authors:
- Hyojung Han
affiliations:
- ThakiCloud
arxiv_id: '2609.16391'
url: https://arxiv.org/abs/2609.16391
pdf_url: https://arxiv.org/pdf/2609.16391
published: '2026-09-14'
collected: '2026-09-16'
category: Training
direction: 模型量化与检索嵌入压缩
tags:
- PTQ
- Quantization
- Text Embedding
- Retrieval
- Model Compression
one_liner: 在检索嵌入模型上系统验证量化启发式建议，发现嵌入表保护和模块敏感度排序均不可迁移，蒸馏学生模型在极端量化下更优
practical_value: '- 量化检索 embedding 模型时不要直接套用 LLM 量化经验：embedding table 并不总是需要最高优先保护，INT4/g16
  下各模块独立量化损失差异不足 1 个 NDCG 点，均匀量化即可，无需复杂的混合精度分配。

  - 在 INT3 及以下位宽，模块敏感度排序因模型家族而异（Qwen 中 FFN 最敏感，BGE-M3 和 E5 中 attention 最敏感），需要针对自有模型重新测量，不能依赖通用排序。

  - 重建误差代理可用于筛选全局位宽，但不可用于选择具体保护哪些 tensor，因为其跨位宽的强预测力是 range-extension 伪影；实际选型应在目标检索任务上做
  per-query bootstrap 检验。

  - 若需 INT3/INT2 极端压缩，可考虑训练一个更小的蒸馏学生模型并量化，可能比直接量化大模型更优（文中 109M 学生 INT3 在 68.4 MB 下
  NDCG@10 达 78.04，优于 0.6B 教师量化版本的 64.46 / 297.9 MB），但注意这种优势仅限蒸馏任务内。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：weight-only PTQ 是压缩检索 embedder 最廉价的手段，但常见建议（保护 embedding table、按模块敏感度分配 bits、偏好 ranking-aware objective）大多直接沿用自 LLM 量化，缺乏针对检索模型的有效性验证。

**方法**：对来自四个架构家族的五个 checkpoint 进行网格化量化（不同位宽与 group size），隔离 embedding、attention 和 FFN 模块，在三个检索语料上评估，并使用 per-query bootstrap 检验。其中一个 checkpoint 是 Qwen3-Embedding-0.6B 及其蒸馏微调版本，构成配对对照。

**关键结果**：所有启发式建议均无法直接迁移。embedding table 在任何家族中都不是孤立保护的最优先项；INT4/g16 时模块间损失差异极小（≤1.01 NDCG），混合精度无分配空间；INT3 时模块敏感度排序随家族变化且损伤非加性；INT2 时重建误差相近（0.315–0.337）但质量保留率从 1.3% 到 65.9% 差异巨大。重建误差代理对全局位宽筛选有用，但用于混合精度选择不可靠。蒸馏 109M 学生模型在 INT3 下达到 78.04 NDCG@10 / 68.4 MB，优于其 0.6B 教师的极端量化版本（64.46 / 297.9 MB），但仅限蒸馏任务内。大小均为实际文件字节数。
