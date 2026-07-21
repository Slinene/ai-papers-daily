---
title: Can We Break LLMs Out of Self-Loops? Fine-Grained Reasoning Control with Activation
  Steering
title_zh: 打破推理自循环：用激活引导实现细粒度推理控制
authors:
- Sheldon Yu
- Tong Yu
- Xunyi Jiang
- Rohan Surana
- Gagan Mundada
- Sungchul Kim
- Lina Yao
- Julian McAuley
- Junda Wu
affiliations:
- UC San Diego
- Adobe Research
- University of New South Wales
arxiv_id: '2607.18100'
url: https://arxiv.org/abs/2607.18100
pdf_url: https://arxiv.org/pdf/2607.18100
published: '2026-07-20'
collected: '2026-07-21'
category: Reasoning
direction: 激活引导的推理状态控制
tags:
- activation steering
- reasoning control
- self-looping
- inference-time intervention
- latent state transition
- large reasoning models
one_liner: 通过分析推理轨迹的潜在状态转移并注入状态特定的残差流方向，无训练地打破LRM的自循环失败模式
practical_value: '- **推理Agent的在线干预**：在对话式推荐或搜索Agent中，可利用类似方法实时检测LLM是否陷入重复验证、重申已知信息的循环，并通过注入已准备好的状态转移向量强制推进流程，避免token预算浪费。

  - **状态特定的控制向量库**：不同于全局统一的greedy或惩罚策略，按当前推理状态（如“问题分解”、“中间计算”、“反复检查”）建立针对性的残差流调整方向，细粒度控制更精准，可移植到多步推荐解释生成场景。

  - **无需微调的推理加速**：方法完全基于缓存的一次性前向激活，不修改模型权重，适合快速部署到已上线的LLM推理服务中，在电商领域如商品对比、多步决策支持时减少无用思考。

  - **状态转移分析用于失败模式定位**：通过聚类推理步骤的隐藏状态并可视化转移矩阵，可以发现模型在哪些状态容易卡住，从而优先优化对应的引导向量，对构建可控的推荐对话系统很有工程参考价值。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
大型推理模型（LRM）在复杂推理任务中表现出色，但常常产生大量冗余的验证和重复内容，陷入“自循环”（self-loop）——模型反复停留在同一推理状态，消耗大量token却无进展。现有控制方法要么需要昂贵训练（如RL），要么只能在表面token层面干预，缺乏对推理过程本身的细粒度控制。本文将推理轨迹视为潜在状态的序列，通过分析状态转移规律，发现自循环是主要失败模式，并提出一种无训练的推理时干预方法。

### 方法关键点
- **状态提取**：使用基础嵌入模型（Qwen3-4B-Base）对推理步骤进行隐状态均值池化，然后对每数据集独立进行K-Means聚类（K=5），得到离散的潜在推理状态。
- **转移向量构建**：对于每个状态c，收集所有“跨出”（crosser）和“停留”（stayer）样本的残差流激活，计算两者之差作为状态特定的引导方向。该方向近似最大化Fisher线性判别，能够提升状态退出的概率。
- **在线控制器**：推理时实时分类当前步骤所属状态，检测连续两步是否在同一状态（自循环），若触发则按v_c方向对目标模型（如Qwen3-4B-Thinking）的残差流进行正干扰，强度由支持度门控制。
- **全流程无训练**：所有引导向量从一次前向缓存中提取，不更新模型参数。

### 关键结果
在GSM8K、AQUA、LOGIQA、MATH四个数学与逻辑推理数据集上，对Qwen3-4B/32B-Thinking和Gemma-4-E2B三个模型进行实验，主要评估诱导状态退出的hit rate：
- 在大多数集群上，SOPHIA的正向引导比无干预的greedy解码显著提升退出率，例如在Qwen3-4B上GSM8K C3从25.0%升至100%，AQUA C0从0%升至51.7%。
- 负向引导降低退出率，随机扰动无显著影响，证实方向特异性。
- 不同状态之间的增益差异表明状态特定向量的必要性，全局统一方向无法适应所有情况。
- 该方法在32B更大模型上同样有效，且跨模型架构（Gemma）也可迁移，无需重新调参。
