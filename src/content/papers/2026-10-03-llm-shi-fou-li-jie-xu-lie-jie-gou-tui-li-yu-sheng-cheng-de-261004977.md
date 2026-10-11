---
title: Do LLMs Understand Sequential Structure? A Controlled Study of Inference and
  Generation
title_zh: LLM 是否理解序列结构？推理与生成的受控研究
authors:
- Jerry Wang
- Zhengxiang Wang
- Ting Yu Liu
- Hsin-Ling Hsu
- Yi-Cheng Lai
- Tengfei Ma
affiliations:
- University of Illinois Urbana-Champaign
- Stony Brook University
- National Chengchi University
arxiv_id: '2610.04977'
url: https://arxiv.org/abs/2610.04977
pdf_url: https://arxiv.org/pdf/2610.04977
published: '2026-10-03'
collected: '2026-10-11'
category: Reasoning
direction: LLM 序列理解与行为模拟评估
tags:
- LLM
- Sequential Structure
- Behavioral Simulation
- Markov
- Evaluation
- Inference
one_liner: 受控实验表明 LLM 对潜在序列结构的识别与生成存在显著落差，表面行为保真可能掩盖错误机制
practical_value: '- 在用户行为模拟（如生成模拟点击/浏览序列用于离线评估）中，不要只看动作分布或边际频率：应评估条件依赖，例如给定历史动作后下一个动作的准确率、校准度或
  n-gram 条件命中率，否则表面分布匹配可能掩盖错误机制。

  - 用 LLM 作为推荐系统用户模拟器时，即使生成序列看起来合理，也可能未学到真实状态转移。建议增加干预测试：修改历史上下文并观察下一个动作是否符合预期规则，或设计探测任务来验证隐式策略是否正确。

  - 现实业务序列往往含高阶依赖，而论文显示 LLM 在高阶依赖下规则恢复明显退化。因此当用户行为序列较长、依赖复杂时，不宜完全依赖 LLM 的隐式序列建模，可考虑混合架构：LLM
  负责语义/意图，专用序列模型（如 RNN、状态机）负责状态转移和条件依赖。

  - 若用 LLM 做多轮 query 改写或对话推荐，长上下文不一定提升潜在意图识别；应显式设计条件推理评估，并谨慎依赖 LLM 对长期依赖的内隐建模。'
score: 6
source: huggingface-daily
depth: abstract
---

动机：LLM 越来越多被用作交互式 Agent 和行为模拟器，但常见评估只比较生成动作的表面频率，无法判断模型是否学到了决定行为的潜在序列依赖。因此需要分离“分布匹配”和“条件规则遵循”。

方法：设计两类受控任务：双人石头剪刀布交互和单玩家随机 n-gram 续写。通过控制潜在策略、马尔可夫规则和高阶条件依赖，测试 LLM 识别策略、遵守规则和维持条件结构的能力。框架独立评估分布匹配与条件规则遵循，避免混淆。

结果：更长上下文没有提升策略识别准确率；模型即使能识别潜在策略，也不能保证忠实模拟其生成机制；当依赖阶数提高时，规则恢复能力显著下降。这表明 LLM 可能表现出与真实数据相似的表面行为分布，但内部生成机制是错误的，单纯的行为保真度不足以证明序列结构被正确理解。
