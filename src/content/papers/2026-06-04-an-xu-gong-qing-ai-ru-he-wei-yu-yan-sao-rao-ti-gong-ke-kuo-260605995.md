---
title: 'Empathy on Demand: How Empathic AI Can Scale Emotional Support for Verbal
  Harassment'
title_zh: 按需共情：AI 如何为语言骚扰提供可扩展情感支持
authors:
- Anouk Bergner
- Philipp Winder
- Christian Hildebrand
affiliations:
- University of Geneva
- University of St. Gallen
arxiv_id: '2606.05995'
url: https://arxiv.org/abs/2606.05995
pdf_url: https://arxiv.org/pdf/2606.05995
published: '2026-06-04'
collected: '2026-06-08'
category: LLM
direction: LLM 情感支持 · 语言信号分析
tags:
- Empathy
- LLM
- Emotional Support
- Verbal Harassment
- Coping
one_liner: LLM 在语言骚扰场景中展现出超越人类专家和非专家的共情倾听能力，显著提升被倾听感和应对效能
practical_value: '- 在电商客服或社区管理系统中，可将 LLM 生成的共情回复注入三大信号：先表达对用户处境的视角采纳，再显式确认其情绪（情感验证），最后给出具体可操作的解决方案（行动导向），以提升用户被倾听感和问题解决意愿。

  - 对话 Agent 设计时，可借鉴该框架构建回复质量评估模块，用 NLP 指标量化视角接纳、情感验证和行动导向程度，作为强化学习的奖励信号或微调目标，优化 Agent
  的共情行为。

  - 对于大规模用户投诉或负面评论处理，使用 LLM 自动生成符合三大信号的共情回复，可降低人工成本同时保持高同理心，但需结合业务语境微调提示词或模型，避免生成空洞的共情话术。

  - 该研究验证了特定语言特征能有效建立人-AI 之间的情感连接，在推荐系统的对话式交互或引导式消费场景中，可引入类似信号增强用户参与度和信任感。'
score: 7
source: arxiv-cs.HC
depth: abstract
---

**动机**：语言骚扰普遍存在且难以及时获得情感支持，人们越来越多转向 AI 寻求倾诉，但 AI 能否产生与人类共情同等的心理益处尚不明确。

**方法**：提出共情倾听的心理框架，包含三个核心语言信号：视角采纳（承认对方观点）、情感验证（命名并接纳情绪）和行动导向（鼓励建设性应对）。让 LLM（如 ChatGPT）对语言骚扰场景生成回应，与非专家人类和训练有素的心理健康专业人员的回应对比，通过 NLP 自动分析和人类评分测量三大信号的强度；随后在线行为实验检验这些信号对被倾听感和应对自我效能的影响。

**关键结果**：LLM 的回应在三大信号上均显著强于人类非专家和专业人员，诱导出更多接近导向（而非回避导向）的应对策略；行为实验进一步证实，强化三大信号的语言能显著提升被倾听感（β=0.38）和应对自我效能（β=0.29）。

**结论**：特定语言特征能在人机间建立共情连接，增强心理韧性，AI 可作为扩展情感支持的可行手段。
