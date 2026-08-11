---
title: 'Beyond Simply Environment Scaling: Designing Effective Environment Distributions
  for Multimodal Agent Learning'
title_zh: 多模态智能体训练：从多样性与难度结构设计有效环境分布
authors:
- Kejian Zhu
- Zhuoran Jin
- Dongqi Huang
- Hongbang Yuan
- Yupu Hao
- Kang Liu
- Jun Zhao
affiliations:
- Institute of Automation, Chinese Academy of Sciences
- University of Chinese Academy of Sciences
arxiv_id: '2608.03571'
url: https://arxiv.org/abs/2608.03571
pdf_url: https://arxiv.org/pdf/2608.03571
published: '2026-08-05'
collected: '2026-08-11'
category: Agent
direction: Agent 训练环境优化 · 多样性 & 课程学习
tags:
- multimodal agent
- environment distribution
- curriculum learning
- diversity
- difficulty
- training
one_liner: 发现简单增加环境数量并不能提升智能体训练，提出能力感知环境选择与层次化难度课程来优化环境分布
practical_value: '- 在构建用户模拟器或交互环境训练推荐/对话 Agent 时，可采用能力感知采样（AES），按所需能力（如物品识别、偏好推理、对话理解）均匀覆盖环境，避免数据偏向简单交互。

  - 借鉴层次化难度课程（HDC），先去除环境中的显式提示信号训练基础能力，再逐步增加状态复杂度（如更多候选物品、更长历史），提升 Agent 的鲁棒性和泛化。

  - 工程实现上，为训练环境标注“所需能力”和“状态规模”等元数据，动态调整采样权重，比盲目扩大环境池更高效。

  - 在强化学习训练推荐策略时，注意环境分布的难度结构，避免随机均匀采样，课程化安排可加速收敛并提升最终效果。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有工作通过大规模环境池训练多模态 Agent，但发现单纯增加环境数量反而可能损害性能。原因在于环境分布的设计只关注单个环境的可执行性，忽略了整体多样性与难度结构。

**方法**：提出两个维度优化环境分布：
- **多样性**：Ability-aware Environment Selection (AES)，利用能力向量对环境聚类，确保训练集覆盖多种能力维度，避免冗余。
- **难度结构**：Hierarchical Difficulty Curriculum (HDC)，将课程学习分为两级——先通过削弱环境中的辅助信号（如去除任务提示）增加初始难度，再逐步扩大状态空间规模（如更长的历史、更多物品），形成递进训练。

**结果**：在多个多模态 Agent 任务上，AES 与 HDC 结合的训练方案显著优于简单环境缩放，有效提升泛化能力，验证了“选择合适的环境分布比单纯扩大数量更重要”。
