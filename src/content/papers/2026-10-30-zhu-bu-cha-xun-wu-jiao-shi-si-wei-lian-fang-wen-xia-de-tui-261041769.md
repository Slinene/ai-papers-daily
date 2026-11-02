---
title: 'Stepwise-Querying: Distilling Reasoning without Access to Teacher Chain-of-Thought'
title_zh: 逐步查询：无教师思维链访问下的推理蒸馏
authors:
- Dicong Yu
- Wenhua Wang
- Tian Wang
affiliations:
- Institute of AI and Future Network, Beijing Normal University
arxiv_id: '2610.41769'
url: https://arxiv.org/abs/2610.41769
pdf_url: https://arxiv.org/pdf/2610.41769
published: '2026-10-30'
collected: '2026-11-02'
category: Training
direction: LLM 推理蒸馏 · 黑盒 query 细化
tags:
- reasoning distillation
- black-box LLM
- stepwise querying
- SFT
- CoT-free
- SEIG
one_liner: 黑盒教师下用逐步独立查询蒸馏推理，无需 CoT，14/16 对比最优
practical_value: '- 黑盒大模型 API 做推理蒸馏：不要只拿 final answer/brief solution，把任务拆成单步 derivation、validity
  check、correction 多轮 query，再拼装 SFT；业务侧拿不到 teacher CoT 权限也能做小模型推理增强。

  - 数据过滤别只按 final answer：答案错误但中间推理有效的轨迹可保留，尤其适合商品属性抽取、query 改写逻辑、广告文案生成等任务；可用 frozen
  student 对正确中间步骤的 log-ratio（类似 SEIG）评估哪些 step 仍有信息增益。

  - 拆解粒度要控成本：逐步 query 有收益但过度分解收益有限，工程上优先拆到关键推导与校验，避免过多 query 调用和延迟。

  - 对 Agent 规划训练可复用：若用大模型生成多步决策轨迹，可把每步 decision/check/修正作为独立 query 组装成微调数据，提升小模型规划稳定性。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：黑盒设置下，教师模型通常只暴露 final answer 和简短 solution，中间计算与有效性条件不可见，导致推理蒸馏监督不足。现有方法如 MathFimer、Trace Inversion 尝试补全或合成 trace，但仍受限于可观测信息。

**方法关键点**：提出 Stepwise Querying，不必访问教师内部 CoT，而是对同一教师发起多个独立 query，分别请求中间推导、有效性检查与逐步修正；将这些 step-specific explanation 拼装成完整解，用于标准 SFT。进一步提出 SEIG 诊断指标：基于 frozen student 在 stepwise explanation 与 global explanation 下完成正确步骤概率的 log-ratio，衡量逐步解释的信息增益。

**关键结果**：跨 2 个教师、2 个学生、4 个数学与代码基准，14/16 个对比中超过 3 个 baseline。GSM8K 分析显示，final answer 错误但中间推理有效的轨迹仍有蒸馏价值；继续过度拆解只会带来有限提升。
