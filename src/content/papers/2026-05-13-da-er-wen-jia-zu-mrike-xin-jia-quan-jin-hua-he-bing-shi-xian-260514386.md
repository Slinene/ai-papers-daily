---
title: 'Darwin Family: MRI-Trust-Weighted Evolutionary Merging for Training-Free Scaling
  of Language-Model Reasoning'
title_zh: 达尔文家族：MRI可信加权进化合并实现语言模型推理的无训练扩展
authors:
- Taebong Kim
- Youngsik Hong
- Minsik Kim
- Sunyoung Choi
- Jaewon Jang
- Junghoon Shin
- Minseo Kim
arxiv_id: '2605.14386'
url: https://arxiv.org/abs/2605.14386
pdf_url: https://arxiv.org/pdf/2605.14386
published: '2026-05-13'
collected: '2026-05-15'
category: LLM
tags:
- Evolutionary Merging
- Model Merging
- Reasoning
- Training-Free
- LLM
one_liner: 通过梯度自由的权重空间进化合并，无需训练即可重组已有检查点的潜在能力以提升推理性能
score: 8
source: huggingface-daily
depth: abstract
---

**动机**：能否在不增加额外训练的情况下，通过重组现有模型检查点中已编码的潜在能力来提升前沿推理性能？

**方法关键点**：
- **14维自适应合并基因组**：实现细粒度的组件级和块级权重重组，精确控制合并过程。
- **MRI-Trust Fusion**：引入可学习的信任参数，自适应平衡诊断层重要性信号与进化搜索，确保合并的可靠性。
- **架构映射器**：支持异构模型家族（如Transformer和Mamba）之间的跨架构繁殖，扩大搜索空间。

**关键结果**：
- Darwin-27B-Opus在GPQA Diamond上取得86.9%的准确率，在1252个评估模型中排名第6，超越其完全训练的基础模型，且未使用任何梯度训练。
- 在4B到35B参数尺度范围内，达尔文模型始终优于父模型，并支持递归多代进化，持续提升性能。
- 成功实现Transformer和Mamba组件的训练自由进化合并，验证框架的通用性。
