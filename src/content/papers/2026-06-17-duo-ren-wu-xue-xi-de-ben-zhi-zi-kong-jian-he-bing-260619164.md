---
title: Essential Subspace Merging for Multi-Task Learning
title_zh: 多任务学习的本质子空间合并
authors:
- Longhua Li
- Lei Qi
- Xin Geng
- Qi Tian
arxiv_id: '2606.19164'
url: https://arxiv.org/abs/2606.19164
pdf_url: https://arxiv.org/pdf/2606.19164
published: '2026-06-17'
collected: '2026-06-18'
category: Training
direction: 模型合并 · 本质子空间分解
tags:
- Model Merging
- Multi-task Learning
- Subspace Decomposition
- Low-rank Experts
- Training-free
one_liner: 利用任务更新的低维本质子空间，通过正交化融合和低秩专家路由实现训练无关的多任务模型合并
practical_value: '- 主要是学术贡献，多任务模型合并目前尚未在电商推荐系统中广泛应用，但可借鉴其思想：若需融合多个微调的单任务模型来服务多任务推荐，可尝试只保留任务更新在本质子空间中的成分以降低冲突。

  - ESM++ 的低秩专家分解和原型路由思想可参考用于推荐模型的多任务动态参数选择，减少参数冗余。

  - 训练无关的静态合并方法可作为快速集成多任务能力的基础工具，例如在试验阶段快速组合多个广告预估模型。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

模型合并面临的核心挑战是任务间干扰，即多个任务特定的参数更新在合并时相互冲突。本文分析发现，任务更新引起的输出偏移能量高度集中于少数主方向（本质子空间），而其余方向虽能量低，但多个任务叠加后会产生严重干扰。基于此，提出本质子空间分解（ESD），通过激活偏移的主成分分解每个任务更新，分离出本质成分和残差。进一步提出本质子空间合并（ESM），一种无需训练的静态合并方法，将各任务更新的本质成分正交化后融合，形成紧凑的多任务模型。为处理残差中遗留的任务特定信息，又提出 ESM++，一种训练无关的动态合并方法：将残差分解为低秩专家，并采用基于原型的路由机制在前向推理时动态选择最相关专家。实验显示，在不同任务组合和模型规模下，ESM 和 ESM++ 能有效保留任务知识，同时显著减少任务间干扰。该方法为训练无关的多任务模型集成提供了新思路。
