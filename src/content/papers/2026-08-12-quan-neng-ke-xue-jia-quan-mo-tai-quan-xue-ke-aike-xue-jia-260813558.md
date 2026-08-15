---
title: 'OmniScientist: An Omni-Modal Omni-Discipline AI Scientist'
title_zh: 全能科学家：全模态全学科AI科学家
authors:
- Bobo Li
- Hao Fei
- Tianjie Ju
- Mong-Li Lee
- Wynne Hsu
affiliations:
- National University of Singapore
- University of Oxford
arxiv_id: '2608.13558'
url: https://arxiv.org/abs/2608.13558
pdf_url: https://arxiv.org/pdf/2608.13558
published: '2026-08-12'
collected: '2026-08-15'
category: MultiAgent
direction: 自主科研多代理 · 多模态感知
tags:
- AI Scientist
- Multimodal Agents
- Autonomous Research
- LLM Agents
- Tool Use
one_liner: 端到端多模态AI科学家，从原始异构证据直接完成研究全流程，感知层让论文质量显著提升
practical_value: '- 在推荐/搜索Agent中，让LLM直接感知原始多模态证据（商品图、视频、音频、评论原声）而非只接收预计算标量特征，可以保留空间/时间/跨通道关系，提升推荐解释或商品描述的事实一致性。

  - 采用“ideation-experiment-writeup”三代理分工结合确定性管道，把生成任务拆为提案、执行、总结，可迁移到自动化选品、广告文案实验、营销报告生成等场景。

  - 借鉴“idea/rigour/claim checks”代码执行校验：对LLM生成的推荐文案、结论做可执行验证，例如数值引用检查、统计显著性检查，增强输出可信度和可追溯性。

  - 感知层与代理解耦的设计，便于在商品知识图谱构建、多模态商品理解等业务中逐步引入多模态原始数据。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有AI科学家系统通常只覆盖文本、代码、标签或预计算摘要，忽略了科学发现所需的原始证据中的空间、时间、跨通道和流程关系，限制了多学科研究的证据基础。

**方法关键点**：OmniScientist 引入感知层和三个自主代理（ideation、experiment、writeup），在确定性管道中直接从异构原始数据开展研究。感知层让观察结果贯穿整个研究生命周期，影响研究问题、实验决策和最终结论。系统通过代码执行 idea、rigour、claim 三类检查，强制进行新颖性筛选、统计有效性验证、执行溯源和数值可追溯。

**关键结果**：在36个真实数据案例上（跨5个学科族、4类科学证据，模态包括图像、信号、音频、视频、3D结构、轨迹、表格、公式、图），系统全部完成从原始数据到编译稿的全流程，平均论文得分6.3（使用参考推理骨干）。与仅接收预计算标量特征的盲变体成对比较，直接感知在所有7个评价维度上均有提升，head-to-head胜率达到85%。
