---
title: 'REAL Loss: Optimizing Real Expected Acceptance Length for Speculative Decoding'
title_zh: REAL Loss：优化推测解码的真实期望接受长度
authors:
- Yu Tian
affiliations:
- The University of Hong Kong
arxiv_id: '2611.14399'
url: https://arxiv.org/abs/2611.14399
pdf_url: https://arxiv.org/pdf/2611.14399
published: '2026-11-10'
collected: '2026-11-12'
category: Training
direction: Speculative Decoding 训练损失优化
tags:
- Speculative Decoding
- Expected Acceptance Length
- Training Loss
- Rao-Blackwellization
- LLM Inference
one_liner: 提出 REAL 损失，通过路径权重与 Rao-Blackwellization 直接无偏优化推测解码的期望接受长度
practical_value: '- 在部署 LLM 在线推理（如电商搜索、广告文案生成、Agent 决策）时，可直接用 REAL 损失训练轻量 draft 模型，提高推测解码的接受长度，在不改动推理架构的情况下降低延迟。

  - 损失函数中的路径权重和 Rao-Blackwellization 技巧可迁移到其他序列决策场景：当优化指标与常用代理损失存在协方差偏差时，应基于真实决策路径构造无偏估计。

  - 注意代理损失与真实目标的差距可能导致梯度方向反转，尤其在草稿模型训练中不要只依赖分布匹配指标，最好直接优化业务相关的吞吐或接受长度。

  - 该方法只需修改训练损失，工程实现成本低，适合在现有推理加速框架上快速验证收益。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

## 动机
推测解码通过 draft 模型提出多个 token 由 target 模型一次验证来加速 LLM 推理，其加速效果由期望接受长度（EAL）决定。但主流训练目标如 cross-entropy、KL 散度、total variation 只关注分布匹配或单步 overlap，与 EAL 存在 gap。近期 block-level 训练目标试图直接优化 EAL，但仍为代理：它们在 target 分布的 continuation 上平均后续接受，而不是在已接受 token 选择的验证分支上平均，引入协方差 gap，甚至可能反转梯度方向。

## 方法关键点
分析该协方差 gap 后，提出 REAL 损失，精确优化真实 EAL。核心技巧：
- 使用路径权重（path weights）对真实验证分支进行无偏估计；
- 采用 Rao-Blackwellization 降低梯度方差；
- 不改变 drafter 架构或 inference 流程，仅替换训练损失。

## 关键结果
在控制损失对比实验中，target 模型为 Qwen3.6-35B-A3B，drafter 为 Domino。REAL 在 9 个任务子集和 5 个评估种子上，概率服务接受长度均优于 WTV、VSD、DBLast 和静态 LK baseline。增益仅来自训练损失改进，证明真实 EAL 训练的实用性。参考实现已开源。
