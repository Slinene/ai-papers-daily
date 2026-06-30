---
title: 'Mixture of Debaters: Learn to Debate at Architectural Level in Multi-Agent
  Reasoning'
title_zh: 辩论专家混合：在多智体推理中学习架构级辩论
authors:
- Dayong Liang
- Kaisong Gong
- Yi Cai
- Changmeng Zheng
- Xiao-Yong Wei
affiliations:
- South China University of Technology
- Tianjin University
- The Hong Kong Polytechnic University
arxiv_id: '2606.29425'
url: https://arxiv.org/abs/2606.29425
pdf_url: https://arxiv.org/pdf/2606.29425
published: '2026-06-28'
collected: '2026-06-30'
category: MultiAgent
direction: 多智体推理 · MoE 内部自辯 · 动态路由
tags:
- multi-agent
- debate
- mixture-of-experts
- self-debate
- multimodal reasoning
- routing stability
one_liner: 通过混合专家架构实现单模型内部动态辩论，解耦角色与流程路由，推理性能超越多智体外辩论，延迟降 3.7 倍，Token 省 87%
practical_value: '- **内部自辯替代多模型辩论架构**：在电商客服、搜索问答等多轮推理场景，可直接用单模型内化辩论，省去多模型通信开销，延迟和
  Token 成本大幅下降，适合对延迟敏感的在线服务。

  - **双路由器解耦角色与流程**：可迁移到推荐系统的理由生成或排序过程，让模型同时扮演“提案者”和“评审者”，动态决定何时辩论、何时合成，提升复杂决策的一致性。

  - **动量切换稳定推理**：滑动窗口平滑专家选择，避免 Token 级路由波动造成的前后矛盾，适合需要连贯多轮交互的产品（如对话式推荐、多步搜索澄清）。

  - **视角转移数据合成**：利用模型自身生成正确/错误回复构造辩论训练数据，可借鉴到推荐解释或搜索摘要的自我修正训练，低成本提升模型纠错能力。'
score: 8
source: arxiv-cs.MM
depth: full_pdf
---

**动机**：现有多智体辩论框架通常需要实例化多个模型副本，架构固定且计算开销大，难以适配真实场景中动态变化的推理需求。本文旨在将辩论过程内化到单一模型，利用混合专家（MoE）范式实现动态角色分配和流程控制。

**方法关键点**：
- **双路由器机制**：将角色分配（解读专家）与流程控制（综合专家）解耦，用两个独立路由器选择专家，通过几何平均（√乘积）融合门控分数，实现不对称专家组合。
- **动量切换**：用因果滑动窗口（默认窗口大小16）平滑 Token 级路由，减少专家频繁切换，保持论证连贯。
- **解耦专家池**：解读专家 A 和综合专家 B 分别独立组成组合路径，形成 N×N 的组合多样性，比耦合的 MoE-LoRA 更灵活。
- **视角转移数据合成**：从基模型采样生成正确与错误回复，构造三种训练轨迹：仅正确链、修正轨迹（视角转移）、鲁棒轨迹（面对误导仍保持正确），迫使模型学习识别错误并修正立场。

**关键结果**：在 LLaVA-v1.6-13B 和 Qwen2.5VL-3B-Instruct 两个多模态基线上，MoD 在 MMLU、ScienceQA、MMMU、MMStar 等基准上均超越常规 MoE-LoRA 和外部多智体辩论。例如 LLaVA-13B 上 MoD 多轮辩论将 ScienceQA 从 74.51 提高到 75.21，MMMU 从 37.29 提高到 38.44，同时推理延迟降为 1/3.7，Token 消耗减少 87%。消融表明双路由器、滑动窗口动量及视角转移数据均对推理增益有显著贡献。
