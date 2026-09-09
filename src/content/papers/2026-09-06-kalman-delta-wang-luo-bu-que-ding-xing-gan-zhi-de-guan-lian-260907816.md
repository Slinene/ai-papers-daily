---
title: 'Kalman Delta Networks: Uncertainty-aware Associative Memory'
title_zh: Kalman Delta 网络：不确定性感知的关联记忆
authors:
- Ngoc Bui
- Tinglin Huang
- Rex Ying
affiliations:
- Department of Computer Science, Yale University
arxiv_id: '2609.07816'
url: https://arxiv.org/abs/2609.07816
pdf_url: https://arxiv.org/pdf/2609.07816
published: '2026-09-06'
collected: '2026-09-09'
category: LLM
direction: 线性注意力 · 状态空间模型 · 不确定性建模
tags:
- linear attention
- Kalman filter
- state-space model
- uncertainty
- associative memory
- efficient inference
one_liner: 将线性注意力循环记忆重构为线性高斯状态空间模型，用卡尔曼滤波跟踪记忆不确定性并提出可并行扫描近似
practical_value: '- 用户长期行为序列建模中若采用线性注意力，可借鉴 KDN 的记忆不确定性机制，通过卡尔曼增益自适应控制写入强度，降低噪声行为对稳定兴趣表征的覆盖风险。

  - Agent 长对话/长程任务的状态维护可引入带置信度的增量写入，根据累积证据决定是否更新记忆，提升记忆稳定性与少样本适应能力。

  - Diagonal/Isotropic KDN 提供 O(dk)/O(1) 辅助状态并支持并行关联扫描，适合工业级实时推理，可用于构建流式用户兴趣追踪或在线学习模块。

  - 若探索生成式推荐中的 Semantic ID 记忆网络，可参考将记忆更新视为状态估计、用变分推断近似后验的思路，处理不确定性和动态环境。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：线性注意力因固定尺寸循环记忆而高效，但每个 token 的写入强度需在线决定；Delta-rule 模型只从当前 token 嵌入学习强度，不跟踪记忆估计的置信度，无法根据累积证据调整写入。

方法：KDN 将循环联想记忆重构为线性高斯状态空间模型，用卡尔曼滤波作为最优递归估计器。状态转移同时传播记忆和不确定性，卡尔曼增益根据累积证据与观测可靠性加权残差写入；Delta 更新成为其特例。为避免精确跟踪中密集 Riccati 递归难以并行的问题，提出两种扫描兼容近似：Diagonal KDN 通过在线平均场变分推断将后验投影到对角高斯族；Isotropic KDN 使用每头一个标量不确定性的各向同性近似。两者的不确定性递归均为 Möbius 映射，可实现对数并行深度的关联扫描，辅助状态分别为 O(dk) 和 O(1)。

结果：在 750M 和 1.3B 参数控制预训练中，KDN 变体持续改善 perplexity 和下游平均准确率，超过现有最好的线性注意力模型。
