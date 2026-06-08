---
title: 'MemDreamer: Decoupling Perception and Reasoning for Long Video Understanding
  via Hierarchical Graph Memory and Agentic Retrieval Mechanism'
title_zh: 'MemDreamer: 分层图记忆与代理检索解耦感知推理的长视频理解框架'
authors:
- Cong Chen
- Guo Gan
- Kaixiang Ji
- ChaoYang Zhang
- Zhen Yang
- Guangming Yao
- Hao Chen
- Jingdong Chen
- Yi Yuan
- Chunhua Shen
affiliations:
- Ant Group
- Zhejiang University
- Central South University
- HKUST(GZ)
arxiv_id: '2606.07512'
url: https://arxiv.org/abs/2606.07512
pdf_url: https://arxiv.org/pdf/2606.07512
published: '2026-06-05'
collected: '2026-06-08'
category: Multimodal
direction: 长视频理解 · 分层图记忆 · 代理检索
tags:
- Long Video Understanding
- Hierarchical Graph Memory
- Agentic Retrieval
- Vision-Language Models
- Tool-Augmented Reasoning
one_liner: 通过分层图记忆和代理工具检索将长视频理解转化为探索过程，仅用2%上下文窗口即实现SOTA
practical_value: '- 层次化图记忆可借鉴到用户行为序列或商品图谱建模：将用户交互构造成多粒度语义图（session→item→attribute），捕捉时序与因果关系，用于召回或推理。

  - 代理式检索（Observation-Reason-Action循环）可应用于对话式推荐：工具增强的代理动态查询知识库，缩小上下文窗口，提升长对话或复杂推荐场景下的推理准确性和效率。

  - 解耦感知与推理：将特征编码（感知）与排序策略（推理）分离，允许流式增量更新用户记忆，缓解长序列带来的注意力稀释，适合实时推荐场景。

  - 稀疏图记忆检索大幅降低计算开销：推理时仅检索关键子图而非全量输入，可在推荐模型推理阶段采用类似检索增强方法，用极低 token 成本维持高性能。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：长视频理解面临全量视觉序列导致的 token 爆炸和注意力稀释，现有 VLMs 难以处理小时级视频。  
**方法**：提出 MemDreamer，将感知与推理解耦，转化为一个代理探索过程。它增量流式处理视频，构建**分层图记忆**（Hierarchical Graph Memory），自顶向下三层：底层为时空因果关系基础图，上层逐步抽象。推理时，推理模型采用**代理工具增强检索**，通过 Observation-Reason-Action 循环导航层级、搜索节点和遍历逻辑边，动态提取相关信息。  
**结果**：在四个主流长视频理解基准上达到 SOTA，与人类专家差距仅 3.7 分；推理上下文窗口仅为全量输入的 2%，却带来 12.5 个绝对准确度提升。此外，分析发现 VLM 的逻辑推理能力与长视频理解性能存在强线性正相关，表明代理能力扩展是通往多模态理解的新范式。
