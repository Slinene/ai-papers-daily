---
title: 'SAIL: Scientific Agentic Intelligence via a Science-Aware Loop'
title_zh: SAIL：通过科学感知循环实现科学智能体智能
authors:
- SAIL Model Team
- Boyuan Sun
- Bryan Dai
- Che Liu
- Chi Liu
- Derek Li
- Hongming Piao
- Mengzhuo Chen
- Xidong Wang
- Yan Shu
affiliations:
- IQuest Research
arxiv_id: '2610.11451'
url: https://arxiv.org/abs/2610.11451
pdf_url: https://arxiv.org/pdf/2610.11451
published: '2026-10-08'
collected: '2026-10-09'
category: Agent
direction: 科学智能体训练循环
tags:
- Scientific Agent
- Agentic RL
- On-policy Distillation
- Failure Diagnosis
- MoE
- Training Data Generation
one_liner: 35B总参/3B激活的开源科学智能体，用失败诊断自动生成训练任务，性能媲美更大模型
practical_value: '- **业务 Agent 失败诊断闭环**：用强模型分析业务 Agent 的失败 case，定位是检索证据选择、规划修订还是工具调用能力不足，再基于业务知识库自动生成带交互轨迹和可执行环境的训练样本，比人工标注更可规模化。

  - **小模型逼近大 Agent 能力的训练组合**：先做子能力 specialist SFT（如 query 改写、搜索结果筛选），再用多个 frontier
  model 做多教师 on-policy 蒸馏，最后接入 Agentic RL。适合电商/搜索推荐场景下用低成本模型达到大模型 Agent 效果。

  - **MoE 架构降低推理成本**：35B 总参 / 3B 激活的设计在保持推理低延迟的同时提升多任务能力，对需要实时响应的搜索推荐 Agent 有直接参考价值。

  - **搜索型任务重点优化证据选择**：论文发现文献任务失败主要来自证据选择，提示可以在搜索推荐 Agent 中显式构造 query 改写、召回结果排序、引用证据一致性等训练数据，而非只依赖端到端生成。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：科学智能体需要处理文献检索、科学编码和多步研究流程，开源模型能力不足，而直接扩大参数成本过高。

**方法关键点**：SAIL 采用 science-aware improvement loop：frontier agent 分析 SAIL 任务失败，诊断文献任务中的搜索与证据选择、编码中的科学假设与推理、长程调查中的规划与修订；基于论文集合和科学代码仓库自动构建问题、交互轨迹和可执行任务；多轮迭代训练，方法包括 SFT、专项训练、多教师 on-policy 蒸馏和 Agentic RL。模型架构为 35B 总参 / 3B 激活的 MoE。

**关键结果**：在 SciCode、DS-1k、LitQA-search、E2E-Bench 等多个科学基准上取得与更大开源模型相当或更优水平，例如 E2E-Bench Hard 86.2（超过 GLM-5.2 的 83.7），而参数量显著更少。
