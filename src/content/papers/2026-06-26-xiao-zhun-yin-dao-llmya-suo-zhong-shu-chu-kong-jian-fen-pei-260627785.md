---
title: 'Output-Space Allocation Costs for Calibration-Guided LLM Compression: An Empirical
  Study'
title_zh: 校准引导LLM压缩中输出空间分配成本实证研究
authors:
- Qiong Tang
- Xiangkun Hu
- Xiangyang Liu
- Yiran Chen
- Yunfan Shao
affiliations:
- Analemma
arxiv_id: '2606.27785'
url: https://arxiv.org/abs/2606.27785
pdf_url: https://arxiv.org/pdf/2606.27785
published: '2026-06-26'
collected: '2026-06-29'
category: LLM
direction: LLM压缩 · 分配成本优化
tags:
- LLM compression
- calibration
- output-space allocation
- ROCKET
- perplexity-accuracy tradeoff
one_liner: 将压缩分配成本对齐到输出空间可小幅提升零样本准确率，但会损害语言建模困惑度，且效果受压缩比影响。
practical_value: '- 电商推荐中若需压缩LLM，低压缩比（<20%）时分配成本函数影响极小，可直接使用简单的权重空间误差，节省工程开销。

  - 高压缩比下，若核心业务指标是下游任务准确率（如推荐解释生成），可将校准分配成本对齐至输出空间（如激活重建误差），但需警惕语言模型困惑度上升可能影响其他文本质量。

  - 不同分配目标会导致准确度与困惑度权衡，建议根据线上 A/B 指标选择最优成本函数，避免只依赖单一代理指标。

  - ROCKET-ActCost 的修改成本低，可直接在现有稀疏分解压缩框架中替换成本计算，对齐方式可迁移到其他校准引导压缩方法。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：主流 LLM 压缩方法（如 ROCKET）使用校准数据指导压缩，但层间分配成本基于权重空间 Frobenius 误差，与最终输出重建目标不一致。该工作探究将分配成本对齐至输出空间能否提升压缩保真度。

**方法**：提出 ROCKET-ActCost，在 MCKP 分配阶段用输出空间误差（激活值重建误差）替代权重空间误差作为成本函数，其余流程不变。在 Qwen3-8B 和 Llama-3.2-1B 上进行 20% 和 50% 压缩比实验，评估零样本准确率与 WikiText 困惑度。

**关键结果**：50% 压缩下，ROCKET-ActCost 在 8 个零样本基准上平均准确率提升 0.8 个百分点（53.1% vs 52.3%），但困惑度恶化 16%（61.46 vs 52.98），揭示分配目标影响下游指标权衡。权重与输出空间误差高度相关（>0.99），限制了分配差异，因此效果温和。20% 压缩下，两种方法性能几乎相同（53.3% vs 53.5% 准确率，14.45 vs 14.66 PPL），表明成本函数影响在低压缩比时微乎其微。
