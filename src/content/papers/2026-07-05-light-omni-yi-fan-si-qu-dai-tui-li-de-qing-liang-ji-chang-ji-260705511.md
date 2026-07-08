---
title: 'Light-Omni: Reflex over Reasoning in Agentic Video Understanding with Long-Term
  Memory'
title_zh: Light-Omni：以反思取代推理的轻量级长时记忆视频智能体
authors:
- Chang Nie
- Jiaju Wei
- Junlan Feng
- Chaoyou Fu
- Caifeng Shan
affiliations:
- Nanjing University
arxiv_id: '2607.05511'
url: https://arxiv.org/abs/2607.05511
pdf_url: https://arxiv.org/pdf/2607.05511
published: '2026-07-05'
collected: '2026-07-08'
category: Agent
direction: Agent 轻量级视频理解框架
tags:
- Agent
- Video Understanding
- Long-Term Memory
- Efficient Inference
- Multimodal
- Reflexive
one_liner: 通过全局与隐状态实现单步上下文驱动动作，以反射取代迭代推理，速度提升12.1倍、精度提高2.4%
practical_value: '- 全局状态压缩历史的方法可迁移到推荐系统的用户行为序列建模：通过层次化合并保留近期细节、总结远期事件，平衡记忆容量与信息保真度

  - 隐状态直接驱动动作的架构能避免昂贵的长链推理，适用于实时推荐中的快速决策（如排序、召回策略的动态生成）

  - 双状态设计（全局上下文 + 条件化隐状态）分离了语义理解与动作执行，可借鉴到 Agent 框架中提升检索语义对齐性

  - 记忆系统作为即插即用模块增强现有模型，推荐大模型可引入类似长短期记忆以提升连续会话的上下文一致性'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有视频理解智能体依赖迭代推理（如搜索、证据聚合）处理长时长流，导致高延迟与计算开销。根源在于缺乏全局上下文和检索时的语义不对齐，迫使模型进行侦探式推理。  
**方法**：提出 Light-Omni，通过双重上下文状态单次前向即可构建所需上下文。其一，维护一个全局状态——从情景记忆中持续整合的有限大小多模态脚本，通过层次化合并保留近期细节并总结过去事件，作为全局上下文。其二，以全局状态为条件，生成参数化隐状态，该隐状态直接驱动自主动作并产生检索嵌入，延迟极低。二者耦合实现了语义对齐的快速检索与反射式响应，完全规避迭代推理。  
**结果**：在多个视频基准上，Light-Omni 超越 M3-Agent，平均精度提升 2.4%，推理速度提升 12.1 倍，GPU 内存效率提升 2.6 倍。此外，它作为记忆系统可增强现有 MLLM 的性能与效率。
