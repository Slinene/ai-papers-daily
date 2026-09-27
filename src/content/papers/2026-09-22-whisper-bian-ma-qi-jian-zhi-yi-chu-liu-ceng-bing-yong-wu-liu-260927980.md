---
title: 'Six Layers Less: Encoder Pruning for Whisper with Label-Free Recovery'
title_zh: Whisper 编码器剪枝：移除六层并用无标签蒸馏恢复
authors:
- Rasmus Aagaard
- Nicki Skafte Detlefsen
affiliations:
- Technical University of Denmark
- Laerdal Medical
arxiv_id: '2609.27980'
url: https://arxiv.org/abs/2609.27980
pdf_url: https://arxiv.org/pdf/2609.27980
published: '2026-09-22'
collected: '2026-09-27'
category: Other
direction: 语音模型压缩 · Encoder 层剪枝
tags:
- model pruning
- knowledge distillation
- ASR
- Whisper
- label-free
- encoder-decoder
one_liner: 按留一层 WER 变化排序剪掉 Whisper 编码器 6 层，再用无标签语音蒸馏恢复精度，无需自定义推理
practical_value: '- 层重要性排序思路可直接迁移到 Transformer 编码器剪枝：在推荐/搜索模型中对 Encoder 层做 leave-one-out
  敏感性分析（如用 A/B 指标或 loss 变化），定位冗余层，避免盲剪。

  - 零样本剪枝 + 无标签蒸馏的组合适合业务场景缺乏标注数据时压缩模型：用大量无监督域内数据做蒸馏恢复精度，降低标注成本。

  - 压缩后保持原始架构（只是更浅的 Encoder）能避免自定义推理代码，可无缝复用现有推理优化和部署工具，这对线上快速迭代很重要。

  - 对语音搜索、客服语音识别等多模态入口模型，可借鉴该剪枝蒸馏 pipeline，在延迟敏感场景下用少量精度损失换取明显推理加速。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：Whisper 解码器剪枝（如 whisper-large-v3-turbo 从 32 层减到 4 层）已广泛采用，但编码器剪枝很少落地，原因之一是压缩后需要自定义推理实现才能获得加速。本文目标是剪掉编码器冗余层，同时不引入特殊推理代码。

**方法关键点**：对 whisper-large-v3-turbo 的编码器逐层做 leave-one-layer-out 实验，计算移除各层后 WER 的变化，按影响从小到大排序，移除影响最小的六层（占编码器 18.5%）。剪枝后的模型就是更浅的编码器，无需任何自定义推理实现。为弥补零样本剪枝带来的性能下降，进一步用无标注单语语音数据对该浅层模型做蒸馏，使用原始大模型作为教师，仅用语音信号（无转录标签）进行恢复训练。

**关键结果**：零样本剪枝后四语言平均 WER 从基线 18.2% 升至 21.9%，经过无标签蒸馏后恢复到 20.1%。该方法证明了编码器层剪枝 + 无标签蒸馏可以在保持标准推理路径的前提下，用少量精度损失换取明显计算节省。
