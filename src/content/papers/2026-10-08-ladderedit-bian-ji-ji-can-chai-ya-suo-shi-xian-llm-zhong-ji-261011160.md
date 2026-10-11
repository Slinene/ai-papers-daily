---
title: 'LadderEdit: Edit-Level Residual Compression for Memory-Efficient Lifelong
  Editing of LLMs'
title_zh: LadderEdit：编辑级残差压缩实现 LLM 终身编辑内存高效
authors:
- Xiaobing Yu
- Peijie Qiu
- Jin Yang
- Xuanzhao Dong
- Weiwei Ma
- Zhaoqi An
- Xiaoqi Zhao
- Xiaofeng Liu
affiliations:
- Yale University
- Washington University in St. Louis
- Icahn School of Medicine at Mount Sinai
- Arizona State University
arxiv_id: '2610.11160'
url: https://arxiv.org/abs/2610.11160
pdf_url: https://arxiv.org/pdf/2610.11160
published: '2026-10-08'
collected: '2026-10-11'
category: Training
direction: 终身模型编辑 · 参数高效存储
tags:
- lifelong editing
- LoRA
- rank adaptation
- memory efficient
- LLM
one_liner: 按编辑难度动态分配 LoRA 秩的压缩方法，内存减少 5.2 倍仍追踪精确 LoRA 性能
practical_value: '- 对大规模个性化 LoRA 适配器（如每用户/每商品/每场景）可直接套用：先以极低秩存储，用少量验证 prompt 检查效果，不达标再提升秩，显著降低存储与显存。

  - 持续更新推荐/广告模型时，可借鉴“编辑合约”：为每次更新设定改写/泛化/局部性指标，仅在满足时接受，避免灾难性遗忘。

  - 工程实现上，维护多级秩 ladder，编辑先以低秩 sketch 存储，失败才逐步提升，可以节省推理时的内存带宽，适合在线部署。

  - 注意：论文侧重事实编辑，与电商场景的偏好/行为数据分布差异较大，需重新设计验证合约才能复用到推荐系统。'
score: 6
source: arxiv-cs.MM
depth: abstract
---

**动机**：终身编辑 LLM 需要存储大量编辑后参数，基于每编辑一个 LoRA 适配器的方法保持行为但存储线性增长，无法扩展到数千次更新。

**方法关键点**：LadderEdit 将每个 LoRA 适配器压缩成低秩残差表示。每个编辑先存储为低秩 sketch，然后在一组 probe prompts 上检查是否满足改写（rewrite）、泛化（generalization）和局部性（locality）合约。通过的编辑保留低秩 sketch；未通过的沿秩梯度逐步提升直到合约满足。这样简单编辑消耗极少秩，困难编辑消耗更多秩，整体存储按编辑难度自适应分配。

**关键结果**：在 LLaMA-3-8B、Mistral-7B、Qwen2.5-7B 上，ZsRE、CounterFact、WikiBigEdit 基准测试显示，LadderEdit 在内存减少 5.2 倍的情况下仍能追踪精确 LoRA 存储的性能，并且在 50,000 次连续编辑后仍有效。
