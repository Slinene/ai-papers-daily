---
title: '4DMemory: Benchmarking Long-Horizon Spatiotemporal Memory with Harness-Augmented
  Agents'
title_zh: 4DMemory：长时程时空记忆基准与 Harness 增强 Agent
authors:
- Yanhao Jia
- Yi Zhu
- Yiran Zhong
- Weigao Sun
- Feida Zhu
- Pengkun Jiao
- Sihan Yang
- Ming Ma
- Steven Hoi
- Erik Cambria
affiliations:
- Nanyang Technological University
- Token Foundry, Alibaba
- The Chinese University of Hong Kong
- Institute of Neuroscience, Chinese Academy of Sciences
- University of Chinese Academy of Sciences
arxiv_id: '2610.32332'
url: https://arxiv.org/abs/2610.32332
pdf_url: https://arxiv.org/pdf/2610.32332
published: '2026-10-23'
collected: '2026-10-26'
category: Eval
direction: 长视频时空记忆评测与 Agent 增强
tags:
- long-horizon
- spatiotemporal
- video benchmark
- RAG
- agent harness
- multimodal
one_liner: 发布900小时长视频基准与4DMemory Harness，使13个基础模型长时程时空推理提升超50%
practical_value: '- 用户长期行为序列（浏览/点击视频、直播切片）可借鉴「感知记忆+工具检索」分离：将原始行为编码成可索引的时空片段，按需用专用工具抽取关键事件，避免把所有帧塞进长上下文，降低遗忘与幻觉。

  - 4DMemory Harness 的多技能+工具模型编排可迁移到电商多模态 Agent：把商品识别、场景理解、OCR、时序定位拆成小模型/工具，由主 LLM
  调度，并通过 model-specific RAG 为不同基底模型定制检索策略，论文中所有模型提升超50%，稳定性可复用。

  - 长时程评测设计值得借鉴：构造跨数小时、数天的细粒度问题（例如商品在第几分钟出现、促销文案变化顺序），压测 Agent 长期记忆与召回模块，提前暴露长会话信息丢失问题。

  - 如业务含直播回放、商品讲解视频或广告素材库，可复用 LongVideo 构建思路，标注时空问答对，评估多模态检索和推荐理由是否准确引用正确时刻。'
score: 7
source: arxiv-cs.MM
depth: abstract
---

**动机**：现有多模态模型和基准集中在短/中上下文，难以在小时到年级时间跨度上保持细粒度时空记忆，限制长时程事件推理。

**方法**：引入 LongVideo 数据集，约900小时视频、5,000+人工审核问题，覆盖视觉、文本与时序空间推理，形成 4DMemoryBench 基准。同时提出 4DMemory Harness，整合四项互补技能、22+专用工具模型，并配置模型专属 RAG 系统，实现按需检索与工具调用。

**结果**：评估13个主流模型，standalone 基础模型在长时程任务上表现差；接入 Harness 后所有模型提升超过50%；同一批模型在 4DMemoryBench 相比此前基准性能下降超过10%，说明该基准更难，更能暴露长记忆能力的真实差距。
