---
title: 'SIRIS: Can LLMs Tell When Simulation Errors Matter in AI-Driven Systems Research'
title_zh: SIRIS：LLM 能否判断模拟误差在 AI 驱动系统研究中是否重要
authors:
- Jinwoo Hwang
- Sukmin Cho
- Tao Zhang
- Soheil Abbasloo
- Jongse Park
- Peng Cheng
affiliations:
- KAIST
- Microsoft Research Asia
arxiv_id: '2611.10329'
url: https://arxiv.org/abs/2611.10329
pdf_url: https://arxiv.org/pdf/2611.10329
published: '2026-11-05'
collected: '2026-11-11'
category: Eval
direction: LLM 对模拟误差的决策判断评估
tags:
- LLM evaluation
- simulation
- systems research
- decision making
- self-correction
- AI agents
one_liner: 提出 SIRIS 基准，通过扰动模拟器构建对照 workload，评估 LLM 判断建模局限是否影响设计推荐的能力
practical_value: '- 在搭建 LLM Agent 自动化实验平台或使用模拟器筛选推荐/排序策略时，应加入参考模拟器对照，避免仅凭单一模拟器结果做出删除或保留策略的决策。

  - 不要只让 LLM 识别模拟器建模局限（如特征缺失、延迟估算偏差），必须强制其基于参考模拟器的对比结果做最终判断；识别局限不等于正确选择。

  - review/self-correction 单轮可能引入新错误，建议在 Agent 决策链路中采用多轮校验、集成投票或置信度阈值，同时监控引入错误率。

  - 对于电商/广告的流量分配、定价策略等离线模拟场景，可借鉴 SIRIS 构造“模拟器有误差但结论仍成立”和“误差改变结论”两类对照 workload，专门测试
  LLM 的鲁棒性。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：LLM Agent 越来越多地驱动系统研究，依赖模拟器大规模评估候选设计。但模拟器本身存在建模局限，可能扭曲预测但不改变推荐，也可能改变设计选择。需要评估 LLM 是否具备判断“模拟误差是否影响最终推荐”的系统理解能力。

**方法关键点**：SIRIS 通过扰动模拟器构造 workload 对：两个 workload 拥有相同候选设计、相同建模局限和相同模拟器推荐；扰动同时改变两个 workload 的预测，但参考模拟器只支持其中一个的推荐。这样迫使 LLM 区分“局限虽存在但推荐仍有效”与“局限使推荐失效”两种情形。在 LLM serving 设计问题上评估 13 个前沿 LLM。

**关键结果数字**：识别出建模局限并不保证做出正确选择；即使是最强模型有时也会放弃有效的模拟器推荐。加入 review 自校正轮次能帮助恢复部分有效选择，但在其他多个模型上引入新的错误。结论强调：评估 LLM 的系统理解应通过 imperfect simulator 下的设计决策进行，而非单纯考察对局限的识别能力。
