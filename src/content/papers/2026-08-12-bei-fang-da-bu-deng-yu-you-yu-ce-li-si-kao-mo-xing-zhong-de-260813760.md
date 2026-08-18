---
title: 'Amplified Does Not Mean Predictive: Reasoning Behaviors in Thinking Models'
title_zh: 被放大不等于有预测力：思考模型中的推理行为
authors:
- Jean de Dieu Nyandwi
- Leena Mathur
- Yonatan Bisk
- Robert Hawkins
- Graham Neubig
affiliations:
- Carnegie Mellon University
- Stanford University
arxiv_id: '2608.13760'
url: https://arxiv.org/abs/2608.13760
pdf_url: https://arxiv.org/pdf/2608.13760
published: '2026-08-12'
collected: '2026-08-18'
category: Reasoning
direction: 推理行为分析与过程奖励
tags:
- Reasoning behaviors
- Behavioral Lift
- Process reward
- Confidence calibration
- LLM
- VLM
one_liner: 提出 Behavioral Lift 指标，发现思考模型放大的推理行为与正确性关联弱，而置信校准等高关联行为未被充分放大
practical_value: '- 在 Agent 或搜索推荐链路中用 LLM 做推理/决策时，不要把“显式自我修正”“承认不确定”等表面行为当作可靠性信号；这些行为被思考训练放大但与最终正确性弱相关甚至负相关。可直接用置信校准类信号（如模型对答案的自信度评分、证据对齐程度）做在线过滤、置信度阈值或路由。

  - 做 generator-evaluator 或 RAG 推理抽取时，过程监督/奖励函数不要奖励“看起来深思熟虑”的语言（如“让我再想想”“我不确定”），要奖励证据引用、知识与问题陈述对齐、对答案置信度的校准；否则会激励模型输出大量无信息量的表面推理。

  - 推理长度不是越长的思考越好；在成本与延迟敏感的推荐/搜索场景，可基于行为 lift 建立更细粒度的过程质量评估，识别哪些中间步骤真正贡献正确性，用于 prompt
  压缩、推理步剪枝或早停。

  - 如果自建 reasoning model 或微调开源 LLM 做 query/商品理解，评估时除了端到端准确率，应监控行为分布，防止训练只改变风格而非能力。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：推理导向后训练让模型输出更长推理轨迹，但准确率看不出来哪些行为真正有效；某些行为可能只是“看起来更审慎”而未被正确性支撑。

**方法关键点**：定义 Behavioral Lift，度量某一推理行为出现与否时正确率的变化；对 15 个模型、6 个文本与视觉语言推理基准的 15,282 条轨迹进行标注，构建覆盖 LLM 与 VLM 的行为 taxonomy。

**关键结果数字**：思考模型显著放大 self-correction、hypothesis testing、uncertainty acknowledgment；但最高 lift 行为是 confidence calibration、knowledge alignment、self-awareness。置信校准在两种模态中都是最强正信号之一，却几乎未被放大；不确定性承认被放大 3–7 倍，但与正确性弱相关或负相关。结论是需要过程级目标奖励校准和扎根推理，而非仅奖励表面形式。
