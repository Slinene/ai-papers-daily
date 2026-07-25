---
title: LLMs Get Lost in Evolving User Intent
title_zh: LLM 在动态变化的用户意图中迷失
authors:
- Jihoon Tack
- Philippe Laban
- Jennifer Neville
affiliations:
- Microsoft Research
arxiv_id: '2607.20734'
url: https://arxiv.org/abs/2607.20734
pdf_url: https://arxiv.org/pdf/2607.20734
published: '2026-07-21'
collected: '2026-07-25'
category: Agent
direction: 动态对话中的意图追踪与评估
tags:
- LLMs
- Collaborative Agents
- Evolving Intent
- Multi-turn Evaluation
- Simulation Framework
- Dynamic User Intent
one_liner: 将静态单轮任务转为带意图演化的多轮对话，发现前沿模型追踪用户意图变化时性能大幅下降
practical_value: "- **对话式推荐/搜索评估必测多轮意图漂移**：电商场景中用户意图常随对话逐步细化或变更，现有单轮静态评估会高估模型真实表现，应构建意图演化式的多轮测试集（如从静态问答对中自动衍生多轮序列）。\
  \  \n- **可复现的意图演化数据构造框架**：论文方法通过将静态基准转化为带意图插入、修订、重定向的多轮对话，无需新标注，可直接用于生成电商对话质量验证数据，低成本评测意图追踪能力。\
  \  \n- **模型架构/训练启示**：高意图变化频率下性能骤降，提示需要显式记忆或意图摘要机制（如维护动态用户画像、对话摘要 Prompt），避免历史信息被冲淡；在微调时加入意图演化样本可针对性提升。\
  \  \n- **工程实现注意**：在构建 Agent 对话系统时，应将用户意图变化作为关键信号，监测并触发内部状态更新（如重置上下文或总结已确认意图），而不是单纯拼接历史消息。"
score: 7
source: huggingface-daily
depth: abstract
---

动机：LLM 正越来越多作为协作代理，在对话中逐步理解、修订并执行用户意图，但现有评估仍停留在单轮、完全指定的静态设定，无法反映真实协同中用户意图不断演化的动态性。  
方法：提出一个框架，将任意静态单轮任务转换为多轮对话，在保留原始评估协议的前提下，自动注入三类意图演化事件：增量揭示、中途修订、目标重定向，模拟用户意图在对话中的自然漂移。该框架不需新标注，可直接复用现有基准（如 SWE-Bench）作为受控测试床。  
结果：在多个任务上，模型在静态设定中的强表现不迁移至演化意图设定，所有测试模型系列均出现显著性能下降。即使是最先进的前沿模型，在经过 6 次意图转换后，任务完成度也大幅衰退，表现出对历史意图的遗忘和错误锚定。研究表明，当前 LLM 缺乏稳定追踪并随用户意图变化而调整行为的能力，这一缺陷在静态评测中完全不可见，却是未来协作式 Agent 落地的关键瓶颈。
