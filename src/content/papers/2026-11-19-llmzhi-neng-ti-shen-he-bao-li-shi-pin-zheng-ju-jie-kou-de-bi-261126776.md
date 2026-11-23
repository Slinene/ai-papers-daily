---
title: What Helps Language-Model Agents Review Violent Video? A Controlled Comparison
  with a Human Evidence Reference
title_zh: LLM智能体审核暴力视频：证据接口的受控比较
authors:
- Mohammed El Amine Mokhtari
- Matei Mancas
- Virginie Vandenbulcke
affiliations:
- University of Mons
arxiv_id: '2611.26776'
url: https://arxiv.org/abs/2611.26776
pdf_url: https://arxiv.org/pdf/2611.26776
published: '2026-11-19'
collected: '2026-11-23'
category: Agent
direction: 多模态 Agent 证据接口的受控比较
tags:
- LLM Agents
- Multimodal
- Evidence Interface
- Violence Detection
- Controlled Study
- F1
one_liner: 在暴力视频审核中，flat text 证据接口追平单一音视频模型，而 graph 与消息传递更差且成本高
practical_value: '- 在 LLM Agent 决策中，把多个感知/数据源的结果一次性拼成 flat text 直接送入推理模型，往往优于多轮消息传递或基于工具的图探索。做商品视频审核、内容安全、广告合规等多模态判断时，可优先采用单轮扁平化证据聚合，避免过度设计
  Agent 通信协议。

  - 复杂的证据图/摘要和多轮工具调用可能引入额外错误（如摘要丢失关键细节、工具检索不准），且计算成本高（本文 pipeline 约 3 倍 GPU 时间）。在需要可解释性时，展示引用片段即可，不必要求模型通过
  graph 导航。

  - 声音/语音等模态能提供增量信号（本文 F1 +0.012），电商场景中商品视频的背景音、用户语音评论、直播口播等可能包含有价值的安全/质量信息，可评估纳入统一证据文本。

  - 引用存储观测虽然忠实，但移除证据约一半决策会翻转，说明证据选择对最终决策影响很大，构建可审核的 Agent 时需记录并测试证据敏感性。'
score: 6
source: arxiv-cs.MM
depth: abstract
---

动机：视频暴力审核需要在准确率和可检查性之间平衡，且无需训练的 LLM 组合感知模型成为可能。但感知观测如何传递给决策模型、哪些证据重要仍不清楚。方法：在 XD-Violence 测试集（799 段）上，固定一组感知 agent（视频描述、物体检测、声音标签、语音识别、语音标签）和同一推理模型，比较三种证据接口：agent 间消息传递、typed evidence graph 通过工具探索、一次性读取 flat text；并对比单一音视频模型。两名标注者提供人类参考，记录决策、事件段及依赖视觉/声音/语音。结果：flat text F1 0.967 与单模型 0.968 相当，graph 与消息传递更差；用单独集开发的 graph 变体未缩小差距，graph 摘要和多轮工具使用均降低准确率。这些结论在改写提示词和更大推理模型下稳健，但大模型进一步削弱消息传递，使 graph 略优于消息。声音事件提升 F1 +0.012（CI [0.004,0.021]），与人类标注一致。引用存储观测忠实，移除证据改变约一半决策，但 graph 不比 flat text 更忠实；agent pipeline GPU 成本约为单模型 3 倍。另报告两个视觉语言描述器伪影误导下游。
