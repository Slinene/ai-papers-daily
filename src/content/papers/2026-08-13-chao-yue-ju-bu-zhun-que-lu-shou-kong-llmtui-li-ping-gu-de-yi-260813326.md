---
title: 'Beyond Local Accuracy: A Protocol-Level Identifiability Audit for Controlled
  LLM Reasoning Evaluation'
title_zh: 超越局部准确率：受控LLM推理评估的协议级可识别性审计
authors:
- Junhao Luo
- Ning Huang
- Ziqi Sha
- Wenxuan Tang
- Wei Deng
affiliations:
- School of Statistics and Data Science, Southwestern University of Finance and Economics
arxiv_id: '2608.13326'
url: https://arxiv.org/abs/2608.13326
pdf_url: https://arxiv.org/pdf/2608.13326
published: '2026-08-13'
collected: '2026-08-16'
category: Eval
direction: 评估协议可识别性审计
tags:
- LLM Evaluation
- Identifiability
- Intervention Response
- Protocol Audit
- Behavioral Policy
- Selective Response
one_liner: 提出零模型调用的协议级可识别性审计，证明静态准确率与干预响应保真度存在结构性分歧
practical_value: '- 评估任何策略干预（如推荐解释、prompt 改动、Agent 行为约束）前，先用协议级可识别性审计检查观测协议是否能区分不同行为策略，避免把静态准确率当作干预响应保真度。

  - 利用最小识别支持思想做实验设计：离线评估时找出能区分策略差异的最小观测单元，减少日志、标注和推理成本。

  - 注意基准正确率不能预测干预响应保真度，线上干预效果需要单独设计评估协议并验证其可识别性，尤其适用于多 Agent 策略对比场景。

  - 可复用的审计是零模型调用的，可以在上线前用合成策略集检查评估协议，适合 Agent 多策略预筛选。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

动机：LLM 基准分数即使精确，也可能不识别目标行为属性；静态正确性和干预响应保真度是两个不同估计量，但常被混淆。

方法关键点：在有限行为策略类上形式化协议级可识别性审计：给定策略集 H、观测支持 O 和估计量 τ，测试 O 是否能分离所有不同 τ 的策略对。审计零模型调用。对 7 个冻结确定性策略诊断发现：仅基础观测将 7 个策略合并为 1 个等价类；完整支持得到 7 个类且无跨估计量碰撞；每个留一支持都保留构造性碰撞见证。

关键结果数字：两种约束生成变体 pair-validity 均为 1.0，但基础准确率与选择性响应保真度分别为 0.620 和 0.324（cluster-bootstrap 95% CI [0.600, 0.642] vs [0.304, 0.345]）；第二个确定性源上同样出现差距（0.646 vs 0.331）。审计还合成了最小识别支持：仅 2 个 cell 即可识别 36-cell 张量中的策略类。结论：评估设计有效性可在模型推理前做结构性检查，基础正确性不决定干预响应保真度。
