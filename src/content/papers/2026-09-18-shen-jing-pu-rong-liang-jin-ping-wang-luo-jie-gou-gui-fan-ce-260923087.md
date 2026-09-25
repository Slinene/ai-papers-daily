---
title: 'Neural Spectral Capacity: Measuring and Designing Architectures from Network
  Specification Alone'
title_zh: 神经谱容量：仅凭网络结构规范测量与设计架构
authors:
- Chenyu Zhu
- Ruoyu Zhao
- Zhichao Lu
affiliations:
- Department of Computer Science, City University of Hong Kong
arxiv_id: '2609.23087'
url: https://arxiv.org/abs/2609.23087
pdf_url: https://arxiv.org/pdf/2609.23087
published: '2026-09-18'
collected: '2026-09-25'
category: Training
direction: 训练无关容量度量与架构设计剪枝
tags:
- Neural Architecture Search
- Training-free Proxy
- Transformer Compression
- Random Matrix Theory
- LLM Pruning
- Dynamic Programming
one_liner: 提出基于权重矩阵奇异值谱的闭式容量指标 NSC，无需实例化/数据/梯度即可评估架构，并给出全局最优 DP 求解器
practical_value: '- 在电商/广告/生成式推荐模型做结构选型时，可用 NSC 作为零成本过滤指标，在训练前快速比较同预算下不同 depth-width、FFN
  ratio、attention head、MoE expert 分配，替代小规模消融或昂贵搜索。

  - 对 LLM 类召回/排序/Agent 策略模型做结构化剪枝或部署压缩时，NSC-DP 可在 CPU 秒级返回给定参数/延迟预算下全局最优的层与组件保留方案，无需
  calibration data，比现有 training-free proxy 快约 5900 倍。

  - 利用 NSC 的 layer-wise additive 性质，可在多域/多任务推荐模型或异构 MoE 中按塔、按 expert 精细核算容量，指导预算在
  tower、shared bottom、task head 间分配。

  - 注意 NSC 依赖随机初始化下的 Marchenko-Pastur 假设，适合做候选架构过滤和初始化分配；最终上线前仍需在业务数据上微调验证，避免把排名绝对化。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：现代 Transformer 设计与压缩本质都是在固定参数/算力预算下分配容量，但常用的 #Params、#FLOPs 只反映规模和计算量，不反映 depth-width、head、FFN 等结构差异，导致同等预算下不同架构得分相同却表现不同。

方法关键点：提出 Neural Spectral Capacity (NSC)，一种基于各个权重矩阵奇异值谱的闭式标量。在标准随机初始化下，由 Marchenko-Pastur 律可直接从网络结构规范计算 NSC，无需实例化模型、数据或梯度。NSC 具有逐层可加性，因此提出 NSC-DP，一个精确动态规划求解器，能在资源约束下全局最大化 NSC，CPU 上秒级完成，弥补了黑盒搜索训练无关代理无法提供全局最优保证的缺陷。

关键结果：在 7 个 Transformer/CNN 家族上，NSC 排名优于 #Params、#FLOPs 及代表性 training-free proxies；FlexiBERT 上参数差 <10% 的配对中，NSC 的 Kendall τ=0.505，而 #Params 仅 0.082。NSC-DP 在 WikiText-103 上 2 秒内搜索到超越人工设计的 Transformer-XL 架构；对 LLaMA-7B 剪枝，无需任何 calibration 数据得到 5.7B 模型，在 8 个常识推理任务上最优，比最强 training-free proxy 快约 5900 倍。
