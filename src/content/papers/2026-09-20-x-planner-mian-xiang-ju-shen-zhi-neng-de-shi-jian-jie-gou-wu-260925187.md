---
title: 'X-Planner: Event-Structured Task Planning for Embodied Intelligence'
title_zh: X-Planner：面向具身智能的事件结构化任务规划
authors:
- Howard Lu
- Shalfun Li
- Porter Pan
- Cris
- Lumen
- Cyril
- Eric Hu
- Lily Li
- Maeve Zhang
- Robert Wang
affiliations:
- X Square Robot Team
arxiv_id: '2609.25187'
url: https://arxiv.org/abs/2609.25187
pdf_url: https://arxiv.org/pdf/2609.25187
published: '2026-09-20'
collected: '2026-09-28'
category: Agent
direction: 具身智能任务规划 · VLA 规划前端
tags:
- Embodied AI
- Task Planning
- VLA
- Chain-of-Thought
- Latent Decoding
- Event-Structured
one_liner: 为 VLA 引入事件结构化规划前端，联合离散事件状态与潜在 CoT 状态，用阶梯解码和冻结重建提升长程规划质量
practical_value: '- 事件结构化规划拆成「可解释离散事件状态 + 连续潜在 CoT 状态」双接口，可迁移到电商 Agent 的长流程任务：让 LLM
  输出可读子目标序列，同时保留 latent 状态跨层传递，兼顾审计与推理深度。

  - 用冻结的 latent-to-text 重建目标作为语义锚点，适合在业务中给隐状态加约束，避免端到端训练后 latent 漂移，尤其适用于没有大量标注的推荐/搜索
  Agent 规划数据。

  - 利用接管时间（takeover time）和人工注入失败样本训练持续错误识别，可借鉴到交互式推荐或对话 Agent：把用户中断/纠正日志作为弱监督，训练模型提前识别错误。

  - 离线评估采用两步法：先评规划文本质量（BERTScore/LLM judge），再测下游执行；业务中可把「规划质量」与「最终业务指标」解耦，缩短迭代周期。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现代 VLA 系统常把高层指令到低层动作的中间规划隐式化，现有 CoT 规划器依赖粗粒度任务级标注或逐 token 生成长推理链，导致监督与表示碎片化。

**方法关键点**：X-Planner 构建分层规划数据，融合 Ego、UMI 和遥操作，按来源设置不同标注深度；用接管时间和人工注入失败监督持续错误识别。模型侧共享 VLM 主干，提供两种事件结构化规划形式：离散接口发射可解释事件状态，潜在接口通过 Staircase Decoding 在交错 Transformer 深度传递连续 CoT 状态；冻结的 latent-to-text 重建目标给潜在表示提供语义锚点。

**关键结果数字**：离线两步规划评估中，X-Planner 在 BERTScore-F1 和 judge-based Overall 均排在四个评估模型第二；真机实验中优于评估基线，表征规划文本质量和下游执行。
