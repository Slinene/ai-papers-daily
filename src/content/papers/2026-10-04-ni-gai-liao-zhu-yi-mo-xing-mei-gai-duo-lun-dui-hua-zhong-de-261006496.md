---
title: 'You Changed Your Mind, The Model Didn''t: Demystifying Intent in Multi-Turn
  Dialogue'
title_zh: 你改了主意，模型没改：多轮对话中的意图解谜
authors:
- Junle Chen
- Wei Chen
- Zhengjun Huang
- Zhoujin Tian
- Yuxuan Liu
- Kai Wang
- Rui Chen
- Xiaofang Zhou
affiliations:
- HKUST
- Tencent Hy
arxiv_id: '2610.06496'
url: https://arxiv.org/abs/2610.06496
pdf_url: https://arxiv.org/pdf/2610.06496
published: '2026-10-04'
collected: '2026-10-10'
category: Training
direction: LLM 多轮意图追踪与自蒸馏训练
tags:
- multi-turn dialogue
- intent tracking
- self-distillation
- instruction following
- benchmark
one_liner: 提出 Intent-Eval 揭示 LLM 将已拒绝/被取代内容当作有效需求，并用 Intent-OPSD 自蒸馏缓解意图混淆
practical_value: '- 在电商导购/客服 Agent 中显式维护 active intent 状态：用户说“换成蓝色”后又取消，不应把蓝色偏好带入后续推荐；可在
  prompt 或上下文状态层标记 rejected/superseded，避免模型把“被提及”当成“仍有效”。

  - 微调多轮指令跟随模型时可借鉴 Intent-OPSD：冻结同模型 Teacher 以最终决策和完整任务生成正确 active-intent 响应，Student
  在含干扰的完整对话上做 on-policy self-distillation；有助于模型忽略被拒绝的中间变更。

  - 构建多轮 Agent 评估集时加入 rejected proposal 和 superseded requirement 负样本，专门测意图混淆；这类错误在单轮指令遵循评测里不可见，但会影响真实转化与体验。

  - 搜索/推荐澄清场景：用户多轮修正 query（如“不要红色，还是蓝色”）时，系统只应保留最终有效约束；可用版本化需求或 turn-level validity
  标记，生成/排序前做一致性校验。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：多轮对话中用户会提出变更后又拒绝，模型应继续执行原始意图；但现有 LLM 容易被 rejected/superseded 内容带偏，把“被提及”当成“仍有效”。

方法：构建 Intent-Eval，覆盖工具调用、代码、数据库、数学任务，系统比较澄清、接受变更、拒绝变更三类情境。发现 mentioned-as-in-effect 混淆：已拒绝或已取代的内容仍被当作 active requirements，准确率下降会随交互持续或加深。基于此提出 Intent-OPSD，一种 decision-conditioned on-policy self-distillation 框架：Teacher 与 Student 由同一模型初始化，冻结 Teacher 根据完整任务和用户最终决定提供 active-intent 监督，Student 在完整对话上训练，只遵循符合用户最终意图的有效需求。

结果：多个任务上模型对 rejected proposals 和 superseded requirements 均表现脆弱；Intent-OPSD 通过显式区分 mentioned 与 in effect，缓解多轮对话中的意图混淆。
