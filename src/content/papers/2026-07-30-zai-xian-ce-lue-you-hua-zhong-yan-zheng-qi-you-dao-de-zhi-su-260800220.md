---
title: Verifier-Induced Support Reshaping in On-Policy Optimization
title_zh: 在线策略优化中验证器诱导的支撑重塑
authors:
- Shaohang Wei
- Zikun Su
- Feifan Song
- Wen Luo
- Wei Li
- Guangyue Peng
- Houfeng Wang
affiliations:
- Peking University
- BUPT
arxiv_id: '2608.00220'
url: https://arxiv.org/abs/2608.00220
pdf_url: https://arxiv.org/pdf/2608.00220
published: '2026-07-30'
collected: '2026-08-18'
category: Training
direction: RLVR在线策略优化的能力保持问题
tags:
- RLVR
- On-Policy Optimization
- Support Reshaping
- Instruction Following
- Math Reasoning
- Continual Learning
one_liner: 在线RLVR优化单一目标会缩小后续任务可采样成功轨迹，导致pass@1与best@k背离
practical_value: '- 多目标 RLVR/RLHF 后训练时，同时监控 pass@1、best@k 与“有成功轨迹的 prompt 比例”，避免平均奖励上升但尾部任务支撑塌缩。

  - 对搜索/推荐 Agent 的指令遵循或格式约束训练，RLVR 可能只重排已有开头 token 而非生成新能力；可对前几个 token 加多样性正则或保留基座策略的开头分布。

  - 顺序多目标训练（如先数学后 IF）应在每个阶段保存 checkpoint 并评估跨任务 best@k；参考策略约束、路由先验、蒸馏只能部分缓解，建议显式混合数据或联合验证器。

  - 若用 RLVR 做转化/点击奖励的 on-policy 优化，需防止模型为提升即时反馈而牺牲搜索/检索友好性；可在 reward 中考虑前几个 token
  的信息量或可搜索性。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：on-policy RLVR 在提升当前任务奖励的同时，可能让后续任务的成功轨迹在固定 rollout 预算下变得难以采样，作者将这一现象称为验证器诱导支撑重塑，并定义有效奖励支撑为固定预算内可达的成功轨迹集。
方法关键点：在两个模型家族上，以数学推理和受约束指令跟随为对象进行双向顺序训练（先 Math-RLVR 后 IF、先 IF-RLVR 后 Math），通过重复验证器评分采样、token 分布分析和受控开头干预刻画支撑变化。
关键结果：Math-RLVR 提高平均指令遵循成功率，但减少有成功响应的 prompt 数；在 Qwen3-8B-Base 上 IFEval pass@1 上升 6.5 个百分点，best@32 下降 9.8 个百分点，两个模型和多个 IF 基准均出现同样背离。反之，IF-RLVR 使数学响应从逐步推理开头转向直接答案，降低各类采样预算下的 best@k，并减少后续 Math-RLVR 的奖励方差。变化集中在前几个响应 token；RLVR 主要重排基座策略中已有的开头，所选择的开头因果影响数学可搜索性。参考策略约束、路由先验、在线蒸馏仅部分保留跨任务支撑，边际收益难以完全转化为既正确又遵循约束的响应。因此端点指标提升不保证未来可训练性或联合能力。
