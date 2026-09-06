---
title: 'Perceive to Hypothesize, Verify to Ground: An Agentic Reasoning Framework
  for Open-World Geo-Localization'
title_zh: 面向开放世界地理定位的感知-假设-验证智能体推理框架
authors:
- Yutian Jiang
- Ruijie Li
- Sisuo Lyu
- Xixuan Hao
- Qingxiang Liu
- Yongzi Yu
- Yuxuan Liang
affiliations:
- The Hong Kong University of Science and Technology (Guangzhou)
- The Hong Kong University of Science and Technology
arxiv_id: '2608.29880'
url: https://arxiv.org/abs/2608.29880
pdf_url: https://arxiv.org/pdf/2608.29880
published: '2026-08-30'
collected: '2026-09-06'
category: Agent
direction: Agent 推理与证据验证定位
tags:
- Agentic Reasoning
- Geo-localization
- Perception-Verification
- Evidence Grounding
- Multimodal LLM
- Hallucination Mitigation
one_liner: 提出 GeoPAVE 双层智能体框架，以感知生成假设、验证证据支撑决策来缓解幻觉与上下文漂移
practical_value: '- 借鉴感知-假设-验证双层结构：在商品图像识别/以图搜货中，先让模型生成候选品牌、款式、材质等假设，再调用商品知识库或属性检测工具对假设做
  support/refute/refine，降低多模态 LLM 的幻觉率和错配率。

  - 显式证据 grounding 适合召回/排序前的 query 理解：对用户上传图片或模糊描述，不直接输出结果，而是要求模型先提取可验证证据（logo、包装、场景文字）并逐步推断，减少上下文漂移。

  - 将决策动作离散化为 support/refute/refine，可以作为推荐 Agent 中的通用校验模块，对 LLM 生成的推荐理由或商品属性进行多轮事实核查后再返回用户，提升可解释性和可信度。

  - 构建包含多跳查询、多轮工具调用和结构化推理轨迹的数据集，方式可迁移到电商场景，用于训练/评估带工具调用的推荐 Agent，但需注意增加在线推理时延与成本控制。'
score: 6
source: arxiv-cs.MM
depth: abstract
---

**动机**：开放世界地理定位需要模型从模糊视觉线索出发，经过多步推理与外部知识校验，但现有视觉语言模型普遍存在感知幻觉和上下文漂移，因为缺少显式证据验证。

**方法关键点**：论文将地理定位重构为类似人类的“先感知再验证”推理问题，提出 GeoPAVE（Geo-localization Perception-and-Verification-Engine）双层智能体框架。上层基于单次 rollout 进行感知假设生成，得到候选位置假设；下层通过验证模块对假设做证据 grounding，输出三种决策动作：support（支持）、refute（反驳）、refine（细化）。该结构把多模态感知、多跳查询和多轮工具调用组织成可追踪的推理轨迹。

**关键结果**：论文同时发布 PAVED 数据集，来源于真实用户签到数据，包含多跳查询、多轮工具调用和结构化感知-验证轨迹，用于更严格地评估具备证据验证的开放世界地理定位能力；代码与数据已开源。摘要未给出具体定位精度数值，主要贡献在于可验证推理框架和配套评估资源。
