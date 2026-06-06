---
title: 'ForeSci: Evaluating LLM Agents for Forward-Looking AI Research Judgment'
title_zh: ForeSci：评估LLM智能体前瞻性AI研究判断的时序基准
authors:
- Qiuyu Tian
- Haojie Yin
- Yingce Xia
- Youyong Kong
- Zequn Liu
affiliations:
- Southeast University
- Beijing Zhongguancun Academy
- Duke Kunshan University
arxiv_id: '2606.00644'
url: https://arxiv.org/abs/2606.00644
pdf_url: https://arxiv.org/pdf/2606.00644
published: '2026-06-03'
collected: '2026-06-06'
category: Agent
direction: Agent 前瞻性判断评估基准
tags:
- LLM Agents
- Benchmark
- Forward-Looking Judgment
- Temporal Reasoning
- RAG
one_liner: 构建时间屏蔽的基准，揭示LLM代理在做前瞻研究决策时证据组织提升可追溯性但存在证据-决策脱节问题
practical_value: '- **时间屏蔽的离线知识库构建**：在电商推荐场景中，可借鉴其按时间切割数据的方式，构建严格避免未来信息泄露的离线评估集，评估模型对用户未来兴趣的预测能力。

  - **显式证据组织提升可解释性**：论文表明让Agent显式组织证据（如引用历史论文片段）能增强事实支撑，可迁移到电商Agent的决策链设计，例如要求推荐Agent在输出商品列表前必须引用用户历史行为证据，提升可追溯性。

  - **证据-决策对齐校验**：发现的脱节问题（证据相关但预测错误）提示在实际Agent部署中应引入一致性校验模块，比如在营销决策Agent生成文案时，自动比对引用的数据点是否真正支持结论，防止“合理却错误”的输出。

  - **任务设计避免随机猜测**：通过预截止分类线索和证据信号衍生任务，而非直接预测特定事件，该设计思路可复用于构建多决策类型的推荐Agent评测（如选品、定价、引流策略），使评测更具可控性。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：AI研究常在缺少未来证据的时点做出决策（如选择攻关瓶颈、研究方向），现有基准不评估LLM智能体能否基于历史信息做出有依据的前瞻判断。该工作旨在填补空白，构建可控的时序基准。

**方法**：ForeSci包含500个任务，跨越4个快速演进的AI领域和4类决策（如识别瓶颈、预测方向）。每个任务绑定截止时间之前的离线知识库，截止后论文仅用于验证。任务由截止前的分类分支和证据信号衍生，避免随机猜测未来事件；同时确保生成答案所用的骨干模型知识截止于任务时间点之前。评估覆盖原生LLM、混合RAG及三种研究智能体变体，搭配四个骨干模型。

**关键结果**：1）显式证据组织（如要求智能体明确列出支撑证据）提升输出可追溯性和事实基础，但效果因决策类型差异显著；2）诊断揭示普遍的“证据-决策脱节”现象——智能体可能引用相关证据却预测错误的对象，表明当前模型虽能检索到有效信息，但未能正确连接证据与目标决策。该基准将前瞻研究判断转化为可重复、可控的评估实验。
