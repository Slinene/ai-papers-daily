---
title: 'Seeing, Maintaining, and Learning: The Evolution of Multimodal Agent Memory'
title_zh: 看见、维持与学习：多模态智能体记忆的演进
authors:
- Minghao Guo
- Qingyue Jiao
- Xiujin Liu
- Jianhong Pang
- Ruimeng Yang
- Naihao Xu
- Liwei Che
- Haochen Xue
- Ziqi Wang
- Xinying Cai
affiliations:
- Rutgers
- Notre Dame
- Michigan
- Fudan
- UC San Diego
arxiv_id: '2610.19366'
url: https://arxiv.org/abs/2610.19366
pdf_url: https://arxiv.org/pdf/2610.19366
published: '2026-10-13'
collected: '2026-10-15'
category: Agent
direction: 多模态 Agent 记忆机制综述
tags:
- Multimodal Agent
- Memory
- Survey
- Long-horizon
- Self-Evolving Memory
one_liner: 提出双轴框架解析多模态Agent记忆的形成/表示与管理演化，总结设计模式与原则
practical_value: '- 将记忆分为 T1 静态 / T2 动态 / T3 自演进三层，可用于电商导购或客服 Agent 的记忆架构：用户长期偏好作为静态记忆（T1），会话内上下文动态更新（T2），跨会话策略通过经验持续优化（T3）。

  - 双轴框架指导多模态商品信息（图片、视频、文本描述）如何编码与表示，可借鉴 modality-specific embeddings、文本/结构化记录、latent/parametric
  representations 的取舍，设计商品知识库和用户画像的融合方式。

  - 原则强调 balancing source fidelity with abstraction、temporal validity and provenance、evidence
  grounding，对构建可解释、防幻觉的推荐/客服 Agent 记忆至关重要，尤其在召回证据和解释推荐理由时。

  - 自演进记忆策略可类比在线学习或 meta-learning，适合需要持续适应用户兴趣漂移的推荐系统，可探索用 LLM 自动更新记忆管理 policy。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**
多模态智能体在长时任务和终身学习场景中，需要从复杂异构的多模态数据中持续获取有用信息，但现有方法缺乏统一的记忆机制视角。

**方法关键点**
论文提出双轴分析框架：
- Axis I 形成与表示：关注保留什么信息、如何编码，包括 modality-specific embeddings、文本与结构化记录、latent/parametric representations。
- Axis II 记忆管理：分三层——T1 静态记忆复用固定记忆；T2 动态记忆通过稳定策略更新；T3 自演进记忆通过可演进的策略更新，从经验中学习记忆管理策略本身。

基于框架，论文梳理了多模态 Agent 记忆的常见设计模式，提炼出若干原则：平衡源保真与抽象、维护时间有效性与溯源、将记忆使用建立在可恢复证据上、随时间演进记忆策略。

**关键结果**
本工作为综述性质，无定量实验数字，但系统归纳了多模态 Agent 记忆的现状、设计空间与未来方向，为后续研究提供了分析工具。
