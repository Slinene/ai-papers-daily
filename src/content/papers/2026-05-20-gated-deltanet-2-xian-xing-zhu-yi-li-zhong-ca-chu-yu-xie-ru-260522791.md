---
title: 'Gated DeltaNet-2: Decoupling Erase and Write in Linear Attention'
title_zh: 'Gated DeltaNet-2: 线性注意力中擦除与写入的解耦'
authors:
- Ali Hatamizadeh
- Yejin Choi
- Jan Kautz
affiliations:
- NVIDIA
arxiv_id: '2605.22791'
url: https://arxiv.org/abs/2605.22791
pdf_url: https://arxiv.org/pdf/2605.22791
published: '2026-05-20'
collected: '2026-05-24'
category: LLM
direction: 线性注意力 · 记忆更新解耦
tags:
- Linear Attention
- Delta Rule
- Gating
- Long Context
- Memory Update
- Linear Recurrent
one_liner: 将 Delta 规则的记忆更新拆分为通道级擦除门与写入门，突破原有标量门控的耦合限制，显著提升长上下文检索性能。
practical_value: '- **超长用户序列建模**：电商中用户行为序列可达数万步，Gated DeltaNet-2 的线性时间复杂度和常量级解码内存可直接用于高效序列编码，其通道级擦除/写入解耦能更精细地更新兴趣记忆，避免旧兴趣过早丢失或新兴趣写入不足。

  - **记忆网络的特征交互**：可将该方法的核心思想——解耦“遗忘”与“记忆”的强度控制——迁移到特征交互的记忆模块，例如在 Deep Interest Network
  中，用独立的通道门控来更新交叉特征的记忆，提升对用户长期偏好的捕获。

  - **并行化训练的工程借鉴**：论文推导的 chunkwise WY 算法和门控感知反向传播可直接用于大规模推荐模型的序列训练，在不牺牲模型表达能力的前提下大幅提高训练吞吐，适合线上内容快速迭代。

  - **Agent 工作记忆的维护**：在多智能体系统中，该技术可用于维护上下文压缩后的记忆状态，通过解耦擦除和写入，实现对对话历史、环境状态的精准增量编辑，增强
  Agent 在长对话或复杂任务中的上下文跟踪能力。'
score: 6
source: huggingface-daily
depth: abstract
---

动机：线性注意力通过固定大小的循环状态压缩历史，但现有 Delta 规则模型（如 Gated DeltaNet、KDA）在更新记忆时，使用单个标量门控同时控制“擦除旧信息”和“写入新信息”，这种耦合限制了记忆编辑的精细度，容易干扰已有关联。

方法：提出 Gated DeltaNet-2，引入两个独立的通道级门控因子：擦除门 \(b_t\) 和写入门 \(w_t\)，分别控制 Key 端旧内容的擦除强度和 Value 端新内容的写入强度。模型可退化为 KDA（两门坍塌为同一标量）和 Gated DeltaNet（进一步退化到无通道级衰减）。同时，给出了快速权重更新视角，推导了将通道级衰减吸收到非对称擦除因子的 chunkwise WY 并行算法，以及保持并行训练效率的门控感知反向传播。

结果：在 1.3B 参数、100B FineWeb-Edu 令牌训练下，模型在语言建模、常识推理和检索任务上整体优于 Mamba-2、Gated DeltaNet、KDA 和 Mamba-3 等基线。在长上下文 RULER 基准中，多键检索能力显著提升，并在循环与混合设置下均保持健壮性。
