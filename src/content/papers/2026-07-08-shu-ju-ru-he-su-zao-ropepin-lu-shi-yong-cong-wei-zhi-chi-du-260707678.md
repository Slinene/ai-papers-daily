---
title: 'How Data Shapes RoPE Frequency Usage: From Positional Scale Matching to Length
  Generalization'
title_zh: 数据如何塑造RoPE频率使用：从位置尺度匹配到长度泛化
authors:
- Xinyi Wu
- Siyuan Liu
- Ali Jadbabaie
affiliations:
- MIT IDSS
- IIIS, Tsinghua University
arxiv_id: '2607.07678'
url: https://arxiv.org/abs/2607.07678
pdf_url: https://arxiv.org/pdf/2607.07678
published: '2026-07-08'
collected: '2026-07-09'
category: LLM
direction: 位置编码的频率选择与数据分布匹配
tags:
- RoPE
- Frequency Usage
- Length Generalization
- Positional Encoding
- Data-Driven
one_liner: 揭示学习到的RoPE频率与训练数据依赖宽度匹配的机制，并基于此解释长度外推的条件
practical_value: '- 在用户行为序列建模中使用 RoPE 时，训练数据中的典型依赖长度（如会话内行为链长度）决定了模型习得的频率分布；若需外推到更长的用户历史，可通过降低所有频率（如
  factor < 1 的缩放）来扩大有效视野，前提是长序列上的依赖模式与训练时近似自相似。

  - 为序列推荐设计位置编码时，可先估计数据中依赖关系的有效宽度（如行为衰减的半衰期），据此初始化 RoPE 基频或频率范围，使模型容量更匹配数据结构，避免频率浪费。

  - 频率缩放方法可类比于对用户行为序列进行多尺度时间聚合：不同频率对应不同分辨率的时间窗口，当需要处理跨场景的长短周期依赖时，可动态调整频率以平衡视野与分辨率。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：RoPE 为 Transformer 提供固定频率网格，但训练后的模型对频率的使用高度不均匀，其原因不明。本文从数据角度解释这一现象，并连接至长度泛化。

**方法关键点**：
- 将每个频率视为一个“位置透镜”，其有效视野与分辨率存在权衡；推导出最优频率与数据中依赖结构宽度 \(W\) 成反比（\(\propto 1/W\)）。
- 通过合成数据和文本数据的控制实验验证频率匹配原则：改变训练数据的依赖宽度，观察到模型学到的 RoPE 频率发生相应偏移。
- 将该原则推广至长度泛化：测试时对频率进行缩放（如线性插值）相当于扩张有效视野但降低分辨率；当长程依赖是训练依赖的近似膨胀时有效，反之则可能失败。

**关键结果**：
- 自然语言具有跨位置尺度的近似自相似性，这解释了为何简单的频率缩放（如 NTK-aware scaling）能支持长上下文泛化。
- 长度泛化成功取决于两重尺度匹配：训练时习得的频率与训练数据依赖宽度匹配，以及频率缩放倍率与依赖结构向更长上下文延伸的方式匹配。
