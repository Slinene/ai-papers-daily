---
title: 'StepBack: Step-Level Error-Localized Resampling for Efficient Test-Time Reasoning'
title_zh: StepBack：步骤级错误定位重采样实现高效测试时推理
authors:
- Yang Ouyang
- Jung-Eun Kim
affiliations:
- North Carolina State University
arxiv_id: '2611.08403'
url: https://arxiv.org/abs/2611.08403
pdf_url: https://arxiv.org/pdf/2611.08403
published: '2026-11-05'
collected: '2026-11-06'
category: Reasoning
direction: LLM 测试时推理 · 自洽性高效解码
tags:
- Self-Consistency
- Test-Time Compute
- Error Localization
- Resampling
- Chain-of-Thought
- Efficient Inference
one_liner: 用轻量信号定位推理首个错误步骤，仅重采样该步及后缀，匹配自洽性准确率且最高省41.26% token
practical_value: '- 多步 LLM Agent（如导购、查询改写、推荐解释）失败或低置信时，不要整段重跑；先用轻量信号定位首个错误步骤，只重采样该步及后缀，可显著降低
  API token/延迟成本。

  - 若已有多数投票或 Self-Consistency 聚合，可在少量 draft 轨迹上做步骤级错误定位，再定向补充采样；与 Adaptive Consistency
  等提前停止策略天然兼容，适合预算敏感的场景。

  - 轻量信号可选 token-level 概率/熵、步骤自验证或轨迹间不一致度，工程上可作为现有推理管线的后处理层，无需额外训练。

  - 在搜索推荐 Agent 中做多步推理时，可把重算预算集中在出错概率高的中间步骤，避免对已正确前缀的重复计算。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

## 动机
Self-Consistency (SC) 需要采样多条完整推理轨迹再投票，token 成本随轨迹数和轨迹长度线性增长；已有高效变体主要在完整轨迹粒度上提前停止或按题分配预算，仍有大量冗余计算。

## 方法关键点
StepBack 先用少量 draft 轨迹生成候选答案；通过轻量信号定位每条轨迹中最可能的“首个错误步骤”；随后只重采样该错误步及其后缀，而不是重新生成整条轨迹；最后对最终答案做多数投票。重算预算因此集中在局部易错片段。

## 关键结果
在 7 个数学推理和多跳 QA benchmark 上，StepBack 平均达到与 SC 相当的准确率，token 使用最多减少 41.26%。例如在 GSM8K 上，Qwen-3B 减少 38.37% token、Llama-3B 减少 34.77% token，同时准确率更高或相当；方法还可与 Adaptive Consistency 等自适应推理方法结合，进一步提升推理时效率。
