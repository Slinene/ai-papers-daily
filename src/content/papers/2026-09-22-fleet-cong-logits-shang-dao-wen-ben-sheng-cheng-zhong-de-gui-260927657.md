---
title: 'FLEET: From Logits Entropy to Enhanced Trajectories in Text Generation'
title_zh: FLEET：从 logits 熵到文本生成中的增强轨迹
authors:
- Oleksii Streltsov
- Oleksandra Vitko
affiliations:
- Kharkiv National University of Radio Electronics, Kharkiv, Ukraine
arxiv_id: '2609.27657'
url: https://arxiv.org/abs/2609.27657
pdf_url: https://arxiv.org/pdf/2609.27657
published: '2026-09-22'
collected: '2026-09-25'
category: LLM
direction: LLM 推理时采样优化
tags:
- LLM
- temperature sampling
- entropy
- decoding
- test-time scaling
- trajectory memory
one_liner: 通过记录高熵 token 轨迹并调整 logits，在相同预算下提升采样效率与复杂任务准确率
practical_value: '- **替代重复采样做集成**：在生成 query、文案、搜索结果标题等场景中，常用 temperature sampling
  生成多个候选再投票/打分。FLEET 的记忆机制可减少重复候选，提升预算利用率，相同精度下速度提升 3 倍。

  - **轻量级 logits 调整模块**：FLEET 只需根据 token 熵阈值记录轨迹并调整 logits，对现有 LLM pipeline 改动小，易于嵌到在线生成服务中，尤其适合需要控制延迟和成本的电商推荐系统。

  - **确定性贪心解码可选**：论文在贪心解码下实现确定性输出，适合对可复现性有要求的 A/B 测试或生产环境；用一次校准 pass 自动确定超参数，降低调参成本。

  - **面向 Agent 的复杂任务提升**：在 LiveCodeBench 等复杂编码任务上大幅提升 Pass@32，说明该方法对多步推理和 agentic
  任务有效，可用于电商导购 Agent 的多步规划与执行。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**
LLM 推理常用 temperature sampling 聚合多个样本提升准确率，但这一过程是无记忆的：后续采样 unaware of 之前生成及评估，导致重复答案比例随样本数增加，收益递减。

**方法关键点**
FLEET 在生成中引入记忆机制：将每次生成表示为稀疏轨迹，只记录熵超过预设阈值的 token 状态；利用这些轨迹推断 per-token utility scores，用于调整 logits，从而改变后续采样分布。该方法在贪心解码下是确定性的，且通过一次 calibration pass 推导主要超参数，对现有 pipeline 只需极小修改。

**关键结果**
在基准评测中，FLEET 达到与重复采样基线相同的准确率，同时速度提升 3 倍；在 LiveCodeBench 上 Pass@32 从 59.9% 提升至 66.2%，证明其在复杂任务上能更有效利用推理预算。
