---
title: The Assistant Persona Differs Across Languages in Activation Space
title_zh: 激活空间中助手人格方向跨语言差异显著
authors:
- Daniel Yoo
- Naama Rozen
- Evan Harris
affiliations:
- Carnegie Mellon University
- Tel Aviv University
- Independent Researcher
arxiv_id: '2611.27504'
url: https://arxiv.org/abs/2611.27504
pdf_url: https://arxiv.org/pdf/2611.27504
published: '2026-11-20'
collected: '2026-11-23'
category: LLM
direction: 跨语言助手人格激活方向差异
tags:
- activation steering
- multilingual safety
- persona direction
- mechanistic interpretability
- safety alignment
- low-resource languages
one_liner: 在31种语言中提取助手人格方向，发现与英语轴余弦相似度仅0.378–0.911，低资源语言偏离更大且更易被反向steering放大越狱
practical_value: '- 多语言电商Agent/客服/审核系统中，不要直接复用英文安全或人设 steering 向量；低资源语言需单独提取或校准，否则
  guardrail 容易被绕过。

  - 需要跨语言保持品牌语气或助手人设一致时，建议按目标语言构建 activation direction 并做 per-language steering/monitoring，可监控“默认状态到
  helpful assistant 方向的距离”。

  - 多语言安全评估应把低资源语言作为重点压力测试：默认 assistant state 偏离更远，persona-based jailbreak 用语言自身轴反向
  steering 更强，攻击者可能利用本地语义方向。

  - 在 RAG/Agent 流水线做多语言输出安全层时，不要只用英语对齐向量做分类；可训练语言特定 probe，至少按资源水平分层评估。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机：** 多语言安全差异已有行为证据，但不知助手人格本身是否跨语言一致；现有激活方向多从英语提取并假设可泛化。

**方法：** 在 Qwen3-32B 中提取 31 种语言的助手人格方向（Assistant Axis），比较与英语轴的余弦相似度；分析方向/幅度与语言资源水平的关系；测量默认助手状态到 helpful assistant 极点的距离；进行反向 steering 实验，比较语言自身轴与英语轴对 persona-based jailbreak 的放大作用。

**结果：** 各语言方向与英语轴相似度为 0.378–0.911，差异显著；方向和幅度均与资源水平相关；低资源语言默认状态更偏离 helpful assistant；用语言自身轴反向 steering 比英语轴更能放大越狱。说明模型没有跨语言统一的助手表示，多语言对齐需显式覆盖助手人格。
