---
title: 'Towards Privacy-Preserving Federated Prompt Tuning under Data Heterogeneity:
  A Subspace-Decomposed Expert Approach'
title_zh: 面向数据异质的隐私保护联邦提示微调：子空间分解专家方法
authors:
- Yuhua Wang
- Xiaodong Li
- Yihao Guo
- Yuxiang Jia
- Qinnan Zhang
- Yifan Sun
- Hainan Zhang
- Yongxin Tong
- Zhiming Zheng
affiliations:
- Beihang University
- Renmin University of China
- Beijing Jiaotong University
arxiv_id: '2607.21417'
url: https://arxiv.org/abs/2607.21417
pdf_url: https://arxiv.org/pdf/2607.21417
published: '2026-07-23'
collected: '2026-07-25'
category: Training
direction: 联邦学习 · 子空间分解 · 多专家提示
tags:
- federated learning
- prompt tuning
- differential privacy
- data heterogeneity
- low-rank decomposition
- mixture of experts
one_liner: 用子空间分解建模多专家提示，以低秩因子通信替代全量专家，在差分隐私下平衡个性化与泛化
practical_value: '- **联邦多场景推荐中的参数低秩解耦**：可将全局共享基础表示与私有残差分离，通信仅传递低秩因子，减少隐私噪声，适合跨商家数据协同训练，例如用户偏好共享底座+店铺私有调整。

  - **动态专家路由用于多域推荐融合**：Instance-aware Expert Fusion 的思路可应用于多场景推荐系统，在服务端缓存各领域 logits，客户端轻量路由实时融合，降低推理延迟。

  - **隐私约束下的多任务 LoRA 合并**：将多个 LoRA 专家表示为共享低秩空间+私有残差，可在不暴露原始参数下进行安全聚合，适合联邦 fine-tuning
  场景。

  - **通信效率与效用平衡的工程灵感**：通过固定公共基底避免每轮传输全量专家，对带宽敏感的边缘推荐模型部署有直接参考价值。'
score: 6
source: arxiv-cs.CV
depth: abstract
---

**动机**：联邦提示微调中，数据异质导致单一共享提示过度平滑，而多专家提示虽能捕获多样性，但全量传输会放大差分隐私噪声和通信开销，且服务器端难以聚合。

**方法**：提出 FedSEPT，核心包含两部分：
1. **子空间分解专家建模 (SEM)**：将多个提示专家参数化为共享低秩因子、固定公共基底和私有残差。通信和 DP 扰动仅作用于低秩因子空间，服务器可在统一坐标系下直接聚合因子，避免传输完整专家参数。
2. **实例感知专家融合 (IEF)**：客户端通过轻量路由网络为每个样本动态选择专家，并在 logit 层面融合预缓存的专家文本特征，无需重复前向计算。

**结果**：在 11 个异构 VL 任务基准上，相同隐私预算 ε 下，FedSEPT 相比 FedPGP、FedOTP 等强基线，局部适应性与全局泛化性的帕累托前沿更优，且通信量减少 30% 以上。
