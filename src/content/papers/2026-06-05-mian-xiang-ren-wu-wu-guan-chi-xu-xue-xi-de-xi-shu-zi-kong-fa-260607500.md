---
title: Sparse Subspace-to-Expert Sharing for Task-Agnostic Continual Learning
title_zh: 面向任务无关持续学习的稀疏子空间到专家共享方法
authors:
- Fatema Siddika
- Md Anwar Hossen
- Tanwi Mallick
- Ali Jannesari
affiliations:
- Iowa State University
- Argonne National Laboratory
arxiv_id: '2606.07500'
url: https://arxiv.org/abs/2606.07500
pdf_url: https://arxiv.org/pdf/2606.07500
published: '2026-06-05'
collected: '2026-06-08'
category: Training
direction: LLM 持续学习 · Mixture of Sparse Experts
tags:
- continual learning
- mixture of experts
- catastrophic forgetting
- sparse experts
- LLM
one_liner: 通过稀疏 MoE 自适应分解任务共享与特有知识，并用弹性锚定和路由正则化缓解灾难性遗忘
practical_value: '- 多任务推荐的增量更新可借鉴任务特定与共享专家分离：当电商推荐需要持续适配新品类或促销时，将突发 pattern 注入专属专家，避免覆盖通用偏好知识。

  - 路由感知正则化与弹性锚定对在线模型稳定更新有参考价值：在推荐系统不停服微调时，可对关键共享参数施加弹性约束，防止遗忘核心基础能力。

  - 稀疏激活的 MoE 结构天然适合低延迟服务：在生成式推荐或 Agent 中，每次推理仅激活少量专家，可控制计算开销，适合在线增量学习场景。

  - 任务无关的自动门控机制对 Agent 长程任务序列有效：Agent 持续学习多工具调用时，门控可按子任务组合历史专家，无需人工指定，提升向后迁移。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

动机：LLM 在持续学习中面临可塑性-稳定性困境——新任务学习常导致旧知识灾难性遗忘。现有方法均等对待所有参数，未区分任务专用知识与跨任务共享能力。

方法：提出 SETA，将参数空间自适应稀疏分解为任务特定专家和共享专家。任务特定专家隔离独立模式，共享专家捕捉通用特征。训练时通过自适应弹性锚定对关键权重施加变化约束，并引入路由感知正则化同时保护权重和路由层面的共享知识；推理时统一门控网络自动检索正确专家组合。模型基于 LLaMA-2 和 Qwen 等 backbone 进行参数高效微调，仅更新少量专家参数。

结果：在多个领域 benchmark 上，SETA 在 LLaMA-2 7B 和 Qwen3-4B 上均达到竞争或最优总体性能，尤其对早期任务知识的保留显著优于 SOTA 基线，后向迁移指标明显提升，验证了隔离与共享分离的有效性。
